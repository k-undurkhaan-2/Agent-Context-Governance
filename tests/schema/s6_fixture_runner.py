"""Deterministic S6 runner for the authenticated v1alpha1 Manifest v3 corpus.

This module is test-only.  It does not expose a production validator, create a
trusted proof source, or turn fixture acceptance into operational authority.
The synthetic proof adapters below are used only to exercise the already-public
S4 validation surface with explicitly synthetic operands.  Pilot proof
responses are sidecar-declared and never inherit generic success defaults.
"""

from __future__ import annotations

from contextlib import ExitStack, contextmanager
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from types import MappingProxyType
from typing import Any, Mapping
from unittest.mock import patch

from jsonschema import Draft202012Validator

from contextctl_schema import build_format_checker
from contextctl_schema import _static_core as static_core
from contextctl_schema._static_baseline import _MaterializedBaselineView
from contextctl_schema.catalog import (
    API_VERSION,
    CATALOG,
    SCHEMA_SET_REVISION,
    get_resource,
)
from contextctl_schema.static_validation import (
    validate_execution_receipt_static,
    validate_governance_bundle,
    validate_task_contract_static,
)
from tests.schema.s4_synthetic import SyntheticPorts
from tests.schema.test_resource_schemas import (
    KINDS,
    denial_resource,
    resource,
    source_registry,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPOSITORY_ROOT / "tests" / "schema" / "fixtures" / "v1alpha1"
MANIFEST_PATH = FIXTURE_ROOT / "manifest.json"
CONTROL_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/README.md",
        "tests/schema/fixtures/v1alpha1/manifest.json",
    }
)
CANDIDATE_MANIFEST_SHA256 = (
    "6663562fb501efde3a103941ae76430e360eabc727d81a0a7f6c076c230e4643"
)
CANDIDATE_MANIFEST_GIT_BLOB = "7ba65b49c9d6e53e8d1aebe53b699624ad588f76"
EXPECTED_INVENTORY_FORMAT_VERSION = 3
EXPECTED_ASSET_COUNT = 152
EXPECTED_CONTROL_COUNT = 2
EXPECTED_CASE_COUNT = 2166
EXPECTED_ACCEPT_COUNT = 516
EXPECTED_REJECT_COUNT = 1535
EXPECTED_DEFERRED_COUNT = 115
EXPECTED_EXECUTABLE_COUNT = 2051
EXPECTED_DIRECT_SCHEMA_COUNT = 1566
EXPECTED_DIRECT_STATIC_COUNT = 485
EXPECTED_TRACE_ONLY_COUNT = 14
EXPECTED_CORRECTED_INVENTORY_COUNT = 2180
EXPECTED_OPEN_PHASE1_GAP_COUNT = 42
EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT = 8
EXPECTED_COVERAGE_OBLIGATION_COUNT = 64
EXPECTED_UTF8_JSON_ASSET_COUNT = 50
# Five v2 correction assets changed at the accepted correction commit.  The
# other 31 UTF-8 JSON assets retain the known checkout-only LF/CRLF exposure.
EXPECTED_UNCHANGED_EOL_SENSITIVE_ASSET_COUNT = 31
V2_CORRECTION_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/schema/negative/structured-remote-matrix.json",
        "tests/schema/fixtures/v1alpha1/static/negative/sg001-matrix-trace.json",
        "tests/schema/fixtures/v1alpha1/static/negative/structured-remote-relations.json",
        "tests/schema/fixtures/v1alpha1/static/positive/sg001-matrix-trace.json",
        "tests/schema/fixtures/v1alpha1/static/positive/sg001-runtime-structure.json",
    }
)
V3_PILOT_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json",
        "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/static-branch-policy-pilot.json",
    }
)
V3_BATCH01_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-ref-batch01.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-ref-batch01.json",
    }
)
V3_BATCH02_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-text-batch02.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-text-batch02.json",
    }
)
V3_BATCH03_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-identifiers-batch03.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-identifiers-batch03.json",
    }
)
V3_BATCH04_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-scalars-batch04.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-scalars-batch04.json",
    }
)
V3_BATCH05_ASSET_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-scalars-batch05.json",
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-scalars-batch05.json",
    }
)
FIXTURE_CONTRACT_ASSET_PATHS = (
    V3_PILOT_ASSET_PATHS
    | V3_BATCH01_ASSET_PATHS
    | V3_BATCH02_ASSET_PATHS
    | V3_BATCH03_ASSET_PATHS
    | V3_BATCH04_ASSET_PATHS
    | V3_BATCH05_ASSET_PATHS
)

FIXTURE_CONTRACT_VERSION = "fixture-contract-v1"
FIXTURE_CONTRACT_SCHEMA_ID = "urn:uuid:7fc0bf0d-c5a6-4b81-b193-44a871d6a3a1"
SCHEMA_DIAGNOSTIC_V1 = "schema-diagnostic-v1"
STATIC_DIAGNOSTIC_V1 = "static-diagnostic-v1"
SCHEMA_VALIDATOR_ENTRY_POINT = (
    "jsonschema.validators.Draft202012Validator.iter_errors"
)
STATIC_VALIDATOR_ENTRY_POINT = (
    "contextctl_schema.static_validation.validate_task_contract_static"
)
PILOT_CASE_IDS = (
    "phase1-static.branch-policy.negative.16-no-allow-match",
    "schema.branch-policy.negative.01-empty-prefix",
    "static.branch-policy.positive.01-exact-allow-no-deny",
)
SCHEMA_REF_BATCH01_ID = "schema-common-ref-batch01"
SCHEMA_REF_BATCH01_CASE_IDS = (
    "schema.common.branchprefix.negative.heads-only",
    "schema.common.branchprefix.negative.ref-0",
    "schema.common.branchprefix.negative.ref-1",
    "schema.common.branchprefix.negative.ref-10",
    "schema.common.branchprefix.negative.ref-11",
    "schema.common.branchprefix.negative.ref-12",
    "schema.common.branchprefix.negative.ref-13",
    "schema.common.branchprefix.negative.ref-14",
    "schema.common.branchprefix.negative.ref-15",
    "schema.common.branchprefix.negative.ref-16",
    "schema.common.branchprefix.negative.ref-17",
    "schema.common.branchprefix.negative.ref-18",
    "schema.common.branchprefix.negative.ref-19",
    "schema.common.branchprefix.negative.ref-2",
    "schema.common.branchprefix.negative.ref-3",
    "schema.common.branchprefix.negative.ref-4",
    "schema.common.branchprefix.negative.ref-5",
    "schema.common.branchprefix.negative.ref-6",
    "schema.common.branchprefix.negative.ref-7",
    "schema.common.branchprefix.negative.ref-8",
    "schema.common.branchprefix.negative.ref-9",
    "schema.common.branchref.negative.ref-0",
    "schema.common.branchref.negative.ref-1",
    "schema.common.branchref.negative.ref-10",
    "schema.common.branchref.negative.ref-11",
    "schema.common.branchref.negative.ref-12",
    "schema.common.branchref.negative.ref-13",
    "schema.common.branchref.negative.ref-14",
    "schema.common.branchref.negative.ref-15",
    "schema.common.branchref.negative.ref-16",
    "schema.common.branchref.negative.ref-17",
    "schema.common.branchref.negative.ref-18",
    "schema.common.branchref.negative.ref-19",
    "schema.common.branchref.negative.ref-2",
    "schema.common.branchref.negative.ref-3",
    "schema.common.branchref.negative.ref-4",
    "schema.common.branchref.negative.ref-5",
    "schema.common.branchref.negative.ref-6",
    "schema.common.branchref.negative.ref-7",
    "schema.common.branchref.negative.ref-8",
    "schema.common.branchref.negative.ref-9",
    "schema.common.branchref.negative.tag",
    "schema.common.gitrefidentifier.negative.ref-0",
    "schema.common.gitrefidentifier.negative.ref-1",
    "schema.common.gitrefidentifier.negative.ref-10",
    "schema.common.gitrefidentifier.negative.ref-11",
    "schema.common.gitrefidentifier.negative.ref-12",
    "schema.common.gitrefidentifier.negative.ref-13",
    "schema.common.gitrefidentifier.negative.ref-14",
    "schema.common.gitrefidentifier.negative.ref-15",
    "schema.common.gitrefidentifier.negative.ref-16",
    "schema.common.gitrefidentifier.negative.ref-17",
    "schema.common.gitrefidentifier.negative.ref-18",
    "schema.common.gitrefidentifier.negative.ref-19",
    "schema.common.gitrefidentifier.negative.ref-2",
    "schema.common.gitrefidentifier.negative.ref-3",
    "schema.common.gitrefidentifier.negative.ref-4",
    "schema.common.gitrefidentifier.negative.ref-5",
    "schema.common.gitrefidentifier.negative.ref-6",
    "schema.common.gitrefidentifier.negative.ref-7",
    "schema.common.gitrefidentifier.negative.ref-8",
    "schema.common.gitrefidentifier.negative.ref-9",
)
SCHEMA_TEXT_BATCH02_ID = 'schema-common-text-batch02'
SCHEMA_TEXT_BATCH02_MEMBERSHIP_SHA256 = (
    '3e23bb284e58ccc5bbbc7d0d3646aca36065fe4cfda90579732c3caf030fe708'
)
SCHEMA_TEXT_BATCH02_CASE_IDS = (
    'schema.common.displaytext.negative.control-0',
    'schema.common.displaytext.negative.control-1',
    'schema.common.displaytext.negative.control-10',
    'schema.common.displaytext.negative.control-11',
    'schema.common.displaytext.negative.control-12',
    'schema.common.displaytext.negative.control-127',
    'schema.common.displaytext.negative.control-128',
    'schema.common.displaytext.negative.control-129',
    'schema.common.displaytext.negative.control-13',
    'schema.common.displaytext.negative.control-130',
    'schema.common.displaytext.negative.control-131',
    'schema.common.displaytext.negative.control-132',
    'schema.common.displaytext.negative.control-133',
    'schema.common.displaytext.negative.control-134',
    'schema.common.displaytext.negative.control-135',
    'schema.common.displaytext.negative.control-136',
    'schema.common.displaytext.negative.control-137',
    'schema.common.displaytext.negative.control-138',
    'schema.common.displaytext.negative.control-139',
    'schema.common.displaytext.negative.control-14',
    'schema.common.displaytext.negative.control-140',
    'schema.common.displaytext.negative.control-141',
    'schema.common.displaytext.negative.control-142',
    'schema.common.displaytext.negative.control-143',
    'schema.common.displaytext.negative.control-144',
    'schema.common.displaytext.negative.control-145',
    'schema.common.displaytext.negative.control-146',
    'schema.common.displaytext.negative.control-147',
    'schema.common.displaytext.negative.control-148',
    'schema.common.displaytext.negative.control-149',
    'schema.common.displaytext.negative.control-15',
    'schema.common.displaytext.negative.control-150',
    'schema.common.displaytext.negative.control-151',
    'schema.common.displaytext.negative.control-152',
    'schema.common.displaytext.negative.control-153',
    'schema.common.displaytext.negative.control-154',
    'schema.common.displaytext.negative.control-155',
    'schema.common.displaytext.negative.control-156',
    'schema.common.displaytext.negative.control-157',
    'schema.common.displaytext.negative.control-158',
    'schema.common.displaytext.negative.control-159',
    'schema.common.displaytext.negative.control-16',
    'schema.common.displaytext.negative.control-17',
    'schema.common.displaytext.negative.control-18',
    'schema.common.displaytext.negative.control-19',
    'schema.common.displaytext.negative.control-2',
    'schema.common.displaytext.negative.control-20',
    'schema.common.displaytext.negative.control-21',
    'schema.common.displaytext.negative.control-22',
    'schema.common.displaytext.negative.control-23',
    'schema.common.displaytext.negative.control-24',
    'schema.common.displaytext.negative.control-25',
    'schema.common.displaytext.negative.control-26',
    'schema.common.displaytext.negative.control-27',
    'schema.common.displaytext.negative.control-28',
    'schema.common.displaytext.negative.control-29',
    'schema.common.displaytext.negative.control-3',
    'schema.common.displaytext.negative.control-30',
    'schema.common.displaytext.negative.control-31',
    'schema.common.displaytext.negative.control-4',
    'schema.common.displaytext.negative.control-5',
    'schema.common.displaytext.negative.control-6',
    'schema.common.displaytext.negative.control-7',
    'schema.common.displaytext.negative.control-8',
    'schema.common.displaytext.negative.control-9',
    'schema.common.displaytext.negative.empty',
    'schema.common.displaytext.negative.too-long',
    'schema.common.displaytext.negative.wrong-type',
    'schema.common.sanitizedsummary.negative.control-0',
    'schema.common.sanitizedsummary.negative.control-1',
    'schema.common.sanitizedsummary.negative.control-10',
    'schema.common.sanitizedsummary.negative.control-11',
    'schema.common.sanitizedsummary.negative.control-12',
    'schema.common.sanitizedsummary.negative.control-127',
    'schema.common.sanitizedsummary.negative.control-13',
    'schema.common.sanitizedsummary.negative.control-14',
    'schema.common.sanitizedsummary.negative.control-15',
    'schema.common.sanitizedsummary.negative.control-16',
    'schema.common.sanitizedsummary.negative.control-17',
    'schema.common.sanitizedsummary.negative.control-18',
    'schema.common.sanitizedsummary.negative.control-19',
    'schema.common.sanitizedsummary.negative.control-2',
    'schema.common.sanitizedsummary.negative.control-20',
    'schema.common.sanitizedsummary.negative.control-21',
    'schema.common.sanitizedsummary.negative.control-22',
    'schema.common.sanitizedsummary.negative.control-23',
    'schema.common.sanitizedsummary.negative.control-24',
    'schema.common.sanitizedsummary.negative.control-25',
    'schema.common.sanitizedsummary.negative.control-26',
    'schema.common.sanitizedsummary.negative.control-27',
    'schema.common.sanitizedsummary.negative.control-28',
    'schema.common.sanitizedsummary.negative.control-29',
    'schema.common.sanitizedsummary.negative.control-3',
    'schema.common.sanitizedsummary.negative.control-30',
    'schema.common.sanitizedsummary.negative.control-31',
    'schema.common.sanitizedsummary.negative.control-4',
    'schema.common.sanitizedsummary.negative.control-5',
    'schema.common.sanitizedsummary.negative.control-6',
    'schema.common.sanitizedsummary.negative.control-7',
    'schema.common.sanitizedsummary.negative.control-8',
    'schema.common.sanitizedsummary.negative.control-9',
    'schema.common.sanitizedsummary.negative.empty',
    'schema.common.sanitizedsummary.negative.too-long',
    'schema.common.sanitizedsummary.negative.wrong-type',
)
SCHEMA_IDENTIFIER_BATCH03_ID = "schema-common-identifiers-batch03"
SCHEMA_IDENTIFIER_BATCH03_MEMBERSHIP_SHA256 = (
    "68f1bcc6d39e769249b065d20ab0ee45c3e0418e45b95aa4cda1df8210444638"
)
SCHEMA_IDENTIFIER_BATCH03_CASE_IDS = (
    "schema.common.checkidentifier.negative.empty-segment",
    "schema.common.checkidentifier.negative.leading-hyphen",
    "schema.common.checkidentifier.negative.missing-segment",
    "schema.common.checkidentifier.negative.segment-33",
    "schema.common.checkidentifier.negative.total-161",
    "schema.common.checkidentifier.negative.trailing-hyphen",
    "schema.common.checkidentifier.negative.trailing-newline",
    "schema.common.checkidentifier.negative.underscore",
    "schema.common.checkidentifier.negative.uppercase",
    "schema.common.checkidentifier.negative.wrong-prefix",
    "schema.common.logicalidentifier.negative.empty",
    "schema.common.logicalidentifier.negative.leading-dot",
    "schema.common.logicalidentifier.negative.leading-hyphen",
    "schema.common.logicalidentifier.negative.number",
    "schema.common.logicalidentifier.negative.slash",
    "schema.common.logicalidentifier.negative.too-long",
    "schema.common.logicalidentifier.negative.trailing-dot",
    "schema.common.logicalidentifier.negative.trailing-hyphen",
    "schema.common.logicalidentifier.negative.trailing-newline",
    "schema.common.logicalidentifier.negative.underscore",
    "schema.common.logicalidentifier.negative.unicode",
    "schema.common.logicalidentifier.negative.uppercase",
    "schema.common.profileidentifier.negative.empty-segment",
    "schema.common.profileidentifier.negative.leading-hyphen",
    "schema.common.profileidentifier.negative.missing-segment",
    "schema.common.profileidentifier.negative.segment-33",
    "schema.common.profileidentifier.negative.total-161",
    "schema.common.profileidentifier.negative.trailing-hyphen",
    "schema.common.profileidentifier.negative.trailing-newline",
    "schema.common.profileidentifier.negative.underscore",
    "schema.common.profileidentifier.negative.uppercase",
    "schema.common.profileidentifier.negative.wrong-prefix",
    "schema.common.reasoncode.negative.empty-segment",
    "schema.common.reasoncode.negative.leading-hyphen",
    "schema.common.reasoncode.negative.missing-segment",
    "schema.common.reasoncode.negative.segment-33",
    "schema.common.reasoncode.negative.total-161",
    "schema.common.reasoncode.negative.trailing-hyphen",
    "schema.common.reasoncode.negative.trailing-newline",
    "schema.common.reasoncode.negative.underscore",
    "schema.common.reasoncode.negative.uppercase",
    "schema.common.reasoncode.negative.wrong-prefix",
    "schema.common.remotenamespacecomponent.negative.component-0",
    "schema.common.remotenamespacecomponent.negative.component-1",
    "schema.common.remotenamespacecomponent.negative.component-10",
    "schema.common.remotenamespacecomponent.negative.component-11",
    "schema.common.remotenamespacecomponent.negative.component-12",
    "schema.common.remotenamespacecomponent.negative.component-13",
    "schema.common.remotenamespacecomponent.negative.component-14",
    "schema.common.remotenamespacecomponent.negative.component-2",
    "schema.common.remotenamespacecomponent.negative.component-3",
    "schema.common.remotenamespacecomponent.negative.component-4",
    "schema.common.remotenamespacecomponent.negative.component-5",
    "schema.common.remotenamespacecomponent.negative.component-6",
    "schema.common.remotenamespacecomponent.negative.component-7",
    "schema.common.remotenamespacecomponent.negative.component-8",
    "schema.common.remotenamespacecomponent.negative.component-9",
    "schema.common.remoterepositoryname.negative.component-0",
    "schema.common.remoterepositoryname.negative.component-1",
    "schema.common.remoterepositoryname.negative.component-10",
    "schema.common.remoterepositoryname.negative.component-11",
    "schema.common.remoterepositoryname.negative.component-12",
    "schema.common.remoterepositoryname.negative.component-13",
    "schema.common.remoterepositoryname.negative.component-14",
    "schema.common.remoterepositoryname.negative.component-2",
    "schema.common.remoterepositoryname.negative.component-3",
    "schema.common.remoterepositoryname.negative.component-4",
    "schema.common.remoterepositoryname.negative.component-5",
    "schema.common.remoterepositoryname.negative.component-6",
    "schema.common.remoterepositoryname.negative.component-7",
    "schema.common.remoterepositoryname.negative.component-8",
    "schema.common.remoterepositoryname.negative.component-9",
    "schema.common.remoterepositoryname.negative.git-suffix",
)
SCHEMA_SCALAR_BATCH04_ID = "schema-common-scalars-batch04"
SCHEMA_SCALAR_BATCH04_MEMBERSHIP_SHA256 = (
    "72fe7b7b2b80fdae80a75afe77377feb332f4b2badab1f8b0331c6c9e089ffe1"
)
SCHEMA_SCALAR_BATCH04_CASE_IDS = (
    "schema.common.capability.negative.null",
    "schema.common.capability.negative.unknown",
    "schema.common.capability.negative.wrong-case-create",
    "schema.common.capability.negative.wrong-case-delete",
    "schema.common.capability.negative.wrong-case-execute-build",
    "schema.common.capability.negative.wrong-case-execute-tests",
    "schema.common.capability.negative.wrong-case-external-secret-use",
    "schema.common.capability.negative.wrong-case-git-branch",
    "schema.common.capability.negative.wrong-case-git-commit",
    "schema.common.capability.negative.wrong-case-git-remote",
    "schema.common.capability.negative.wrong-case-git-stage",
    "schema.common.capability.negative.wrong-case-inspect",
    "schema.common.capability.negative.wrong-case-modify",
    "schema.common.capability.negative.wrong-case-network",
    "schema.common.capability.negative.wrong-case-validate",
    "schema.common.checkoutcome.negative.execution-cancelled",
    "schema.common.checkoutcome.negative.execution-succeeded",
    "schema.common.checkoutcome.negative.null",
    "schema.common.checkoutcome.negative.unknown",
    "schema.common.checkoutcome.negative.wrong-case-failed",
    "schema.common.checkoutcome.negative.wrong-case-indeterminate",
    "schema.common.checkoutcome.negative.wrong-case-passed",
    "schema.common.executioncheckoutcome.negative.non-execution-passed",
    "schema.common.executioncheckoutcome.negative.not-attempted",
    "schema.common.executioncheckoutcome.negative.null",
    "schema.common.executioncheckoutcome.negative.unknown",
    "schema.common.executioncheckoutcome.negative.wrong-case-cancelled",
    "schema.common.executioncheckoutcome.negative.wrong-case-failed",
    "schema.common.executioncheckoutcome.negative.wrong-case-indeterminate",
    "schema.common.executioncheckoutcome.negative.wrong-case-succeeded",
    "schema.common.executionoutcome.negative.null",
    "schema.common.executionoutcome.negative.unknown",
    "schema.common.executionoutcome.negative.wrong-case-cancelled",
    "schema.common.executionoutcome.negative.wrong-case-failed",
    "schema.common.executionoutcome.negative.wrong-case-indeterminate",
    "schema.common.executionoutcome.negative.wrong-case-not-attempted",
    "schema.common.executionoutcome.negative.wrong-case-succeeded",
    "schema.common.gitmode.negative.null",
    "schema.common.gitmode.negative.number",
    "schema.common.gitmode.negative.unknown",
    "schema.common.indexstage.negative.above",
    "schema.common.indexstage.negative.below",
    "schema.common.indexstage.negative.bool",
    "schema.common.indexstage.negative.fraction",
    "schema.common.indexstage.negative.null",
    "schema.common.indexstage.negative.string",
    "schema.common.kind.negative.null",
    "schema.common.kind.negative.unknown",
    "schema.common.kind.negative.wrong-case-domain",
    "schema.common.kind.negative.wrong-case-executionreceipt",
    "schema.common.kind.negative.wrong-case-hostoverlay",
    "schema.common.kind.negative.wrong-case-project",
    "schema.common.kind.negative.wrong-case-routingpolicy",
    "schema.common.kind.negative.wrong-case-taskcontract",
    "schema.common.kind.negative.wrong-case-worktreerole",
    "schema.common.lifecycleoutcome.negative.null",
    "schema.common.lifecycleoutcome.negative.unknown",
    "schema.common.lifecycleoutcome.negative.wrong-case-cancelled",
    "schema.common.lifecycleoutcome.negative.wrong-case-denied",
    "schema.common.lifecycleoutcome.negative.wrong-case-failed",
    "schema.common.lifecycleoutcome.negative.wrong-case-indeterminate",
    "schema.common.lifecycleoutcome.negative.wrong-case-succeeded",
    "schema.common.receiptdeliveryoutcome.negative.null",
    "schema.common.receiptdeliveryoutcome.negative.unknown",
    "schema.common.receiptdeliveryoutcome.negative.wrong-case-failed",
    "schema.common.receiptdeliveryoutcome.negative.wrong-case-indeterminate",
    "schema.common.receiptdeliveryoutcome.negative.wrong-case-not-attempted",
    "schema.common.receiptdeliveryoutcome.negative.wrong-case-succeeded",
    "schema.common.redactioncount.negative.above",
    "schema.common.redactioncount.negative.below",
    "schema.common.redactioncount.negative.bool",
    "schema.common.redactioncount.negative.fraction",
    "schema.common.redactioncount.negative.null",
    "schema.common.redactioncount.negative.string",
    "schema.common.releaseoutcome.negative.null",
    "schema.common.releaseoutcome.negative.unknown",
    "schema.common.releaseoutcome.negative.wrong-case-failed",
    "schema.common.releaseoutcome.negative.wrong-case-indeterminate",
    "schema.common.releaseoutcome.negative.wrong-case-not-required",
    "schema.common.releaseoutcome.negative.wrong-case-succeeded",
    "schema.common.remoteport.negative.above",
    "schema.common.remoteport.negative.below",
    "schema.common.remoteport.negative.bool",
    "schema.common.remoteport.negative.fraction",
    "schema.common.remoteport.negative.null",
    "schema.common.remoteport.negative.string",
    "schema.common.routingpriority.negative.above",
    "schema.common.routingpriority.negative.below",
    "schema.common.routingpriority.negative.bool",
    "schema.common.routingpriority.negative.fraction",
    "schema.common.routingpriority.negative.null",
    "schema.common.routingpriority.negative.string",
    "schema.common.sequence.negative.above",
    "schema.common.sequence.negative.below",
    "schema.common.sequence.negative.bool",
    "schema.common.sequence.negative.fraction",
    "schema.common.sequence.negative.null",
    "schema.common.sequence.negative.string",
)
SCHEMA_SCALAR_BATCH05_ID = "schema-common-scalars-batch05"
SCHEMA_SCALAR_BATCH05_MEMBERSHIP_SHA256 = (
    "24b46a203b26ce928c5c953c172e520fda7b034d7f41449dda96709c6b0ef5a6"
)
SCHEMA_SCALAR_BATCH05_CASE_IDS = (
    "schema.common.allowwrite.negative.type-0",
    "schema.common.allowwrite.negative.type-1",
    "schema.common.allowwrite.negative.type-2",
    "schema.common.allowwrite.negative.type-3",
    "schema.common.apiversion.negative.missing-string",
    "schema.common.apiversion.negative.unknown-version",
    "schema.common.canonicalutctimestamp.negative.timestamp-15",
    "schema.common.canonicalutctimestamp.negative.timestamp-16",
    "schema.common.canonicalutctimestamp.negative.timestamp-17",
    "schema.common.canonicalutctimestamp.negative.timestamp-18",
    "schema.common.canonicalutctimestamp.negative.timestamp-2",
    "schema.common.canonicalutctimestamp.negative.timestamp-20",
    "schema.common.canonicalutctimestamp.negative.timestamp-3",
    "schema.common.canonicalutctimestamp.negative.timestamp-4",
    "schema.common.canonicalutctimestamp.negative.timestamp-5",
    "schema.common.canonicalutctimestamp.negative.timestamp-6",
    "schema.common.canonicalutctimestamp.negative.timestamp-7",
    "schema.common.canonicalutctimestamp.negative.timestamp-8",
    "schema.common.canonicaluuid.negative.braces",
    "schema.common.canonicaluuid.negative.newline",
    "schema.common.canonicaluuid.negative.no-hyphens",
    "schema.common.canonicaluuid.negative.urn",
    "schema.common.capabilities.negative.wrong-type",
    "schema.common.mode.negative.null",
    "schema.common.mode.negative.unknown",
    "schema.common.mode.negative.wrong-case-implementation",
    "schema.common.mode.negative.wrong-case-plan-only",
    "schema.common.posixabsolutehostpath.negative.empty",
    "schema.common.posixabsolutehostpath.negative.too-long",
    "schema.common.remotednshost.negative.host-20",
    "schema.common.repositoryrelativepath.negative.path-0",
    "schema.common.repositoryrelativepath.negative.path-23",
    "schema.common.taggeddigest.negative.long",
    "schema.common.taggeddigest.negative.newline",
    "schema.common.taggeddigest.negative.short",
    "schema.common.taggeddigest.negative.wrong-tag",
    "schema.common.verificationoutcome.negative.null",
    "schema.common.verificationoutcome.negative.unknown",
    "schema.common.verificationoutcome.negative.wrong-case-failed",
    "schema.common.verificationoutcome.negative.wrong-case-indeterminate",
    "schema.common.verificationoutcome.negative.wrong-case-not-performed",
    "schema.common.verificationoutcome.negative.wrong-case-passed",
    "schema.common.windowsdriveabsolutehostpath.negative.empty",
    "schema.common.windowsdriveabsolutehostpath.negative.too-long",
)
FIXTURE_CONTRACT_CASE_IDS = (
    PILOT_CASE_IDS
    + SCHEMA_REF_BATCH01_CASE_IDS
    + SCHEMA_TEXT_BATCH02_CASE_IDS
    + SCHEMA_IDENTIFIER_BATCH03_CASE_IDS
    + SCHEMA_SCALAR_BATCH04_CASE_IDS
    + SCHEMA_SCALAR_BATCH05_CASE_IDS
)

SCHEMA_DIRECT = "schema-direct"
STATIC_DIRECT = "static-direct"
DEFERRED_PRESERVED = "deferred-preserved"

EXPECTED_EXECUTION_MODE_COUNTS = {
    SCHEMA_DIRECT: EXPECTED_DIRECT_SCHEMA_COUNT,
    STATIC_DIRECT: EXPECTED_DIRECT_STATIC_COUNT,
    DEFERRED_PRESERVED: 115,
}

_EXPECTED_TOP_LEVEL_KEYS = frozenset(
    {
        "apiVersion",
        "assets",
        "authorityClaim",
        "cases",
        "corpusPurpose",
        "coverageObligations",
        "coverageReconciliation",
        "designBlob",
        "designPath",
        "evidenceClaim",
        "fixtureContract",
        "fixtureRoot",
        "implementationBaseline",
        "inventory",
        "inventoryFormatVersion",
        "inventoryProvenance",
        "ordering",
        "ownershipBoundary",
        "productionReceiptClaim",
        "resourceCatalog",
        "schemaSetRevision",
    }
)
_CASE_REQUIRED_KEYS = frozenset(
    {
        "asset",
        "coverage",
        "designReferences",
        "expectedDisposition",
        "expectedFailureIdentity",
        "expectedStage",
        "id",
        "inventoryDisposition",
        "layer",
        "owner",
        "polarity",
        "resource",
    }
)
_COVERAGE_OBLIGATION_REQUIRED_KEYS = frozenset(
    {
        "asset",
        "assetPointer",
        "countedInCorrectedInventory",
        "coverageStatus",
        "inventoryDisposition",
        "originalCaseId",
    }
)
_DISPOSITIONS = frozenset({"ACCEPT", "REJECT", "DEFERRED"})
_INVENTORY_DISPOSITIONS = frozenset(
    {"DIRECT_SCHEMA", "DIRECT_STATIC", "DEFERRED"}
)
_COVERAGE_INVENTORY_DISPOSITIONS = frozenset(
    {"TRACE_ONLY", "COVERAGE_LEDGER_OPEN", "FUTURE_MODEL_OBLIGATION"}
)
_OWNERS = frozenset(
    {
        "schema",
        "phase1-static",
        "model-codec-deferred",
        "phase3-live-deferred",
        "phase4-evidence-deferred",
    }
)
_STAGES = frozenset(
    {
        "schema",
        "phase1-static",
        "model-strict-decoder",
        "model-canonical-codec",
        "phase3-live",
        "phase3-live-deferred",
    }
)
_POINTER_INDEX = re.compile(r"0|[1-9][0-9]*")
_EXPECTED_INVENTORY_PROVENANCE = {
    "acceptedDecision": "SCHEMA-S5-POST-INTEGRATION-INVENTORY-DISPOSITION-R1",
    "acceptedDecisionArtifactManifestSha256": (
        "164fb5c1c4a71707a6e83e0a95c18889c0b01e2e4eeebc1ae47b62c7015aa810"
    ),
    "acceptedUpstreamEvidenceManifestSha256": (
        "a72bd31ed2bfe7877f7abb4a0d92c93aa16c5d6313b70d68b73625a5e652c787"
    ),
    "historicalS5": {
        "designBlob": "c77bbc39da8a631918bde5cf4041659ddada8998",
        "designPath": "docs/schema-contract-v1alpha1.md",
        "implementationBaseline": "3619ce3f21731241ccec6b989452e57da2f14e12",
        "schemaSetRevision": "v1alpha1-r1",
    },
    "sourceCommit": "44b41272b56ebadb4ddb557e23593c22f6b0c2b9",
    "sourceManifestSha256": (
        "45187054fec6d52b74790438e07b14bf0c1da8835dee0bec8f0e6dc638d87b9c"
    ),
}


def _schema_ref_batch01_binding(case_id: str) -> dict[str, Any]:
    descriptor_path = (
        "tests/schema/fixtures/v1alpha1/schema/negative/common-profile-vectors.json"
    )
    operand_path = (
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-ref-batch01.json"
    )
    oracle_path = (
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-ref-batch01.json"
    )
    pointer = f"/cases/{case_id}"
    return {
        "caseId": case_id,
        "descriptorRef": {
            "byteLength": 179081,
            "path": descriptor_path,
            "pointer": pointer,
            "sha256": (
                "62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749"
            ),
        },
        "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
        "expectedValidationStatus": "INVALID",
        "operandRef": {
            "byteLength": 25393,
            "path": operand_path,
            "pointer": pointer,
            "sha256": (
                "f37015ee29a6933278b898a0953c0e4f97688f7fa0e6e1b7d68867b69496b038"
            ),
        },
        "oracleRef": {
            "byteLength": 26997,
            "path": oracle_path,
            "pointer": pointer,
            "sha256": (
                "f603ee91c4859e58539f7b5bbcf133a0dabb18fbcdd20231fe65d1355ee7effc"
            ),
        },
        "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
    }


def _schema_text_batch02_binding(case_id: str) -> dict[str, Any]:
    descriptor_path = (
        "tests/schema/fixtures/v1alpha1/schema/negative/common-profile-vectors.json"
    )
    operand_path = (
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-text-batch02.json"
    )
    oracle_path = (
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-text-batch02.json"
    )
    pointer = f"/cases/{case_id}"
    return {
        "caseId": case_id,
        "descriptorRef": {
            "byteLength": 179081,
            "path": descriptor_path,
            "pointer": pointer,
            "sha256": (
                "62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749"
            ),
        },
        "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
        "expectedValidationStatus": "INVALID",
        "operandRef": {
            "byteLength": 39337,
            "path": operand_path,
            "pointer": pointer,
            "sha256": (
                "7dee52bb82d5187d6e7a933973c129d3103982828d295ba09d29de26ebe4ff89"
            ),
        },
        "oracleRef": {
            "byteLength": 41354,
            "path": oracle_path,
            "pointer": pointer,
            "sha256": (
                "e16613e4d3dcfd712fc6902a37a064799fa61f045974a6d6e41611bec7b74b17"
            ),
        },
        "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
    }


def _schema_identifier_batch03_binding(case_id: str) -> dict[str, Any]:
    descriptor_path = (
        "tests/schema/fixtures/v1alpha1/schema/negative/common-profile-vectors.json"
    )
    operand_path = (
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-identifiers-batch03.json"
    )
    oracle_path = (
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-identifiers-batch03.json"
    )
    pointer = f"/cases/{case_id}"
    return {
        "caseId": case_id,
        "descriptorRef": {
            "byteLength": 179081,
            "path": descriptor_path,
            "pointer": pointer,
            "sha256": (
                "62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749"
            ),
        },
        "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
        "expectedValidationStatus": "INVALID",
        "operandRef": {
            "byteLength": 27747,
            "path": operand_path,
            "pointer": pointer,
            "sha256": (
                "057699046579a57a5da528eab3b0cf0cb30f4a0cfa310e9d12d2f77bf6ddb48b"
            ),
        },
        "oracleRef": {
            "byteLength": 32210,
            "path": oracle_path,
            "pointer": pointer,
            "sha256": (
                "452b14fc97e2730ac815efa306c9804fe57fa3f8bf4815a32db507b1e81ce050"
            ),
        },
        "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
    }


def _schema_scalar_batch04_binding(case_id: str) -> dict[str, Any]:
    descriptor_path = (
        "tests/schema/fixtures/v1alpha1/schema/negative/common-profile-vectors.json"
    )
    operand_path = (
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-scalars-batch04.json"
    )
    oracle_path = (
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-scalars-batch04.json"
    )
    pointer = f"/cases/{case_id}"
    return {
        "caseId": case_id,
        "descriptorRef": {
            "byteLength": 179081,
            "path": descriptor_path,
            "pointer": pointer,
            "sha256": (
                "62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749"
            ),
        },
        "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
        "expectedValidationStatus": "INVALID",
        "operandRef": {
            "byteLength": 35046,
            "path": operand_path,
            "pointer": pointer,
            "sha256": (
                "7d4f2587f6228d1d9994d3d50f3a372229e91327414c1ef1054af1eb91c36953"
            ),
        },
        "oracleRef": {
            "byteLength": 41193,
            "path": oracle_path,
            "pointer": pointer,
            "sha256": (
                "e35cee2f297fec67f035220214ea67fd16065843453d7bc2b055cb293ec0063f"
            ),
        },
        "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
    }


def _schema_scalar_batch05_binding(case_id: str) -> dict[str, Any]:
    descriptor_path = (
        "tests/schema/fixtures/v1alpha1/schema/negative/common-profile-vectors.json"
    )
    operand_path = (
        "tests/schema/fixtures/v1alpha1/s6/operands/"
        "schema-common-scalars-batch05.json"
    )
    oracle_path = (
        "tests/schema/fixtures/v1alpha1/s6/oracles/"
        "schema-common-scalars-batch05.json"
    )
    pointer = f"/cases/{case_id}"
    return {
        "caseId": case_id,
        "descriptorRef": {
            "byteLength": 179081,
            "path": descriptor_path,
            "pointer": pointer,
            "sha256": (
                "62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749"
            ),
        },
        "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
        "expectedValidationStatus": "INVALID",
        "operandRef": {
            "byteLength": 29105,
            "path": operand_path,
            "pointer": pointer,
            "sha256": (
                "069f9715e259969c8272fc83f75b86888a01ad91c226241834d67bb4a385078b"
            ),
        },
        "oracleRef": {
            "byteLength": 26754,
            "path": oracle_path,
            "pointer": pointer,
            "sha256": (
                "ca7eba0e46f1f68dff2eb6f65c43c16aa73588dff927d170138ef1e9aff83678"
            ),
        },
        "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
    }


_EXPECTED_INVENTORY = {
    "casePackAssets": 135,
    "controlFiles": EXPECTED_CONTROL_COUNT,
    "correctedInventoryTotal": EXPECTED_CORRECTED_INVENTORY_COUNT,
    "coverageObligationPackAssets": 3,
    "directSchema": EXPECTED_DIRECT_SCHEMA_COUNT,
    "directStatic": EXPECTED_DIRECT_STATIC_COUNT,
    "directTotal": EXPECTED_EXECUTABLE_COUNT,
    "excludedCoverageObligations": (
        EXPECTED_OPEN_PHASE1_GAP_COUNT + EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT
    ),
    "expectedDispositionCounts": {
        "ACCEPT": EXPECTED_ACCEPT_COUNT,
        "DEFERRED": EXPECTED_DEFERRED_COUNT,
        "REJECT": EXPECTED_REJECT_COUNT,
    },
    "fixtureContractAssets": len(FIXTURE_CONTRACT_ASSET_PATHS),
    "futureModelObligations": EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT,
    "manifestCaseRows": EXPECTED_CASE_COUNT,
    "openPhase1CoverageGaps": EXPECTED_OPEN_PHASE1_GAP_COUNT,
    "physicalAssets": EXPECTED_ASSET_COUNT,
    "pilotCaseCount": len(PILOT_CASE_IDS),
    "schemaOracleBatchCaseCount": (
        len(SCHEMA_REF_BATCH01_CASE_IDS)
        + len(SCHEMA_TEXT_BATCH02_CASE_IDS)
        + len(SCHEMA_IDENTIFIER_BATCH03_CASE_IDS)
        + len(SCHEMA_SCALAR_BATCH04_CASE_IDS)
        + len(SCHEMA_SCALAR_BATCH05_CASE_IDS)
    ),
    "schemaOracleBatchCount": 5,
    "totalCorpusPaths": EXPECTED_ASSET_COUNT + EXPECTED_CONTROL_COUNT,
    "traceOnly": EXPECTED_TRACE_ONLY_COUNT,
    "withdrawnClaims": {
        "correctedCaseInventoryCount": 2230,
        "executableAcceptanceCount": 2115,
        "status": "withdrawn; neither value is an active acceptance count",
    },
}
_EXPECTED_FIXTURE_CONTRACT = {
    "contractSchema": {
        "byteLength": 14450,
        "path": "tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json",
        "schemaId": FIXTURE_CONTRACT_SCHEMA_ID,
        "sha256": "887b79afd12950bad428fda4b2d3402ee5f3e7e82a75991f25cbabb53a14ed71",
    },
    "contractVersion": FIXTURE_CONTRACT_VERSION,
    "diagnosticIdentityVersions": [SCHEMA_DIAGNOSTIC_V1, STATIC_DIAGNOSTIC_V1],
    "pilotCases": [
        {
            "caseId": "phase1-static.branch-policy.negative.16-no-allow-match",
            "descriptorRef": {
                "byteLength": 6758,
                "path": "tests/schema/fixtures/v1alpha1/static/negative/branch-policy-matrix.json",
                "pointer": "/cases/phase1-static.branch-policy.negative.16-no-allow-match",
                "sha256": "4e96e524af2426e480719a23cb2b54609fba87db6f008164ed3c0cf93b8b3e99",
            },
            "diagnosticIdentityVersion": STATIC_DIAGNOSTIC_V1,
            "expectedValidationStatus": "INVALID",
            "operandRef": {
                "byteLength": 31786,
                "path": "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json",
                "pointer": "/cases/phase1-static.branch-policy.negative.16-no-allow-match",
                "sha256": "8375e157311c2aa04be3297efaf6cf85d998a06fcc0b85ce7fcc30d31cdec2dc",
            },
            "oracleRef": {
                "byteLength": 727,
                "path": "tests/schema/fixtures/v1alpha1/s6/oracles/static-branch-policy-pilot.json",
                "pointer": "/cases/phase1-static.branch-policy.negative.16-no-allow-match",
                "sha256": "3e5ebd6ddc07e1695cacb2d8610621c7173b4ce37023ed81af55570a3240b0a6",
            },
            "validatorEntryPoint": STATIC_VALIDATOR_ENTRY_POINT,
        },
        {
            "caseId": "schema.branch-policy.negative.01-empty-prefix",
            "descriptorRef": {
                "byteLength": 2772,
                "path": "tests/schema/fixtures/v1alpha1/schema/negative/branch-policy-matrix.json",
                "pointer": "/cases/schema.branch-policy.negative.01-empty-prefix",
                "sha256": "47296d0c2f514c51e754a3dae2df2fb3220dcdb1da7fb7bba98123e701309690",
            },
            "diagnosticIdentityVersion": SCHEMA_DIAGNOSTIC_V1,
            "expectedValidationStatus": "INVALID",
            "operandRef": {
                "byteLength": 31786,
                "path": "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json",
                "pointer": "/cases/schema.branch-policy.negative.01-empty-prefix",
                "sha256": "8375e157311c2aa04be3297efaf6cf85d998a06fcc0b85ce7fcc30d31cdec2dc",
            },
            "oracleRef": {
                "byteLength": 1059,
                "path": "tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json",
                "pointer": "/cases/schema.branch-policy.negative.01-empty-prefix",
                "sha256": "a3bbea2f6834ca0511e370b51e71c32c0e6854cecf24d2869cea7698c4c571ae",
            },
            "validatorEntryPoint": SCHEMA_VALIDATOR_ENTRY_POINT,
        },
        {
            "caseId": "static.branch-policy.positive.01-exact-allow-no-deny",
            "descriptorRef": {
                "byteLength": 2932,
                "path": "tests/schema/fixtures/v1alpha1/static/positive/branch-policy-matrix.json",
                "pointer": "/cases/static.branch-policy.positive.01-exact-allow-no-deny",
                "sha256": "64249db00a085ed0e6287a7618fac860621f65ecbae73425453298769f3c0dfa",
            },
            "diagnosticIdentityVersion": STATIC_DIAGNOSTIC_V1,
            "expectedValidationStatus": "PASS",
            "operandRef": {
                "byteLength": 31786,
                "path": "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json",
                "pointer": "/cases/static.branch-policy.positive.01-exact-allow-no-deny",
                "sha256": "8375e157311c2aa04be3297efaf6cf85d998a06fcc0b85ce7fcc30d31cdec2dc",
            },
            "oracleRef": None,
            "validatorEntryPoint": STATIC_VALIDATOR_ENTRY_POINT,
        },
    ],
    "schemaOracleBatches": [
        {
            "batchId": SCHEMA_REF_BATCH01_ID,
            "caseCount": len(SCHEMA_REF_BATCH01_CASE_IDS),
            "cases": [
                _schema_ref_batch01_binding(case_id)
                for case_id in SCHEMA_REF_BATCH01_CASE_IDS
            ],
        },
        {
            "batchId": SCHEMA_TEXT_BATCH02_ID,
            "caseCount": len(SCHEMA_TEXT_BATCH02_CASE_IDS),
            "cases": [
                _schema_text_batch02_binding(case_id)
                for case_id in SCHEMA_TEXT_BATCH02_CASE_IDS
            ],
        },
        {
            "batchId": SCHEMA_IDENTIFIER_BATCH03_ID,
            "caseCount": len(SCHEMA_IDENTIFIER_BATCH03_CASE_IDS),
            "cases": [
                _schema_identifier_batch03_binding(case_id)
                for case_id in SCHEMA_IDENTIFIER_BATCH03_CASE_IDS
            ],
        },
        {
            "batchId": SCHEMA_SCALAR_BATCH04_ID,
            "caseCount": len(SCHEMA_SCALAR_BATCH04_CASE_IDS),
            "cases": [
                _schema_scalar_batch04_binding(case_id)
                for case_id in SCHEMA_SCALAR_BATCH04_CASE_IDS
            ],
        },
        {
            "batchId": SCHEMA_SCALAR_BATCH05_ID,
            "caseCount": len(SCHEMA_SCALAR_BATCH05_CASE_IDS),
            "cases": [
                _schema_scalar_batch05_binding(case_id)
                for case_id in SCHEMA_SCALAR_BATCH05_CASE_IDS
            ],
        },
    ],
}
_COVERAGE_DISPOSITION_CONTRACT = {
    "TRACE_ONLY": (
        "PRESERVED_NON_AUTHORIZING_LATER_OBSERVATION",
        True,
    ),
    "COVERAGE_LEDGER_OPEN": ("OPEN_PHASE1_COVERAGE_GAP", False),
    "FUTURE_MODEL_OBLIGATION": ("FUTURE_OWNER_OPEN", False),
}


class FixtureContractError(AssertionError):
    """The immutable fixture contract is malformed or internally inconsistent."""


class DuplicateJsonKeyError(ValueError):
    """A JSON object contains a duplicate member name."""


class ValidatorCapabilityError(RuntimeError):
    """The selected validator could not return a valid diagnostic result."""


class DiagnosticAttributionError(ValidatorCapabilityError):
    """A Schema error cannot be attributed to one exact catalog location."""


@dataclass(frozen=True, slots=True)
class FixtureCase:
    id: str
    asset: str | None
    asset_pointer: str | None
    owner: str
    layer: str
    expected_disposition: str
    expected_stage: str
    expected_failure_identity: str | None
    polarity: str
    resource: str
    coverage: tuple[str, ...]
    inventory_disposition: str
    expected_diagnostic_identities: tuple[str, ...] | None


@dataclass(frozen=True, slots=True)
class CoverageObligation:
    original_case_id: str
    asset: str
    asset_pointer: str
    inventory_disposition: str
    coverage_status: str
    counted_in_corrected_inventory: bool


@dataclass(frozen=True, slots=True)
class SchemaDiagnostic:
    schema_resource_id: str
    instance_pointer: str
    schema_pointer: str
    keyword: str

    @property
    def identity(self) -> str:
        return "|".join(
            (
                self.schema_resource_id,
                self.instance_pointer,
                self.schema_pointer,
                self.keyword,
            )
        )


@dataclass(frozen=True, slots=True)
class StaticDiagnosticIdentity:
    code: str
    subject_id: str | None
    instance_pointer: str
    predicate_family: str
    schema_id: str | None
    schema_pointer: str | None
    keyword: str

    @property
    def identity(self) -> str:
        return "|".join(
            (
                self.code,
                self.subject_id or "<null>",
                self.instance_pointer,
                self.predicate_family,
                self.schema_id or "<null>",
                self.schema_pointer or "<null>",
                self.keyword,
            )
        )


DiagnosticIdentity = SchemaDiagnostic | StaticDiagnosticIdentity


@dataclass(frozen=True, slots=True)
class DiagnosticSetComparison:
    status: str
    missing: tuple[DiagnosticIdentity, ...]
    unexpected: tuple[DiagnosticIdentity, ...]


@dataclass(frozen=True, slots=True)
class CaseResult:
    case_id: str
    source_asset: str | None
    owner: str
    expected_disposition: str
    expected_stage: str
    execution_mode: str
    actual_result: str
    declared_diagnostic_identity: str | None
    actual_diagnostic_identities: tuple[str, ...]
    expected_diagnostic_identities: tuple[str, ...] | None = None
    execution_status: str = "EXECUTED"
    oracle_status: str = "NOT_APPLICABLE"
    schema_diagnostics: tuple[SchemaDiagnostic, ...] = ()
    static_diagnostics: tuple[StaticDiagnosticIdentity, ...] = ()
    diagnostic_identity_version: str | None = None
    expected_typed_diagnostics: tuple[DiagnosticIdentity, ...] | None = None
    missing_diagnostics: tuple[DiagnosticIdentity, ...] = ()
    unexpected_diagnostics: tuple[DiagnosticIdentity, ...] = ()
    validation_status: str | None = None
    static_status: str | None = None
    proof_treatment: str | None = None


@dataclass(frozen=True, slots=True)
class ManifestAudit:
    asset_count: int
    control_count: int
    case_count: int
    deferred_count: int
    executable_count: int
    trace_only_count: int
    corrected_inventory_count: int
    open_phase1_gap_count: int
    future_model_obligation_count: int
    checkout_eol_adjusted_count: int
    missing_oracle_count: int
    direct_execution_gap_count: int
    problems: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CoverageGapDisposition:
    case_id: str
    responsible_workstreams: tuple[str, ...]
    missing_obligations: tuple[str, ...]
    existing_executable_coverage: tuple[str, ...]
    disposition: str


def _reject_constant(token: str) -> None:
    raise ValueError(f"non-standard JSON constant: {token}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKeyError(key)
        result[key] = value
    return result


def strict_json_loads(source: str | bytes) -> Any:
    """Decode JSON without duplicate keys or non-standard numeric constants."""
    if isinstance(source, bytes):
        source = source.decode("utf-8", errors="strict")
    return json.loads(
        source,
        object_pairs_hook=_unique_object,
        parse_constant=_reject_constant,
    )


def _sha256(source: bytes) -> str:
    return hashlib.sha256(source).hexdigest()


def git_blob_oid(source: bytes) -> str:
    header = f"blob {len(source)}\0".encode("ascii")
    return hashlib.sha1(header + source, usedforsecurity=False).hexdigest()


def canonical_checkout_bytes(
    source: bytes,
    *,
    expected_sha256: str,
    expected_length: int | None,
    encoding: str,
    identity: str,
) -> tuple[bytes, bool]:
    """Return authenticated bytes, permitting only an exact CRLF checkout view.

    Raw-byte fixtures are never normalized.  UTF-8 JSON and the manifest may
    use the canonical Git LF bytes when, and only when, replacing CRLF with LF
    reproduces both authenticated identities exactly and no other CR remains.
    """
    if _sha256(source) == expected_sha256 and (
        expected_length is None or len(source) == expected_length
    ):
        return source, False
    if encoding != "utf-8-json":
        raise FixtureContractError(
            f"raw checkout bytes differ from the authenticated identity: {identity}"
        )
    without_crlf = source.replace(b"\r\n", b"")
    if b"\r\n" not in source or b"\r" in without_crlf:
        raise FixtureContractError(
            f"checkout bytes are not an exact CRLF view: {identity}"
        )
    canonical = source.replace(b"\r\n", b"\n")
    if _sha256(canonical) != expected_sha256 or (
        expected_length is not None and len(canonical) != expected_length
    ):
        raise FixtureContractError(
            f"CRLF canonicalization does not reproduce the authenticated identity: {identity}"
        )
    return canonical, True


MANIFEST_PHYSICAL_BYTES = MANIFEST_PATH.read_bytes()
MANIFEST_PHYSICAL_SHA256 = _sha256(MANIFEST_PHYSICAL_BYTES)
MANIFEST_BYTES, MANIFEST_EOL_ADJUSTED = canonical_checkout_bytes(
    MANIFEST_PHYSICAL_BYTES,
    expected_sha256=CANDIDATE_MANIFEST_SHA256,
    expected_length=None,
    encoding="utf-8-json",
    identity="fixture manifest",
)
MANIFEST_SHA256 = _sha256(MANIFEST_BYTES)
MANIFEST_GIT_BLOB = git_blob_oid(MANIFEST_BYTES)
MANIFEST: dict[str, Any] = strict_json_loads(MANIFEST_BYTES)
FIXTURE_CONTRACT = MANIFEST["fixtureContract"]
PILOT_BINDINGS = tuple(FIXTURE_CONTRACT["pilotCases"])
SCHEMA_ORACLE_BATCHES = tuple(FIXTURE_CONTRACT["schemaOracleBatches"])
SCHEMA_ORACLE_BATCH_BINDINGS = tuple(
    binding
    for batch in SCHEMA_ORACLE_BATCHES
    for binding in batch["cases"]
)
FIXTURE_CONTRACT_BINDINGS = PILOT_BINDINGS + SCHEMA_ORACLE_BATCH_BINDINGS
FIXTURE_CONTRACTS_BY_CASE = {
    item["caseId"]: item for item in FIXTURE_CONTRACT_BINDINGS
}


def _make_case(item: Mapping[str, Any]) -> FixtureCase:
    expected_diagnostics = item.get("expectedDiagnosticIdentities")
    return FixtureCase(
        id=item["id"],
        asset=item["asset"],
        asset_pointer=item.get("assetPointer"),
        owner=item["owner"],
        layer=item["layer"],
        expected_disposition=item["expectedDisposition"],
        expected_stage=item["expectedStage"],
        expected_failure_identity=item["expectedFailureIdentity"],
        polarity=item["polarity"],
        resource=item["resource"],
        coverage=tuple(item["coverage"]),
        inventory_disposition=item["inventoryDisposition"],
        expected_diagnostic_identities=(
            tuple(expected_diagnostics)
            if isinstance(expected_diagnostics, list)
            else None
        ),
    )


CASES = tuple(_make_case(item) for item in MANIFEST["cases"])
CASES_BY_ID = {case.id: case for case in CASES}
ASSETS_BY_PATH = {item["path"]: item for item in MANIFEST["assets"]}
COVERAGE_OBLIGATIONS = tuple(
    CoverageObligation(
        original_case_id=item["originalCaseId"],
        asset=item["asset"],
        asset_pointer=item["assetPointer"],
        inventory_disposition=item["inventoryDisposition"],
        coverage_status=item["coverageStatus"],
        counted_in_corrected_inventory=item["countedInCorrectedInventory"],
    )
    for item in MANIFEST["coverageObligations"]
)


def json_pointer(parts: Any) -> str:
    """Return an RFC 6901 pointer with deterministic token escaping."""
    encoded = []
    for part in parts:
        token = str(part).replace("~", "~0").replace("/", "~1")
        encoded.append(token)
    return "/" + "/".join(encoded) if encoded else ""


def _decode_pointer_token(raw: str) -> str:
    output: list[str] = []
    index = 0
    while index < len(raw):
        if raw[index] != "~":
            output.append(raw[index])
            index += 1
            continue
        if index + 1 >= len(raw) or raw[index + 1] not in "01":
            raise FixtureContractError(f"invalid JSON Pointer escape: {raw!r}")
        output.append("~" if raw[index + 1] == "0" else "/")
        index += 2
    return "".join(output)


def resolve_json_pointer(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise FixtureContractError(f"JSON Pointer is not absolute: {pointer!r}")
    current = document
    for raw in pointer[1:].split("/"):
        token = _decode_pointer_token(raw)
        if isinstance(current, list):
            if _POINTER_INDEX.fullmatch(token) is None:
                raise FixtureContractError(f"invalid array index in pointer: {token!r}")
            index = int(token)
            if index >= len(current):
                raise FixtureContractError(f"array index is out of range: {token!r}")
            current = current[index]
        elif isinstance(current, dict):
            if token not in current:
                raise FixtureContractError(f"missing pointer member: {token!r}")
            current = current[token]
        else:
            raise FixtureContractError("JSON Pointer traverses a scalar value")
    return current


def checked_fixture_path(relative_path: str, *, must_exist: bool = True) -> Path:
    """Resolve one manifest path and reject aliases or escape from the corpus."""
    if not isinstance(relative_path, str) or not relative_path:
        raise FixtureContractError("fixture path must be a non-empty string")
    if "\\" in relative_path or relative_path.startswith(("/", "//")):
        raise FixtureContractError(
            f"fixture path is not canonical POSIX relative: {relative_path!r}"
        )
    pure = PurePosixPath(relative_path)
    if (
        pure.is_absolute()
        or any(part in ("", ".", "..") for part in pure.parts)
        or (pure.parts and ":" in pure.parts[0])
    ):
        raise FixtureContractError(f"fixture path is unsafe: {relative_path!r}")
    fixture_prefix = ("tests", "schema", "fixtures", "v1alpha1")
    if pure.parts[: len(fixture_prefix)] != fixture_prefix:
        raise FixtureContractError(f"fixture path is outside the approved root: {relative_path!r}")
    candidate = REPOSITORY_ROOT.joinpath(*pure.parts)
    root_resolved = FIXTURE_ROOT.resolve(strict=True)
    resolved = candidate.resolve(strict=must_exist)
    if not resolved.is_relative_to(root_resolved):
        raise FixtureContractError(
            f"fixture path resolves outside the approved root: {relative_path!r}"
        )
    return candidate


@lru_cache(maxsize=None)
def _asset_physical_bytes(relative_path: str) -> bytes:
    return checked_fixture_path(relative_path).read_bytes()


@lru_cache(maxsize=None)
def _asset_bytes(relative_path: str) -> bytes:
    record = ASSETS_BY_PATH.get(relative_path)
    if record is None:
        raise FixtureContractError(f"asset is not in the authenticated inventory: {relative_path}")
    canonical, _adjusted = canonical_checkout_bytes(
        _asset_physical_bytes(relative_path),
        expected_sha256=record["sha256"],
        expected_length=record["byteLength"],
        encoding=record["encoding"],
        identity=relative_path,
    )
    return canonical


def asset_uses_checkout_eol_adjustment(relative_path: str) -> bool:
    return _asset_bytes(relative_path) != _asset_physical_bytes(relative_path)


@lru_cache(maxsize=None)
def _asset_document(relative_path: str) -> Any:
    return strict_json_loads(_asset_bytes(relative_path))


def fixture_contract_binding(case: FixtureCase | str) -> Mapping[str, Any] | None:
    case_id = case if isinstance(case, str) else case.id
    return FIXTURE_CONTRACTS_BY_CASE.get(case_id)


def _authenticated_reference_payload(
    reference: Mapping[str, Any], *, validate_sidecar: bool = False
) -> Any:
    path = reference.get("path")
    record = ASSETS_BY_PATH.get(path)
    if record is None:
        raise FixtureContractError(f"fixture-contract reference is not an asset: {path!r}")
    if (
        record.get("byteLength") != reference.get("byteLength")
        or record.get("sha256") != reference.get("sha256")
    ):
        raise FixtureContractError(
            f"fixture-contract reference identity differs from its asset: {path!r}"
        )
    document = (
        _validated_fixture_sidecar_document(path)
        if validate_sidecar
        else _asset_document(path)
    )
    pointer = reference.get("pointer")
    return resolve_json_pointer(document, pointer) if pointer is not None else document


@lru_cache(maxsize=1)
def _fixture_contract_validator() -> Draft202012Validator:
    schema_reference = FIXTURE_CONTRACT["contractSchema"]
    schema = _authenticated_reference_payload(schema_reference)
    if not isinstance(schema, dict) or schema.get("$id") != FIXTURE_CONTRACT_SCHEMA_ID:
        raise FixtureContractError("fixture-contract schema identity mismatch")
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(
        schema,
        registry=source_registry(),
        format_checker=build_format_checker(),
    )


@lru_cache(maxsize=None)
def _validated_fixture_sidecar_document(relative_path: str) -> Mapping[str, Any]:
    if relative_path == FIXTURE_CONTRACT["contractSchema"]["path"]:
        raise FixtureContractError("the contract schema is not an operand or oracle sidecar")
    document = _asset_document(relative_path)
    if not isinstance(document, dict):
        raise FixtureContractError(f"fixture sidecar is not an object: {relative_path}")
    errors = tuple(_fixture_contract_validator().iter_errors(document))
    if errors:
        raise FixtureContractError(
            f"fixture sidecar violates fixture-contract-v1: {relative_path}"
        )
    return document


@lru_cache(maxsize=None)
def fixture_operand(case: FixtureCase | str) -> Mapping[str, Any] | None:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    binding = fixture_contract_binding(case)
    if binding is None:
        return None
    payload = _authenticated_reference_payload(
        binding["operandRef"], validate_sidecar=True
    )
    if not isinstance(payload, dict) or payload.get("caseId") != case.id:
        raise FixtureContractError(
            f"fixture-contract operand identity mismatch: {case.id}"
        )
    return payload


def _diagnostic_sort_key(
    version: str, diagnostic: DiagnosticIdentity
) -> tuple[str, ...]:
    if version == SCHEMA_DIAGNOSTIC_V1 and isinstance(diagnostic, SchemaDiagnostic):
        return (
            diagnostic.instance_pointer,
            diagnostic.schema_resource_id,
            diagnostic.schema_pointer,
            diagnostic.keyword,
        )
    if version == STATIC_DIAGNOSTIC_V1 and isinstance(
        diagnostic, StaticDiagnosticIdentity
    ):
        return (
            diagnostic.instance_pointer,
            diagnostic.schema_id or "",
            diagnostic.schema_pointer or "",
            diagnostic.keyword,
            diagnostic.code,
            diagnostic.subject_id or "",
            diagnostic.predicate_family,
        )
    raise FixtureContractError(
        f"diagnostic does not match identity version {version!r}"
    )


def _parse_typed_diagnostic(
    version: str, item: Mapping[str, Any]
) -> DiagnosticIdentity:
    if version == SCHEMA_DIAGNOSTIC_V1:
        return SchemaDiagnostic(
            schema_resource_id=item["schemaResourceId"],
            instance_pointer=item["instancePointer"],
            schema_pointer=item["schemaPointer"],
            keyword=item["keyword"],
        )
    if version == STATIC_DIAGNOSTIC_V1:
        return StaticDiagnosticIdentity(
            code=item["code"],
            subject_id=item["subjectId"],
            instance_pointer=item["instancePointer"],
            predicate_family=item["predicateFamily"],
            schema_id=item["schemaId"],
            schema_pointer=item["schemaPointer"],
            keyword=item["keyword"],
        )
    raise FixtureContractError(f"unsupported diagnostic identity version: {version!r}")


@lru_cache(maxsize=None)
def expected_typed_diagnostics(
    case: FixtureCase | str,
) -> tuple[DiagnosticIdentity, ...] | None:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    binding = fixture_contract_binding(case)
    if binding is None or binding["oracleRef"] is None:
        return None
    document = _validated_fixture_sidecar_document(binding["oracleRef"]["path"])
    if document.get("diagnosticIdentityVersion") != binding[
        "diagnosticIdentityVersion"
    ]:
        raise FixtureContractError(f"oracle identity-version mismatch: {case.id}")
    payload = _authenticated_reference_payload(
        binding["oracleRef"], validate_sidecar=True
    )
    if not isinstance(payload, dict) or payload.get("caseId") != case.id:
        raise FixtureContractError(
            f"fixture-contract oracle identity mismatch: {case.id}"
        )
    version = binding["diagnosticIdentityVersion"]
    expected = tuple(
        _parse_typed_diagnostic(version, item)
        for item in payload["expectedDiagnostics"]
    )
    if not expected or expected != tuple(
        sorted(set(expected), key=lambda item: _diagnostic_sort_key(version, item))
    ):
        raise FixtureContractError(
            "fixture-contract oracle is not nonempty, unique, and canonically "
            f"ordered: {case.id}"
        )
    return expected


def compare_diagnostic_identity_sets(
    version: str,
    expected: tuple[DiagnosticIdentity, ...],
    actual: tuple[DiagnosticIdentity, ...],
) -> DiagnosticSetComparison:
    if not expected:
        raise FixtureContractError("an exact negative oracle must be nonempty")
    for diagnostic in (*expected, *actual):
        _diagnostic_sort_key(version, diagnostic)
    expected_set = set(expected)
    actual_set = set(actual)
    missing = tuple(
        sorted(expected_set - actual_set, key=lambda item: _diagnostic_sort_key(version, item))
    )
    unexpected = tuple(
        sorted(actual_set - expected_set, key=lambda item: _diagnostic_sort_key(version, item))
    )
    return DiagnosticSetComparison(
        status="EXACT_MATCH" if not missing and not unexpected else "EXACT_SET_MISMATCH",
        missing=missing,
        unexpected=unexpected,
    )


def case_payload(case: FixtureCase | str) -> Any:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    if case.asset is None:
        raise FixtureContractError(f"case {case.id} has no source asset")
    if case.asset_pointer is None:
        raise FixtureContractError(f"case {case.id} has no decoded payload pointer")
    return resolve_json_pointer(_asset_document(case.asset), case.asset_pointer)


def compare_asset_inventory(
    declared: set[str] | frozenset[str], actual: set[str] | frozenset[str]
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return tuple(sorted(declared - actual)), tuple(sorted(actual - declared))


def coverage_obligation_payload(obligation: CoverageObligation | str) -> Mapping[str, Any]:
    if isinstance(obligation, str):
        matches = [
            item for item in COVERAGE_OBLIGATIONS if item.original_case_id == obligation
        ]
        if len(matches) != 1:
            raise FixtureContractError(
                f"coverage obligation identity is not unique: {obligation!r}"
            )
        obligation = matches[0]
    payload = resolve_json_pointer(
        _asset_document(obligation.asset), obligation.asset_pointer
    )
    if not isinstance(payload, dict):
        raise FixtureContractError(
            f"coverage obligation {obligation.original_case_id} is not an object"
        )
    if payload.get("originalCaseId") != obligation.original_case_id:
        raise FixtureContractError(
            f"coverage obligation pointer identity mismatch: {obligation.original_case_id}"
        )
    return payload


def missing_negative_oracle_case_ids() -> tuple[str, ...]:
    """Return direct REJECT rows without an independent exact identity-set oracle."""
    return tuple(
        case.id
        for case in CASES
        if case.inventory_disposition in {"DIRECT_SCHEMA", "DIRECT_STATIC"}
        and case.expected_disposition == "REJECT"
        and case.expected_diagnostic_identities is None
        and expected_typed_diagnostics(case) is None
    )


def direct_execution_gap_case_ids() -> tuple[str, ...]:
    """Return direct rows whose immutable fixture payload has no executable operand."""
    gaps: list[str] = []
    for case in CASES:
        if case.inventory_disposition != "DIRECT_STATIC":
            continue
        contract_operand = fixture_operand(case)
        if contract_operand is not None:
            if contract_operand.get("operandKind") != "static":
                gaps.append(case.id)
            continue
        payload = case_payload(case)
        if not isinstance(payload, dict) or "subject" not in payload:
            gaps.append(case.id)
    return tuple(gaps)


def coverage_gap_dispositions() -> tuple[CoverageGapDisposition, ...]:
    dispositions: list[CoverageGapDisposition] = []
    for obligation in COVERAGE_OBLIGATIONS:
        if obligation.inventory_disposition != "COVERAGE_LEDGER_OPEN":
            continue
        payload = coverage_obligation_payload(obligation)
        dispositions.append(
            CoverageGapDisposition(
                case_id=obligation.original_case_id,
                responsible_workstreams=tuple(
                    payload.get("responsiblePhasesOrWorkstreams", ())
                ),
                missing_obligations=tuple(payload.get("missingCoverageObligations", ())),
                existing_executable_coverage=tuple(
                    payload.get("existingConcreteExecutableCoverage", ())
                ),
                disposition=obligation.inventory_disposition,
            )
        )
    return tuple(dispositions)


def trace_only_obligation_ids() -> tuple[str, ...]:
    return tuple(
        item.original_case_id
        for item in COVERAGE_OBLIGATIONS
        if item.inventory_disposition == "TRACE_ONLY"
    )


def future_model_obligation_ids() -> tuple[str, ...]:
    return tuple(
        item.original_case_id
        for item in COVERAGE_OBLIGATIONS
        if item.inventory_disposition == "FUTURE_MODEL_OBLIGATION"
    )


def _has_top_level_manifest_self_digest(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    for key in value:
        folded = key.casefold()
        manifest_identity = "manifest" in folded and any(
            token in folded for token in ("sha", "digest", "blob")
        )
        if manifest_identity or ("self" in folded and "digest" in folded):
            return True
    return False


def manifest_structure_problems(manifest: Mapping[str, Any]) -> tuple[str, ...]:
    """Return deterministic structural problems without touching fixture files."""
    problems: list[str] = []
    if frozenset(manifest) != _EXPECTED_TOP_LEVEL_KEYS:
        problems.append("manifest top-level key set differs from the frozen contract")
    if manifest.get("apiVersion") != API_VERSION:
        problems.append("manifest apiVersion mismatch")
    if manifest.get("schemaSetRevision") != SCHEMA_SET_REVISION:
        problems.append("manifest schemaSetRevision mismatch")
    if manifest.get("fixtureRoot") != "tests/schema/fixtures/v1alpha1":
        problems.append("manifest fixtureRoot mismatch")
    if manifest.get("authorityClaim") is not False:
        problems.append("manifest authorityClaim must be false")
    if manifest.get("evidenceClaim") is not False:
        problems.append("manifest evidenceClaim must be false")
    if manifest.get("productionReceiptClaim") is not False:
        problems.append("manifest productionReceiptClaim must be false")
    if manifest.get("inventoryFormatVersion") != EXPECTED_INVENTORY_FORMAT_VERSION:
        problems.append("manifest inventoryFormatVersion mismatch")
    if manifest.get("inventoryProvenance") != _EXPECTED_INVENTORY_PROVENANCE:
        problems.append("manifest inventory provenance mismatch")
    if manifest.get("inventory") != _EXPECTED_INVENTORY:
        problems.append("manifest inventory aggregates mismatch")
    if manifest.get("fixtureContract") != _EXPECTED_FIXTURE_CONTRACT:
        problems.append("manifest fixture-contract metadata mismatch")
    if _has_top_level_manifest_self_digest(manifest):
        problems.append("manifest must not contain a self-digest")

    assets = manifest.get("assets")
    cases = manifest.get("cases")
    obligations = manifest.get("coverageObligations")
    if not isinstance(assets, list):
        problems.append("manifest assets must be an array")
        assets = []
    if not isinstance(cases, list):
        problems.append("manifest cases must be an array")
        cases = []
    if not isinstance(obligations, list):
        problems.append("manifest coverageObligations must be an array")
        obligations = []

    asset_paths = [item.get("path") for item in assets if isinstance(item, dict)]
    if len(asset_paths) != len(assets) or any(not isinstance(path, str) for path in asset_paths):
        problems.append("every asset must have a string path")
    else:
        if len(set(asset_paths)) != len(asset_paths):
            problems.append("duplicate manifest asset path")
        if asset_paths != sorted(asset_paths):
            problems.append("manifest asset paths are not strictly sorted")

    case_ids = [item.get("id") for item in cases if isinstance(item, dict)]
    if len(case_ids) != len(cases) or any(not isinstance(case_id, str) for case_id in case_ids):
        problems.append("every logical case must have a string id")
    else:
        if len(set(case_ids)) != len(case_ids):
            problems.append("duplicate logical case id")
        if case_ids != sorted(case_ids):
            problems.append("logical case ids are not strictly sorted")
        if any(not case_id.isascii() for case_id in case_ids):
            problems.append("logical case ids must be ASCII")

    for item in cases:
        if not isinstance(item, dict):
            problems.append("logical case entry is not an object")
            continue
        missing = sorted(_CASE_REQUIRED_KEYS - frozenset(item))
        if missing:
            problems.append(f"case {item.get('id')!r} is missing fields: {','.join(missing)}")
            continue
        if item["expectedDisposition"] not in _DISPOSITIONS:
            problems.append(f"case {item['id']} has an unknown disposition")
        if item["inventoryDisposition"] not in _INVENTORY_DISPOSITIONS:
            problems.append(f"case {item['id']} has an unknown inventory disposition")
        if item["owner"] not in _OWNERS:
            problems.append(f"case {item['id']} has an unknown owner")
        if item["expectedStage"] not in _STAGES:
            problems.append(f"case {item['id']} has an unknown expected stage")
        if (
            item["inventoryDisposition"] == "DIRECT_SCHEMA"
            and (item["owner"], item["layer"]) != ("schema", "schema")
        ):
            problems.append(f"case {item['id']} has an invalid direct-Schema owner")
        if (
            item["inventoryDisposition"] == "DIRECT_STATIC"
            and item["expectedDisposition"] == "DEFERRED"
        ):
            problems.append(f"case {item['id']} marks a direct static row DEFERRED")
        if (
            item["inventoryDisposition"] == "DEFERRED"
            and item["expectedDisposition"] != "DEFERRED"
        ):
            problems.append(f"case {item['id']} has an active deferred row")
        if (
            item["expectedDisposition"] == "DEFERRED"
            and item["inventoryDisposition"] != "DEFERRED"
        ):
            problems.append(f"case {item['id']} has a direct DEFERRED disposition")
        coverage = item["coverage"]
        if (
            not isinstance(coverage, list)
            or not coverage
            or any(not isinstance(value, str) or not value.isascii() for value in coverage)
            or coverage != sorted(set(coverage))
        ):
            problems.append(f"case {item['id']} has non-canonical coverage identities")
        if item["polarity"] == "positive" and item["expectedDisposition"] == "REJECT":
            problems.append(f"positive case {item['id']} declares REJECT")
        if item["polarity"] == "negative" and item["expectedDisposition"] == "ACCEPT":
            problems.append(f"negative case {item['id']} declares ACCEPT")
        failure = item["expectedFailureIdentity"]
        if item["expectedDisposition"] == "REJECT" and not isinstance(failure, str):
            problems.append(f"reject case {item['id']} lacks a diagnostic identity")
        if item["expectedDisposition"] == "ACCEPT" and failure is not None:
            problems.append(
                f"accept case {item['id']} unexpectedly declares a diagnostic identity"
            )
        expected_set = item.get("expectedDiagnosticIdentities")
        if expected_set is not None:
            if item["expectedDisposition"] != "REJECT":
                problems.append(
                    f"non-reject case {item['id']} declares a negative diagnostic oracle"
                )
            if (
                not isinstance(expected_set, list)
                or not expected_set
                or any(not isinstance(value, str) or not value for value in expected_set)
                or expected_set != sorted(set(expected_set))
            ):
                problems.append(
                    f"case {item['id']} has a non-canonical diagnostic identity set"
                )

    obligation_ids = [
        item.get("originalCaseId") for item in obligations if isinstance(item, dict)
    ]
    if len(obligation_ids) != len(obligations) or any(
        not isinstance(case_id, str) for case_id in obligation_ids
    ):
        problems.append("every coverage obligation must have a string originalCaseId")
    else:
        if obligation_ids != sorted(obligation_ids):
            problems.append("coverage obligation ids are not strictly sorted")
        if len(obligation_ids) != len(set(obligation_ids)):
            problems.append("duplicate coverage obligation id")
        if any(not case_id.isascii() for case_id in obligation_ids):
            problems.append("coverage obligation ids must be ASCII")

    for item in obligations:
        if not isinstance(item, dict):
            problems.append("coverage obligation entry is not an object")
            continue
        if frozenset(item) != _COVERAGE_OBLIGATION_REQUIRED_KEYS:
            problems.append(
                f"coverage obligation {item.get('originalCaseId')!r} has a non-canonical envelope"
            )
            continue
        disposition = item["inventoryDisposition"]
        if disposition not in _COVERAGE_INVENTORY_DISPOSITIONS:
            problems.append(
                f"coverage obligation {item['originalCaseId']} has an unknown disposition"
            )
            continue
        expected_status, expected_counted = _COVERAGE_DISPOSITION_CONTRACT[disposition]
        if (
            item["coverageStatus"] != expected_status
            or item["countedInCorrectedInventory"] is not expected_counted
        ):
            problems.append(
                f"coverage obligation {item['originalCaseId']} violates its disposition contract"
            )
    return tuple(sorted(set(problems)))


def fixture_contract_structure_problems() -> tuple[str, ...]:
    """Authenticate the historical Pilot and Schema Oracle Batches 01 through 04."""
    problems: list[str] = []
    try:
        schema = _authenticated_reference_payload(FIXTURE_CONTRACT["contractSchema"])
        if not isinstance(schema, dict) or schema.get("$id") != FIXTURE_CONTRACT_SCHEMA_ID:
            problems.append("fixture-contract schema identity mismatch")
        _fixture_contract_validator()

        expected_classes = {
            "tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json": (
                "fixture-contract-schema"
            ),
            "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json": (
                "operand-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json": (
                "oracle-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/static-branch-policy-pilot.json": (
                "oracle-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-ref-batch01.json": (
                "operand-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-ref-batch01.json": (
                "oracle-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-text-batch02.json": (
                "operand-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-text-batch02.json": (
                "oracle-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-identifiers-batch03.json": (
                "operand-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-identifiers-batch03.json": (
                "oracle-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/operands/schema-common-scalars-batch04.json": (
                "operand-sidecar"
            ),
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-scalars-batch04.json": (
                "oracle-sidecar"
            ),
        }
        for path, expected_class in expected_classes.items():
            if ASSETS_BY_PATH[path].get("inventoryClass") != expected_class:
                problems.append(f"fixture-contract asset class mismatch: {path}")
            _asset_bytes(path)

        operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json"
        )
        operand_document = _validated_fixture_sidecar_document(operand_path)
        if tuple(operand_document["cases"]) != PILOT_CASE_IDS:
            problems.append("pilot operand case identities or ordering mismatch")

        schema_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json"
        )
        static_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/static-branch-policy-pilot.json"
        )
        schema_oracles = _validated_fixture_sidecar_document(schema_oracle_path)
        static_oracles = _validated_fixture_sidecar_document(static_oracle_path)
        if tuple(schema_oracles["cases"]) != (
            "schema.branch-policy.negative.01-empty-prefix",
        ):
            problems.append("Schema pilot oracle case inventory mismatch")
        if tuple(static_oracles["cases"]) != (
            "phase1-static.branch-policy.negative.16-no-allow-match",
        ):
            problems.append("static pilot oracle case inventory mismatch")

        if tuple(item["caseId"] for item in PILOT_BINDINGS) != PILOT_CASE_IDS:
            problems.append("manifest pilot case identities or ordering mismatch")

        if len(SCHEMA_ORACLE_BATCHES) != 5:
            problems.append("Schema Oracle batch inventory mismatch")
        else:
            batch01, batch02, batch03, batch04, batch05 = SCHEMA_ORACLE_BATCHES
            if (
                batch01.get("batchId") != SCHEMA_REF_BATCH01_ID
                or batch01.get("caseCount") != len(SCHEMA_REF_BATCH01_CASE_IDS)
                or tuple(item["caseId"] for item in batch01.get("cases", ()))
                != SCHEMA_REF_BATCH01_CASE_IDS
            ):
                problems.append("Schema Oracle Batch 01 metadata mismatch")
            if (
                batch02.get("batchId") != SCHEMA_TEXT_BATCH02_ID
                or batch02.get("caseCount") != len(SCHEMA_TEXT_BATCH02_CASE_IDS)
                or tuple(item["caseId"] for item in batch02.get("cases", ()))
                != SCHEMA_TEXT_BATCH02_CASE_IDS
            ):
                problems.append("Schema Oracle Batch 02 metadata mismatch")
            if (
                batch03.get("batchId") != SCHEMA_IDENTIFIER_BATCH03_ID
                or batch03.get("caseCount")
                != len(SCHEMA_IDENTIFIER_BATCH03_CASE_IDS)
                or tuple(item["caseId"] for item in batch03.get("cases", ()))
                != SCHEMA_IDENTIFIER_BATCH03_CASE_IDS
            ):
                problems.append("Schema Oracle Batch 03 metadata mismatch")
            if (
                batch04.get("batchId") != SCHEMA_SCALAR_BATCH04_ID
                or batch04.get("caseCount") != len(SCHEMA_SCALAR_BATCH04_CASE_IDS)
                or tuple(item["caseId"] for item in batch04.get("cases", ()))
                != SCHEMA_SCALAR_BATCH04_CASE_IDS
            ):
                problems.append("Schema Oracle Batch 04 metadata mismatch")
            if (
                batch05.get("batchId") != SCHEMA_SCALAR_BATCH05_ID
                or batch05.get("caseCount") != len(SCHEMA_SCALAR_BATCH05_CASE_IDS)
                or tuple(item["caseId"] for item in batch05.get("cases", ()))
                != SCHEMA_SCALAR_BATCH05_CASE_IDS
            ):
                problems.append("Schema Oracle Batch 05 metadata mismatch")

        batch_operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/"
            "schema-common-ref-batch01.json"
        )
        batch_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/"
            "schema-common-ref-batch01.json"
        )
        batch_operands = _validated_fixture_sidecar_document(batch_operand_path)
        batch_oracles = _validated_fixture_sidecar_document(batch_oracle_path)
        if tuple(batch_operands["cases"]) != SCHEMA_REF_BATCH01_CASE_IDS:
            problems.append("Schema Oracle Batch 01 operand inventory mismatch")
        if tuple(batch_oracles["cases"]) != SCHEMA_REF_BATCH01_CASE_IDS:
            problems.append("Schema Oracle Batch 01 oracle inventory mismatch")

        text_operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/"
            "schema-common-text-batch02.json"
        )
        text_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/"
            "schema-common-text-batch02.json"
        )
        text_operands = _validated_fixture_sidecar_document(text_operand_path)
        text_oracles = _validated_fixture_sidecar_document(text_oracle_path)
        if tuple(text_operands["cases"]) != SCHEMA_TEXT_BATCH02_CASE_IDS:
            problems.append("Schema Oracle Batch 02 operand inventory mismatch")
        if tuple(text_oracles["cases"]) != SCHEMA_TEXT_BATCH02_CASE_IDS:
            problems.append("Schema Oracle Batch 02 oracle inventory mismatch")

        identifier_operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/"
            "schema-common-identifiers-batch03.json"
        )
        identifier_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/"
            "schema-common-identifiers-batch03.json"
        )
        identifier_operands = _validated_fixture_sidecar_document(
            identifier_operand_path
        )
        identifier_oracles = _validated_fixture_sidecar_document(
            identifier_oracle_path
        )
        if tuple(identifier_operands["cases"]) != SCHEMA_IDENTIFIER_BATCH03_CASE_IDS:
            problems.append("Schema Oracle Batch 03 operand inventory mismatch")
        if tuple(identifier_oracles["cases"]) != SCHEMA_IDENTIFIER_BATCH03_CASE_IDS:
            problems.append("Schema Oracle Batch 03 oracle inventory mismatch")

        scalar_operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/"
            "schema-common-scalars-batch04.json"
        )
        scalar_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/"
            "schema-common-scalars-batch04.json"
        )
        scalar_operands = _validated_fixture_sidecar_document(scalar_operand_path)
        scalar_oracles = _validated_fixture_sidecar_document(scalar_oracle_path)
        if tuple(scalar_operands["cases"]) != SCHEMA_SCALAR_BATCH04_CASE_IDS:
            problems.append("Schema Oracle Batch 04 operand inventory mismatch")
        if tuple(scalar_oracles["cases"]) != SCHEMA_SCALAR_BATCH04_CASE_IDS:
            problems.append("Schema Oracle Batch 04 oracle inventory mismatch")

        batch05_operand_path = (
            "tests/schema/fixtures/v1alpha1/s6/operands/"
            "schema-common-scalars-batch05.json"
        )
        batch05_oracle_path = (
            "tests/schema/fixtures/v1alpha1/s6/oracles/"
            "schema-common-scalars-batch05.json"
        )
        batch05_operands = _validated_fixture_sidecar_document(batch05_operand_path)
        batch05_oracles = _validated_fixture_sidecar_document(batch05_oracle_path)
        if tuple(batch05_operands["cases"]) != SCHEMA_SCALAR_BATCH05_CASE_IDS:
            problems.append("Schema Oracle Batch 05 operand inventory mismatch")
        if tuple(batch05_oracles["cases"]) != SCHEMA_SCALAR_BATCH05_CASE_IDS:
            problems.append("Schema Oracle Batch 05 oracle inventory mismatch")

        if (
            len(FIXTURE_CONTRACT_BINDINGS) != len(FIXTURE_CONTRACT_CASE_IDS)
            or len(FIXTURE_CONTRACTS_BY_CASE) != len(FIXTURE_CONTRACT_CASE_IDS)
            or set(FIXTURE_CONTRACTS_BY_CASE) != set(FIXTURE_CONTRACT_CASE_IDS)
        ):
            problems.append("fixture-contract case identities are missing or duplicated")

        for case_id in PILOT_CASE_IDS:
            case = CASES_BY_ID[case_id]
            binding = FIXTURE_CONTRACTS_BY_CASE[case_id]
            descriptor_reference = binding["descriptorRef"]
            if (
                descriptor_reference["path"] != case.asset
                or descriptor_reference["pointer"] != case.asset_pointer
            ):
                problems.append(f"historical descriptor binding changed: {case_id}")
                continue
            descriptor = _authenticated_reference_payload(descriptor_reference)
            if descriptor != case_payload(case):
                problems.append(f"descriptor reference payload mismatch: {case_id}")
                continue

            operand = fixture_operand(case)
            if operand is None:
                problems.append(f"pilot operand is absent: {case_id}")
                continue
            if case.owner == "schema":
                schema_operand = operand.get("schemaOperand", {})
                if (
                    operand.get("operandKind") != "schema"
                    or binding["validatorEntryPoint"] != SCHEMA_VALIDATOR_ENTRY_POINT
                    or binding["diagnosticIdentityVersion"] != SCHEMA_DIAGNOSTIC_V1
                    or descriptor != {"prefix": schema_operand.get("instance")}
                ):
                    problems.append(f"Schema pilot operand projection mismatch: {case_id}")
            else:
                if (
                    operand.get("operandKind") != "static"
                    or binding["validatorEntryPoint"] != STATIC_VALIDATOR_ENTRY_POINT
                    or binding["diagnosticIdentityVersion"] != STATIC_DIAGNOSTIC_V1
                ):
                    problems.append(f"static pilot dispatch mismatch: {case_id}")
                    continue
                subject = operand["subject"]
                context = operand["validationContext"]
                roles = [
                    role
                    for role in context["governanceBundle"]["worktreeRoles"]
                    if role["metadata"]["id"]
                    == subject["spec"]["target"]["worktreeRoleRef"]["id"]
                ]
                if len(roles) != 1:
                    problems.append(f"static pilot role binding is not exact: {case_id}")
                    continue
                expected_ref = subject["spec"]["expectedBaseline"]["ref"]
                if (
                    roles[0]["spec"]["branchPolicy"] != descriptor.get("branchPolicy")
                    or expected_ref.get("branchRef") != descriptor.get("branchRef")
                ):
                    problems.append(f"static pilot descriptor projection mismatch: {case_id}")
                if "headState" in descriptor and subject["spec"]["expectedBaseline"][
                    "head"
                ]["state"] != descriptor["headState"]:
                    problems.append(f"static pilot HEAD projection mismatch: {case_id}")

                proof_responses = context["proofResponses"]
                expected_provenance = {
                    ("#/subject", get_resource("task-contract.schema.json").schema_id),
                    (
                        "#/validationContext/governanceBundle",
                        get_resource("governance-bundle.schema.json").schema_id,
                    ),
                    (
                        "#/validationContext/hostOverlay",
                        get_resource("host-overlay.schema.json").schema_id,
                    ),
                }
                observed_provenance = {
                    (item["subjectRef"], item["schemaResourceId"])
                    for item in proof_responses["inputProvenance"]
                    if item["schemaSetRevision"] == SCHEMA_SET_REVISION
                }
                if observed_provenance != expected_provenance:
                    problems.append(f"pilot input-provenance inventory mismatch: {case_id}")

                materialized = proof_responses["baselineMaterialization"]
                baseline = subject["spec"]["expectedBaseline"]
                if (
                    materialized["values"]["ref"] != baseline["ref"]
                    or materialized["values"]["head"] != baseline["head"]
                    or materialized["values"]["activeOperations"]
                    != baseline["activeOperations"]
                    or materialized["values"]["administrativeLocks"]
                    != baseline["administrativeLocks"]
                ):
                    problems.append(f"pilot baseline materialization mismatch: {case_id}")

            expected = expected_typed_diagnostics(case)
            if case.expected_disposition == "REJECT" and expected is None:
                problems.append(f"negative pilot lacks a typed oracle: {case_id}")
            if case.expected_disposition == "ACCEPT" and expected is not None:
                problems.append(f"positive pilot unexpectedly has an oracle: {case_id}")

        membership_bytes = (
            "\n".join(SCHEMA_TEXT_BATCH02_CASE_IDS) + "\n"
        ).encode("ascii")
        if _sha256(membership_bytes) != SCHEMA_TEXT_BATCH02_MEMBERSHIP_SHA256:
            problems.append("Schema Oracle Batch 02 membership identity mismatch")

        identifier_membership_bytes = (
            "\n".join(SCHEMA_IDENTIFIER_BATCH03_CASE_IDS) + "\n"
        ).encode("ascii")
        if (
            _sha256(identifier_membership_bytes)
            != SCHEMA_IDENTIFIER_BATCH03_MEMBERSHIP_SHA256
        ):
            problems.append("Schema Oracle Batch 03 membership identity mismatch")

        scalar_membership_bytes = (
            "\n".join(SCHEMA_SCALAR_BATCH04_CASE_IDS) + "\n"
        ).encode("ascii")
        if _sha256(scalar_membership_bytes) != SCHEMA_SCALAR_BATCH04_MEMBERSHIP_SHA256:
            problems.append("Schema Oracle Batch 04 membership identity mismatch")

        batch05_membership_bytes = (
            "\n".join(SCHEMA_SCALAR_BATCH05_CASE_IDS) + "\n"
        ).encode("ascii")
        if (
            _sha256(batch05_membership_bytes)
            != SCHEMA_SCALAR_BATCH05_MEMBERSHIP_SHA256
        ):
            problems.append("Schema Oracle Batch 05 membership identity mismatch")

        batch_contracts = (
            (
                "Batch 01",
                SCHEMA_REF_BATCH01_CASE_IDS,
                {
                    "gitRefIdentifier": "/$defs/gitRefIdentifier",
                    "branchRef": "/$defs/branchRef",
                    "branchPrefix": "/$defs/branchPrefix",
                },
            ),
            (
                "Batch 02",
                SCHEMA_TEXT_BATCH02_CASE_IDS,
                {
                    "displayText": "/$defs/displayText",
                    "sanitizedSummary": "/$defs/sanitizedSummary",
                },
            ),
            (
                "Batch 03",
                SCHEMA_IDENTIFIER_BATCH03_CASE_IDS,
                {
                    "checkIdentifier": "/$defs/checkIdentifier",
                    "logicalIdentifier": "/$defs/logicalIdentifier",
                    "profileIdentifier": "/$defs/profileIdentifier",
                    "reasonCode": "/$defs/reasonCode",
                    "remoteNamespaceComponent": "/$defs/remoteNamespaceComponent",
                    "remoteRepositoryName": "/$defs/remoteRepositoryName",
                },
            ),
            (
                "Batch 04",
                SCHEMA_SCALAR_BATCH04_CASE_IDS,
                {
                    "capability": "/$defs/capability",
                    "checkOutcome": "/$defs/checkOutcome",
                    "executionCheckOutcome": "/$defs/executionCheckOutcome",
                    "executionOutcome": "/$defs/executionOutcome",
                    "gitMode": "/$defs/gitMode",
                    "indexStage": "/$defs/indexStage",
                    "kind": "/$defs/kind",
                    "lifecycleOutcome": "/$defs/lifecycleOutcome",
                    "receiptDeliveryOutcome": "/$defs/receiptDeliveryOutcome",
                    "redactionCount": "/$defs/redactionCount",
                    "releaseOutcome": "/$defs/releaseOutcome",
                    "remotePort": "/$defs/remotePort",
                    "routingPriority": "/$defs/routingPriority",
                    "sequence": "/$defs/sequence",
                },
            ),
            (
                "Batch 05",
                SCHEMA_SCALAR_BATCH05_CASE_IDS,
                {
                    "allowWrite": "/$defs/allowWrite",
                    "apiVersion": "/$defs/apiVersion",
                    "canonicalUtcTimestamp": "/$defs/canonicalUtcTimestamp",
                    "canonicalUuid": "/$defs/canonicalUuid",
                    "capabilities": "/$defs/capabilities",
                    "mode": "/$defs/mode",
                    "posixAbsoluteHostPath": "/$defs/posixAbsoluteHostPath",
                    "remoteDnsHost": "/$defs/remoteDnsHost",
                    "repositoryRelativePath": "/$defs/repositoryRelativePath",
                    "taggedDigest": "/$defs/taggedDigest",
                    "verificationOutcome": "/$defs/verificationOutcome",
                    "windowsDriveAbsoluteHostPath": (
                        "/$defs/windowsDriveAbsoluteHostPath"
                    ),
                },
            ),
        )
        common_schema_id = get_resource("common.schema.json").schema_id
        for batch_label, batch_case_ids, profile_roots in batch_contracts:
            for case_id in batch_case_ids:
                case = CASES_BY_ID[case_id]
                binding = FIXTURE_CONTRACTS_BY_CASE[case_id]
                descriptor_reference = binding["descriptorRef"]
                if (
                    descriptor_reference["path"] != case.asset
                    or descriptor_reference["pointer"] != case.asset_pointer
                ):
                    problems.append(f"historical descriptor binding changed: {case_id}")
                    continue
                descriptor = _authenticated_reference_payload(descriptor_reference)
                if descriptor != case_payload(case):
                    problems.append(f"descriptor reference payload mismatch: {case_id}")
                    continue
                if (
                    case.inventory_disposition != "DIRECT_SCHEMA"
                    or case.owner != "schema"
                    or case.layer != "schema"
                    or case.polarity != "negative"
                    or case.expected_disposition != "REJECT"
                    or case.expected_diagnostic_identities is not None
                    or binding["validatorEntryPoint"] != SCHEMA_VALIDATOR_ENTRY_POINT
                    or binding["diagnosticIdentityVersion"] != SCHEMA_DIAGNOSTIC_V1
                    or binding["expectedValidationStatus"] != "INVALID"
                ):
                    problems.append(
                        f"Schema Oracle {batch_label} dispatch mismatch: {case_id}"
                    )
                    continue

                operand = fixture_operand(case)
                if operand is None or operand.get("operandKind") != "schema":
                    problems.append(
                        f"Schema Oracle {batch_label} operand is absent: {case_id}"
                    )
                    continue
                schema_operand = operand["schemaOperand"]
                profile = (
                    descriptor.get("profile") if isinstance(descriptor, dict) else None
                )
                if (
                    operand.get("caseId") != case_id
                    or schema_operand.get("instance") != descriptor.get("value")
                    or schema_operand.get("schemaResourceId") != common_schema_id
                    or schema_operand.get("schemaPointer") != profile_roots.get(profile)
                ):
                    problems.append(
                        f"Schema Oracle {batch_label} projection mismatch: {case_id}"
                    )
                    continue

                expected = expected_typed_diagnostics(case)
                if not expected or any(
                    not isinstance(item, SchemaDiagnostic) for item in expected
                ):
                    problems.append(
                        f"Schema Oracle {batch_label} lacks a typed Schema oracle: "
                        f"{case_id}"
                    )
    except Exception as error:
        problems.append(
            "fixture-contract validation failure: "
            f"{type(error).__name__}: {error}"
        )
    return tuple(sorted(set(problems)))


def audit_current_corpus() -> ManifestAudit:
    problems = list(manifest_structure_problems(MANIFEST))
    problems.extend(fixture_contract_structure_problems())
    assets = MANIFEST["assets"]
    cases = MANIFEST["cases"]
    obligations = MANIFEST["coverageObligations"]
    asset_paths = [item["path"] for item in assets]
    declared_assets = set(asset_paths)
    declared_cases_by_asset: dict[str, list[dict[str, Any]]] = {
        path: [] for path in asset_paths
    }
    declared_obligations_by_asset: dict[str, list[dict[str, Any]]] = {
        path: [] for path in asset_paths
    }

    if MANIFEST_SHA256 != CANDIDATE_MANIFEST_SHA256:
        problems.append("fixture manifest SHA-256 differs from the candidate v3 identity")
    if MANIFEST_GIT_BLOB != CANDIDATE_MANIFEST_GIT_BLOB:
        problems.append("fixture manifest Git blob differs from the candidate v3 identity")
    if len(assets) != EXPECTED_ASSET_COUNT:
        problems.append(f"fixture asset count is {len(assets)}, expected {EXPECTED_ASSET_COUNT}")
    if len(cases) != EXPECTED_CASE_COUNT:
        problems.append(f"logical case count is {len(cases)}, expected {EXPECTED_CASE_COUNT}")
    if len(obligations) != EXPECTED_COVERAGE_OBLIGATION_COUNT:
        problems.append(
            "coverage obligation count is "
            f"{len(obligations)}, expected {EXPECTED_COVERAGE_OBLIGATION_COUNT}"
        )

    checkout_eol_adjusted: list[str] = []
    for item in assets:
        path = item["path"]
        try:
            content = _asset_bytes(path)
            if asset_uses_checkout_eol_adjustment(path):
                checkout_eol_adjusted.append(path)
        except (OSError, FixtureContractError) as error:
            problems.append(f"asset path failure for {path}: {type(error).__name__}")
            continue
        if len(content) != item.get("byteLength"):
            problems.append(f"asset byteLength mismatch: {path}")
        if _sha256(content) != item.get("sha256"):
            problems.append(f"asset SHA-256 mismatch: {path}")

    utf8_json_paths = {
        item["path"] for item in assets if item.get("encoding") == "utf-8-json"
    }
    if len(utf8_json_paths) != EXPECTED_UTF8_JSON_ASSET_COUNT:
        problems.append("UTF-8 JSON asset count mismatch")
    if not V2_CORRECTION_ASSET_PATHS <= utf8_json_paths:
        problems.append("v2 correction paths are not all UTF-8 JSON assets")
    if not V3_PILOT_ASSET_PATHS <= utf8_json_paths:
        problems.append("v3 pilot paths are not all UTF-8 JSON assets")
    if not V3_BATCH01_ASSET_PATHS <= utf8_json_paths:
        problems.append("Schema Oracle Batch 01 paths are not all UTF-8 JSON assets")
    if not V3_BATCH02_ASSET_PATHS <= utf8_json_paths:
        problems.append("Schema Oracle Batch 02 paths are not all UTF-8 JSON assets")
    if not V3_BATCH03_ASSET_PATHS <= utf8_json_paths:
        problems.append("Schema Oracle Batch 03 paths are not all UTF-8 JSON assets")
    if not V3_BATCH04_ASSET_PATHS <= utf8_json_paths:
        problems.append("Schema Oracle Batch 04 paths are not all UTF-8 JSON assets")
    if not V3_BATCH05_ASSET_PATHS <= utf8_json_paths:
        problems.append("Schema Oracle Batch 05 paths are not all UTF-8 JSON assets")
    if (
        len(
            utf8_json_paths
            - V2_CORRECTION_ASSET_PATHS
            - V3_PILOT_ASSET_PATHS
            - V3_BATCH01_ASSET_PATHS
            - V3_BATCH02_ASSET_PATHS
            - V3_BATCH03_ASSET_PATHS
            - V3_BATCH04_ASSET_PATHS
            - V3_BATCH05_ASSET_PATHS
        )
        != EXPECTED_UNCHANGED_EOL_SENSITIVE_ASSET_COUNT
    ):
        problems.append("unchanged LF/CRLF-sensitive asset count mismatch")
    if not set(checkout_eol_adjusted) <= utf8_json_paths:
        problems.append("a raw-byte asset received checkout EOL adjustment")

    for item in cases:
        path = item["asset"]
        if path is None:
            if item["expectedDisposition"] != "DEFERRED" or "assetPointer" in item:
                problems.append(f"case {item['id']} has an invalid null asset binding")
            continue
        if path not in declared_cases_by_asset:
            problems.append(f"case {item['id']} references an unmanifested asset")
            continue
        declared_cases_by_asset[path].append(item)
        pointer = item.get("assetPointer")
        if pointer is not None:
            expected_pointer = "/cases/" + item["id"].replace("~", "~0").replace("/", "~1")
            if pointer != expected_pointer:
                problems.append(f"case {item['id']} has a non-canonical asset pointer")
            try:
                payload = resolve_json_pointer(_asset_document(path), pointer)
                if not isinstance(payload, dict):
                    problems.append(f"case {item['id']} does not resolve to an object payload")
            except (OSError, ValueError, FixtureContractError) as error:
                problems.append(f"case pointer failure for {item['id']}: {type(error).__name__}")

    for item in obligations:
        path = item["asset"]
        if path not in declared_obligations_by_asset:
            problems.append(
                f"coverage obligation {item['originalCaseId']} references an unmanifested asset"
            )
            continue
        declared_obligations_by_asset[path].append(item)
        try:
            payload = resolve_json_pointer(_asset_document(path), item["assetPointer"])
            if not isinstance(payload, dict):
                problems.append(
                    f"coverage obligation {item['originalCaseId']} does not resolve to an object"
                )
            elif payload.get("originalCaseId") != item["originalCaseId"]:
                problems.append(
                    f"coverage obligation pointer identity mismatch: {item['originalCaseId']}"
                )
        except (OSError, ValueError, FixtureContractError) as error:
            problems.append(
                "coverage obligation pointer failure for "
                f"{item['originalCaseId']}: {type(error).__name__}"
            )

    for asset in assets:
        path = asset["path"]
        if "caseCount" not in asset and "obligationCount" not in asset:
            continue
        try:
            document = _asset_document(path)
        except (OSError, ValueError, FixtureContractError) as error:
            problems.append(f"fixture pack is malformed: {path}: {type(error).__name__}")
            continue
        if "caseCount" in asset:
            pack_cases = document.get("cases") if isinstance(document, dict) else None
            if not isinstance(pack_cases, dict):
                problems.append(f"fixture case pack lacks a cases object: {path}")
                continue
            referenced = [item["id"] for item in declared_cases_by_asset[path]]
            if asset["caseCount"] != len(pack_cases):
                problems.append(f"asset caseCount mismatch: {path}")
            if set(pack_cases) != set(referenced) or len(referenced) != len(set(referenced)):
                problems.append(f"manifest-to-pack case ownership mismatch: {path}")
            if list(pack_cases) != sorted(pack_cases):
                problems.append(f"fixture pack cases are not strictly sorted: {path}")
        else:
            pack_obligations = (
                document.get("obligations") if isinstance(document, dict) else None
            )
            if not isinstance(pack_obligations, list):
                problems.append(f"coverage obligation pack lacks an obligations array: {path}")
                continue
            pack_ids = [
                item.get("originalCaseId")
                for item in pack_obligations
                if isinstance(item, dict)
            ]
            referenced = [
                item["originalCaseId"] for item in declared_obligations_by_asset[path]
            ]
            if asset["obligationCount"] != len(pack_obligations):
                problems.append(f"asset obligationCount mismatch: {path}")
            if pack_ids != sorted(pack_ids):
                problems.append(f"fixture pack obligations are not strictly sorted: {path}")
            if set(pack_ids) != set(referenced) or len(referenced) != len(set(referenced)):
                problems.append(f"manifest-to-pack obligation ownership mismatch: {path}")

    actual_files = {
        path.relative_to(REPOSITORY_ROOT).as_posix()
        for path in FIXTURE_ROOT.rglob("*")
        if path.is_file() or path.is_symlink()
    }
    missing, extra = compare_asset_inventory(declared_assets | CONTROL_PATHS, actual_files)
    if missing:
        problems.append("missing fixture/control paths: " + ",".join(missing))
    if extra:
        problems.append("unmanifested fixture/control paths: " + ",".join(extra))

    deferred_rows = {item["id"] for item in cases if item["inventoryDisposition"] == "DEFERRED"}
    reconciliation = MANIFEST["coverageReconciliation"]
    declared_deferred = reconciliation["deferredCases"]
    if declared_deferred != sorted(set(declared_deferred)):
        problems.append("declared deferred case identities are not canonical")
    if deferred_rows != set(declared_deferred):
        problems.append("deferred case list does not match DEFERRED rows")
    if reconciliation["deferredCaseCount"] != len(deferred_rows):
        problems.append("deferred case count does not match DEFERRED rows")
    if len(deferred_rows) != EXPECTED_DEFERRED_COUNT:
        problems.append("deferred case count differs from the approved S5 aggregate")
    for name, cardinality in reconciliation["cardinalities"].items():
        if cardinality.get("expected") != cardinality.get("observed"):
            problems.append(f"coverage cardinality mismatch: {name}")

    disposition_counts = {
        value: sum(item["inventoryDisposition"] == value for item in cases)
        for value in _INVENTORY_DISPOSITIONS
    }
    if disposition_counts != {
        "DIRECT_SCHEMA": EXPECTED_DIRECT_SCHEMA_COUNT,
        "DIRECT_STATIC": EXPECTED_DIRECT_STATIC_COUNT,
        "DEFERRED": EXPECTED_DEFERRED_COUNT,
    }:
        problems.append("manifest case inventory-disposition aggregates mismatch")
    expected_disposition_counts = {
        value: sum(item["expectedDisposition"] == value for item in cases)
        for value in _DISPOSITIONS
    }
    if expected_disposition_counts != {
        "ACCEPT": EXPECTED_ACCEPT_COUNT,
        "REJECT": EXPECTED_REJECT_COUNT,
        "DEFERRED": EXPECTED_DEFERRED_COUNT,
    }:
        problems.append("manifest expected-disposition aggregates mismatch")

    obligation_counts = {
        value: sum(item["inventoryDisposition"] == value for item in obligations)
        for value in _COVERAGE_INVENTORY_DISPOSITIONS
    }
    trace_only_count = obligation_counts["TRACE_ONLY"]
    open_gap_count = obligation_counts["COVERAGE_LEDGER_OPEN"]
    future_model_count = obligation_counts["FUTURE_MODEL_OBLIGATION"]
    if trace_only_count != EXPECTED_TRACE_ONLY_COUNT:
        problems.append("TRACE_ONLY obligation count mismatch")
    if open_gap_count != EXPECTED_OPEN_PHASE1_GAP_COUNT:
        problems.append("open Phase-1 coverage-gap count mismatch")
    if future_model_count != EXPECTED_FUTURE_MODEL_OBLIGATION_COUNT:
        problems.append("future-model obligation count mismatch")
    corrected_inventory_count = len(cases) + trace_only_count
    if corrected_inventory_count != EXPECTED_CORRECTED_INVENTORY_COUNT:
        problems.append("corrected inventory count mismatch")

    for obligation in COVERAGE_OBLIGATIONS:
        try:
            payload = coverage_obligation_payload(obligation)
        except (OSError, ValueError, FixtureContractError) as error:
            problems.append(
                f"coverage obligation payload failure for {obligation.original_case_id}: "
                f"{type(error).__name__}"
            )
            continue
        existing = payload.get("existingConcreteExecutableCoverage")
        missing_obligations = payload.get("missingCoverageObligations")
        if obligation.inventory_disposition == "COVERAGE_LEDGER_OPEN":
            if existing != [] or not isinstance(missing_obligations, list) or not missing_obligations:
                problems.append(
                    f"open coverage gap is not explicitly unsatisfied: {obligation.original_case_id}"
                )
        elif obligation.inventory_disposition == "TRACE_ONLY":
            if payload.get("authorizesExecution") is not False or missing_obligations != []:
                problems.append(
                    f"TRACE_ONLY obligation claims execution or missing coverage: "
                    f"{obligation.original_case_id}"
                )
        elif not isinstance(missing_obligations, list) or not missing_obligations:
            problems.append(
                f"future-model obligation lacks an explicit missing obligation: "
                f"{obligation.original_case_id}"
            )

    if reconciliation.get("correctedInventory") != {
        "DEFERRED": EXPECTED_DEFERRED_COUNT,
        "DIRECT_SCHEMA": EXPECTED_DIRECT_SCHEMA_COUNT,
        "DIRECT_STATIC": EXPECTED_DIRECT_STATIC_COUNT,
        "DIRECT_TOTAL": EXPECTED_EXECUTABLE_COUNT,
        "TOTAL": EXPECTED_CORRECTED_INVENTORY_COUNT,
        "TRACE_ONLY": EXPECTED_TRACE_ONLY_COUNT,
    }:
        problems.append("coverage reconciliation inventory mismatch")
    if reconciliation.get("traceOnlyObservationIds") != list(trace_only_obligation_ids()):
        problems.append("TRACE_ONLY reconciliation identities mismatch")
    if reconciliation.get("traceOnlyObservationCount") != trace_only_count:
        problems.append("TRACE_ONLY reconciliation count mismatch")
    if reconciliation.get("openPhase1CoverageGapCount") != open_gap_count:
        problems.append("open-gap reconciliation count mismatch")
    if reconciliation.get("futureModelObligationCount") != future_model_count:
        problems.append("future-model reconciliation count mismatch")
    if reconciliation.get("excludedCoverageObligationCount") != open_gap_count + future_model_count:
        problems.append("excluded-obligation reconciliation count mismatch")
    if reconciliation.get("coverageObligationCount") != open_gap_count + future_model_count:
        problems.append("coverage-obligation reconciliation count mismatch")

    catalog = MANIFEST["resourceCatalog"]
    expected_resources = [
        record.resource_name.removesuffix(".schema.json") for record in CATALOG
    ]
    if catalog["schemaResources"] != expected_resources:
        problems.append("manifest Schema resource catalog mismatch")
    expected_kinds = [record.kind for record in CATALOG if record.dispatchable_kind]
    if catalog["dispatchableKinds"] != expected_kinds:
        problems.append("manifest dispatchable kind catalog mismatch")

    executable_count = sum(
        item["inventoryDisposition"] in {"DIRECT_SCHEMA", "DIRECT_STATIC"}
        for item in cases
    )
    if executable_count != EXPECTED_EXECUTABLE_COUNT:
        problems.append("direct case count differs from the manifest-derived S6 inventory")
    return ManifestAudit(
        asset_count=len(assets),
        control_count=len(CONTROL_PATHS),
        case_count=len(cases),
        deferred_count=len(deferred_rows),
        executable_count=executable_count,
        trace_only_count=trace_only_count,
        corrected_inventory_count=corrected_inventory_count,
        open_phase1_gap_count=open_gap_count,
        future_model_obligation_count=future_model_count,
        checkout_eol_adjusted_count=len(checkout_eol_adjusted),
        missing_oracle_count=len(missing_negative_oracle_case_ids()),
        direct_execution_gap_count=len(direct_execution_gap_case_ids()),
        problems=tuple(sorted(set(problems))),
    )


def execution_mode(case: FixtureCase | str) -> str:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    if case.inventory_disposition == "DEFERRED":
        return DEFERRED_PRESERVED
    if case.inventory_disposition == "DIRECT_SCHEMA":
        return SCHEMA_DIRECT
    if case.inventory_disposition == "DIRECT_STATIC":
        return STATIC_DIRECT
    raise FixtureContractError(
        f"case {case.id} has unsupported inventory disposition: "
        f"{case.inventory_disposition!r}"
    )


def _resource_name(resource: str) -> str:
    if resource in KINDS:
        return KINDS[resource]
    if resource.startswith("TaskContract"):
        return "task-contract"
    if resource.startswith("ExecutionReceipt"):
        return "execution-receipt"
    if resource.startswith("WorktreeRole"):
        return "worktree-role"
    if resource in {
        "common",
        "resource",
        "project",
        "domain",
        "worktree-role",
        "routing-policy",
        "host-overlay",
        "task-contract",
        "execution-receipt",
        "governance-bundle",
        "receipt-delivery-result",
    }:
        return resource
    raise FixtureContractError(f"case resource has no Schema root: {resource!r}")


_COMMON_ALIASES = {
    "acceptedRemotes": "acceptedRemotes",
    "remoteExpectation": "remoteExpectation",
    "structuredRemote": "structuredRemote",
}


def schema_reference(case: FixtureCase, payload: Mapping[str, Any]) -> str:
    if "fragment" in payload:
        fragment = payload["fragment"]
        if not isinstance(fragment, str) or not fragment.startswith("#/"):
            raise FixtureContractError(f"case {case.id} has an invalid Schema fragment")
        return get_resource(_resource_name(case.resource) + ".schema.json").schema_id + fragment
    if "#" in case.resource:
        base, fragment = case.resource.split("#", 1)
        return get_resource(_resource_name(base) + ".schema.json").schema_id + "#" + fragment
    if case.resource in _COMMON_ALIASES:
        common = get_resource("common.schema.json").schema_id
        return common + "#/$defs/" + _COMMON_ALIASES[case.resource]
    return get_resource(_resource_name(case.resource) + ".schema.json").schema_id


def schema_instance(payload: Mapping[str, Any]) -> Any:
    for key in ("instance", "value", "subject"):
        if key in payload:
            return payload[key]
    raise FixtureContractError("direct Schema case has no instance, value, or subject")


def _receipt_origin_schema_instance(mutation: str) -> dict[str, Any]:
    issued = resource("ExecutionReceipt")
    denial = denial_resource()
    issued_origin = issued["spec"]["origin"]
    denial_origin = denial["spec"]["origin"]
    if mutation == "issued-missing-contract-id":
        del issued_origin["contractId"]
        return issued
    if mutation == "issued-missing-contract-digest":
        del issued_origin["contractDigest"]
        return issued
    if mutation == "issued-containing-denial-checkpoint":
        issued_origin["denialCheckpoint"] = denial_origin["denialCheckpoint"]
        return issued
    if mutation == "issued-containing-pre-contract-evidence":
        issued_origin["preContractEvidence"] = deepcopy(
            denial_origin["preContractEvidence"]
        )
        return issued
    if mutation == "issued-containing-denial-lease-acquisition":
        issued_origin["leaseAcquisition"] = deepcopy(denial_origin["leaseAcquisition"])
        return issued
    if mutation == "denial-containing-contract-id":
        denial_origin["contractId"] = issued_origin["contractId"]
        return denial
    if mutation == "denial-containing-contract-digest":
        denial_origin["contractDigest"] = issued_origin["contractDigest"]
        return denial
    if mutation == "denial-missing-checkpoint":
        del denial_origin["denialCheckpoint"]
        return denial
    if mutation == "evidence-missing-sanitized-summary":
        del denial_origin["preContractEvidence"]["sanitizedSummary"]
        return denial
    if mutation == "evidence-missing-controller-check-id":
        del denial_origin["preContractEvidence"]["controllerCheckId"]
        return denial
    if mutation == "denial-lease-branch-extra-member":
        denial_origin["leaseAcquisition"]["leaseId"] = (
            "00000000-0000-4000-8000-000000000004"
        )
        return denial
    if mutation == "receipt-secret-like-field":
        issued["spec"]["credential"] = "conspicuously-synthetic-secret-like-value"
        return issued
    if mutation == "receipt-authority-grant-field":
        issued["spec"]["authorityGrant"] = {"allowWrite": True}
        return issued
    raise FixtureContractError(f"unsupported receipt-origin mutation: {mutation!r}")


def schema_case_input(
    case: FixtureCase, payload: Mapping[str, Any]
) -> tuple[Any, str]:
    """Materialize one manifest-declared direct Schema operand and exact root."""
    if set(payload) == {"prefix"} and case.resource == "WorktreeRole.spec.branchPolicy":
        common_id = get_resource("common.schema.json").schema_id
        return payload["prefix"], common_id + "#/$defs/branchPrefix"
    if set(payload) == {"branchPolicy"} and case.resource == "WorktreeRole.spec.branchPolicy":
        common_id = get_resource("common.schema.json").schema_id
        return payload["branchPolicy"], common_id + "#/$defs/branchPolicy"
    if set(payload) == {"baseResource", "isolatedMutation"} and payload.get(
        "baseResource"
    ) == "ExecutionReceipt":
        return (
            _receipt_origin_schema_instance(payload["isolatedMutation"]),
            get_resource("execution-receipt.schema.json").schema_id,
        )
    if set(payload) == {"formerTransitionType"} and case.resource.startswith(
        "TaskContract.permittedTransitions"
    ):
        transition = {
            "type": payload["formerTransitionType"],
            "path": "synthetic/file.txt",
            "from": "absent",
            "to": "present",
        }
        task_contract_id = get_resource("task-contract.schema.json").schema_id
        return transition, task_contract_id + "#/$defs/permittedTransition"
    return schema_instance(payload), schema_reference(case, payload)


@lru_cache(maxsize=None)
def _schema_locations() -> dict[int, tuple[tuple[str, str], ...]]:
    locations: dict[int, set[tuple[str, str]]] = {}

    def walk(value: Any, resource_id: str, parts: tuple[Any, ...] = ()) -> None:
        if isinstance(value, dict):
            locations.setdefault(id(value), set()).add(
                (resource_id, json_pointer(parts))
            )
            for key, child in value.items():
                walk(child, resource_id, (*parts, key))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, resource_id, (*parts, index))

    registry = source_registry()
    for record in CATALOG:
        walk(registry.contents(record.schema_id), record.schema_id)
    return {
        identity: tuple(sorted(candidates))
        for identity, candidates in locations.items()
    }


@lru_cache(maxsize=None)
def _validator(schema_ref: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$ref": schema_ref},
        registry=source_registry(),
        format_checker=build_format_checker(),
    )


def collect_schema_diagnostics(
    instance: Any,
    schema_ref: str,
    *,
    validator: Any | None = None,
) -> tuple[SchemaDiagnostic, ...]:
    """Return structured, prose-independent, deterministically ordered errors."""
    selected = validator if validator is not None else _validator(schema_ref)
    try:
        errors = tuple(selected.iter_errors(instance))
    except Exception as error:
        raise ValidatorCapabilityError(
            f"validator failed instead of returning a result: {type(error).__name__}"
        ) from error

    locations = _schema_locations()
    diagnostics: set[SchemaDiagnostic] = set()
    for error in errors:
        candidates = locations.get(id(error.schema), ())
        if len(candidates) != 1:
            condition = "unknown" if not candidates else "ambiguous"
            raise DiagnosticAttributionError(
                f"validator returned an {condition} Schema object location"
            )
        resource_id, schema_object_pointer = candidates[0]
        keyword = error.validator
        if (
            not isinstance(keyword, str)
            or not keyword
            or not isinstance(error.schema, Mapping)
            or keyword not in error.schema
        ):
            raise DiagnosticAttributionError(
                "validator returned an unattributable keyword location"
            )
        keyword_pointer = json_pointer((keyword,))
        schema_pointer = schema_object_pointer + keyword_pointer
        diagnostics.add(
            SchemaDiagnostic(
                schema_resource_id=resource_id,
                instance_pointer=json_pointer(error.absolute_path),
                schema_pointer=schema_pointer,
                keyword=keyword,
            )
        )
    return tuple(
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


def run_schema_case(case: FixtureCase | str) -> tuple[SchemaDiagnostic, ...]:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    binding = fixture_contract_binding(case)
    if binding is not None:
        if binding["validatorEntryPoint"] != SCHEMA_VALIDATOR_ENTRY_POINT:
            raise FixtureContractError(
                f"fixture-contract Schema validator entry point mismatch: {case.id}"
            )
        operand = fixture_operand(case)
        if operand is None or operand.get("operandKind") != "schema":
            raise FixtureContractError(
                f"fixture-contract Schema operand is missing: {case.id}"
            )
        schema_operand = operand["schemaOperand"]
        schema_ref = (
            schema_operand["schemaResourceId"] + "#" + schema_operand["schemaPointer"]
        )
        return collect_schema_diagnostics(schema_operand["instance"], schema_ref)
    payload = case_payload(case)
    if not isinstance(payload, dict):
        raise FixtureContractError(f"case {case.id} payload is not an object")
    instance, schema_ref = schema_case_input(case, payload)
    return collect_schema_diagnostics(instance, schema_ref)


@contextmanager
def _synthetic_proof_environment():
    """Install the existing private S4 test double for one bounded call."""
    ports = SyntheticPorts()

    def proof_method(operation: str):
        def method(_self: Any, *args: Any) -> Any:
            return ports.issue(operation, args)

        return method

    operations = (
        "require_input_provenance",
        "require_canonical_comparison",
        "require_digest",
        "require_complete_host_snapshot",
        "require_baseline_materialization",
        "require_completed_static_validation",
    )
    with ExitStack() as stack:
        stack.enter_context(patch.object(static_core, "build_registry", source_registry))
        for operation in operations:
            stack.enter_context(
                patch.object(static_core._ProofContext, operation, proof_method(operation))
            )
        stack.enter_context(
            patch.object(
                static_core._ProofContext,
                "_validate_handle",
                lambda _self, handle, operation, args: ports.validate(
                    handle, operation, args
                ),
            )
        )
        yield ports


@contextmanager
def _explicit_pilot_proof_environment(operand: Mapping[str, Any]):
    """Consume only proof responses explicitly frozen in one pilot operand."""
    ports = SyntheticPorts()
    subject = operand["subject"]
    validation_context = operand["validationContext"]
    bundle = validation_context["governanceBundle"]
    overlay = validation_context["hostOverlay"]
    inventory_context = validation_context["inventoryContext"]
    responses = validation_context["proofResponses"]

    subjects = {
        "#/subject": subject,
        "#/validationContext/governanceBundle": bundle,
        "#/validationContext/hostOverlay": overlay,
    }
    declared_provenance = {
        (
            id(subjects[item["subjectRef"]]),
            item["schemaResourceId"],
            item["schemaSetRevision"],
        )
        for item in responses["inputProvenance"]
    }

    baseline = responses["baselineMaterialization"]
    values = {
        key: tuple(value)
        if key in {"index", "tracked", "untracked", "ignored", "submodules"}
        else value
        for key, value in baseline["values"].items()
    }
    baseline_view = _MaterializedBaselineView(
        subject,
        MappingProxyType(values),
        tuple(baseline["headEntries"]),
        MappingProxyType(dict(baseline["leafKinds"])),
        MappingProxyType({}),
    )

    snapshot = responses["completeHostSnapshot"]

    def input_provenance(candidate: Any, root_id: str, revision: str) -> Any:
        return True if (id(candidate), root_id, revision) in declared_provenance else None

    def complete_host_snapshot(host_id: str, marker: Any) -> Any:
        if (
            host_id != snapshot["hostId"]
            or marker is not inventory_context
            or snapshot["inventoryContextRef"]
            != "#/validationContext/inventoryContext"
        ):
            return None
        members = []
        for member in snapshot["members"]:
            if member != {
                "hostOverlayRef": "#/validationContext/hostOverlay",
                "governanceBundleRef": "#/validationContext/governanceBundle",
            }:
                return None
            members.append((overlay, bundle))
        return tuple(members), tuple(snapshot["trustedRoots"])

    def baseline_materialization(candidate: Any, dimensions: Any) -> Any:
        return (
            baseline_view
            if candidate is subject and tuple(dimensions) == tuple(baseline["dimensions"])
            else None
        )

    def undeclared_response(*_args: Any) -> None:
        return None

    ports.overrides.update(
        {
            "require_input_provenance": input_provenance,
            "require_canonical_comparison": undeclared_response,
            "require_digest": undeclared_response,
            "require_complete_host_snapshot": complete_host_snapshot,
            "require_baseline_materialization": baseline_materialization,
            "require_completed_static_validation": undeclared_response,
        }
    )

    operations = tuple(ports.overrides)
    with ExitStack() as stack:
        stack.enter_context(patch.object(static_core, "build_registry", source_registry))
        for operation in operations:
            stack.enter_context(
                patch.object(
                    static_core._ProofContext,
                    operation,
                    lambda _self, *args, _operation=operation: ports.issue(
                        _operation, args
                    ),
                )
            )
        stack.enter_context(
            patch.object(
                static_core._ProofContext,
                "_validate_handle",
                lambda _self, handle, operation, args: ports.validate(
                    handle, operation, args
                ),
            )
        )
        yield ports, baseline_view


def _invoke_static(payload: Mapping[str, Any], proof_context: Any, ports: Any = None):
    validation = payload.get("validation")
    subject = payload["subject"]
    if validation == "governance-bundle":
        return validate_governance_bundle(subject, proof_context=proof_context)
    if validation == "execution-receipt":
        context = payload.get("context", {})
        contract = context.get("taskContract")
        if ports is not None and contract is not None:
            ports.complete(contract, "task-contract")
        return validate_execution_receipt_static(
            subject,
            contract_context=contract,
            sources=tuple(context.get("sources", ())),
            proof_context=proof_context,
        )
    if validation in ("task-contract", "task-contract-truth-table"):
        # Every materialized S5 case in these groups rejects before the
        # unavailable bundle/overlay operands can be consumed.
        return validate_task_contract_static(
            subject,
            bundle=None,
            host_overlay=None,
            proof_context=proof_context,
        )
    raise FixtureContractError(f"unsupported direct S4 validation: {validation!r}")


def run_static_case(case: FixtureCase | str):
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    binding = fixture_contract_binding(case)
    if binding is not None:
        if binding["validatorEntryPoint"] != STATIC_VALIDATOR_ENTRY_POINT:
            raise FixtureContractError(
                f"fixture-contract static validator entry point mismatch: {case.id}"
            )
        operand = fixture_operand(case)
        if operand is None or operand.get("operandKind") != "static":
            raise FixtureContractError(
                f"fixture-contract static operand is missing: {case.id}"
            )
        context = operand["validationContext"]
        with _explicit_pilot_proof_environment(operand) as (
            ports,
            baseline_context,
        ):
            return validate_task_contract_static(
                operand["subject"],
                bundle=context["governanceBundle"],
                host_overlay=context["hostOverlay"],
                inventory_context=context["inventoryContext"],
                proof_context=ports.context,
                baseline_context=baseline_context,
            )
    payload = case_payload(case)
    if not isinstance(payload, dict) or "subject" not in payload:
        raise FixtureContractError(f"case {case.id} is not a materialized static case")
    if payload.get("validation") == "delivery-shape":
        raise FixtureContractError("delivery-shape is a Schema-only materialized case")
    with _synthetic_proof_environment() as ports:
        return _invoke_static(payload, ports.context, ports)


def run_static_case_without_proofs(case: FixtureCase | str):
    """Exercise the same public S4 entry point without granting synthetic proof."""
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    payload = case_payload(case)
    if not isinstance(payload, dict) or "subject" not in payload:
        raise FixtureContractError(f"case {case.id} is not a materialized static case")
    with patch.object(static_core, "build_registry", source_registry):
        return _invoke_static(payload, None)


def _legacy_oracle_status(
    case: FixtureCase, actual_diagnostic_identities: tuple[str, ...]
) -> str:
    if case.expected_disposition != "REJECT":
        return "NOT_APPLICABLE"
    expected = case.expected_diagnostic_identities
    if expected is None:
        return "MISSING_EXPECTED_SET"
    if frozenset(actual_diagnostic_identities) == frozenset(expected):
        return "EXACT_MATCH"
    return "EXACT_SET_MISMATCH"


def _static_diagnostic_identity(diagnostic: Any) -> StaticDiagnosticIdentity:
    return StaticDiagnosticIdentity(
        code=diagnostic.code,
        subject_id=diagnostic.subject_id,
        instance_pointer=diagnostic.instance_pointer,
        predicate_family=diagnostic.predicate_family,
        schema_id=diagnostic.schema_id,
        schema_pointer=diagnostic.schema_pointer,
        keyword=diagnostic.keyword,
    )


def _fixture_contract_oracle_comparison(
    case: FixtureCase,
    actual: tuple[DiagnosticIdentity, ...],
) -> DiagnosticSetComparison | None:
    binding = fixture_contract_binding(case)
    if binding is None or case.expected_disposition != "REJECT":
        return None
    expected = expected_typed_diagnostics(case)
    if expected is None:
        return DiagnosticSetComparison("MISSING_EXPECTED_SET", (), ())
    return compare_diagnostic_identity_sets(
        binding["diagnosticIdentityVersion"], expected, actual
    )


@lru_cache(maxsize=None)
def evaluate_case(case_id: str) -> CaseResult:
    case = CASES_BY_ID[case_id]
    mode = execution_mode(case)
    binding = fixture_contract_binding(case)
    diagnostic_version = (
        binding["diagnosticIdentityVersion"] if binding is not None else None
    )
    expected_typed = expected_typed_diagnostics(case)
    if mode == DEFERRED_PRESERVED:
        declared = set(MANIFEST["coverageReconciliation"]["deferredCases"])
        if case.id not in declared:
            raise FixtureContractError(f"deferred case {case.id} is not reconciled")
        return CaseResult(
            case_id=case.id,
            source_asset=case.asset,
            owner=case.owner,
            expected_disposition=case.expected_disposition,
            expected_stage=case.expected_stage,
            execution_mode=mode,
            actual_result="DEFERRED_PRESERVED",
            declared_diagnostic_identity=case.expected_failure_identity,
            actual_diagnostic_identities=(),
            expected_diagnostic_identities=case.expected_diagnostic_identities,
            execution_status="DEFERRED_PRESERVED",
        )

    payload = case_payload(case)
    if mode == STATIC_DIRECT and (
        not isinstance(payload, dict) or "subject" not in payload
    ) and fixture_operand(case) is None:
        return CaseResult(
            case_id=case.id,
            source_asset=case.asset,
            owner=case.owner,
            expected_disposition=case.expected_disposition,
            expected_stage=case.expected_stage,
            execution_mode=mode,
            actual_result="EXECUTION_BLOCKED",
            declared_diagnostic_identity=case.expected_failure_identity,
            actual_diagnostic_identities=(),
            expected_diagnostic_identities=case.expected_diagnostic_identities,
            execution_status="BLOCKED_MISSING_EXECUTABLE_OPERAND",
            oracle_status=(
                "MISSING_EXPECTED_SET"
                if case.expected_disposition == "REJECT"
                and case.expected_diagnostic_identities is None
                and expected_typed is None
                else "NOT_EVALUATED"
            ),
        )

    if mode == SCHEMA_DIRECT or (
        mode == STATIC_DIRECT
        and isinstance(payload, dict)
        and payload.get("validation") == "delivery-shape"
    ):
        diagnostics = run_schema_case(case)
        validation_status = "INVALID" if diagnostics else "PASS"
        if binding is not None and validation_status != binding[
            "expectedValidationStatus"
        ]:
            raise FixtureContractError(
                f"case {case.id} expected validation status "
                f"{binding['expectedValidationStatus']}, got {validation_status}"
            )
        actual = "REJECT" if diagnostics else "ACCEPT"
        if actual != case.expected_disposition:
            raise FixtureContractError(
                f"case {case.id} expected {case.expected_disposition}, got {actual}"
            )
        if actual == "REJECT" and not case.expected_failure_identity:
            raise FixtureContractError(f"negative Schema case {case.id} lacks declared identity")
        identities = tuple(item.identity for item in diagnostics)
        comparison = _fixture_contract_oracle_comparison(case, diagnostics)
        return CaseResult(
            case_id=case.id,
            source_asset=case.asset,
            owner=case.owner,
            expected_disposition=case.expected_disposition,
            expected_stage=case.expected_stage,
            execution_mode=mode,
            actual_result=actual,
            declared_diagnostic_identity=case.expected_failure_identity,
            actual_diagnostic_identities=identities,
            expected_diagnostic_identities=case.expected_diagnostic_identities,
            oracle_status=(
                comparison.status
                if comparison is not None
                else _legacy_oracle_status(case, identities)
            ),
            schema_diagnostics=diagnostics,
            diagnostic_identity_version=diagnostic_version,
            expected_typed_diagnostics=expected_typed,
            missing_diagnostics=comparison.missing if comparison is not None else (),
            unexpected_diagnostics=(
                comparison.unexpected if comparison is not None else ()
            ),
            validation_status=validation_status,
        )

    static_result = run_static_case(case)
    if binding is not None and static_result.status != binding[
        "expectedValidationStatus"
    ]:
        raise FixtureContractError(
            f"case {case.id} expected validation status "
            f"{binding['expectedValidationStatus']}, got {static_result.status}"
        )
    actual = {
        "PASS": "ACCEPT",
        "INVALID": "REJECT",
        "PROOF_REQUIRED": "PROOF_REQUIRED",
    }[static_result.status]
    if actual != case.expected_disposition:
        raise FixtureContractError(
            f"case {case.id} expected {case.expected_disposition}, got {actual}"
        )
    identities = tuple(sorted({diagnostic.code for diagnostic in static_result.diagnostics}))
    typed_diagnostics = tuple(
        _static_diagnostic_identity(diagnostic)
        for diagnostic in static_result.diagnostics
    )
    comparison = _fixture_contract_oracle_comparison(case, typed_diagnostics)
    return CaseResult(
        case_id=case.id,
        source_asset=case.asset,
        owner=case.owner,
        expected_disposition=case.expected_disposition,
        expected_stage=case.expected_stage,
        execution_mode=mode,
        actual_result=actual,
        declared_diagnostic_identity=case.expected_failure_identity,
        actual_diagnostic_identities=identities,
        expected_diagnostic_identities=case.expected_diagnostic_identities,
        oracle_status=(
            comparison.status
            if comparison is not None
            else _legacy_oracle_status(case, identities)
        ),
        static_diagnostics=typed_diagnostics,
        diagnostic_identity_version=diagnostic_version,
        expected_typed_diagnostics=expected_typed,
        missing_diagnostics=comparison.missing if comparison is not None else (),
        unexpected_diagnostics=(
            comparison.unexpected if comparison is not None else ()
        ),
        validation_status=static_result.status,
        static_status=static_result.status,
        proof_treatment=(
            "fixture-contract-v1-explicit-test-only-synthetic-proof"
            if binding is not None
            else "explicit-test-only-synthetic-proof"
        ),
    )


@lru_cache(maxsize=1)
def coverage_inventory() -> tuple[CaseResult, ...]:
    return tuple(evaluate_case(case.id) for case in CASES)


def source_schema_documents() -> dict[str, Any]:
    return {
        record.schema_id: strict_json_loads(
            (REPOSITORY_ROOT / record.repository_path).read_bytes()
        )
        for record in CATALOG
    }
