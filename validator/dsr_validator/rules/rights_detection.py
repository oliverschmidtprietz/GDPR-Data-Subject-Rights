"""RIGHTS-1 : right-detection completeness (read the request generously).

SKILL.md's own worked intake guidance: "read it generously, a 'delete
everything and tell me what you have' email is BOTH Art. 17 and Art. 15."
This rule flags — as an advisory warning, not a hard rejection, since the
absence may be a deliberate scoping choice — an Art. 17-only triage whose
captured request text plainly also asks an access-style question.
"""
from ..findings import Finding
from ..registry import rule

SPEC = "SKILL.md#intake-questions"

_ACCESS_TRIGGER_PHRASES = (
    "what do you have on me",
    "what data do you have on me",
    "what information do you have on me",
    "what data do you hold about me",
    "tell me what you have",
    "tell me what you have on me",
)


@rule(id="RIGHTS-1", severity="warning", category="completeness",
      description="An Art. 17-only triage must not silently drop an Art. 15 component when "
                  "the intake text plainly also asks an access-style question.",
      spec_anchor=SPEC)
def art17_request_should_not_drop_art15_component(sidecar, ctx):
    rights = sidecar.get("rights_invoked")
    request = sidecar.get("request")
    if not isinstance(rights, list) or not isinstance(request, dict):
        return []
    text = request.get("text")
    if not isinstance(text, str):
        return []
    if "art17" in rights and "art15" not in rights:
        lowered = text.lower()
        if any(phrase in lowered for phrase in _ACCESS_TRIGGER_PHRASES):
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
    return []
