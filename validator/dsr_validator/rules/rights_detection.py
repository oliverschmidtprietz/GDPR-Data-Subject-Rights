"""RIGHTS-1 : right-detection completeness (read the request generously).

SKILL.md's own worked intake guidance: "read it generously, a 'delete
everything and tell me what you have' email is BOTH Art. 17 and Art. 15."
This rule flags — as an advisory warning, not a hard rejection, since the
absence may be a deliberate scoping choice — a triage whose captured request
text plainly also asks for the OTHER right, in either direction:

  * an Art. 17-only triage whose text plainly also asks an access-style
    question (missing an Art. 15 component), and
  * an Art. 15-only triage whose text plainly also asks for erasure (missing
    an Art. 17 component) — the reverse direction (break-it test 2026-10-02).

Phrase lists are modestly widened (same date) to catch common phrasings the
original lists missed, e.g. "what personal data you store about me" and
"delete my account".
"""
from ..findings import Finding
from ..registry import rule

SPEC = "SKILL.md#intake-questions"

_ACCESS_TRIGGER_PHRASES = (
    "what do you have on me",
    "what data do you have on me",
    "what information do you have on me",
    "what data do you hold about me",
    "what personal data you hold about me",
    "what information you hold about me",
    "what data you store about me",
    "what personal data you store about me",
    "what information you store about me",
    "let me know what personal data",
    "let me know what data",
    "let me know what information",
    "tell me what you have",
    "tell me what you have on me",
    "tell me what personal data",
)

_ERASURE_TRIGGER_PHRASES = (
    "delete everything",
    "delete all my data",
    "delete all of my data",
    "erase everything",
    "erase all my data",
    "erase all of my data",
    "delete my data",
    "erase my data",
    "delete my account",
    "close my account and delete",
    "right to be forgotten",
    "forget me",
)


def _fires(text: str, phrases) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in phrases)


@rule(id="RIGHTS-1", severity="warning", category="completeness",
      description="An Art. 17-only triage must not silently drop an Art. 15 component (or vice "
                  "versa) when the intake text plainly also asks for the other right.",
      spec_anchor=SPEC)
def art17_request_should_not_drop_art15_component(sidecar, ctx):
    rights = sidecar.get("rights_invoked")
    request = sidecar.get("request")
    if not isinstance(rights, list) or not isinstance(request, dict):
        return []
    text = request.get("text")
    if not isinstance(text, str):
        return []

    if "art17" in rights and "art15" not in rights and _fires(text, _ACCESS_TRIGGER_PHRASES):
        return [Finding(
            rule_id="RIGHTS-1", category="completeness", severity="warning",
            priority="high",
            message=("rights_invoked names art17 only, but request.text asks an "
                      "access-style question — read generously: this likely also "
                      "invokes Art. 15."),
            spec_anchor=SPEC, field="rights_invoked",
            fix_hint="Add 'art15' to rights_invoked if the access component is genuinely "
                     "in scope for this request.",
        )]

    if "art15" in rights and "art17" not in rights and _fires(text, _ERASURE_TRIGGER_PHRASES):
        return [Finding(
            rule_id="RIGHTS-1", category="completeness", severity="warning",
            priority="high",
            message=("rights_invoked names art15 only, but request.text asks for erasure — "
                      "read generously: this likely also invokes Art. 17."),
            spec_anchor=SPEC, field="rights_invoked",
            fix_hint="Add 'art17' to rights_invoked if the erasure component is genuinely "
                     "in scope for this request.",
        )]

    return []
