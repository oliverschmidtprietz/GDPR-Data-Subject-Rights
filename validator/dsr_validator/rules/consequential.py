"""CONSEQ-1 : a genuine procedural contradiction, not just a schema shape check.

The Assessment Flow (SKILL.md) runs an identity check "only if reasonable
doubts" are raised — but if reasonable doubts WERE flagged and were never
resolved (`identity_verification.verified` is not `true`), granting or
partially granting the request skips the gate the skill's own procedure
requires before disclosure or erasure. Refusing or extending is unaffected —
this rule only fires on `decision in {"grant", "partial"}`.
"""
from ..findings import Finding
from ..registry import rule

SPEC = "SKILL.md#assessment-flow"


@rule(id="CONSEQ-1", severity="rejection", category="procedural",
      description="decision=grant/partial with identity_verification.reasonable_doubts=true "
                  "requires identity_verification.verified=true.",
      spec_anchor=SPEC)
def grant_requires_verified_identity_when_doubted(sidecar, ctx):
    decision = sidecar.get("decision")
    idv = sidecar.get("identity_verification")
    if not isinstance(idv, dict):
        return []  # SCHEMA-1 already reports the missing/malformed object
    if decision in ("grant", "partial") and idv.get("reasonable_doubts") is True \
            and idv.get("verified") is not True:
        return [Finding(
            rule_id="CONSEQ-1", category="procedural", severity="rejection",
            message=(f"decision={decision!r} but identity_verification.reasonable_doubts=true "
                      "and verified is not true — a procedural contradiction: the Assessment "
                      "Flow's identity check gate ('only if reasonable doubts') must be "
                      "resolved before granting or partially granting a request."),
            spec_anchor=SPEC, field="identity_verification.verified",
            fix_hint="Either resolve the identity doubt (set verified=true) or change the "
                     "decision to refuse/extend pending verification.",
        )]
    return []
