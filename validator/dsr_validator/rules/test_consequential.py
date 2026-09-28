import json
from pathlib import Path

from dsr_validator.rules.consequential import grant_requires_verified_identity_when_doubted
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"


def _ctx():
    return Context(mode="internal", schema_path=SCHEMA, references_dir=VALIDATOR.parent / "references")


def test_fires_on_grant_with_doubted_unverified_identity():
    sidecar = json.loads(
        (FIX / "must_fail" / "CONSEQ-1__grant-without-verified-identity.json").read_text())
    findings = grant_requires_verified_identity_when_doubted(sidecar, _ctx())
    assert len(findings) == 1
    assert findings[0].rule_id == "CONSEQ-1"
    assert findings[0].severity == "rejection"


def test_fires_on_partial_too():
    sidecar = json.loads(
        (FIX / "must_fail" / "CONSEQ-1__grant-without-verified-identity.json").read_text())
    sidecar["decision"] = "partial"
    findings = grant_requires_verified_identity_when_doubted(sidecar, _ctx())
    assert len(findings) == 1


def test_silent_on_refuse_even_with_doubted_unverified_identity():
    sidecar = json.loads(
        (FIX / "must_fail" / "CONSEQ-1__grant-without-verified-identity.json").read_text())
    sidecar["decision"] = "refuse"
    assert grant_requires_verified_identity_when_doubted(sidecar, _ctx()) == []


def test_silent_when_no_reasonable_doubts_were_ever_raised():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    assert sidecar["identity_verification"]["reasonable_doubts"] is False
    assert grant_requires_verified_identity_when_doubted(sidecar, _ctx()) == []


def test_silent_when_doubts_were_raised_and_resolved():
    sidecar = json.loads(
        (FIX / "must_fail" / "CONSEQ-1__grant-without-verified-identity.json").read_text())
    sidecar["identity_verification"]["verified"] = True
    assert grant_requires_verified_identity_when_doubted(sidecar, _ctx()) == []


def test_malformed_identity_verification_does_not_raise():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    sidecar["identity_verification"] = "not-a-dict"
    assert grant_requires_verified_identity_when_doubted(sidecar, _ctx()) == []
