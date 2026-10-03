"""Project-owned format assertions for the canonical S2 string profiles.

These checks supply lexical and calendar evidence only, not a strict decoder,
model codec, cross-field chronology check, or trusted-clock freshness check.
"""

from datetime import datetime
import re
from uuid import UUID

from jsonschema import FormatChecker

PROJECT_FORMATS = ("uuid", "date-time")

_UUID_PATTERN = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)
_TIMESTAMP_PATTERN = re.compile(
    r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$"
)


def _is_canonical_uuid(value: object) -> bool:
    if not isinstance(value, str):
        return True
    if _UUID_PATTERN.fullmatch(value) is None:
        return False
    # Parsing is additional evidence; the lexical check establishes canonicality.
    UUID(value)
    return True


def _is_canonical_utc_timestamp(value: object) -> bool:
    if not isinstance(value, str):
        return True
    if _TIMESTAMP_PATTERN.fullmatch(value) is None:
        return False
    # Fixed components avoid permissive parsing or normalization. datetime
    # independently rejects year zero and invalid Gregorian calendar dates.
    datetime(
        int(value[0:4]), int(value[5:7]), int(value[8:10]),
        int(value[11:13]), int(value[14:16]), int(value[17:19]),
    )
    return True


def build_format_checker() -> FormatChecker:
    """Return a fresh checker for exactly uuid and date-time, with no extras.

    This fixed surface accepts no format configuration. Pass the returned
    checker explicitly as the validator's format_checker argument.
    """
    checker = FormatChecker(formats=())
    checker.checks("uuid", raises=ValueError)(_is_canonical_uuid)
    checker.checks("date-time", raises=ValueError)(_is_canonical_utc_timestamp)
    return checker
