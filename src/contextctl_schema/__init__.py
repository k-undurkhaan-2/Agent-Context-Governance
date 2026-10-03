"""Unpublished Schema catalog, offline registry, and S2 format assertions."""

from .catalog import API_VERSION, CATALOG, SCHEMA_SET_REVISION, get_resource, lookup_kind
from .formats import PROJECT_FORMATS, build_format_checker
from .registry import build_registry

__version__ = "0.0.0"

__all__ = [
    "API_VERSION",
    "CATALOG",
    "PROJECT_FORMATS",
    "SCHEMA_SET_REVISION",
    "build_format_checker",
    "build_registry",
    "get_resource",
    "lookup_kind",
]
