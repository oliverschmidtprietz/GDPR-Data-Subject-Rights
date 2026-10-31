"""ERASURE-1 : an Art. 17 decision must carry its ground/exception, and a full
grant must not contradict a recorded statutory-retention exception.

art17-erasure.md's two-step test (lines 5-30): test an Art. 17(1) ground
first, then an Art. 17(3) exception. A lawful refusal "states: the ground
examined, why it fails (or which exception prevails)" (art17-erasure.md
lines 60-62) — a refusal that records neither is procedurally incomplete.
Conversely, a *full* grant is self-contradictory if the sidecar itself
records that an Art. 17(3) exception applies (most commonly (b), statutory
retention, e.g. invoices under AO § 147/HGB § 257) — partial disposition is
the norm in that case (art17-erasure.md line 30), not a blanket grant.

Only meaningful when `rights_invoked` includes `art17`; the optional
`erasure_decision` field is otherwise untouched by this rule.
"""
from ..findings import Finding
from ..registry import rule

SPEC = "references/art17-erasure.md#two-step-test"


def _has_value(value) -> bool:
    """True if the field states something meaningful. 'none_found' IS meaningful for
    ground_examined (the Art. 17(1) examination concluded no ground applies — that's a
    stated reason for refusal); only '' and 'none' count as "nothing stated"."""
    return isinstance(value, str) and value not in ("", "none")


@rule(id="ERASURE-1", severity="rejection", category="procedural",
      description="An art17 refuse must record erasure_decision.ground_examined or "
                  ".exception_relied_on; an art17 grant must not record an Art. 17(3) "
                  "exception (partial disposition is the norm instead).",
      spec_anchor=SPEC)
def erasure_decision_ground_and_exception_consistency(sidecar, ctx):
    rights = sidecar.get("rights_invoked")
    if not isinstance(rights, list) or "art17" not in rights:
        return []
    decision = sidecar.get("decision")
    erasure_decision = sidecar.get("erasure_decision")

    if decision == "refuse":
        ground = erasure_decision.get("ground_examined") if isinstance(erasure_decision, dict) else None
        exception = erasure_decision.get("exception_relied_on") if isinstance(erasure_decision, dict) else None
        if not _has_value(ground) and not _has_value(exception):
            return [Finding(
                rule_id="ERASURE-1", category="procedural", severity="rejection",
                message=("decision=refuse on an art17 request but erasure_decision records "
                          "neither a ground_examined nor an exception_relied_on — a lawful "
                          "refusal must state the Art. 17(1) ground examined (and why it "
                          "fails) or the Art. 17(3) exception that prevails."),
                spec_anchor=SPEC, field="erasure_decision",
                fix_hint="Record erasure_decision.ground_examined (the Art. 17(1) ground "
                         "tested) and/or .exception_relied_on (the Art. 17(3) exception "
                         "relied on) before refusing.",
            )]

    if decision == "grant" and isinstance(erasure_decision, dict):
        exception = erasure_decision.get("exception_relied_on")
        if _has_value(exception):
            return [Finding(
                rule_id="ERASURE-1", category="procedural", severity="rejection",
                message=(f"decision=grant on an art17 request but erasure_decision."
                          f"exception_relied_on={exception!r} is recorded — a full grant is "
                          "self-contradictory where an Art. 17(3) exception (e.g. (b) "
                          "statutory retention) applies to any part of the data; partial "
                          "disposition is the norm (erase what the exception doesn't cover, "
                          "retain the rest under purpose limitation and access controls)."),
                spec_anchor=SPEC, field="erasure_decision.exception_relied_on",
                fix_hint="Change decision to 'partial' and record which records are retained "
                         "under the exception, with a scheduled deletion date — or clear "
                         "exception_relied_on if, on reflection, no exception actually applies.",
            )]

    return []
