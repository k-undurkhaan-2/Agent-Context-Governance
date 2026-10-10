"""Deterministic S6 runner for the immutable v1alpha1 fixture manifest.

This module is test-only.  It does not expose a production validator, create a
trusted proof source, or turn fixture acceptance into operational authority.
The synthetic proof adapter below is used only to exercise the already-public
S4 validation surface with explicitly synthetic operands.
"""

from __future__ import annotations

from contextlib import ExitStack, contextmanager
from dataclasses import dataclass
from functools import lru_cache
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any, Mapping
from unittest.mock import patch

from jsonschema import Draft202012Validator

from contextctl_schema import build_format_checker
from contextctl_schema import _static_core as static_core
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
from tests.schema.test_resource_schemas import KINDS, source_registry


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPOSITORY_ROOT / "tests" / "schema" / "fixtures" / "v1alpha1"
MANIFEST_PATH = FIXTURE_ROOT / "manifest.json"
CONTROL_PATHS = frozenset(
    {
        "tests/schema/fixtures/v1alpha1/README.md",
        "tests/schema/fixtures/v1alpha1/manifest.json",
    }
)
APPROVED_MANIFEST_SHA256 = (
    "45187054fec6d52b74790438e07b14bf0c1da8835dee0bec8f0e6dc638d87b9c"
)
EXPECTED_ASSET_COUNT = 138
EXPECTED_CONTROL_COUNT = 2
EXPECTED_CASE_COUNT = 2230
EXPECTED_DEFERRED_COUNT = 115
EXPECTED_EXECUTABLE_COUNT = 2115

SCHEMA_DIRECT = "schema-direct"
SCHEMA_TRACE = "schema-trace"
STATIC_DIRECT = "static-direct"
STATIC_TRACE = "static-trace"
DEFERRED_PRESERVED = "deferred-preserved"

EXPECTED_EXECUTION_MODE_COUNTS = {
    SCHEMA_DIRECT: 1534,
    SCHEMA_TRACE: 33,
    STATIC_DIRECT: 57,
    STATIC_TRACE: 491,
    DEFERRED_PRESERVED: 115,
}

_EXPECTED_TOP_LEVEL_KEYS = frozenset(
    {
        "apiVersion",
        "assets",
        "authorityClaim",
        "cases",
        "corpusPurpose",
        "coverageReconciliation",
        "designBlob",
        "designPath",
        "evidenceClaim",
        "fixtureRoot",
        "implementationBaseline",
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
        "layer",
        "owner",
        "polarity",
        "resource",
    }
)
_DISPOSITIONS = frozenset({"ACCEPT", "REJECT", "DEFERRED"})
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


class FixtureContractError(AssertionError):
    """The immutable fixture contract is malformed or internally inconsistent."""


class DuplicateJsonKeyError(ValueError):
    """A JSON object contains a duplicate member name."""


class ValidatorCapabilityError(RuntimeError):
    """The selected validator could not return a valid diagnostic result."""


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
    schema_diagnostics: tuple[SchemaDiagnostic, ...] = ()
    static_status: str | None = None
    proof_treatment: str | None = None


@dataclass(frozen=True, slots=True)
class ManifestAudit:
    asset_count: int
    control_count: int
    case_count: int
    deferred_count: int
    executable_count: int
    problems: tuple[str, ...]


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


MANIFEST_BYTES = MANIFEST_PATH.read_bytes()
MANIFEST_SHA256 = hashlib.sha256(MANIFEST_BYTES).hexdigest()
MANIFEST: dict[str, Any] = strict_json_loads(MANIFEST_BYTES)


def _make_case(item: Mapping[str, Any]) -> FixtureCase:
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
    )


CASES = tuple(_make_case(item) for item in MANIFEST["cases"])
CASES_BY_ID = {case.id: case for case in CASES}


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
def _asset_bytes(relative_path: str) -> bytes:
    return checked_fixture_path(relative_path).read_bytes()


@lru_cache(maxsize=None)
def _asset_document(relative_path: str) -> Any:
    return strict_json_loads(_asset_bytes(relative_path))


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

    assets = manifest.get("assets")
    cases = manifest.get("cases")
    if not isinstance(assets, list):
        problems.append("manifest assets must be an array")
        assets = []
    if not isinstance(cases, list):
        problems.append("manifest cases must be an array")
        cases = []

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
        if item["owner"] not in _OWNERS:
            problems.append(f"case {item['id']} has an unknown owner")
        if item["expectedStage"] not in _STAGES:
            problems.append(f"case {item['id']} has an unknown expected stage")
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
    return tuple(sorted(set(problems)))


def audit_current_corpus() -> ManifestAudit:
    problems = list(manifest_structure_problems(MANIFEST))
    assets = MANIFEST["assets"]
    cases = MANIFEST["cases"]
    asset_paths = [item["path"] for item in assets]
    declared_assets = set(asset_paths)
    declared_cases_by_asset: dict[str, list[dict[str, Any]]] = {
        path: [] for path in asset_paths
    }

    if MANIFEST_SHA256 != APPROVED_MANIFEST_SHA256:
        problems.append("fixture manifest SHA-256 differs from the approved S5 identity")
    if len(assets) != EXPECTED_ASSET_COUNT:
        problems.append(f"fixture asset count is {len(assets)}, expected {EXPECTED_ASSET_COUNT}")
    if len(cases) != EXPECTED_CASE_COUNT:
        problems.append(f"logical case count is {len(cases)}, expected {EXPECTED_CASE_COUNT}")

    for item in assets:
        path = item["path"]
        try:
            content = _asset_bytes(path)
        except (OSError, FixtureContractError) as error:
            problems.append(f"asset path failure for {path}: {type(error).__name__}")
            continue
        if len(content) != item.get("byteLength"):
            problems.append(f"asset byteLength mismatch: {path}")
        if hashlib.sha256(content).hexdigest() != item.get("sha256"):
            problems.append(f"asset SHA-256 mismatch: {path}")

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

    for asset in assets:
        if "caseCount" not in asset:
            continue
        path = asset["path"]
        try:
            document = _asset_document(path)
        except (OSError, ValueError, FixtureContractError) as error:
            problems.append(f"fixture case pack is malformed: {path}: {type(error).__name__}")
            continue
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

    deferred_rows = {
        item["id"] for item in cases if item["expectedDisposition"] == "DEFERRED"
    }
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
        item["expectedDisposition"] != "DEFERRED" for item in cases
    )
    if executable_count != EXPECTED_EXECUTABLE_COUNT:
        problems.append("executable case count differs from the manifest-derived S6 inventory")
    return ManifestAudit(
        asset_count=len(assets),
        control_count=len(CONTROL_PATHS),
        case_count=len(cases),
        deferred_count=len(deferred_rows),
        executable_count=executable_count,
        problems=tuple(sorted(set(problems))),
    )


def execution_mode(case: FixtureCase | str) -> str:
    if isinstance(case, str):
        case = CASES_BY_ID[case]
    if case.expected_disposition == "DEFERRED":
        return DEFERRED_PRESERVED
    payload = case_payload(case)
    if case.owner == "schema":
        direct = (
            case.id
            != "schema.structured-remote.negative.58-duplicate-outer-remote-name"
            and isinstance(payload, dict)
            and ("instance" in payload or "value" in payload)
        )
        return SCHEMA_DIRECT if direct else SCHEMA_TRACE
    return STATIC_DIRECT if isinstance(payload, dict) and "subject" in payload else STATIC_TRACE


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


@lru_cache(maxsize=None)
def _schema_locations() -> dict[int, tuple[str, str]]:
    locations: dict[int, tuple[str, str]] = {}

    def walk(value: Any, resource_id: str, parts: tuple[Any, ...] = ()) -> None:
        if isinstance(value, dict):
            locations[id(value)] = (resource_id, json_pointer(parts))
            for key, child in value.items():
                walk(child, resource_id, (*parts, key))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, resource_id, (*parts, index))

    registry = source_registry()
    for record in CATALOG:
        walk(registry.contents(record.schema_id), record.schema_id)
    return locations


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
    fallback_resource = schema_ref.split("#", 1)[0]
    diagnostics: set[SchemaDiagnostic] = set()
    for error in errors:
        resource_id, schema_object_pointer = locations.get(
            id(error.schema), (fallback_resource, "")
        )
        keyword = str(error.validator or "unknown")
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
    payload = case_payload(case)
    if not isinstance(payload, dict):
        raise FixtureContractError(f"case {case.id} payload is not an object")
    return collect_schema_diagnostics(
        schema_instance(payload), schema_reference(case, payload)
    )


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


def _verify_trace_case(case: FixtureCase, payload: Any) -> None:
    if not isinstance(payload, dict) or not payload:
        raise FixtureContractError(f"trace case {case.id} lacks a declarative object")
    if case.expected_disposition == "REJECT":
        if not case.expected_failure_identity:
            raise FixtureContractError(f"trace reject {case.id} lacks diagnostic identity")
    elif case.expected_disposition == "ACCEPT":
        if case.expected_failure_identity is not None:
            raise FixtureContractError(f"trace accept {case.id} declares a diagnostic identity")
    else:
        raise FixtureContractError(f"trace case {case.id} has a deferred disposition")
    if case.polarity == "positive" and case.expected_disposition != "ACCEPT":
        raise FixtureContractError(f"positive trace case {case.id} is not ACCEPT")
    if case.polarity == "negative" and case.expected_disposition != "REJECT":
        raise FixtureContractError(f"negative trace case {case.id} is not REJECT")


@lru_cache(maxsize=None)
def evaluate_case(case_id: str) -> CaseResult:
    case = CASES_BY_ID[case_id]
    mode = execution_mode(case)
    if mode == DEFERRED_PRESERVED:
        declared = set(MANIFEST["coverageReconciliation"]["deferredCases"])
        if case.id not in declared:
            raise FixtureContractError(f"deferred case {case.id} is not reconciled")
        return CaseResult(
            case.id,
            case.asset,
            case.owner,
            case.expected_disposition,
            case.expected_stage,
            mode,
            "DEFERRED_PRESERVED",
            case.expected_failure_identity,
            (),
        )

    payload = case_payload(case)
    if mode in (SCHEMA_TRACE, STATIC_TRACE):
        _verify_trace_case(case, payload)
        return CaseResult(
            case.id,
            case.asset,
            case.owner,
            case.expected_disposition,
            case.expected_stage,
            mode,
            "TRACE_VERIFIED",
            case.expected_failure_identity,
            (),
        )

    if mode == SCHEMA_DIRECT or (
        mode == STATIC_DIRECT
        and isinstance(payload, dict)
        and payload.get("validation") == "delivery-shape"
    ):
        diagnostics = run_schema_case(case)
        actual = "REJECT" if diagnostics else "ACCEPT"
        if actual != case.expected_disposition:
            raise FixtureContractError(
                f"case {case.id} expected {case.expected_disposition}, got {actual}"
            )
        if actual == "REJECT" and not case.expected_failure_identity:
            raise FixtureContractError(f"negative Schema case {case.id} lacks declared identity")
        return CaseResult(
            case.id,
            case.asset,
            case.owner,
            case.expected_disposition,
            case.expected_stage,
            mode,
            actual,
            case.expected_failure_identity,
            tuple(item.identity for item in diagnostics),
            schema_diagnostics=diagnostics,
        )

    static_result = run_static_case(case)
    actual = {
        "PASS": "ACCEPT",
        "INVALID": "REJECT",
        "PROOF_REQUIRED": "PROOF_REQUIRED",
    }[static_result.status]
    if actual != case.expected_disposition:
        raise FixtureContractError(
            f"case {case.id} expected {case.expected_disposition}, got {actual}"
        )
    identities = tuple(diagnostic.code for diagnostic in static_result.diagnostics)
    if actual == "REJECT" and case.expected_failure_identity not in identities:
        raise FixtureContractError(
            f"case {case.id} did not produce {case.expected_failure_identity}"
        )
    return CaseResult(
        case.id,
        case.asset,
        case.owner,
        case.expected_disposition,
        case.expected_stage,
        mode,
        actual,
        case.expected_failure_identity,
        identities,
        static_status=static_result.status,
        proof_treatment="explicit-test-only-synthetic-proof",
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
