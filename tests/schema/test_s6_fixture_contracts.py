"""Executable and trace-preserving S6 coverage for every S5 logical case."""

from collections import Counter

import pytest

from tests.schema.s6_fixture_runner import (
    CASES,
    DEFERRED_PRESERVED,
    EXPECTED_CASE_COUNT,
    EXPECTED_EXECUTABLE_COUNT,
    EXPECTED_EXECUTION_MODE_COUNTS,
    SCHEMA_DIRECT,
    SCHEMA_TRACE,
    STATIC_DIRECT,
    STATIC_TRACE,
    coverage_inventory,
    evaluate_case,
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

    if result.execution_mode in (SCHEMA_DIRECT, STATIC_DIRECT):
        assert result.actual_result == case.expected_disposition
        if result.actual_result == "REJECT":
            assert result.actual_diagnostic_identities
    elif result.execution_mode in (SCHEMA_TRACE, STATIC_TRACE):
        assert result.actual_result == "TRACE_VERIFIED"
        assert result.actual_diagnostic_identities == ()
    else:
        assert result.execution_mode == DEFERRED_PRESERVED
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
    assert all(
        record.actual_result in {"ACCEPT", "REJECT", "TRACE_VERIFIED"}
        for record in executable
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


def test_direct_negative_cases_retain_declared_and_actual_diagnostics() -> None:
    direct_negatives = [
        record
        for record in coverage_inventory()
        if record.execution_mode in (SCHEMA_DIRECT, STATIC_DIRECT)
        and record.expected_disposition == "REJECT"
    ]
    assert direct_negatives
    assert all(record.declared_diagnostic_identity for record in direct_negatives)
    assert all(record.actual_diagnostic_identities for record in direct_negatives)


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


def test_trace_cases_do_not_claim_validator_execution() -> None:
    trace_records = [
        record
        for record in coverage_inventory()
        if record.execution_mode in (SCHEMA_TRACE, STATIC_TRACE)
    ]
    assert len(trace_records) == 33 + 491
    assert {record.actual_result for record in trace_records} == {"TRACE_VERIFIED"}
    assert all(record.static_status is None for record in trace_records)
    assert all(record.schema_diagnostics == () for record in trace_records)
