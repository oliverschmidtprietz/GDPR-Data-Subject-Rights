"""DEADLINE-1 : deadline arithmetic sanity against the Art. 12(3) window.
DEADLINE-2 : an Art. 12(3) extension must be declared within the first month.

`deadline.computed_date` must fall within one month of `request.intake_date`
(Art. 12(3) base period), or within two months if `deadline.extended` is
true (the base month plus the +2-month extension, so three months total from
intake). Month addition clamps the day-of-month to the last valid day of the
target month (Reg. 1182/71's no-such-date rule) rather than overflowing into
the next month.

Weekend/holiday rollover (Reg. (EEC, Euratom) No 1182/71 Art. 3(4), confirmed
against the current consolidated text 2026-10-02 — see sources.lock.json):
"Where the last day of a period expressed otherwise than in hours is a public
holiday, Sunday or Saturday, the period shall end with the expiry of the last
hour of the following working day." Saturdays and Sundays are deterministic
and always rolled forward. A public holiday is NOT inferred — it only rolls
the deadline when the sidecar explicitly declares it via the optional
`deadline.holiday_rollover` field (a list of {date, reason} entries), so a
later computed_date is accepted only when the controller actually recorded
why, never silently.
"""
import calendar
from datetime import date, timedelta

from ..findings import Finding
from ..registry import rule

SPEC = "references/procedural-framework.md#deadlines"
_WEEKEND_SPEC = "references/procedural-framework.md#deadlines (Reg. 1182/71 Art. 3(4))"


def _add_months(d: date, months: int) -> date:
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def _is_weekend(d: date) -> bool:
    return d.weekday() >= 5  # 5 = Saturday, 6 = Sunday


def _declared_holidays(deadline: dict) -> set:
    """Parse the optional `deadline.holiday_rollover` sidecar field. Malformed or
    absent input yields an empty set (no silent rollover is ever invented)."""
    raw = deadline.get("holiday_rollover")
    if not isinstance(raw, list):
        return set()
    out = set()
    for entry in raw:
        if not isinstance(entry, dict):
            continue
        raw_date = entry.get("date")
        if not isinstance(raw_date, str):
            continue
        try:
            out.add(date.fromisoformat(raw_date))
        except ValueError:
            continue
    return out


def _roll_forward_to_working_day(d: date, holidays: set) -> date:
    while _is_weekend(d) or d in holidays:
        d += timedelta(days=1)
    return d


@rule(id="DEADLINE-1", severity="rejection", category="deadline",
      description="deadline.computed_date must fall within the Art. 12(3) one-month (or, if "
                  "extended, three-month) window from request.intake_date, rolled forward past "
                  "a weekend or (if declared) a public holiday per Reg. 1182/71 Art. 3(4).",
      spec_anchor=SPEC)
def deadline_within_statutory_window(sidecar, ctx):
    request = sidecar.get("request")
    deadline = sidecar.get("deadline")
    if not isinstance(request, dict) or not isinstance(deadline, dict):
        return []  # SCHEMA-1 already reports the missing/malformed object
    intake_raw = request.get("intake_date")
    computed_raw = deadline.get("computed_date")
    if not isinstance(intake_raw, str) or not isinstance(computed_raw, str):
        return []
    try:
        intake = date.fromisoformat(intake_raw)
        computed = date.fromisoformat(computed_raw)
    except ValueError:
        return []  # SCHEMA-1 already reports the format violation

    extended = bool(deadline.get("extended"))
    max_months = 3 if extended else 1
    statutory_latest = _add_months(intake, max_months)
    holidays = _declared_holidays(deadline)
    latest = _roll_forward_to_working_day(statutory_latest, holidays)

    if computed < intake:
        return [Finding(
            rule_id="DEADLINE-1", category="deadline", severity="rejection",
            message=f"deadline.computed_date {computed.isoformat()} is before "
                     f"request.intake_date {intake.isoformat()}.",
            spec_anchor=SPEC, field="deadline.computed_date",
            fix_hint="computed_date must be on or after intake_date.",
        )]
    if computed > latest:
        rollover_note = ""
        if latest != statutory_latest:
            rollover_note = (f" (statutory date {statutory_latest.isoformat()} falls on a "
                              f"weekend/declared holiday and rolls to {latest.isoformat()} "
                              f"per Reg. 1182/71 Art. 3(4))")
        return [Finding(
            rule_id="DEADLINE-1", category="deadline", severity="rejection",
            message=(f"deadline.computed_date {computed.isoformat()} exceeds the Art. 12(3) "
                      f"{max_months}-month window from intake ({intake.isoformat()}); the "
                      f"latest permitted date is {latest.isoformat()}{rollover_note}."),
            spec_anchor=SPEC, field="deadline.computed_date",
            fix_hint="Recompute the deadline, or set deadline.extended=true if a reasoned "
                     "extension was actually declared within the first month. If the statutory "
                     "last day is a public holiday, declare it in deadline.holiday_rollover "
                     "(date + reason) rather than silently moving the date.",
        )]
    return []


@rule(id="DEADLINE-2", severity="rejection", category="deadline",
      description="deadline.extension_declared_at, when present, must fall within the first "
                  "month from request.intake_date (Art. 12(3)) — a late declaration is a "
                  "violation, not an extension.",
      spec_anchor=SPEC)
def extension_must_be_declared_within_the_first_month(sidecar, ctx):
    request = sidecar.get("request")
    deadline = sidecar.get("deadline")
    if not isinstance(request, dict) or not isinstance(deadline, dict):
        return []  # SCHEMA-1 already reports the missing/malformed object
    if deadline.get("extended") is not True:
        return []
    declared_raw = deadline.get("extension_declared_at")
    if not isinstance(declared_raw, str):
        return []  # extension_declared_at is optional; nothing to check if absent
    intake_raw = request.get("intake_date")
    if not isinstance(intake_raw, str):
        return []
    try:
        intake = date.fromisoformat(intake_raw)
        declared = date.fromisoformat(declared_raw)
    except ValueError:
        return []  # SCHEMA-1 already reports the format violation

    first_month_end = _add_months(intake, 1)
    if declared > first_month_end:
        return [Finding(
            rule_id="DEADLINE-2", category="deadline", severity="rejection",
            message=(f"deadline.extension_declared_at {declared.isoformat()} is after the first "
                      f"month from intake ends ({first_month_end.isoformat()}). Art. 12(3) "
                      "requires the extension to be declared, with reasons, within the first "
                      "month — a late declaration is a violation, not a valid extension."),
            spec_anchor=SPEC, field="deadline.extension_declared_at",
            fix_hint="A late extension notice does not toll the deadline — treat the response "
                     "as overdue rather than extended, or correct the recorded declaration date.",
        )]
    return []
