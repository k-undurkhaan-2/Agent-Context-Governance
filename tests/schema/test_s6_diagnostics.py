"""S6 structured diagnostics and Phase-1 proof-boundary checks."""

from dataclasses import replace
from unittest.mock import patch

import pytest

from contextctl_schema import _static_core as static_core
from tests.schema.s6_fixture_runner import (
    CASES_BY_ID,
    DiagnosticAttributionError,
    SchemaDiagnostic,
    StaticDiagnosticIdentity,
    ValidatorCapabilityError,
    collect_schema_diagnostics,
    compare_diagnostic_identity_sets,
    evaluate_case,
    expected_typed_diagnostics,
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


@pytest.mark.parametrize(
    "case_id,expected_identity",
    [
        (
            "schema.resource.domain.negative.envelope-wrong-api",
            "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864"
            "|/apiVersion|/$defs/apiVersion/const|const",
        ),
        (
            "schema.resource.domain.negative.unknown-depth-006",
            "urn:uuid:d5cecdb5-eadf-491d-80c6-869a7f4d10d9"
            "|/spec/permissions|/$defs/permissions/additionalProperties"
            "|additionalProperties",
        ),
        (
            "schema.resource.hostoverlay.negative.unknown-depth-006",
            "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864"
            "|/spec/repositoryIdentity/acceptedRemotes/0"
            "|/$defs/structuredRemote/additionalProperties|additionalProperties",
        ),
    ],
)
def test_cross_resource_ref_diagnostics_retain_exact_catalog_attribution(
    case_id: str, expected_identity: str
) -> None:
    diagnostics = run_schema_case(case_id)
    assert tuple(item.identity for item in diagnostics) == (expected_identity,)


def test_unknown_schema_object_attribution_fails_explicitly() -> None:
    unknown_schema = {"type": "integer"}

    class UnknownLocationError:
        schema = unknown_schema
        validator = "type"
        absolute_path = ()

    class UnknownLocationValidator:
        def iter_errors(self, _instance):
            return (UnknownLocationError(),)

    with pytest.raises(
        DiagnosticAttributionError, match="unknown Schema object location"
    ):
        collect_schema_diagnostics(
            "not-an-integer",
            "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864#/$defs/apiVersion",
            validator=UnknownLocationValidator(),
        )


def test_ambiguous_schema_object_attribution_fails_explicitly() -> None:
    ambiguous_schema = {"type": "integer"}

    class AmbiguousLocationError:
        schema = ambiguous_schema
        validator = "type"
        absolute_path = ()

    class AmbiguousLocationValidator:
        def iter_errors(self, _instance):
            return (AmbiguousLocationError(),)

    ambiguous_locations = {
        id(ambiguous_schema): (
            ("urn:uuid:00000000-0000-4000-8000-000000000001", "/$defs/a"),
            ("urn:uuid:00000000-0000-4000-8000-000000000002", "/$defs/b"),
        )
    }
    with patch(
        "tests.schema.s6_fixture_runner._schema_locations",
        return_value=ambiguous_locations,
    ):
        with pytest.raises(
            DiagnosticAttributionError, match="ambiguous Schema object location"
        ):
            collect_schema_diagnostics(
                "not-an-integer",
                "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864#/$defs/apiVersion",
                validator=AmbiguousLocationValidator(),
            )


def test_static_negative_uses_stable_diagnostic_code() -> None:
    result = evaluate_case("static.sg001.index.negative.duplicate-path-different-content")
    assert result.actual_result == "REJECT"
    assert result.static_status == "INVALID"
    assert result.declared_diagnostic_identity == "S4.ARRAY.31"
    assert result.actual_diagnostic_identities == ("S4.ARRAY.31",)


def test_schema_diagnostic_v1_reports_missing_and_unexpected_identities() -> None:
    case_id = "schema.branch-policy.negative.01-empty-prefix"
    expected = expected_typed_diagnostics(case_id)
    assert expected is not None and len(expected) == 3

    missing = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, expected[1:]
    )
    assert missing.status == "EXACT_SET_MISMATCH"
    assert missing.missing == (expected[0],)
    assert missing.unexpected == ()

    extra = SchemaDiagnostic(
        schema_resource_id="urn:uuid:78833fbe-1819-45db-824c-2edb235f2864",
        instance_pointer="",
        schema_pointer="/$defs/branchPrefix/description",
        keyword="description",
    )
    unexpected = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, (*expected, extra)
    )
    assert unexpected.status == "EXACT_SET_MISMATCH"
    assert unexpected.missing == ()
    assert unexpected.unexpected == (extra,)


def test_schema_ref_batch01_rejects_missing_and_unexpected_diagnostics() -> None:
    case_id = "schema.common.branchref.negative.ref-0"
    expected = expected_typed_diagnostics(case_id)
    assert expected is not None and len(expected) == 3

    missing = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, expected[1:]
    )
    assert missing.status == "EXACT_SET_MISMATCH"
    assert missing.missing == (expected[0],)
    assert missing.unexpected == ()

    extra = SchemaDiagnostic(
        schema_resource_id="urn:uuid:78833fbe-1819-45db-824c-2edb235f2864",
        instance_pointer="",
        schema_pointer="/$defs/branchRef/description",
        keyword="description",
    )
    unexpected = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, (*expected, extra)
    )
    assert unexpected.status == "EXACT_SET_MISMATCH"
    assert unexpected.missing == ()
    assert unexpected.unexpected == (extra,)

    result = evaluate_case(case_id)
    assert result.schema_diagnostics == expected
    assert result.oracle_status == "EXACT_MATCH"


def test_schema_text_batch02_rejects_missing_and_unexpected_diagnostics() -> None:
    case_id = "schema.common.displaytext.negative.empty"
    expected = expected_typed_diagnostics(case_id)
    assert expected is not None and len(expected) == 2

    missing = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, expected[1:]
    )
    assert missing.status == "EXACT_SET_MISMATCH"
    assert missing.missing == (expected[0],)
    assert missing.unexpected == ()

    extra = SchemaDiagnostic(
        schema_resource_id="urn:uuid:78833fbe-1819-45db-824c-2edb235f2864",
        instance_pointer="",
        schema_pointer="/$defs/displayText/description",
        keyword="description",
    )
    unexpected = compare_diagnostic_identity_sets(
        "schema-diagnostic-v1", expected, (*expected, extra)
    )
    assert unexpected.status == "EXACT_SET_MISMATCH"
    assert unexpected.missing == ()
    assert unexpected.unexpected == (extra,)

    result = evaluate_case(case_id)
    assert result.schema_diagnostics == expected
    assert result.oracle_status == "EXACT_MATCH"


def test_static_diagnostic_v1_uses_every_public_field_and_exact_sets() -> None:
    case_id = "phase1-static.branch-policy.negative.16-no-allow-match"
    expected = expected_typed_diagnostics(case_id)
    assert expected is not None and len(expected) == 1
    identity = expected[0]
    assert isinstance(identity, StaticDiagnosticIdentity)
    assert identity == StaticDiagnosticIdentity(
        code="S4.BRANCH.STATIC",
        subject_id="00000000-0000-4000-8000-000000000116",
        instance_pointer="/spec/expectedBaseline/ref",
        predicate_family="branch-policy",
        schema_id=None,
        schema_pointer=None,
        keyword="BRANCH.STATIC",
    )

    missing = compare_diagnostic_identity_sets("static-diagnostic-v1", expected, ())
    assert missing.status == "EXACT_SET_MISMATCH"
    assert missing.missing == expected
    assert missing.unexpected == ()

    extra = replace(identity, code="S4.BRANCH.UNEXPECTED")
    unexpected = compare_diagnostic_identity_sets(
        "static-diagnostic-v1", expected, (*expected, extra)
    )
    assert unexpected.status == "EXACT_SET_MISMATCH"
    assert unexpected.missing == ()
    assert unexpected.unexpected == (extra,)

    result = evaluate_case(case_id)
    assert result.static_diagnostics == expected
    assert result.oracle_status == "EXACT_MATCH"


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
