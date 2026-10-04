"""Fixed-checkout source evidence for the unchanged offline registry."""

import json
import socket
import urllib.request
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from referencing.exceptions import NoSuchResource, Unresolvable
from referencing.jsonschema import DRAFT202012

from contextctl_schema.catalog import CATALOG
from contextctl_schema.registry import DIALECT, build_registry

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(autouse=True)
def source_package_resources(monkeypatch):
    # Source-only S3 verification; no package rebuild or reinstall.
    monkeypatch.setattr("contextctl_schema.registry.files", lambda _package: ROOT)



@pytest.fixture
def offline_registry(monkeypatch):
    def forbidden_network(*args, **kwargs):
        pytest.fail("Offline registry attempted network access")

    monkeypatch.setattr(socket.socket, "connect", forbidden_network)
    monkeypatch.setattr(socket, "create_connection", forbidden_network)
    monkeypatch.setattr(urllib.request, "urlopen", forbidden_network)
    return build_registry()


def test_complete_local_registry(offline_registry):
    assert len(offline_registry) == 11
    assert set(offline_registry) == {r.schema_id for r in CATALOG}


@pytest.mark.parametrize("record", CATALOG, ids=lambda r: r.resource_name)
def test_source_resource_identity_and_dialect(record, offline_registry):
    document = json.loads((ROOT / record.repository_path).read_text("utf-8"))
    if record.resource_name == "common.schema.json":
        assert "$defs" in document
        assert "not" not in document
    elif record.resource_name == "resource.schema.json":
        assert len(document["oneOf"]) == 7
        assert document["oneOf"] == [
            {"$ref": item.schema_id} for item in CATALOG if item.dispatchable_kind
        ]
    else:
        assert document["type"] == "object"
        assert document["additionalProperties"] is False
    assert document.get("not") != {}
    assert document["$id"] == record.schema_id
    assert document["$schema"] == DIALECT
    Draft202012Validator.check_schema(document)
    assert offline_registry.resolver().lookup(record.schema_id).contents == document
    assert offline_registry[record.schema_id] == DRAFT202012.create_resource(document)


@pytest.mark.parametrize(
    "record", [r for r in CATALOG if r.resource_name != "common.schema.json"],
    ids=lambda r: r.resource_name,
)
@pytest.mark.parametrize("instance", [
    None, False, True, 0, -1, 1.5, "", "synthetic",
    [], [None], {}, {"synthetic": [1, True, None]},
    {"apiVersion": "contextctl.dev/v1alpha1", "kind": "Project"},
])
def test_resources_reject_non_resource_and_incomplete_instances(record, instance, offline_registry):
    schema = offline_registry.contents(record.schema_id)
    validator = Draft202012Validator(schema, registry=offline_registry)
    errors = list(validator.iter_errors(instance))
    assert errors
    assert not validator.is_valid(instance)


@pytest.mark.parametrize("uri", [
    "urn:uuid:00000000-0000-0000-0000-000000000000",
    "https://synthetic.invalid/schema.json",
    "http://synthetic.invalid/schema.json",
    "file:///synthetic/unknown.schema.json",
    "schemas/v1alpha1/project.schema.json",
])
def test_unknown_resources_fail_without_retrieval(uri, offline_registry):
    with pytest.raises(NoSuchResource):
        offline_registry.get_or_retrieve(uri)
    with pytest.raises(Unresolvable):
        offline_registry.resolver().lookup(uri)


def test_unknown_fragment_fails(offline_registry):
    with pytest.raises(Unresolvable):
        offline_registry.resolver().lookup(CATALOG[0].schema_id + "#missing")


def test_registry_instances_do_not_share_mutable_documents():
    first = build_registry()
    first.contents(CATALOG[0].schema_id)["synthetic-mutation"] = True
    second = build_registry()
    assert "synthetic-mutation" not in second.contents(CATALOG[0].schema_id)
    assert len(second) == 11
