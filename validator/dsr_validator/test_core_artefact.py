"""Tests for dsr_validator.core_artefact.to_core_artefact."""
import json
from pathlib import Path

import jsonschema
import pytest

from dsr_validator.core_artefact import to_core_artefact, blocked_artefact
from dsr_validator._schema_paths import find_schema

_ARTEFACT_SCHEMA = json.loads(
    find_schema("skill-artefact-1.1.schema.json").read_text(encoding="utf-8")
)


def _native() -> dict:
    return {
        "schema_version": "1.0",
        "generated_by": "data-subject-rights skill v1.2",
        "generated_at": "2026-09-24T09:12:00Z",
        "request": {
            "id": "dsr-2026-0091",
            "intake_date": "2026-09-01",
            "channel": "privacy@example.com",
            "requester_relationship": "customer",
            "text": "Please send me a copy of the personal data you hold about me.",
        },
        "rights_invoked": ["art15"],
        "identity_verification": {"verified": True, "reasonable_doubts": False},
        "decision": "grant",
        "deadline": {"computed_date": "2026-10-01", "extended": False},
        "downstream_duties": [],
        "validation": {"status": "passed", "findings": []},
    }


def test_projection_is_schema_valid():
    jsonschema.validate(to_core_artefact(_native(), skill_version="1.2"), _ARTEFACT_SCHEMA)


def test_subject_is_derived_from_the_request():
    doc = to_core_artefact(_native(), skill_version="1.2")
    assert doc["subject"]["id"] == "dsr-2026-0091"
    assert doc["subject"]["type"] == "other"
    assert "art15" in doc["subject"]["label"]


def test_subject_id_is_an_unmistakable_placeholder_when_request_is_entirely_absent():
    native = _native()
    del native["request"]
    doc = to_core_artefact(native, skill_version="1.2")
    assert doc["subject"]["id"] == "unknown-request"
    assert doc["subject"]["type"] == "other"


def test_outcome_summary_names_rights_and_decision():
    doc = to_core_artefact(_native(), skill_version="1.2")
    assert "art15" in doc["outcome"]["summary"]
    assert "grant" in doc["outcome"]["summary"]


def test_native_artefact_is_not_mutated():
    native = _native()
    before = json.dumps(native, sort_keys=True)
    to_core_artefact(native, skill_version="1.2")
    assert json.dumps(native, sort_keys=True) == before


def test_validation_findings_project_into_gaps_and_document_still_validates():
    native = _native()
    native["validation"] = {
        "status": "passed_with_warnings",
        "findings": [
            {"rule_id": "SRC-1", "category": "freshness", "severity": "warning",
             "message": "Evidence is nearing staleness.", "entry_id": "references/templates.md"},
        ],
    }
    doc = to_core_artefact(native, skill_version="1.2")
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert doc["gaps"] == [{"id": "references/templates.md", "severity": "warning",
                            "message": "Evidence is nearing staleness."}]
    assert doc["outcome"]["status"] == "provisional"


def test_undischarged_plain_downstream_duty_becomes_a_gap_not_a_handoff():
    native = _native()
    native["downstream_duties"] = [
        {"duty": "art19_third_party_notification", "discharged": False},
    ]
    doc = to_core_artefact(native, skill_version="1.2")
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert {"id": "art19_third_party_notification", "severity": "warning",
            "message": "Downstream duty 'art19_third_party_notification' is not yet discharged."} \
        in doc["gaps"]
    assert doc["handoffs"] == []


def test_discharged_plain_downstream_duty_is_not_a_gap():
    native = _native()
    native["downstream_duties"] = [
        {"duty": "art19_third_party_notification", "discharged": True},
    ]
    doc = to_core_artefact(native, skill_version="1.2")
    assert doc["gaps"] == []


@pytest.mark.parametrize("duty,sibling", [
    ("locate_personal_data_ropa", "ropa"),
    ("objection_rebalancing_legitimate_interest", "legitimate-interest"),
    ("processor_assistance_dpa28", "dpa-art28"),
    ("notice_accuracy_privacy_notice", "privacy-notice-eu"),
])
def test_sibling_duty_present_becomes_a_handoff_regardless_of_discharged(duty, sibling):
    native = _native()
    native["downstream_duties"] = [{"duty": duty, "discharged": True}]
    doc = to_core_artefact(native, skill_version="1.2")
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert {"sibling_skill": sibling, "reason": doc["handoffs"][0]["reason"]} in doc["handoffs"]
    # A discharged sibling duty is a handoff, never also a plain gap.
    assert doc["gaps"] == []


def test_all_four_siblings_absent_become_unknowns_not_silently_dropped():
    doc = to_core_artefact(_native(), skill_version="1.2")  # downstream_duties == []
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert doc["handoffs"] == []
    unknown_siblings = {u["id"] for u in doc["unknowns"]}
    assert unknown_siblings == {
        "unrecorded-handoff-ropa",
        "unrecorded-handoff-legitimate-interest",
        "unrecorded-handoff-dpa-art28",
        "unrecorded-handoff-privacy-notice-eu",
    }
    assert all(u["blocking"] is False for u in doc["unknowns"])


def test_sources_are_populated_from_the_live_sources_lock_file():
    doc = to_core_artefact(_native(), skill_version="1.2")
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert doc["sources"], "sources[] must not be hard-coded empty"
    ids = {s["id"] for s in doc["sources"]}
    assert "references/procedural-framework.md" in ids


def test_blocked_artefact_is_schema_valid_and_carries_the_reason():
    doc = blocked_artefact(skill_version="1.2", reason="ValueError: boom")
    jsonschema.validate(doc, _ARTEFACT_SCHEMA)
    assert doc["outcome"]["status"] == "blocked"
    assert "boom" in doc["gaps"][0]["message"]
    assert doc["subject"]["type"] == "other"
