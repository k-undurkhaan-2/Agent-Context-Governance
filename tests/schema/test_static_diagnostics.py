"""Deterministic structured diagnostics, bounded prose and failure ownership."""

from copy import deepcopy
import pytest
from contextctl_schema import _static_core as core
from contextctl_schema.static_validation import validate_governance_bundle
from tests.schema.s4_synthetic import proofs, bundle, context


def test_diagnostics_ignore_mapping_iteration_order(proofs):
    value = bundle()
    value["unsafe/field"] = "sensitive-invalid-example"
    value["project"]["spec"]["unexpected"] = 123
    other = dict(reversed(list(value.items())))
    first, second = (validate_governance_bundle(v, proof_context=proofs.context) for v in (value, other))
    assert first.diagnostics == second.diagnostics
    assert first.status == "INVALID"
    for d in first.diagnostics:
        assert "sensitive-invalid-example" not in d.message
        assert "unsafe/field" not in d.message
        assert d.schema_id and d.keyword
        assert d.schema_pointer is not None


def test_missing_validator_is_distinct_from_empty_findings(monkeypatch):
    def broken():
        raise RuntimeError("synthetic private exception text")
    monkeypatch.setattr(core, "build_registry", broken)
    result = validate_governance_bundle(bundle())
    assert result.status == "PROOF_REQUIRED"
    assert result.direct_checks_passed is None
    assert all("exception text" not in d.message for d in result.diagnostics)


def test_diagnostic_order_and_fixed_explanations():
    ctx = context()
    ctx.check("Z", False, "/b")
    ctx.check("A", False, "/a")
    ctx.check("A", False, "/a")
    result = core._finish_result("governance-bundle", ctx)
    assert [d.code for d in result.diagnostics] == ["S4.A", "S4.Z"]
    assert result.direct_checks_passed is False and not result.full_static_acceptance


def test_invalid_wins_over_missing_external_proof():
    ctx = context()
    ctx.unavailable("PROOF.INPUT")
    ctx.check("BUNDLE.REFERENCES", False)
    result = core._finish_result("governance-bundle", ctx)
    assert result.status == "INVALID"
    assert result.required_proofs
