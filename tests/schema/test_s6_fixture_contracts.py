"""Manifest-v3 execution, oracle, and unresolved-obligation S6 contracts."""

from collections import Counter
import hashlib

import pytest

from tests.schema.s6_fixture_runner import (
    CASES,
    DEFERRED_PRESERVED,
    EXPECTED_CASE_COUNT,
    EXPECTED_EXECUTABLE_COUNT,
    EXPECTED_EXECUTION_MODE_COUNTS,
    PILOT_CASE_IDS,
    SCHEMA_REF_BATCH01_CASE_IDS,
    SCHEMA_TEXT_BATCH02_CASE_IDS,
    SCHEMA_TEXT_BATCH02_MEMBERSHIP_SHA256,
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

    if case.id in (
        set(PILOT_CASE_IDS)
        | set(SCHEMA_REF_BATCH01_CASE_IDS)
        | set(SCHEMA_TEXT_BATCH02_CASE_IDS)
    ):
        assert result.execution_status == "EXECUTED"
        assert result.validation_status in {"PASS", "INVALID"}
        assert result.diagnostic_identity_version in {
            "schema-diagnostic-v1",
            "static-diagnostic-v1",
        }

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
        "Manifest v3 declares DIRECT execution, but authenticated fixture contracts do not "
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
    assert len(blocked) == 426
    assert not set(PILOT_CASE_IDS).intersection(blocked)
    blocked_set = set(blocked)
    assert all(
        record.execution_mode == STATIC_DIRECT
        for record in coverage_inventory()
        if record.case_id in blocked_set
    )
    assert sum(
        record.execution_status == "EXECUTED" for record in coverage_inventory()
    ) == 1625


def test_exact_three_case_fixture_contract_pilot_executes_with_strict_oracles() -> None:
    assert tuple(case_id for case_id in PILOT_CASE_IDS) == (
        "phase1-static.branch-policy.negative.16-no-allow-match",
        "schema.branch-policy.negative.01-empty-prefix",
        "static.branch-policy.positive.01-exact-allow-no-deny",
    )
    results = {case_id: evaluate_case(case_id) for case_id in PILOT_CASE_IDS}

    static_negative = results[
        "phase1-static.branch-policy.negative.16-no-allow-match"
    ]
    assert static_negative.actual_result == "REJECT"
    assert static_negative.validation_status == "INVALID"
    assert static_negative.oracle_status == "EXACT_MATCH"
    assert static_negative.expected_typed_diagnostics == static_negative.static_diagnostics
    assert static_negative.missing_diagnostics == ()
    assert static_negative.unexpected_diagnostics == ()

    schema_negative = results["schema.branch-policy.negative.01-empty-prefix"]
    assert schema_negative.actual_result == "REJECT"
    assert schema_negative.validation_status == "INVALID"
    assert schema_negative.oracle_status == "EXACT_MATCH"
    assert schema_negative.expected_typed_diagnostics == schema_negative.schema_diagnostics
    assert schema_negative.missing_diagnostics == ()
    assert schema_negative.unexpected_diagnostics == ()

    positive = results["static.branch-policy.positive.01-exact-allow-no-deny"]
    assert positive.actual_result == "ACCEPT"
    assert positive.validation_status == "PASS"
    assert positive.static_status == "PASS"
    assert positive.oracle_status == "NOT_APPLICABLE"
    assert positive.static_diagnostics == ()
    assert positive.expected_typed_diagnostics is None


def test_schema_ref_batch01_executes_with_exact_typed_oracles() -> None:
    assert len(SCHEMA_REF_BATCH01_CASE_IDS) == 62
    assert SCHEMA_REF_BATCH01_CASE_IDS == tuple(sorted(SCHEMA_REF_BATCH01_CASE_IDS))
    assert len(set(SCHEMA_REF_BATCH01_CASE_IDS)) == 62

    results = tuple(evaluate_case(case_id) for case_id in SCHEMA_REF_BATCH01_CASE_IDS)
    assert all(result.execution_status == "EXECUTED" for result in results)
    assert all(result.validation_status == "INVALID" for result in results)
    assert all(result.actual_result == "REJECT" for result in results)
    assert all(result.oracle_status == "EXACT_MATCH" for result in results)
    assert all(
        result.diagnostic_identity_version == "schema-diagnostic-v1"
        for result in results
    )
    assert all(
        result.expected_typed_diagnostics == result.schema_diagnostics
        for result in results
    )
    assert all(result.missing_diagnostics == () for result in results)
    assert all(result.unexpected_diagnostics == () for result in results)
    assert Counter(len(result.schema_diagnostics) for result in results) == {
        1: 53,
        2: 5,
        3: 4,
    }
    assert sum(len(result.schema_diagnostics) for result in results) == 75


def test_schema_text_batch02_executes_with_exact_typed_oracles() -> None:
    assert len(SCHEMA_TEXT_BATCH02_CASE_IDS) == 104
    assert SCHEMA_TEXT_BATCH02_CASE_IDS == tuple(sorted(SCHEMA_TEXT_BATCH02_CASE_IDS))
    assert len(set(SCHEMA_TEXT_BATCH02_CASE_IDS)) == 104
    membership_bytes = (
        "\n".join(SCHEMA_TEXT_BATCH02_CASE_IDS) + "\n"
    ).encode("ascii")
    assert (
        hashlib.sha256(membership_bytes).hexdigest()
        == SCHEMA_TEXT_BATCH02_MEMBERSHIP_SHA256
    )
    assert SCHEMA_TEXT_BATCH02_MEMBERSHIP_SHA256 == (
        "3e23bb284e58ccc5bbbc7d0d3646aca36065fe4cfda90579732c3caf030fe708"
    )

    results = tuple(evaluate_case(case_id) for case_id in SCHEMA_TEXT_BATCH02_CASE_IDS)
    assert all(result.execution_status == "EXECUTED" for result in results)
    assert all(result.validation_status == "INVALID" for result in results)
    assert all(result.actual_result == "REJECT" for result in results)
    assert all(result.oracle_status == "EXACT_MATCH" for result in results)
    assert all(
        result.diagnostic_identity_version == "schema-diagnostic-v1"
        for result in results
    )
    assert all(
        result.expected_typed_diagnostics == result.schema_diagnostics
        for result in results
    )
    assert all(result.missing_diagnostics == () for result in results)
    assert all(result.unexpected_diagnostics == () for result in results)
    assert Counter(len(result.schema_diagnostics) for result in results) == {
        1: 102,
        2: 2,
    }
    assert sum(len(result.schema_diagnostics) for result in results) == 106


def test_remaining_acceptance_blocker_counts_remain_fail_closed() -> None:
    assert len(direct_execution_gap_case_ids()) == 426
    assert len(missing_negative_oracle_case_ids()) == 1367
    assert not set(PILOT_CASE_IDS).intersection(direct_execution_gap_case_ids())
    assert not set(PILOT_CASE_IDS).intersection(missing_negative_oracle_case_ids())
    assert not set(SCHEMA_REF_BATCH01_CASE_IDS).intersection(
        missing_negative_oracle_case_ids()
    )
    assert not set(SCHEMA_TEXT_BATCH02_CASE_IDS).intersection(
        missing_negative_oracle_case_ids()
    )


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
