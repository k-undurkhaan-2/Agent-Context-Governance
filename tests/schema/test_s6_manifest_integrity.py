"""S6 integrity checks for the immutable S5 fixture inventory."""

from collections import Counter
from copy import deepcopy

import pytest

from tests.schema.s6_fixture_runner import (
    APPROVED_MANIFEST_SHA256,
    CASES,
    CONTROL_PATHS,
    EXPECTED_ASSET_COUNT,
    EXPECTED_CASE_COUNT,
    EXPECTED_CONTROL_COUNT,
    EXPECTED_DEFERRED_COUNT,
    EXPECTED_EXECUTABLE_COUNT,
    EXPECTED_EXECUTION_MODE_COUNTS,
    MANIFEST,
    MANIFEST_SHA256,
    DuplicateJsonKeyError,
    FixtureContractError,
    audit_current_corpus,
    checked_fixture_path,
    compare_asset_inventory,
    execution_mode,
    manifest_structure_problems,
    strict_json_loads,
)


def test_approved_manifest_identity_and_complete_corpus() -> None:
    audit = audit_current_corpus()
    assert MANIFEST_SHA256 == APPROVED_MANIFEST_SHA256
    assert audit.problems == ()
    assert audit.asset_count == EXPECTED_ASSET_COUNT == 138
    assert audit.control_count == EXPECTED_CONTROL_COUNT == 2
    assert audit.case_count == EXPECTED_CASE_COUNT == 2230
    assert audit.deferred_count == EXPECTED_DEFERRED_COUNT == 115
    assert audit.executable_count == EXPECTED_EXECUTABLE_COUNT == 2115


def test_execution_modes_reconcile_the_accepted_s5_handoff() -> None:
    observed = Counter(execution_mode(case) for case in CASES)
    assert observed == Counter(EXPECTED_EXECUTION_MODE_COUNTS)
    assert sum(observed.values()) == EXPECTED_CASE_COUNT
    assert sum(
        count
        for mode, count in observed.items()
        if mode != "deferred-preserved"
    ) == EXPECTED_EXECUTABLE_COUNT


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


def test_declared_dispositions_have_exact_aggregate_counts() -> None:
    observed = Counter(case.expected_disposition for case in CASES)
    assert observed == {"ACCEPT": 555, "REJECT": 1560, "DEFERRED": 115}
