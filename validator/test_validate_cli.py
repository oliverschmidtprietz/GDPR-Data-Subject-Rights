"""CLI-level fail-closed tests for validate.py (break-it test 2026-10-02, X1).

The file-read/parse step must never crash with a raw traceback on missing
file, unreadable file, invalid UTF-8, invalid JSON, or a non-object
top-level JSON value — it must print a clean one-line message and exit 1.
No exit code was previously defined for bad input in this skill's docs, so
this follows the FIX-BRIEF default: exit 1, consistent with the runner's
own `status == "failed"` exit code.
"""
import json
from pathlib import Path

import pytest

import validate  # the validator/validate.py CLI module itself

FIX = Path(__file__).resolve().parent / "fixtures"


def test_missing_file_fails_closed(tmp_path, capsys):
    missing = tmp_path / "does-not-exist.json"
    rc = validate.main([str(missing)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert "not found" in out


def test_invalid_json_fails_closed(tmp_path, capsys):
    bad = tmp_path / "bad.json"
    bad.write_text("{ not valid json", encoding="utf-8")
    rc = validate.main([str(bad)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert "not valid JSON" in out


def test_top_level_array_fails_closed(tmp_path, capsys):
    arr = tmp_path / "array.json"
    arr.write_text("[]", encoding="utf-8")
    rc = validate.main([str(arr)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert "must be an object" in out


def test_top_level_null_fails_closed(tmp_path, capsys):
    nul = tmp_path / "null.json"
    nul.write_text("null", encoding="utf-8")
    rc = validate.main([str(nul)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert "must be an object" in out


def test_invalid_utf8_fails_closed(tmp_path, capsys):
    bad = tmp_path / "bad-utf8.json"
    bad.write_bytes(b"\xff\xfe{bad")
    rc = validate.main([str(bad)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert "UTF-8" in out


def test_directory_instead_of_file_fails_closed(tmp_path, capsys):
    rc = validate.main([str(tmp_path)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out


def test_emit_core_artefact_with_non_object_top_level_never_reaches_the_adapter(tmp_path, capsys):
    # Regression for the generic X1 TypeError at the old line 62 ({**sidecar, ...} on a
    # non-dict): the top-level-object check now rejects before --emit-core-artefact runs.
    arr = tmp_path / "array.json"
    arr.write_text("[]", encoding="utf-8")
    artefact_path = tmp_path / "artefact.json"
    rc = validate.main([str(arr), "--emit-core-artefact", str(artefact_path)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "Traceback" not in out
    assert not artefact_path.exists()


def test_clean_fixture_still_passes(capsys):
    rc = validate.main([str(FIX / "must_pass" / "minimal-clean.json")])
    out = capsys.readouterr().out
    assert rc == 0
    assert "status: passed" in out
