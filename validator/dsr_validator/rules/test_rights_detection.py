import json
from pathlib import Path

from dsr_validator.rules.rights_detection import art17_request_should_not_drop_art15_component
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_minimal_clean_fixture_is_silent():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert art17_request_should_not_drop_art15_component(sidecar, _ctx()) == []


def test_fires_when_art17_only_but_text_plainly_asks_an_access_question():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    sidecar["request"]["text"] = "Please delete everything and tell me what you have on me."
    findings = art17_request_should_not_drop_art15_component(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "RIGHTS-1"
    assert findings[0].severity == "warning"


def test_silent_when_art15_already_present():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art15", "art17"]
    sidecar["request"]["text"] = "Please delete everything and tell me what you have on me."
    assert art17_request_should_not_drop_art15_component(sidecar, _ctx()) == []


def test_silent_when_no_trigger_phrase_present():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    sidecar["request"]["text"] = "Please delete my account."
    assert art17_request_should_not_drop_art15_component(sidecar, _ctx()) == []


def test_missing_text_does_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["rights_invoked"] = ["art17"]
    del sidecar["request"]["text"]
    assert art17_request_should_not_drop_art15_component(sidecar, _ctx()) == []
