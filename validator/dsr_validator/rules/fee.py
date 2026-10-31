"""FEE-1 : a charged fee must carry a stated Art. 12(5) ground.

The first copy under an Art. 15 access request is free by default (Art.
15(3); confirmed even for a first copy of a patient file under a non-privacy
purpose — CJEU C-307/22 *FT*). A fee (or refusal) is lawful only for further
copies, or where the controller demonstrates the request is manifestly
unfounded or excessive (Art. 12(5)) — and the burden of that demonstration is
on the controller (procedural-framework.md "Fees and refusal (Art. 12(5))").

This rule is deliberately narrow: it only fires when the optional `fee`
sidecar field is present AND `fee.charged` is `true`. A sidecar that never
mentions `fee` at all (the overwhelming majority — free first copies are the
default) is untouched.
"""
from ..findings import Finding
from ..registry import rule

SPEC = "references/procedural-framework.md#fees-and-refusal-art-125"
_VALID_GROUNDS = ("further_copy", "manifestly_unfounded_or_excessive")


@rule(id="FEE-1", severity="rejection", category="fees",
      description="fee.charged=true requires fee.ground to be 'further_copy' or "
                  "'manifestly_unfounded_or_excessive' — the first copy is free by default "
                  "(Art. 15(3)/12(5)).",
      spec_anchor=SPEC)
def fee_requires_art12_5_ground(sidecar, ctx):
    fee = sidecar.get("fee")
    if not isinstance(fee, dict):
        return []
    if fee.get("charged") is not True:
        return []
    ground = fee.get("ground")
    if ground in _VALID_GROUNDS:
        return []
    return [Finding(
        rule_id="FEE-1", category="fees", severity="rejection",
        message=("fee.charged=true but fee.ground is missing or not one of "
                  f"{_VALID_GROUNDS} — the first copy is free under Art. 15(3); a fee or "
                  "refusal is lawful only for further copies, or for a manifestly unfounded "
                  "or excessive request with the controller's demonstration on file (Art. "
                  "12(5))."),
        spec_anchor=SPEC, field="fee.ground",
        fix_hint="Either waive the fee for a first copy, or set fee.ground to 'further_copy' "
                 "or 'manifestly_unfounded_or_excessive' with the Art. 12(5) demonstration "
                 "documented.",
    )]
