import json
from pathlib import Path

from dsr_validator.rules.deadline import deadline_within_statutory_window, _add_months
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
