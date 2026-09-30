"""Unpublished S1 Schema catalog; every bundled placeholder rejects all instances."""

from .catalog import API_VERSION, CATALOG, SCHEMA_SET_REVISION, get_resource, lookup_kind
from .registry import build_registry

__version__ = "0.0.0"

__all__ = [
    "API_VERSION",
    "CATALOG",
    "SCHEMA_SET_REVISION",
    "build_registry",
    "get_resource",
    "lookup_kind",
]
