"""Project a native data-subject-rights sidecar into the portfolio core artefact.

A PROJECTION, not a rewrite (D-WS3-06): the native sidecar is never modified
or restructured. Structure mirrors toms-art32's adapter
(skills/toms-art32/validator/toms_validator/core_artefact.py) — same
`to_core_artefact(sidecar, *, skill_version) -> dict` signature — but the
mapping is this skill's own.

subject: the DSR request itself (not an organisation), so
`subject.type == "other"` — none of the schema's other enum values
(organisation|processing_activity|transfer|assessment) fit a single incoming
request. `subject.id` falls back to an unmistakable placeholder if
`request` is missing or malformed; this is a NEW 1.1 emitter, so
`subject.type` is always populated, never optional.

gaps[]: two sources, both driven by real run input, never hard-coded.
  1. The deterministic validator's own diagnostics (`validation.findings[]`,
     gate vocabulary rejection|warning|info) — same pattern as toms-art32.
  2. Undischarged plain downstream duties (`art19_third_party_notification`,
     `art17_2_public_disclosure_notice`) from the sidecar's own
     `downstream_duties[]` — per the adoption brief, "gaps = downstream
     duties not yet discharged".

handoffs[]/unknowns[]: SKILL.md's "Sibling Skill Handoffs" section names
exactly four siblings (ropa, legitimate-interest, dpa-art28,
privacy-notice-eu). Each has a matching `downstream_duties[].duty` value.
When that duty value is present in this run's sidecar (whether discharged or
not — its presence means the topic came up), it becomes a `handoffs[]`
entry; when a given sibling's duty value never appears in the sidecar at
all, it is an open question this run didn't record, and becomes an
`unknowns[]` entry instead. This mapping is exhaustive over the four named
siblings and is read from the sidecar's own data every run, never emitted as
a constant.

sources[]: every `sources.lock.json` entry with a usable `last_verified`,
read live from disk (never hard-coded `[]`) — for a structural-tier skill
with no per-run source selection, the full declared reference set is what
backs any DSR triage.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ARTEFACT_SCHEMA_VERSION = "1.1"
SKILL_NAME = "data-subject-rights"

_DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")

_OUTCOME_BY_VALIDATION_STATUS = {
    "passed": "complete",
    "passed_with_warnings": "provisional",
    "failed": "blocked",
}

_UNKNOWN_REQUEST_ID = "unknown-request"

# Downstream duties that are plain gaps (no sibling skill owns them) when not discharged.
_GAP_DUTIES = {"art19_third_party_notification", "art17_2_public_disclosure_notice"}

# The four sibling handoffs SKILL.md's "Sibling Skill Handoffs" section names, each keyed by
# the downstream_duties[].duty value that signals the topic came up in this run.
_DUTY_SIBLING_MAP = {
    "locate_personal_data_ropa": (
        "ropa",
        "Locating the personal data for this request — ropa's Art. 30 register (and its "
        "JSON sidecar) is the authoritative inventory of where it lives.",
    ),
    "objection_rebalancing_legitimate_interest": (
        "legitimate-interest",
        "Art. 21(1) general objection: the compelling-grounds re-assessment runs in the "
        "legitimate-interest skill.",
    ),
    "processor_assistance_dpa28": (
        "dpa-art28",
        "This request reached (or must be routed to) a processor — dpa-art28 covers the "
        "Art. 28(3)(e) assistance duty.",
    ),
    "notice_accuracy_privacy_notice": (
        "privacy-notice-eu",
        "Handling this request surfaced a privacy-notice accuracy gap — flag it via the "
        "privacy-notice-eu skill.",
    ),
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _generated_at(sidecar: dict) -> str:
    """The sidecar's own `generated_at` is untrusted input: a malformed sidecar can carry
    `null`, a number, or anything else JSON allows there. Fall back to now rather than ever
    copying a non-string or malformed value through."""
    value = sidecar.get("generated_at")
    if isinstance(value, str) and _DATETIME_RE.match(value):
        return value
    return _now_iso()


def _subject(sidecar: dict) -> dict:
    request = sidecar.get("request")
    if not isinstance(request, dict):
        request = {}
    req_id = request.get("id")
    rights = sidecar.get("rights_invoked")
    rights_label = ", ".join(sorted(str(r) for r in rights)) if isinstance(rights, list) and rights \
        else "no rights recorded"
    if isinstance(req_id, str) and req_id.strip():
        subject_id = req_id.strip()
    else:
        subject_id = _UNKNOWN_REQUEST_ID
    return {
        "id": subject_id,
        "label": f"DSR request {subject_id} ({rights_label})",
        "type": "other",
    }


def _outcome_summary(sidecar: dict) -> str:
    rights = sidecar.get("rights_invoked")
    rights_label = ", ".join(sorted(str(r) for r in rights)) if isinstance(rights, list) and rights \
        else "no rights recorded"
    decision = sidecar.get("decision")
    decision_label = decision if isinstance(decision, str) and decision else "no decision recorded"
    return f"Rights invoked: {rights_label}. Decision: {decision_label}."


def _gap(f: dict) -> dict:
    """A single validation.findings[] entry, defensively read (a malformed sidecar's own
    validation.findings[] may contain a non-dict entry)."""
    return {
        "id": f.get("entry_id") or f.get("rule_id") or "gap",
        "severity": f.get("severity") or "rejection",
        "message": f.get("message") or "(no message on this finding)",
    }


def _duties(sidecar: dict) -> list:
    duties = sidecar.get("downstream_duties")
    return duties if isinstance(duties, list) else []


def _duty_gaps(duties: list) -> list:
    out = []
    for entry in duties:
        if not isinstance(entry, dict):
            continue
        duty = entry.get("duty")
        if duty in _GAP_DUTIES and entry.get("discharged") is not True:
            out.append({
                "id": duty,
                "severity": "warning",
                "message": f"Downstream duty '{duty}' is not yet discharged.",
            })
    return out


def _handoffs_and_unknowns(duties: list):
    present = set()
    handoffs = []
    for entry in duties:
        if not isinstance(entry, dict):
            continue
        duty = entry.get("duty")
        mapping = _DUTY_SIBLING_MAP.get(duty)
        if mapping is None or duty in present:
            continue
        present.add(duty)
        sibling, reason = mapping
        handoffs.append({"sibling_skill": sibling, "reason": reason})
    unknowns = []
    for duty, (sibling, _reason) in _DUTY_SIBLING_MAP.items():
        if duty not in present:
            unknowns.append({
                "id": f"unrecorded-handoff-{sibling}",
                "question": f"Whether this request needed the '{sibling}' sibling handoff "
                             f"({duty}) was not recorded in downstream_duties for this run.",
                "blocking": False,
            })
    return handoffs, unknowns


def _sources() -> list:
    """Read sources.lock.json live from disk — never a hard-coded constant. For a
    structural-tier skill with no per-run source selection, every declared reference file
    backs any DSR triage this validator ran against."""
    lock_path = Path(__file__).resolve().parents[2] / "sources.lock.json"
    try:
        manifest = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    files = manifest.get("files")
    if not isinstance(files, dict):
        return []
    out = []
    for path, entry in sorted(files.items()):
        if not isinstance(entry, dict):
            continue
        last_verified = entry.get("last_verified")
        if not isinstance(last_verified, str):
            continue
        out.append({
            "id": path,
            "citation": entry.get("url") or path,
            "last_verified": last_verified,
        })
    return out


def to_core_artefact(sidecar: dict, *, skill_version: str) -> dict:
    validation = sidecar.get("validation")
    if not isinstance(validation, dict):
        validation = {}
    validation_findings = validation.get("findings")
    if not isinstance(validation_findings, list):
        validation_findings = []
    duties = _duties(sidecar)
    handoffs, unknowns = _handoffs_and_unknowns(duties)
    gaps = [_gap(f) for f in validation_findings if isinstance(f, dict)] + _duty_gaps(duties)
    return {
        "artefact_schema_version": ARTEFACT_SCHEMA_VERSION,
        "skill": SKILL_NAME,
        "skill_version": skill_version,
        "generated_at": _generated_at(sidecar),
        "subject": _subject(sidecar),
        "outcome": {
            "status": _OUTCOME_BY_VALIDATION_STATUS.get(
                validation.get("status", "passed"), "provisional"),
            "summary": _outcome_summary(sidecar),
        },
        "gaps": gaps,
        "sources": _sources(),
        "handoffs": handoffs,
        "unknowns": unknowns,
    }


def blocked_artefact(*, skill_version: str, reason: str) -> dict:
    """Minimal, always schema-valid artefact for when `to_core_artefact` itself raises
    despite the guards above (defence in depth — mirrors dsr_validator.runner.validate()'s
    per-rule exception handler)."""
    return {
        "artefact_schema_version": ARTEFACT_SCHEMA_VERSION,
        "skill": SKILL_NAME,
        "skill_version": skill_version,
        "generated_at": _now_iso(),
        "subject": {"id": _UNKNOWN_REQUEST_ID, "label": "unknown DSR request", "type": "other"},
        "outcome": {
            "status": "blocked",
            "summary": f"Core artefact adapter failed: {reason}",
        },
        "gaps": [{
            "id": "core-artefact-adapter-error",
            "severity": "rejection",
            "message": f"to_core_artefact raised: {reason}",
        }],
        "sources": [],
        "handoffs": [],
        "unknowns": [],
    }
