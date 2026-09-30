"""Build the fixed offline registry from this distribution's bundled resources."""

import json
from importlib.resources import files

from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

from .catalog import CATALOG

DIALECT = "https://json-schema.org/draft/2020-12/schema"


def _deny_retrieval(uri: str) -> Resource:
    """Unknown identifiers never select a network or filesystem retriever."""
    raise NoSuchResource(ref=uri)


def build_registry() -> Registry:
    """Return a fresh immutable Registry containing exactly the 11 frozen IDs.

    Reads only trusted package resources selected by the fixed catalog. JSON
    loading here is not the deferred strict decoder for governance instances.
    No caller-provided path, identifier construction, or retrieval hook exists.
    """
    root = files("contextctl_schema").joinpath("schemas", "v1alpha1")
    resources = []
    for record in CATALOG:
        document = json.loads(root.joinpath(record.resource_name).read_text("utf-8"))
        if document.get("$schema") != DIALECT or document.get("$id") != record.schema_id:
            raise ValueError(f"Packaged Schema identity mismatch: {record.resource_name}")
        Draft202012Validator.check_schema(document)
        resources.append((record.schema_id, DRAFT202012.create_resource(document)))
    return Registry(retrieve=_deny_retrieval).with_resources(resources).crawl()
