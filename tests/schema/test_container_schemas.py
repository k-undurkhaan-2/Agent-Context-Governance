"""S3 dispatch/container structure, using conspicuously synthetic inline data."""

from copy import deepcopy
import json

import pytest
from jsonschema import Draft202012Validator

from contextctl_schema.catalog import API_VERSION, CATALOG, get_resource
from contextctl_schema.registry import DIALECT
from tests.schema.test_resource_schemas import (
    DIGEST, KINDS, RECEIPT_ID, ROOT, TIME, resource, source_registry, validator,
)


def bundle():
    return {
        "apiVersion": API_VERSION, "project": resource("Project"),
        "domains": [resource("Domain")],
        "worktreeRoles": [resource("WorktreeRole")],
        "routingPolicy": resource("RoutingPolicy"),
    }


def delivery():
    return {
        "apiVersion": API_VERSION, "receiptId": RECEIPT_ID, "receiptDigest": DIGEST,
        "outcome": "not-attempted", "attemptedAt": TIME, "reasonCodes": [],
        "sanitizedSummary": "Conspicuously synthetic delivery evidence.",
    }


def unique_keys(pairs):
    # Parse Schema documents, not a production governance-instance decoder.
    result = {}
    for key, value in pairs:
        assert key not in result, f"Duplicate Schema key: {key}"
        result[key] = value
    return result


@pytest.mark.parametrize("record", CATALOG, ids=lambda r: r.resource_name)
def test_all_eleven_source_resources_parse_and_check_schema(record):
    raw = (ROOT / record.repository_path).read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf")
    document = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_keys)
    assert document["$id"] == record.schema_id
    assert document["$schema"] == DIALECT
    assert document.get("not") != {}
    Draft202012Validator.check_schema(document)
    assert source_registry().contents(record.schema_id) == document


def test_dispatch_is_exactly_seven_catalogued_kind_references():
    document = source_registry().contents(get_resource("resource.schema.json").schema_id)
    assert document["oneOf"] == [
        {"$ref": get_resource(name + ".schema.json").schema_id}
        for name in KINDS.values()
    ]
    assert len(document["oneOf"]) == 7
    assert sum(record.dispatchable_kind for record in CATALOG) == 7
    assert len(source_registry()) == 11


@pytest.mark.parametrize("kind", KINDS)
def test_dispatch_accepts_each_public_kind(kind):
    validator("resource").validate(resource(kind))


@pytest.mark.parametrize("kind", [
    "Unknown", "GovernanceBundle", "ReceiptDeliveryResult", "Resource", "Common", "project",
])
def test_no_unknown_or_eighth_kind_dispatch(kind):
    value = resource("Project")
    value["kind"] = kind
    assert not validator("resource").is_valid(value)


@pytest.mark.parametrize("value", [bundle(), delivery(), {}, None, []])
def test_non_kind_records_do_not_dispatch(value):
    assert not validator("resource").is_valid(value)


def test_portable_governance_container():
    validator("governance-bundle").validate(bundle())


@pytest.mark.parametrize("field", ["apiVersion", "project", "domains", "worktreeRoles", "routingPolicy"])
def test_bundle_requires_each_field(field):
    value = bundle()
    del value[field]
    assert not validator("governance-bundle").is_valid(value)


@pytest.mark.parametrize("field,value", [
    ("kind", "GovernanceBundle"),
    ("hostOverlay", resource("HostOverlay")),
    ("taskContract", resource("TaskContract")),
    ("executionReceipt", resource("ExecutionReceipt")),
    ("receiptDeliveryResult", delivery()),
    ("hostPath", "/srv/synthetic.invalid"),
    ("leases", []), ("locks", []), ("runtimeState", {}),
])
def test_bundle_excludes_host_and_runtime_fields(field, value):
    candidate = bundle()
    candidate[field] = value
    assert not validator("governance-bundle").is_valid(candidate)


@pytest.mark.parametrize("slot,kind", [
    ("project", "HostOverlay"), ("project", "TaskContract"),
    ("routingPolicy", "ExecutionReceipt"), ("domains", "Project"),
    ("worktreeRoles", "Domain"),
])
def test_bundle_members_have_fixed_kind_schemas(slot, kind):
    value = bundle()
    value[slot] = [resource(kind)] if slot in ["domains", "worktreeRoles"] else resource(kind)
    assert not validator("governance-bundle").is_valid(value)


def test_bundle_duplicate_objects_and_nested_extras_reject():
    value = bundle()
    value["domains"].append(deepcopy(value["domains"][0]))
    assert not validator("governance-bundle").is_valid(value)
    value = bundle()
    value["project"]["spec"]["hostPath"] = "/srv/synthetic.invalid"
    assert not validator("governance-bundle").is_valid(value)


def test_bundle_reference_integrity_remains_s4():
    value = bundle()
    value["project"]["spec"]["domainRefs"][0]["id"] = "missing.invalid"
    validator("governance-bundle").validate(value)
    # Shape acceptance does not establish reference existence or association.


@pytest.mark.parametrize("outcome", ["not-attempted", "succeeded", "failed", "indeterminate"])
def test_delivery_outcome_vocabulary(outcome):
    value = delivery()
    value["outcome"] = outcome
    validator("receipt-delivery-result").validate(value)


@pytest.mark.parametrize("field", [
    "apiVersion", "receiptId", "receiptDigest", "outcome",
    "attemptedAt", "reasonCodes", "sanitizedSummary",
])
def test_delivery_required_fields(field):
    value = delivery()
    del value[field]
    assert not validator("receipt-delivery-result").is_valid(value)


@pytest.mark.parametrize("field,bad", [
    ("apiVersion", "contextctl.dev/v1alpha2"),
    ("kind", "ReceiptDeliveryResult"), ("allowWrite", True),
    ("authority", {}), ("receipt", resource("ExecutionReceipt")),
    ("receiptId", "synthetic.invalid"), ("receiptDigest", "sha256:0"),
    ("outcome", "passed"), ("attemptedAt", "2000-02-30T00:00:00Z"),
    ("reasonCodes", ["reason.synthetic.denied", "reason.synthetic.denied"]),
    ("reasonCodes", ["invalid"]), ("sanitizedSummary", ""),
    ("sanitizedSummary", "x" * 1025), ("sanitizedSummary", "line\nbreak"),
])
def test_delivery_closed_bounded_evidence(field, bad):
    value = delivery()
    value[field] = bad
    assert not validator("receipt-delivery-result").is_valid(value)


def test_all_supporting_resources_remain_non_kind_catalog_entries():
    for name in ["common", "resource", "governance-bundle", "receipt-delivery-result"]:
        record = get_resource(name + ".schema.json")
        assert record.kind is None
        assert record.dispatchable_kind is False
