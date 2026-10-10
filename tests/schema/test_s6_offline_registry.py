"""S6 fail-closed checks for the approved offline validator binding."""

from importlib.metadata import version
from pathlib import Path
import sys
from unittest.mock import patch

import pytest
from jsonschema import Draft202012Validator
from jsonschema.exceptions import FormatError
from referencing.exceptions import NoSuchResource

import contextctl_schema
from contextctl_schema import PROJECT_FORMATS, build_format_checker
from contextctl_schema.catalog import API_VERSION, CATALOG, SCHEMA_SET_REVISION
from contextctl_schema.registry import DIALECT
from tests.schema.s6_fixture_runner import REPOSITORY_ROOT, source_schema_documents
from tests.schema.test_resource_schemas import source_registry


def _walk_formats(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "format":
                yield child
            yield from _walk_formats(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_formats(child)


def _walk_keys(value):
    if isinstance(value, dict):
        yield from value
        for child in value.values():
            yield from _walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_keys(child)


def test_approved_interpreter_and_dependency_profile_is_exact() -> None:
    assert sys.version_info[:2] == (3, 13)
    assert version("jsonschema") == "4.26.0"
    assert version("referencing") == "0.37.0"
    assert version("jsonschema-specifications") == "2025.9.1"
    assert version("pytest") == "9.1.1"


def test_tests_bind_repository_source_not_an_ambient_installed_package() -> None:
    module_path = Path(contextctl_schema.__file__).resolve()
    expected = (REPOSITORY_ROOT / "src" / "contextctl_schema" / "__init__.py").resolve()
    assert module_path == expected


def test_fixed_registry_contains_exactly_the_approved_catalog_resources() -> None:
    registry = source_registry()
    documents = source_schema_documents()
    assert len(tuple(registry)) == len(CATALOG) == 11
    assert set(registry) == {record.schema_id for record in CATALOG}
    for record in CATALOG:
        document = registry.contents(record.schema_id)
        assert document == documents[record.schema_id]
        assert document["$schema"] == DIALECT
        assert document["$id"] == record.schema_id
        Draft202012Validator.check_schema(document)


def test_missing_registry_resource_fails_without_network_fallback() -> None:
    registry = source_registry()
    with patch("socket.create_connection", side_effect=AssertionError("network attempted")):
        with pytest.raises(NoSuchResource):
            registry.get_or_retrieve("https://network.invalid/missing-schema")


def test_adopted_formats_are_explicit_and_mandatory() -> None:
    formats = set()
    for document in source_schema_documents().values():
        formats.update(_walk_formats(document))
    assert formats == set(PROJECT_FORMATS) == {"uuid", "date-time"}

    checker = build_format_checker()
    checker.check("00000000-0000-4000-8000-000000000001", "uuid")
    checker.check("2000-01-01T00:00:00Z", "date-time")
    with pytest.raises(FormatError):
        checker.check("NOT-A-UUID", "uuid")
    with pytest.raises(FormatError):
        checker.check("2000-01-01T00:00:00+00:00", "date-time")


def test_s6_used_keyword_capabilities_are_present_in_the_frozen_schema_set() -> None:
    keys = set()
    for document in source_schema_documents().values():
        keys.update(_walk_keys(document))
    assert {
        "$schema",
        "$id",
        "$defs",
        "$ref",
        "const",
        "allOf",
        "anyOf",
        "oneOf",
        "if",
        "then",
        "else",
        "additionalProperties",
        "format",
        "required",
        "type",
    } <= keys


def test_catalog_revision_api_and_dispatchable_kinds_are_frozen() -> None:
    assert API_VERSION == "contextctl.dev/v1alpha1"
    assert SCHEMA_SET_REVISION == "v1alpha1-r1"
    assert [record.kind for record in CATALOG if record.dispatchable_kind] == [
        "Project",
        "Domain",
        "WorktreeRole",
        "RoutingPolicy",
        "HostOverlay",
        "TaskContract",
        "ExecutionReceipt",
    ]
