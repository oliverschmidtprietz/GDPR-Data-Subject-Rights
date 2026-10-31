"""CONSEQ-1 : a genuine procedural contradiction, not just a schema shape check.

The Assessment Flow (SKILL.md) runs an identity check "only if reasonable
doubts" are raised — but if reasonable doubts WERE flagged and were never
resolved (`identity_verification.verified` is not `true`), granting or
partially granting the request skips the gate the skill's own procedure
requires before disclosure or erasure. Refusing or extending is unaffected —
this rule only fires on `decision in {"grant", "partial"}`.

A second, independent trigger (added 2026-10-02, break-it test): Art. 12(6)
(procedural-framework.md "Identity verification") makes "reasonable doubts"
the TRIGGER for running a check, not the only thing that matters once
`verified` has actually been recorded `false` — an explicit `verified: false`
means an identity check was attempted and failed (or is still open), which is
itself a disclosure/destruction risk regardless of whether `reasonable_doubts`
was (perhaps wrongly) left `false`. This second trigger is scoped to Art. 15
(access — wrongful disclosure) and Art. 17 (erasure — wrongful destruction),
the two rights where granting to the wrong person causes irreversible harm;
it deliberately does not fire for lower-risk rights (e.g. Art. 16
rectification, Art. 18 restriction) to avoid false positives there.
"""
from ..findings import Finding
from ..registry import rule

SPEC = "SKILL.md#assessment-flow"
_HIGH_RISK_RIGHTS = ("art15", "art17")


@rule(id="CONSEQ-1", severity="rejection", category="procedural",
      description="decision=grant/partial requires identity_verification.verified=true "
                  "whenever reasonable_doubts=true, and (for Art. 15/Art. 17 requests) "
                  "whenever verified is explicitly false.",
      spec_anchor=SPEC)
def grant_requires_verified_identity_when_doubted(sidecar, ctx):
    decision = sidecar.get("decision")
    idv = sidecar.get("identity_verification")
    if not isinstance(idv, dict):
        return []  # SCHEMA-1 already reports the missing/malformed object
    if decision not in ("grant", "partial"):
        return []

    verified = idv.get("verified")
    reasonable_doubts = idv.get("reasonable_doubts")

    if reasonable_doubts is True and verified is not True:
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

    rights = sidecar.get("rights_invoked")
    if verified is False and isinstance(rights, list) \
            and any(r in _HIGH_RISK_RIGHTS for r in rights):
        return [Finding(
            rule_id="CONSEQ-1", category="procedural", severity="rejection",
            message=(f"decision={decision!r} on a request invoking {sorted(set(rights) & set(_HIGH_RISK_RIGHTS))} "
                      "but identity_verification.verified=false — granting access or erasure to "
                      "an unverified requester risks disclosure/destruction to the wrong person, "
                      "regardless of whether reasonable_doubts was separately flagged."),
            spec_anchor=SPEC, field="identity_verification.verified",
            fix_hint="Resolve identity (set verified=true) before granting, or change the "
                     "decision to refuse/extend pending verification.",
        )]
    return []
