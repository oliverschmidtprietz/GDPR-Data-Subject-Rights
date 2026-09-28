"""DEADLINE-1 : deadline arithmetic sanity against the Art. 12(3) window.

`deadline.computed_date` must fall within one month of `request.intake_date`
(Art. 12(3) base period), or within two months if `deadline.extended` is
true (the base month plus the +2-month extension, so three months total from
intake). Month addition clamps the day-of-month to the last valid day of the
target month (Reg. 1182/71's no-such-date rule) rather than overflowing into
the next month.
"""
import calendar
from datetime import date

from ..findings import Finding
from ..registry import rule

SPEC = "references/procedural-framework.md#deadlines"


def _add_months(d: date, months: int) -> date:
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


@rule(id="DEADLINE-1", severity="rejection", category="deadline",
      description="deadline.computed_date must fall within the Art. 12(3) one-month (or, if "
                  "extended, three-month) window from request.intake_date.",
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
    latest = _add_months(intake, max_months)

    if computed < intake:
        return [Finding(
            rule_id="DEADLINE-1", category="deadline", severity="rejection",
            message=f"deadline.computed_date {computed.isoformat()} is before "
                     f"request.intake_date {intake.isoformat()}.",
            spec_anchor=SPEC, field="deadline.computed_date",
            fix_hint="computed_date must be on or after intake_date.",
        )]
    if computed > latest:
        return [Finding(
            rule_id="DEADLINE-1", category="deadline", severity="rejection",
            message=(f"deadline.computed_date {computed.isoformat()} exceeds the Art. 12(3) "
                      f"{max_months}-month window from intake ({intake.isoformat()}); the "
                      f"latest permitted date is {latest.isoformat()}."),
            spec_anchor=SPEC, field="deadline.computed_date",
            fix_hint="Recompute the deadline, or set deadline.extended=true if a reasoned "
                     "extension was actually declared within the first month.",
        )]
    return []
