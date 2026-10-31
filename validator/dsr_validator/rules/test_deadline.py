import json
from pathlib import Path

from dsr_validator.rules.deadline import (
    deadline_within_statutory_window,
    extension_must_be_declared_within_the_first_month,
    _add_months,
)
from dsr_validator.runner import Context
from datetime import date

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_minimal_clean_fixture_deadline_is_within_the_one_month_window():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


def test_deadline_beyond_one_month_without_extension_is_rejected():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["computed_date"] = "2026-12-01"  # 3 months out, not extended
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "DEADLINE-1"
    assert findings[0].severity == "rejection"


def test_deadline_within_three_months_when_extended_is_accepted():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extended"] = True
    sidecar["deadline"]["computed_date"] = "2026-12-01"  # 3 months from 2026-09-01
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


def test_deadline_beyond_three_months_even_when_extended_is_rejected():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extended"] = True
    sidecar["deadline"]["computed_date"] = "2027-01-15"
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1


def test_deadline_before_intake_is_rejected():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["computed_date"] = "2026-08-15"  # before intake 2026-09-01
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1
    assert "before" in findings[0].message


def test_month_addition_clamps_to_the_last_valid_day():
    # 31 Jan + 1 month -> no 31 Feb, clamp to 28 Feb 2026 (not a leap year).
    assert _add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)


def test_malformed_dates_do_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["computed_date"] = "not-a-date"
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


# --- break-it test 2026-10-02: weekend/holiday rollover (DEADLINE-1 false positive) --------

def test_weekend_rollover_false_positive_is_fixed():
    # P01: 1 month from 2026-08-19 is Sat 2026-09-19 -> rolls to Mon 2026-09-21.
    sidecar = json.loads(
        (FIX / "must_pass" / "DEADLINE-1__weekend-rollover.json").read_text())
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


def test_declared_holiday_chains_into_the_weekend_rule():
    # Statutory last day (Fri 2026-12-25) is a declared holiday -> rolls through the
    # following Sat/Sun to Mon 2026-12-28.
    sidecar = json.loads(
        (FIX / "must_pass" / "DEADLINE-1__declared-holiday-rollover.json").read_text())
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


def test_undeclared_holiday_is_never_silently_accepted():
    # Same scenario as the declared-holiday fixture, minus the holiday_rollover
    # declaration -- must still be rejected (a holiday rolls the deadline only when
    # the sidecar says so, never inferred).
    sidecar = json.loads(
        (FIX / "must_fail" / "DEADLINE-1__undeclared-holiday-not-silently-accepted.json")
        .read_text())
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "DEADLINE-1"
    assert findings[0].severity == "rejection"


def test_leap_year_month_end_without_weekend_still_rejects():
    # P12 control: 1 month from 2028-01-29 is Tue 2028-02-29 (leap year, weekday) --
    # the fix must not loosen correct leap-year clamping.
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["request"]["intake_date"] = "2028-01-29"
    sidecar["deadline"]["computed_date"] = "2028-03-01"
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "DEADLINE-1"


def test_extension_at_exactly_the_three_month_boundary_still_passes():
    # P13 control: 3 months from 2026-09-01 is Tue 2026-12-01 (weekday) -- exact
    # boundary equality must still pass.
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extended"] = True
    sidecar["deadline"]["computed_date"] = "2026-12-01"
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


def test_month_overflow_clamp_without_weekend_still_rejects():
    # P14 control: 1 month from 2026-10-31 clamps to Mon 2026-11-30 (weekday) -- the
    # clamp must still reject a date past it.
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["request"]["intake_date"] = "2026-10-31"
    sidecar["deadline"]["computed_date"] = "2026-12-01"
    findings = deadline_within_statutory_window(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "DEADLINE-1"


def test_malformed_holiday_rollover_is_ignored_not_raised():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["holiday_rollover"] = "not-a-list"
    assert deadline_within_statutory_window(sidecar, _ctx()) == []


# --- DEADLINE-2 : extension must be declared within the first month ------------------------

def test_extension_declared_late_is_rejected():
    sidecar = json.loads(
        (FIX / "must_fail" / "DEADLINE-2__extension-declared-late.json").read_text())
    findings = extension_must_be_declared_within_the_first_month(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "DEADLINE-2"
    assert findings[0].severity == "rejection"


def test_extension_declared_within_first_month_passes():
    sidecar = json.loads(
        (FIX / "must_pass" / "DEADLINE-2__extension-declared-on-time.json").read_text())
    assert extension_must_be_declared_within_the_first_month(sidecar, _ctx()) == []


def test_extension_declared_at_absent_is_silent():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extended"] = True
    sidecar["deadline"]["computed_date"] = "2026-12-01"
    assert extension_must_be_declared_within_the_first_month(sidecar, _ctx()) == []


def test_extension_declared_at_silent_when_not_extended():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extension_declared_at"] = "2027-01-01"  # absurdly late but irrelevant
    assert extension_must_be_declared_within_the_first_month(sidecar, _ctx()) == []


def test_extension_declared_at_malformed_does_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["deadline"]["extended"] = True
    sidecar["deadline"]["extension_declared_at"] = "not-a-date"
    assert extension_must_be_declared_within_the_first_month(sidecar, _ctx()) == []
