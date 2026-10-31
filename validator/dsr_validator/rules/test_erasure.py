import json
from pathlib import Path

from dsr_validator.rules.erasure import erasure_decision_ground_and_exception_consistency
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_minimal_clean_fixture_is_not_art17_and_is_silent():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert "art17" not in sidecar["rights_invoked"]
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_refuse_with_no_ground_is_rejected():
    sidecar = json.loads(
        (FIX / "must_fail" / "ERASURE-1__refuse-no-ground.json").read_text())
    findings = erasure_decision_ground_and_exception_consistency(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "ERASURE-1"
    assert findings[0].severity == "rejection"


def test_refuse_with_ground_passes():
    sidecar = json.loads(
        (FIX / "must_pass" / "ERASURE-1__refuse-with-ground.json").read_text())
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_grant_despite_recorded_retention_exception_is_rejected():
    sidecar = json.loads(
        (FIX / "must_fail" / "ERASURE-1__grant-despite-retention-exception.json").read_text())
    findings = erasure_decision_ground_and_exception_consistency(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "ERASURE-1"


def test_partial_grant_with_recorded_exception_passes():
    sidecar = json.loads(
        (FIX / "must_pass" / "ERASURE-1__partial-grant-with-exception.json").read_text())
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_grant_with_no_exception_recorded_passes():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    sidecar["decision"] = "grant"
    sidecar["erasure_decision"] = {"ground_examined": "b"}
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_grant_with_exception_none_passes():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    sidecar["decision"] = "grant"
    sidecar["erasure_decision"] = {"ground_examined": "b", "exception_relied_on": "none"}
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_not_an_art17_request_is_silent_even_with_refuse():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["decision"] = "refuse"
    assert erasure_decision_ground_and_exception_consistency(sidecar, _ctx()) == []


def test_malformed_erasure_decision_does_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    sidecar["decision"] = "refuse"
    sidecar["erasure_decision"] = "not-a-dict"
    findings = erasure_decision_ground_and_exception_consistency(sidecar, _ctx())
    # erasure_decision is malformed -> treated as absent -> refuse-with-no-ground still fires
    assert len(findings) == 1
    assert findings[0].rule_id == "ERASURE-1"
