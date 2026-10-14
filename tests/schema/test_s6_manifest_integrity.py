"""S6 integrity checks for the authenticated forward-only Manifest v3 inventory."""

from collections import Counter
from copy import deepcopy
import hashlib

import pytest

from tests.schema.s6_fixture_runner import (
    CANDIDATE_MANIFEST_GIT_BLOB,
    CANDIDATE_MANIFEST_SHA256,
    CASES,
    CONTROL_PATHS,
    EXPECTED_ASSET_COUNT,
    EXPECTED_CASE_COUNT,
    EXPECTED_CORRECTED_INVENTORY_COUNT,
    EXPECTED_CONTROL_COUNT,
    EXPECTED_DEFERRED_COUNT,
    EXPECTED_EXECUTABLE_COUNT,
    EXPECTED_EXECUTION_MODE_COUNTS,
    EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT,
    EXPECTED_INVENTORY_FORMAT_VERSION,
    EXPECTED_OPEN_PHASE1_GAP_COUNT,
    EXPECTED_TRACE_ONLY_COUNT,
    EXPECTED_UNCHANGED_EOL_SENSITIVE_ASSET_COUNT,
    EXPECTED_UTF8_JSON_ASSET_COUNT,
    FIXTURE_CONTRACT,
    MANIFEST,
    MANIFEST_EOL_ADJUSTED,
    MANIFEST_GIT_BLOB,
    MANIFEST_PHYSICAL_SHA256,
    MANIFEST_SHA256,
    SCHEMA_IDENTIFIER_BATCH03_CASE_IDS,
    SCHEMA_REF_BATCH01_CASE_IDS,
    SCHEMA_TEXT_BATCH02_CASE_IDS,
    V2_CORRECTION_ASSET_PATHS,
    V3_BATCH01_ASSET_PATHS,
    V3_BATCH02_ASSET_PATHS,
    V3_BATCH03_ASSET_PATHS,
    V3_PILOT_ASSET_PATHS,
    DuplicateJsonKeyError,
    FixtureContractError,
    audit_current_corpus,
    canonical_checkout_bytes,
    checked_fixture_path,
    compare_asset_inventory,
    execution_mode,
    future_model_obligation_ids,
    fixture_contract_structure_problems,
    manifest_structure_problems,
    strict_json_loads,
    trace_only_obligation_ids,
)


def test_candidate_manifest_identity_and_complete_corpus() -> None:
    audit = audit_current_corpus()
    assert MANIFEST_SHA256 == CANDIDATE_MANIFEST_SHA256
    assert MANIFEST_GIT_BLOB == CANDIDATE_MANIFEST_GIT_BLOB
    assert MANIFEST["inventoryFormatVersion"] == EXPECTED_INVENTORY_FORMAT_VERSION == 3
    assert audit.problems == ()
    assert audit.asset_count == EXPECTED_ASSET_COUNT == 148
    assert audit.control_count == EXPECTED_CONTROL_COUNT == 2
    assert audit.case_count == EXPECTED_CASE_COUNT == 2166
    assert audit.deferred_count == EXPECTED_DEFERRED_COUNT == 115
    assert audit.executable_count == EXPECTED_EXECUTABLE_COUNT == 2051
    assert audit.trace_only_count == EXPECTED_TRACE_ONLY_COUNT == 14
    assert audit.corrected_inventory_count == EXPECTED_CORRECTED_INVENTORY_COUNT == 2180
    assert audit.open_phase1_gap_count == EXPECTED_OPEN_PHASE1_GAP_COUNT == 42
    assert (
        audit.future_model_obligation_count
        == EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT
        == 8
    )


def test_execution_modes_reconcile_manifest_v3_without_key_inference() -> None:
    observed = Counter(execution_mode(case) for case in CASES)
    assert observed == Counter(EXPECTED_EXECUTION_MODE_COUNTS)
    assert sum(observed.values()) == EXPECTED_CASE_COUNT
    assert sum(
        count
        for mode, count in observed.items()
        if mode != "deferred-preserved"
    ) == EXPECTED_EXECUTABLE_COUNT


def test_manifest_v2_withdraws_the_old_active_case_claims() -> None:
    withdrawn = MANIFEST["inventory"]["withdrawnClaims"]
    assert withdrawn == {
        "correctedCaseInventoryCount": 2230,
        "executableAcceptanceCount": 2115,
        "status": "withdrawn; neither value is an active acceptance count",
    }
    assert EXPECTED_CASE_COUNT != withdrawn["correctedCaseInventoryCount"]
    assert EXPECTED_EXECUTABLE_COUNT != withdrawn["executableAcceptanceCount"]


def test_coverage_obligation_classes_remain_distinct_and_nonexecutable() -> None:
    assert len(trace_only_obligation_ids()) == EXPECTED_TRACE_ONLY_COUNT == 14
    assert (
        len(future_model_obligation_ids())
        == EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT
        == 8
    )
    obligation_counts = Counter(
        item["inventoryDisposition"] for item in MANIFEST["coverageObligations"]
    )
    assert obligation_counts == {
        "TRACE_ONLY": 14,
        "COVERAGE_LEDGER_OPEN": 42,
        "FUTURE_MODEL_OBLIGATION": 8,
    }
    assert not set(trace_only_obligation_ids()) & {case.id for case in CASES}
    assert not set(future_model_obligation_ids()) & {case.id for case in CASES}


def test_windows_checkout_eol_handling_preserves_authenticated_canonical_bytes() -> None:
    audit = audit_current_corpus()
    utf8_paths = {
        asset["path"]
        for asset in MANIFEST["assets"]
        if asset["encoding"] == "utf-8-json"
    }
    assert len(utf8_paths) == EXPECTED_UTF8_JSON_ASSET_COUNT == 46
    assert V2_CORRECTION_ASSET_PATHS <= utf8_paths
    assert V3_PILOT_ASSET_PATHS <= utf8_paths
    assert V3_BATCH01_ASSET_PATHS <= utf8_paths
    assert V3_BATCH02_ASSET_PATHS <= utf8_paths
    assert V3_BATCH03_ASSET_PATHS <= utf8_paths
    assert (
        len(
            utf8_paths
            - V2_CORRECTION_ASSET_PATHS
            - V3_PILOT_ASSET_PATHS
            - V3_BATCH01_ASSET_PATHS
            - V3_BATCH02_ASSET_PATHS
            - V3_BATCH03_ASSET_PATHS
        )
        == EXPECTED_UNCHANGED_EOL_SENSITIVE_ASSET_COUNT
        == 31
    )
    assert 0 <= audit.checkout_eol_adjusted_count <= EXPECTED_UTF8_JSON_ASSET_COUNT
    if MANIFEST_EOL_ADJUSTED:
        assert MANIFEST_PHYSICAL_SHA256 != CANDIDATE_MANIFEST_SHA256
    else:
        assert MANIFEST_PHYSICAL_SHA256 == CANDIDATE_MANIFEST_SHA256


def test_checkout_eol_arrangement_is_exact_and_never_applies_to_raw_bytes() -> None:
    canonical = b'{"synthetic":true}\n'
    checkout = canonical.replace(b"\n", b"\r\n")
    expected = hashlib.sha256(canonical).hexdigest()
    assert canonical_checkout_bytes(
        checkout,
        expected_sha256=expected,
        expected_length=len(canonical),
        encoding="utf-8-json",
        identity="synthetic-test-only-json",
    ) == (canonical, True)
    with pytest.raises(FixtureContractError, match="raw checkout bytes"):
        canonical_checkout_bytes(
            checkout,
            expected_sha256=expected,
            expected_length=len(canonical),
            encoding="raw-bytes",
            identity="synthetic-test-only-raw",
        )


def test_manifest_case_and_asset_order_is_deterministic() -> None:
    case_ids = [case.id for case in CASES]
    asset_paths = [asset["path"] for asset in MANIFEST["assets"]]
    assert case_ids == sorted(case_ids)
    assert len(case_ids) == len(set(case_ids))
    assert asset_paths == sorted(asset_paths)
    assert len(asset_paths) == len(set(asset_paths))
    assert all(case_id.isascii() for case_id in case_ids)


def test_deferred_reconciliation_is_exact_and_non_promoting() -> None:
    deferred_rows = [
        case.id for case in CASES if case.expected_disposition == "DEFERRED"
    ]
    reconciliation = MANIFEST["coverageReconciliation"]
    assert deferred_rows == reconciliation["deferredCases"]
    assert len(deferred_rows) == reconciliation["deferredCaseCount"] == 115
    assert all(
        execution_mode(case) == "deferred-preserved"
        for case in CASES
        if case.id in deferred_rows
    )


def test_control_files_are_exactly_the_two_approved_paths() -> None:
    assert CONTROL_PATHS == {
        "tests/schema/fixtures/v1alpha1/README.md",
        "tests/schema/fixtures/v1alpha1/manifest.json",
    }


def test_fixture_contract_v3_is_exact_authenticated_and_has_no_self_digest() -> None:
    assert fixture_contract_structure_problems() == ()
    assert FIXTURE_CONTRACT["contractVersion"] == "fixture-contract-v1"
    assert [item["caseId"] for item in FIXTURE_CONTRACT["pilotCases"]] == [
        "phase1-static.branch-policy.negative.16-no-allow-match",
        "schema.branch-policy.negative.01-empty-prefix",
        "static.branch-policy.positive.01-exact-allow-no-deny",
    ]
    assert len(FIXTURE_CONTRACT["schemaOracleBatches"]) == 3
    batch01, batch02, batch03 = FIXTURE_CONTRACT["schemaOracleBatches"]
    assert batch01["batchId"] == "schema-common-ref-batch01"
    assert batch01["caseCount"] == 62
    assert tuple(item["caseId"] for item in batch01["cases"]) == (
        SCHEMA_REF_BATCH01_CASE_IDS
    )
    assert batch02["batchId"] == "schema-common-text-batch02"
    assert batch02["caseCount"] == 104
    assert tuple(item["caseId"] for item in batch02["cases"]) == (
        SCHEMA_TEXT_BATCH02_CASE_IDS
    )
    assert batch03["batchId"] == "schema-common-identifiers-batch03"
    assert batch03["caseCount"] == 73
    assert tuple(item["caseId"] for item in batch03["cases"]) == (
        SCHEMA_IDENTIFIER_BATCH03_CASE_IDS
    )
    assert not any(
        key in MANIFEST
        for key in ("manifestDigest", "manifestSha256", "manifestGitBlob", "selfDigest")
    )
    assert MANIFEST["inventory"]["fixtureContractAssets"] == 10
    assert MANIFEST["inventory"]["pilotCaseCount"] == 3
    assert MANIFEST["inventory"]["schemaOracleBatchCount"] == 3
    assert MANIFEST["inventory"]["schemaOracleBatchCaseCount"] == 239


@pytest.mark.parametrize(
    "source,exception",
    [
        ('{"key": 1, "key": 2}', DuplicateJsonKeyError),
        ('{"unterminated":', ValueError),
        ('{"value": NaN}', ValueError),
        (b"\xff", UnicodeDecodeError),
    ],
)
def test_strict_manifest_decoder_rejects_malformed_inputs(
    source: str | bytes, exception: type[Exception]
) -> None:
    with pytest.raises(exception):
        strict_json_loads(source)


@pytest.mark.parametrize(
    "path",
    [
        "../escape.json",
        "tests/schema/fixtures/v1alpha1/../escape.json",
        "/tests/schema/fixtures/v1alpha1/escape.json",
        "C:/tests/schema/fixtures/v1alpha1/escape.json",
        "tests\\schema\\fixtures\\v1alpha1\\escape.json",
        "tests/schema/not-the-fixture-root/escape.json",
    ],
)
def test_fixture_path_guard_rejects_traversal_and_out_of_root_references(path: str) -> None:
    with pytest.raises(FixtureContractError):
        checked_fixture_path(path, must_exist=False)


def test_inventory_comparison_detects_missing_and_unmanifested_assets() -> None:
    missing, extra = compare_asset_inventory(
        {"fixture/a.json", "fixture/b.json"},
        {"fixture/a.json", "fixture/c.json"},
    )
    assert missing == ("fixture/b.json",)
    assert extra == ("fixture/c.json",)


def test_structure_audit_detects_duplicate_asset_path() -> None:
    candidate = deepcopy(MANIFEST)
    candidate["assets"].append(deepcopy(candidate["assets"][0]))
    problems = manifest_structure_problems(candidate)
    assert "duplicate manifest asset path" in problems


def test_structure_audit_detects_duplicate_logical_case() -> None:
    candidate = deepcopy(MANIFEST)
    candidate["cases"].append(deepcopy(candidate["cases"][0]))
    problems = manifest_structure_problems(candidate)
    assert "duplicate logical case id" in problems


def test_structure_audit_detects_missing_case_contract_field() -> None:
    candidate = deepcopy(MANIFEST)
    del candidate["cases"][0]["expectedStage"]
    problems = manifest_structure_problems(candidate)
    assert any("missing fields: expectedStage" in problem for problem in problems)


def test_structure_audit_detects_noncanonical_case_coverage() -> None:
    candidate = deepcopy(MANIFEST)
    candidate["cases"][0]["coverage"] = ["Z", "A", "A"]
    problems = manifest_structure_problems(candidate)
    assert any("non-canonical coverage identities" in problem for problem in problems)


def test_structure_audit_detects_provenance_or_inventory_tampering() -> None:
    provenance = deepcopy(MANIFEST)
    provenance["inventoryProvenance"]["sourceCommit"] = "0" * 40
    assert "manifest inventory provenance mismatch" in manifest_structure_problems(
        provenance
    )

    inventory = deepcopy(MANIFEST)
    inventory["inventory"]["directTotal"] += 1
    assert "manifest inventory aggregates mismatch" in manifest_structure_problems(
        inventory
    )


def test_structure_audit_detects_fixture_contract_reference_tampering() -> None:
    candidate = deepcopy(MANIFEST)
    candidate["fixtureContract"]["pilotCases"][0]["operandRef"]["sha256"] = "0" * 64
    assert "manifest fixture-contract metadata mismatch" in manifest_structure_problems(
        candidate
    )

    batch_candidate = deepcopy(MANIFEST)
    batch_candidate["fixtureContract"]["schemaOracleBatches"][0]["cases"][0][
        "oracleRef"
    ]["sha256"] = "0" * 64
    assert "manifest fixture-contract metadata mismatch" in manifest_structure_problems(
        batch_candidate
    )

    batch02_candidate = deepcopy(MANIFEST)
    batch02_candidate["fixtureContract"]["schemaOracleBatches"][1]["cases"][0][
        "operandRef"
    ]["sha256"] = "0" * 64
    assert "manifest fixture-contract metadata mismatch" in manifest_structure_problems(
        batch02_candidate
    )

    batch03_candidate = deepcopy(MANIFEST)
    batch03_candidate["fixtureContract"]["schemaOracleBatches"][2]["cases"][0][
        "oracleRef"
    ]["byteLength"] += 1
    assert "manifest fixture-contract metadata mismatch" in manifest_structure_problems(
        batch03_candidate
    )

    self_digest = deepcopy(MANIFEST)
    self_digest["manifestSha256"] = "0" * 64
    problems = manifest_structure_problems(self_digest)
    assert "manifest top-level key set differs from the frozen contract" in problems
    assert "manifest must not contain a self-digest" in problems


def test_structure_audit_detects_invalid_case_inventory_disposition() -> None:
    candidate = deepcopy(MANIFEST)
    candidate["cases"][0]["inventoryDisposition"] = "TRACE_ONLY"
    problems = manifest_structure_problems(candidate)
    assert any("unknown inventory disposition" in problem for problem in problems)


def test_structure_audit_detects_coverage_obligation_reclassification() -> None:
    candidate = deepcopy(MANIFEST)
    obligation = candidate["coverageObligations"][0]
    obligation["countedInCorrectedInventory"] = not obligation[
        "countedInCorrectedInventory"
    ]
    problems = manifest_structure_problems(candidate)
    assert any("violates its disposition contract" in problem for problem in problems)


def test_declared_dispositions_have_exact_aggregate_counts() -> None:
    observed = Counter(case.expected_disposition for case in CASES)
    assert observed == {"ACCEPT": 516, "REJECT": 1535, "DEFERRED": 115}
