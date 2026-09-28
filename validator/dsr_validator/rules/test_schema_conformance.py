import json
from pathlib import Path

from dsr_validator.rules.schema_conformance import schema_conformance
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_minimal_clean_fixture_has_no_schema_violations():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert schema_conformance(sidecar, _ctx()) == []


def test_missing_required_field_is_reported_not_raised():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    del sidecar["decision"]
    findings = schema_conformance(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "SCHEMA-1"
    assert findings[0].severity == "rejection"


def test_bad_enum_value_is_reported():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["decision"] = "approve"  # not in the enum
    findings = schema_conformance(sidecar, _ctx())
    assert any(f.rule_id == "SCHEMA-1" for f in findings)
