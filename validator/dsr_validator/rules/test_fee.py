import json
from pathlib import Path

from dsr_validator.rules.fee import fee_requires_art12_5_ground
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_minimal_clean_fixture_has_no_fee_field_and_is_silent():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert "fee" not in sidecar
    assert fee_requires_art12_5_ground(sidecar, _ctx()) == []


def test_fee_charged_without_ground_is_rejected():
    sidecar = json.loads(
        (FIX / "must_fail" / "FEE-1__charged-first-copy-no-ground.json").read_text())
    findings = fee_requires_art12_5_ground(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "FEE-1"
    assert findings[0].severity == "rejection"


def test_fee_charged_for_further_copy_passes():
    sidecar = json.loads(
        (FIX / "must_pass" / "FEE-1__further-copy-charged.json").read_text())
    assert fee_requires_art12_5_ground(sidecar, _ctx()) == []


def test_fee_charged_for_manifestly_unfounded_passes():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["fee"] = {"charged": True, "ground": "manifestly_unfounded_or_excessive"}
    assert fee_requires_art12_5_ground(sidecar, _ctx()) == []


def test_fee_present_but_not_charged_is_silent():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["fee"] = {"charged": False}
    assert fee_requires_art12_5_ground(sidecar, _ctx()) == []


def test_fee_with_invalid_ground_is_rejected():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["fee"] = {"charged": True, "ground": "first_copy_admin_cost"}
    findings = fee_requires_art12_5_ground(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "FEE-1"


def test_malformed_fee_does_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["fee"] = "not-a-dict"
    assert fee_requires_art12_5_ground(sidecar, _ctx()) == []
