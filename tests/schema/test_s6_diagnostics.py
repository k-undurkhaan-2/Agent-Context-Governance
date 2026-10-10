"""S6 structured diagnostics and Phase-1 proof-boundary checks."""

from unittest.mock import patch

import pytest

from contextctl_schema import _static_core as static_core
from tests.schema.s6_fixture_runner import (
    CASES_BY_ID,
    ValidatorCapabilityError,
    collect_schema_diagnostics,
    evaluate_case,
    json_pointer,
    run_schema_case,
    run_static_case_without_proofs,
    schema_instance,
    schema_reference,
    case_payload,
)
from tests.schema.test_resource_schemas import source_registry


def test_json_pointer_tokens_are_escaped_exactly() -> None:
    assert json_pointer(("a/b", "c~d", 0)) == "/a~1b/c~0d/0"


def test_schema_diagnostics_are_structured_and_deterministic() -> None:
    case = CASES_BY_ID["schema.resource.domain.negative.unknown-depth-001"]
    first = run_schema_case(case)
    second = run_schema_case(case)
    assert first == second
    assert first
    assert tuple(item.identity for item in first) == tuple(
        sorted(item.identity for item in first)
    )
    for diagnostic in first:
        assert diagnostic.schema_resource_id.startswith("urn:uuid:")
        assert diagnostic.instance_pointer == "" or diagnostic.instance_pointer.startswith("/")
        assert diagnostic.schema_pointer.startswith("/")
        assert diagnostic.keyword


def test_static_negative_uses_stable_diagnostic_code() -> None:
    result = evaluate_case("static.sg001.index.negative.duplicate-path-different-content")
    assert result.actual_result == "REJECT"
    assert result.static_status == "INVALID"
    assert result.declared_diagnostic_identity == "S4.ARRAY.31"
    assert "S4.ARRAY.31" in result.actual_diagnostic_identities


def test_ordinary_decoded_input_cannot_claim_full_static_acceptance() -> None:
    case_id = "static.bundle.positive.multi-domain-declared-overlap"
    untrusted = run_static_case_without_proofs(case_id)
    assert untrusted.status == "PROOF_REQUIRED"
    assert untrusted.full_static_acceptance is False
    assert untrusted.required_proofs
    assert any(item.requirement_id == "PROOF.INPUT" for item in untrusted.required_proofs)

    explicit_test_result = evaluate_case(case_id)
    assert explicit_test_result.actual_result == "ACCEPT"
    assert explicit_test_result.static_status == "PASS"
    assert explicit_test_result.proof_treatment == "explicit-test-only-synthetic-proof"


def test_validator_failure_is_not_reported_as_a_valid_empty_result() -> None:
    case = CASES_BY_ID["schema.container.receipt-delivery-result.positive"]
    payload = case_payload(case)

    class BrokenValidator:
        def iter_errors(self, _instance):
            raise RuntimeError("synthetic unavailable capability")

    with pytest.raises(ValidatorCapabilityError):
        collect_schema_diagnostics(
            schema_instance(payload),
            schema_reference(case, payload),
            validator=BrokenValidator(),
        )


def test_structural_validator_unavailability_remains_proof_required() -> None:
    case = CASES_BY_ID["static.bundle.positive.multi-domain-declared-overlap"]
    payload = case_payload(case)
    with patch.object(static_core, "build_registry", side_effect=RuntimeError("unavailable")):
        from contextctl_schema.static_validation import validate_governance_bundle

        result = validate_governance_bundle(payload["subject"])
    assert result.status == "PROOF_REQUIRED"
    assert result.full_static_acceptance is False
    assert any(
        diagnostic.keyword == "VALIDATOR.STRUCTURED_ERRORS"
        for diagnostic in result.diagnostics
    )


def test_deferred_case_is_preserved_without_schema_or_static_promotion() -> None:
    result = evaluate_case("model.raw.decoder.negative.duplicate-json-key")
    assert result.execution_mode == "deferred-preserved"
    assert result.actual_result == "DEFERRED_PRESERVED"
    assert result.static_status is None
    assert result.schema_diagnostics == ()


def test_source_registry_patch_is_test_scoped() -> None:
    # This check documents that source binding is a test-only patch, not a
    # production registry configuration or caller-selectable retrieval path.
    with patch.object(static_core, "build_registry", source_registry):
        assert static_core.build_registry() is source_registry()
