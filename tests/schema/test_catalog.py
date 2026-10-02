"""Frozen-catalog and dispatch boundary evidence for S1 only."""

from dataclasses import FrozenInstanceError

import pytest

from contextctl_schema.catalog import (
    API_VERSION,
    CATALOG,
    SCHEMA_SET_REVISION,
    get_resource,
    lookup_kind,
)

EXPECTED = (
    ("common.schema.json", "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864", None),
    ("resource.schema.json", "urn:uuid:77fb943a-f8f8-491b-beaf-c1b4d9684801", None),
    ("project.schema.json", "urn:uuid:d5cecdb5-eadf-491d-80c6-869a7f4d10d9", "Project"),
    ("domain.schema.json", "urn:uuid:2bab91f3-c4d5-43e5-90f6-ffb786b42e65", "Domain"),
    ("worktree-role.schema.json", "urn:uuid:4393a3fc-40da-41be-aca9-4276ddc752fa", "WorktreeRole"),
    ("routing-policy.schema.json", "urn:uuid:5d929622-e8b2-40b4-80aa-5d8630625108", "RoutingPolicy"),
    ("host-overlay.schema.json", "urn:uuid:c0de9354-1096-4cea-9cde-a33ad38ab313", "HostOverlay"),
    ("task-contract.schema.json", "urn:uuid:314c8f9e-2554-4ebc-b688-d48598693282", "TaskContract"),
    ("execution-receipt.schema.json", "urn:uuid:53faa365-c113-4b2d-a9c5-022cd87a21dd", "ExecutionReceipt"),
    ("governance-bundle.schema.json", "urn:uuid:e1293323-8af3-41ed-a55e-dc0c27f35206", None),
    ("receipt-delivery-result.schema.json", "urn:uuid:ffa1dcf4-5eb3-4a16-b1b2-be3bc1898684", None),
)
KINDS = {
    "Project", "Domain", "WorktreeRole", "RoutingPolicy",
    "HostOverlay", "TaskContract", "ExecutionReceipt",
}


def test_complete_frozen_catalog():
    assert isinstance(CATALOG, tuple)
    assert len(CATALOG) == 11
    assert SCHEMA_SET_REVISION == "v1alpha1-r1"
    assert API_VERSION == "contextctl.dev/v1alpha1"
    assert {(r.resource_name, r.schema_id, r.kind) for r in CATALOG} == set(EXPECTED)
    assert len({r.resource_name for r in CATALOG}) == 11
    assert len({r.schema_id for r in CATALOG}) == 11
    assert {r.kind for r in CATALOG if r.dispatchable_kind} == KINDS
    assert sum(r.dispatchable_kind for r in CATALOG) == 7
    assert sum(not r.dispatchable_kind for r in CATALOG) == 4


@pytest.mark.parametrize("name,schema_id,kind", EXPECTED)
def test_exact_resource_records(name, schema_id, kind):
    record = get_resource(name)
    assert record.resource_name == name
    assert record.repository_path == f"schemas/v1alpha1/{name}"
    assert record.schema_id == schema_id
    assert record.schema_set_revision == "v1alpha1-r1"
    assert record.api_version == "contextctl.dev/v1alpha1"
    assert record.kind == kind
    assert record.dispatchable_kind is (kind is not None)
    if kind is not None:
        assert lookup_kind("v1alpha1-r1", "contextctl.dev/v1alpha1", kind) is record
    else:
        with pytest.raises(KeyError):
            lookup_kind("v1alpha1-r1", "contextctl.dev/v1alpha1", name)
        with pytest.raises(KeyError):
            lookup_kind("v1alpha1-r1", "contextctl.dev/v1alpha1", None)


def test_records_are_immutable():
    record = get_resource("project.schema.json")
    with pytest.raises(FrozenInstanceError):
        record.schema_id = "urn:uuid:00000000-0000-0000-0000-000000000000"
    with pytest.raises(TypeError):
        CATALOG[0] = record


@pytest.mark.parametrize("name", [
    "", "unknown.schema.json", "Project.schema.json",
    "schemas/v1alpha1/project.schema.json", "../project.schema.json",
    "project.schema.json#fragment", "project.schema.json ",
])
def test_unknown_resource_names_fail(name):
    with pytest.raises(KeyError):
        get_resource(name)


@pytest.mark.parametrize("revision,api,kind", [
    ("v1alpha1-r2", "contextctl.dev/v1alpha1", "Project"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha2", "Project"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "Unknown"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "project"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "GovernanceBundle"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "ReceiptDeliveryResult"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "Common"),
    ("v1alpha1-r1", "contextctl.dev/v1alpha1", "Resource"),
    ("", "", ""),
])
def test_unsupported_dispatch_fails(revision, api, kind):
    with pytest.raises(KeyError):
        lookup_kind(revision, api, kind)
