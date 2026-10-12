"""Manifest-v2 execution, oracle, and unresolved-obligation S6 contracts."""

from collections import Counter

import pytest

from tests.schema.s6_fixture_runner import (
    CASES,
    DEFERRED_PRESERVED,
    EXPECTED_CASE_COUNT,
    EXPECTED_EXECUTABLE_COUNT,
    EXPECTED_EXECUTION_MODE_COUNTS,
    SCHEMA_DIRECT,
    STATIC_DIRECT,
    coverage_gap_dispositions,
    coverage_inventory,
    direct_execution_gap_case_ids,
    evaluate_case,
    future_model_obligation_ids,
    missing_negative_oracle_case_ids,
    trace_only_obligation_ids,
)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.id)
def test_s6_manifest_logical_case(case) -> None:
    result = evaluate_case(case.id)
    assert result.case_id == case.id
    assert result.source_asset == case.asset
    assert result.owner == case.owner
    assert result.expected_disposition == case.expected_disposition
    assert result.expected_stage == case.expected_stage
    assert result.declared_diagnostic_identity == case.expected_failure_identity
    assert result.expected_diagnostic_identities == case.expected_diagnostic_identities

    if result.execution_mode in (SCHEMA_DIRECT, STATIC_DIRECT) and (
        result.execution_status == "EXECUTED"
    ):
        assert result.actual_result == case.expected_disposition
        if result.actual_result == "REJECT":
            assert result.actual_diagnostic_identities
    elif result.execution_mode == STATIC_DIRECT:
        assert result.execution_status == "BLOCKED_MISSING_EXECUTABLE_OPERAND"
        assert result.actual_result == "EXECUTION_BLOCKED"
        assert result.actual_diagnostic_identities == ()
    else:
        assert result.execution_mode == DEFERRED_PRESERVED
        assert result.execution_status == "DEFERRED_PRESERVED"
        assert result.actual_result == "DEFERRED_PRESERVED"
        assert result.actual_diagnostic_identities == ()


def test_pytest_native_coverage_inventory_is_complete_and_stable() -> None:
    inventory = coverage_inventory()
    assert len(inventory) == EXPECTED_CASE_COUNT
    assert [record.case_id for record in inventory] == [case.id for case in CASES]
    assert len({record.case_id for record in inventory}) == EXPECTED_CASE_COUNT
    assert Counter(record.execution_mode for record in inventory) == Counter(
        EXPECTED_EXECUTION_MODE_COUNTS
    )


def test_every_non_deferred_case_has_an_actual_s6_result() -> None:
    inventory = coverage_inventory()
    executable = [
        record for record in inventory if record.expected_disposition != "DEFERRED"
    ]
    assert len(executable) == EXPECTED_EXECUTABLE_COUNT
    blocked = tuple(
        record.case_id for record in executable if record.execution_status != "EXECUTED"
    )
    assert blocked == (), (
        "Manifest v2 declares DIRECT execution, but immutable fixture payloads do not "
        f"materialize validator operands for {len(blocked)} cases: {blocked!r}"
    )


def test_deferred_cases_are_counted_but_never_promoted_to_acceptance() -> None:
    deferred = [
        record
        for record in coverage_inventory()
        if record.execution_mode == DEFERRED_PRESERVED
    ]
    assert len(deferred) == 115
    assert {record.actual_result for record in deferred} == {"DEFERRED_PRESERVED"}
    assert not any(record.actual_result in {"ACCEPT", "REJECT"} for record in deferred)


def test_direct_negative_cases_require_an_independent_exact_diagnostic_set() -> None:
    direct_negatives = [
        record
        for record in coverage_inventory()
        if record.execution_mode in (SCHEMA_DIRECT, STATIC_DIRECT)
        and record.expected_disposition == "REJECT"
    ]
    assert direct_negatives
    assert all(record.declared_diagnostic_identity for record in direct_negatives)
    missing = missing_negative_oracle_case_ids()
    mismatched = tuple(
        record.case_id
        for record in direct_negatives
        if record.oracle_status == "EXACT_SET_MISMATCH"
    )
    assert missing == (), (
        "Direct negative fixtures lack independently declared exact diagnostic identity "
        f"sets for {len(missing)} cases: {missing!r}"
    )
    assert mismatched == (), f"Exact diagnostic identity-set mismatches: {mismatched!r}"
    assert all(record.oracle_status == "EXACT_MATCH" for record in direct_negatives)


def test_direct_schema_diagnostics_are_structured_unique_and_ordered() -> None:
    schema_negatives = [
        record
        for record in coverage_inventory()
        if record.execution_mode == SCHEMA_DIRECT
        and record.expected_disposition == "REJECT"
    ]
    assert schema_negatives
    for record in schema_negatives:
        diagnostics = record.schema_diagnostics
        identities = tuple(item.identity for item in diagnostics)
        assert identities == record.actual_diagnostic_identities
        assert len(identities) == len(set(identities))
        assert diagnostics == tuple(
            sorted(
                diagnostics,
                key=lambda item: (
                    item.instance_pointer,
                    item.schema_resource_id,
                    item.schema_pointer,
                    item.keyword,
                    item.identity,
                ),
            )
        )
        assert all(item.schema_resource_id.startswith("urn:uuid:") for item in diagnostics)
        assert all(
            item.instance_pointer == "" or item.instance_pointer.startswith("/")
            for item in diagnostics
        )
        assert all(item.schema_pointer.startswith("/") for item in diagnostics)
        assert all(item.keyword for item in diagnostics)


def test_no_direct_case_uses_trace_verified_as_an_execution_substitute() -> None:
    records = coverage_inventory()
    assert not any(record.actual_result == "TRACE_VERIFIED" for record in records)
    assert Counter(record.execution_mode for record in records) == Counter(
        EXPECTED_EXECUTION_MODE_COUNTS
    )


def test_direct_execution_gap_detector_reports_exact_nonmaterialized_rows() -> None:
    blocked = tuple(
        record.case_id
        for record in coverage_inventory()
        if record.execution_status == "BLOCKED_MISSING_EXECUTABLE_OPERAND"
    )
    assert blocked == direct_execution_gap_case_ids()
    assert len(blocked) == 428
    blocked_set = set(blocked)
    assert all(
        record.execution_mode == STATIC_DIRECT
        for record in coverage_inventory()
        if record.case_id in blocked_set
    )
    assert sum(
        record.execution_status == "EXECUTED" for record in coverage_inventory()
    ) == 1623


def test_trace_only_and_future_model_obligations_stay_outside_direct_inventory() -> None:
    case_ids = {case.id for case in CASES}
    assert len(trace_only_obligation_ids()) == 14
    assert len(future_model_obligation_ids()) == 8
    assert not case_ids.intersection(trace_only_obligation_ids())
    assert not case_ids.intersection(future_model_obligation_ids())


def test_open_phase1_coverage_gaps_remain_explicit_and_block_s6_acceptance() -> None:
    gaps = coverage_gap_dispositions()
    assert len(gaps) == 42
    assert all(gap.disposition == "COVERAGE_LEDGER_OPEN" for gap in gaps)
    assert all(gap.missing_obligations for gap in gaps)
    assert all(gap.existing_executable_coverage == () for gap in gaps)
    assert all(gap.responsible_workstreams for gap in gaps)
    assert gaps == (), (
        "S6 acceptance remains blocked by explicit Phase-1 coverage-ledger gaps: "
        f"{tuple(gap.case_id for gap in gaps)!r}"
    )
