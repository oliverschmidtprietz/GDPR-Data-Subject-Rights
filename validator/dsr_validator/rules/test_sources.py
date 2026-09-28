import json
from pathlib import Path

from dsr_validator.rules.sources import source_manifest_coverage_and_freshness
from dsr_validator.runner import Context

VALIDATOR = Path(__file__).resolve().parents[2]
SCHEMA = VALIDATOR.parent / "references" / "dsr-sidecar-schema.json"
FIX = VALIDATOR / "fixtures"
REFS = VALIDATOR.parent / "references"


def _ctx(**kwargs):
    return Context(mode="internal", schema_path=SCHEMA, references_dir=REFS, **kwargs)


def test_real_sources_lock_covers_every_on_disk_reference_file():
    sidecar = json.loads((FIX / "must_pass" / "minimal-clean.json").read_text())
    findings = source_manifest_coverage_and_freshness(sidecar, _ctx())
    missing_file_findings = [f for f in findings if f.entry_type == "reference_file"]
    assert missing_file_findings == [], missing_file_findings


def test_missing_manifest_is_reported_not_raised(tmp_path):
    sidecar = {}
    ctx = Context(mode="internal", schema_path=SCHEMA, references_dir=tmp_path / "references")
    findings = source_manifest_coverage_and_freshness(sidecar, ctx)
    assert len(findings) == 1
    assert findings[0].rule_id == "SRC-1"
    assert findings[0].severity == "warning"


def test_stale_entry_is_flagged():
    sidecar = {}
    override = {"files": {"references/procedural-framework.md": {"last_verified": "2020-01-01"}}}
    ctx = _ctx(sources_lock_override=override)
    findings = source_manifest_coverage_and_freshness(sidecar, ctx)
    assert any(f.field == "last_verified" for f in findings)


def test_malformed_override_is_reported_not_raised():
    sidecar = {}
    ctx = _ctx(sources_lock_override=["not", "a", "dict"])
    findings = source_manifest_coverage_and_freshness(sidecar, ctx)
    assert len(findings) == 1
    assert "not a JSON object" in findings[0].message
