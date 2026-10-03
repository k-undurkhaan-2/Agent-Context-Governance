"""S2 common-profile Schema evidence, read directly from the checkout.

All data are conspicuously synthetic. General vectors assert structure/lexical
rules and the explicit project formats. Timestamp format/calendar vectors use
the same project-owned checker without optional dependencies or blocked skips.
No strict decoder, model, static resolver, path matcher, or runtime is implemented.
"""

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

from contextctl_schema import PROJECT_FORMATS, build_format_checker

COMMON_PATH = (
    Path(__file__).resolve().parents[2] / "schemas/v1alpha1/common.schema.json"
)
COMMON = json.loads(COMMON_PATH.read_text(encoding="utf-8"))
COMMON_ID = "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864"


def deny_retrieval(uri):
    raise NoSuchResource(ref=uri)


REGISTRY = Registry(retrieve=deny_retrieval).with_resource(
    COMMON_ID, DRAFT202012.create_resource(COMMON)
)
# Both required assertions are explicit and independent of optional checkers.
PROJECT_CHECKER = build_format_checker()

POSITIVE_VECTORS = []
NEGATIVE_VECTORS = []


def positive(profile, label, value):
    POSITIVE_VECTORS.append((profile, label, value))


def negative(profile, label, value):
    NEGATIVE_VECTORS.append((profile, label, value))


UUID = "01234567-89ab-cdef-0123-456789abcdef"
OID = {"algorithm": "sha1", "value": "a" * 40}
REFERENCE = {
    "apiVersion": "contextctl.dev/v1alpha1",
    "kind": "Project",
    "id": "project.invalid",
}
HTTPS = {
    "transport": "https",
    "host": "repo.invalid",
    "namespace": ["synthetic"],
    "repository": "governance",
}
SSH = {**HTTPS, "transport": "ssh"}
FRESHNESS = {
    "issuedAt": "2000-01-01T00:00:00Z",
    "expiresAt": "2000-01-01T00:00:01Z",
}
SELECTION = {"exact": ["refs/heads/synthetic"], "prefixes": []}

ENUM_VALUES = {
    "kind": [
        "Project", "Domain", "WorktreeRole", "RoutingPolicy", "HostOverlay",
        "TaskContract", "ExecutionReceipt",
    ],
    "mode": ["plan-only", "implementation"],
    "capability": [
        "inspect", "validate", "create", "modify", "delete", "execute-tests",
        "execute-build", "git-stage", "git-commit", "git-branch", "git-remote",
        "network", "external-secret-use",
    ],
    "gitMode": ["100644", "100755", "120000", "160000"],
    "checkOutcome": ["passed", "failed", "indeterminate"],
    "executionCheckOutcome": ["succeeded", "failed", "cancelled", "indeterminate"],
    "executionOutcome": [
        "not-attempted", "succeeded", "failed", "cancelled", "indeterminate",
    ],
    "verificationOutcome": ["not-performed", "passed", "failed", "indeterminate"],
    "releaseOutcome": ["not-required", "succeeded", "failed", "indeterminate"],
    "lifecycleOutcome": ["denied", "succeeded", "failed", "cancelled", "indeterminate"],
    "receiptDeliveryOutcome": ["not-attempted", "succeeded", "failed", "indeterminate"],
}
for profile, values in ENUM_VALUES.items():
    for value in values:
        positive(profile, value, value)
        if value.swapcase() != value:
            negative(profile, "wrong-case-" + value, value.swapcase())
    negative(profile, "unknown", "synthetic-unknown")
    negative(profile, "null", None)
negative("checkOutcome", "execution-succeeded", "succeeded")
negative("checkOutcome", "execution-cancelled", "cancelled")
negative("executionCheckOutcome", "non-execution-passed", "passed")
negative("executionCheckOutcome", "not-attempted", "not-attempted")
negative("gitMode", "number", 100644)

positive("apiVersion", "frozen", "contextctl.dev/v1alpha1")
negative("apiVersion", "unknown-version", "contextctl.dev/v1alpha2")
negative("apiVersion", "missing-string", None)
for label, value in [
    ("minimum", "a"), ("maximum", "a" * 63),
    ("punctuation", "project.synthetic-1.invalid"), ("internal-dots", "a..b"),
]:
    positive("logicalIdentifier", label, value)
for label, value in [
    ("empty", ""), ("too-long", "a" * 64), ("uppercase", "Project"),
    ("leading-dot", ".a"), ("trailing-dot", "a."), ("leading-hyphen", "-a"),
    ("trailing-hyphen", "a-"), ("underscore", "a_b"), ("slash", "a/b"),
    ("unicode", "\u4f8b"), ("trailing-newline", "a\n"), ("number", 1),
]:
    negative("logicalIdentifier", label, value)

for profile, prefix in [
    ("reasonCode", "reason"), ("profileIdentifier", "profile"),
    ("checkIdentifier", "check"),
]:
    positive(profile, "minimum", prefix + ".a")
    positive(profile, "segmented", prefix + ".synthetic.valid-1")
    positive(profile, "segment-32", prefix + "." + "a" * 32)
    # Four 32-character segments plus a final segment reach exactly 160.
    tail_length = 160 - len(prefix) - 1 - 4 * 33
    positive(profile, "total-160", prefix + "." + ("a" * 32 + ".") * 4 + "a" * tail_length)
    for label, value in [
        ("empty-segment", prefix + "..a"), ("segment-33", prefix + "." + "a" * 33),
        ("leading-hyphen", prefix + ".-a"), ("trailing-hyphen", prefix + ".a-"),
        ("uppercase", prefix + ".A"), ("underscore", prefix + ".a_b"),
        ("missing-segment", prefix + "."), ("wrong-prefix", "synthetic.a"),
        ("trailing-newline", prefix + ".a\n"),
        ("total-161", prefix + "." + ("a" * 32 + ".") * 4 + "a" * (tail_length + 1)),
    ]:
        negative(profile, label, value)

positive("canonicalUuid", "lowercase", UUID)
positive("canonicalUuid", "nil", "00000000-0000-0000-0000-000000000000")
for label, value in [
    ("uppercase", UUID.upper()), ("no-hyphens", UUID.replace("-", "")),
    ("braces", "{" + UUID + "}"), ("urn", "urn:uuid:" + UUID),
    ("non-hex", "g" + UUID[1:]), ("newline", UUID + "\n"),
]:
    negative("canonicalUuid", label, value)

for profile in ("displayText", "sanitizedSummary"):
    positive(profile, "minimum", "x")
    positive(profile, "maximum", "x" * 1024)
    positive(profile, "nfc-unicode", "Synthetic \u00e9 \u4f8b")
    negative(profile, "empty", "")
    negative(profile, "too-long", "x" * 1025)
    negative(profile, "wrong-type", [])
    for code in [*range(32), 127]:
        negative(profile, "control-" + str(code), "synthetic" + chr(code))
for code in range(128, 160):
    negative("displayText", "control-" + str(code), "synthetic" + chr(code))

PATH_POSITIVES = [
    "a", "src/synthetic.py", ".gitignore", ".gitmodules", ".github",
    "foo.git", "dir/.gitignore", "dir/.github/workflow.yml", ".Git/config",
    "synthetic/\u4f8b", "x" * 4096,
]
for i, value in enumerate(PATH_POSITIVES):
    positive("repositoryRelativePath", "path-" + str(i), value)
PATH_NEGATIVES = [
    "", "/src/a", "C:relative", "C:/synthetic", "src\\a", "src//a", "src/",
    ".", "..", "./src", "../src", "src/./a", "src/../a", "src/.", "src/..",
    ".git", ".git/config", ".git/hooks/pre-commit", ".git/worktrees/x/HEAD",
    "foo/.git", "foo/.git/config", "nested/repository/.git/HEAD",
    "src/\0a", "x" * 4097,
]
for i, value in enumerate(PATH_NEGATIVES):
    negative("repositoryRelativePath", "path-" + str(i), value)
for i, value in enumerate([
    "**", "src/**", "**/synthetic?.py", "src/*.py", "a*b?", "a/**/b",
    ".gitignore", ".github/**", "foo.git/**", "dir/.git*", "x" * 4096,
]):
    positive("pathPattern", "pattern-" + str(i), value)
for i, value in enumerate(PATH_NEGATIVES + [
    ".git/**", "foo/.git/**", "!src/**", "src/!a", "{src,docs}/**",
    "[ab]/*.py", "@(src)/**", "src/**x", "src/x**", "src/***/a",
]):
    negative("pathPattern", "pattern-" + str(i), value)

POSIX_PATHS = ["/", "/srv/synthetic.invalid/worktree", "/srv/synthetic.invalid/\u4f8b", "/" + "a" * 4095]
WINDOWS_PATHS = ["C:\\", "C:\\Synthetic.Invalid\\Worktree", "C:\\Synthetic.Invalid\\\u4f8b", "Z:\\" + "a" * 4093]
for profile, platform, paths in [
    ("posixAbsoluteHostPath", "posix", POSIX_PATHS),
    ("windowsDriveAbsoluteHostPath", "windows", WINDOWS_PATHS),
]:
    for i, value in enumerate(paths):
        positive(profile, "path-" + str(i), value)
        positive("absoluteHostPath", platform + "-" + str(i), {"platform": platform, "value": value})
    negative(profile, "empty", "")
    negative(profile, "too-long", paths[-1] + "a")
    for code in [*range(32), *range(127, 160)]:
        negative(profile, "control-" + str(code), paths[1] + chr(code) + "x")
for i, value in enumerate(["relative", "//srv", "/srv//x", "/srv/", "/.", "/..", "/srv/./x", "/srv/../x", "/srv\\x"]):
    negative("posixAbsoluteHostPath", "syntax-" + str(i), value)
for i, value in enumerate([
    "c:\\Synthetic", "C:relative", "\\relative", "\\\\host.invalid\\share",
    "\\\\?\\C:\\Synthetic", "\\\\.\\C:\\Synthetic", "C:/Synthetic",
    "C:\\Synthetic/child", "C:\\Synthetic\\\\child", "C:\\Synthetic\\",
    "C:\\.", "C:\\..", "C:\\Synthetic\\a.", "C:\\Synthetic\\a ",
]):
    negative("windowsDriveAbsoluteHostPath", "syntax-" + str(i), value)
for char in '<>:"/|?*':
    negative("windowsDriveAbsoluteHostPath", "punctuation-" + str(ord(char)), "C:\\Synthetic\\a" + char + "b")
for device in ["CON", "PRN", "AUX", "NUL", "CLOCK$", *("COM" + str(n) for n in range(1, 10)), *("LPT" + str(n) for n in range(1, 10))]:
    for suffix, spelling in [("", device), (".txt", device.lower()), (".log", device.swapcase())]:
        negative("windowsDriveAbsoluteHostPath", "device-" + device + suffix, "C:\\Synthetic\\" + spelling + suffix)
positive("windowsDriveAbsoluteHostPath", "similar-devices", "C:\\Synthetic\\COM0\\COM10\\xCON\\CONSOLE")
negative("absoluteHostPath", "platform-mismatch", {"platform": "windows", "value": "/srv/synthetic.invalid"})
negative("absoluteHostPath", "unknown-platform", {"platform": "win32", "value": "C:\\"})
negative("absoluteHostPath", "unc", {"platform": "windows", "value": "\\\\host.invalid\\share"})

for value in [False, True]:
    positive("allowWrite", str(value), value)
for i, value in enumerate([0, 1, "true", None]):
    negative("allowWrite", "type-" + str(i), value)
positive("capabilities", "empty", [])
positive("capabilities", "multiple", ["inspect", "validate"])
negative("capabilities", "duplicate", ["inspect", "inspect"])
negative("capabilities", "unknown", ["write"])
negative("capabilities", "wrong-type", "inspect")

positive("taggedDigest", "sha256", "sha256:" + "a" * 64)
for label, value in [
    ("short", "sha256:" + "a" * 63), ("long", "sha256:" + "a" * 65),
    ("uppercase", "sha256:" + "A" * 64), ("wrong-tag", "sha1:" + "a" * 64),
    ("non-hex", "sha256:" + "g" * 64), ("newline", "sha256:" + "a" * 64 + "\n"),
]:
    negative("taggedDigest", label, value)
positive("gitObjectId", "sha1", OID)
positive("gitObjectId", "sha256", {"algorithm": "sha256", "value": "b" * 64})
for algorithm, value in [("sha1", "a" * 64), ("sha256", "a" * 40), ("sha1", "A" * 40), ("sha512", "a" * 128), ("sha1", "g" * 40)]:
    negative("gitObjectId", algorithm + "-" + str(len(value)) + "-" + value[0], {"algorithm": algorithm, "value": value})

for profile in ("gitRefIdentifier", "branchRef", "branchPrefix"):
    for label, value in [
        ("ordinary", "refs/heads/synthetic"), ("nested", "refs/heads/synthetic/topic"),
        ("literal-dot", "refs/heads/synthetic.v1"), ("segment-255", "refs/heads/" + "a" * 255),
        ("total-1024", "refs/heads/" + ("a" * 252 + "/") * 3 + "b" * 254),
    ]:
        positive(profile, label, value)
    for i, value in enumerate([
        "", "main", "refs/heads/", "refs/heads//a", "refs/heads/a/",
        "refs/heads/.a", "refs/heads/a.", "refs/heads/a.lock",
        "refs/heads/a..b", "refs/heads/a b", "refs/heads/a~b",
        "refs/heads/a^b", "refs/heads/a:b", "refs/heads/a?b",
        "refs/heads/a*b", "refs/heads/a[b", "refs/heads/a\\b",
        "refs/heads/a\n", "refs/heads/" + "a" * 256,
        "refs/heads/" + ("a" * 253 + "/") * 4,
    ]):
        negative(profile, "ref-" + str(i), value)
positive("gitRefIdentifier", "minimum", "refs/a")
positive("gitRefIdentifier", "tag", "refs/tags/synthetic")
negative("branchRef", "tag", "refs/tags/synthetic")
negative("branchPrefix", "heads-only", "refs/heads")
negative("branchSelection", "duplicate-exact", {"exact": ["refs/heads/synthetic"] * 2, "prefixes": []})
negative("branchSelection", "duplicate-prefix", {"exact": [], "prefixes": ["refs/heads/synthetic"] * 2})
negative("refState", "branch-missing-ref", {"state": "branch"})
negative("refState", "detached-with-ref", {"state": "detached", "branchRef": "refs/heads/synthetic"})
negative("headState", "commit-missing-id", {"state": "commit"})
negative("headState", "unborn-with-id", {"state": "unborn", "objectId": OID})

TIMESTAMP_POSITIVES = [
    "0001-01-01T00:00:00Z", "9999-12-31T23:59:59Z",
    "2000-02-29T00:00:00Z", "2004-02-29T23:59:59Z",
    "2001-01-01T00:00:00Z",
]
for i, value in enumerate(TIMESTAMP_POSITIVES):
    positive("canonicalUtcTimestamp", "timestamp-" + str(i), value)
for i, value in enumerate([
    "2000-01-01t00:00:00Z", "2000-01-01T00:00:00z",
    "2000-01-01T00:00:00+00:00", "2000-01-01T00:00:00",
    "2000-1-01T00:00:00Z", "2000-01-01T00:00:00.1Z",
    "2000-01-01T00:00:00.001Z", "2000-01-01T00:00:00.000001Z",
    "2000-01-01T00:00:00.Z", "2000-01-01T00:00:60Z",
    "2000-01-01T24:00:00Z", "2000-13-01T00:00:00Z",
    "2000-01-32T00:00:00Z", "2000-00-01T00:00:00Z",
    "2000-01-00T00:00:00Z", "10000-01-01T00:00:00Z",
    "+2000-01-01T00:00:00Z", " 2000-01-01T00:00:00Z",
    "2000-01-01T00:00:00Z ", "2000-01-01 00:00:00Z",
    "2000-01-01T00:00:00Z\n",
]):
    negative("canonicalUtcTimestamp", "timestamp-" + str(i), value)
TIMESTAMP_CALENDAR_NEGATIVES = [
    "0000-01-01T00:00:00Z", "2001-02-29T00:00:00Z",
    "1900-02-29T00:00:00Z", "2000-04-31T00:00:00Z",
]

for i, value in enumerate(["a.b", "repo.invalid", ".".join(["a" * 63] * 3 + ["b" * 61])]):
    positive("remoteDnsHost", "host-" + str(i), value)
for i, value in enumerate([
    "Repo.invalid", "localhost", "synthetic", ".repo.invalid", "repo.invalid.",
    "repo..invalid", "-repo.invalid", "repo-.invalid", "re_po.invalid",
    "xn--synthetic.invalid", "repo.xn--invalid", "\u4f8b.invalid", "127.0.0.1",
    "::1", "[::1]", "fe80::1%eth0", "user@repo.invalid", "https://repo.invalid",
    "repo.invalid\n", "a" * 64 + ".invalid",
    ".".join(["a" * 63] * 3 + ["b" * 62]),
]):
    negative("remoteDnsHost", "host-" + str(i), value)
for profile, maximum in [("remoteNamespaceComponent", 63), ("remoteRepositoryName", 128)]:
    for label, value in [("minimum", "a"), ("maximum", "a" * maximum), ("punctuation", "a_b-c.d")]:
        positive(profile, label, value)
    for i, value in enumerate(["", "a" * (maximum + 1), ".", "..", "a..b", ".a", "a.", "-a", "a-", "a/b", "a\\b", "A", "\u4f8b", "a b", "a\n"]):
        negative(profile, "component-" + str(i), value)
positive("remoteNamespaceComponent", "git-literal", "synthetic.git")
negative("remoteRepositoryName", "git-suffix", "synthetic.git")
positive("remoteRepositoryName", "nonterminal-git", "synthetic.git.data")
positive("remoteNamespace", "minimum", ["a"])
positive("remoteNamespace", "ordered-repetition", ["synthetic", "synthetic"])
positive("remoteNamespace", "maximum-joined-1023", ["a" * 63] * 16)
negative("remoteNamespace", "empty", [])
negative("remoteNamespace", "too-many", ["a"] * 17)
negative("remoteNamespace", "bad-item", ["A"])
positive("structuredRemote", "https", HTTPS)
positive("structuredRemote", "ssh", SSH)
positive("structuredRemote", "https-non-default", {**HTTPS, "port": 8443})
positive("structuredRemote", "ssh-non-default", {**SSH, "port": 2222})
positive("structuredRemote", "https-ssh-port", {**HTTPS, "port": 22})
positive("structuredRemote", "ssh-https-port", {**SSH, "port": 443})
negative("structuredRemote", "transport", {**HTTPS, "transport": "git"})
for label, value in [("zero", 0), ("negative", -1), ("too-large", 65536), ("string", "8443"), ("fraction", 1.5), ("bool", True)]:
    negative("structuredRemote", "port-" + label, {**HTTPS, "port": value})
negative("structuredRemote", "https-explicit-default", {**HTTPS, "port": 443})
negative("structuredRemote", "ssh-explicit-default", {**SSH, "port": 22})
positive("acceptedRemotes", "multiple", [HTTPS, SSH])
negative("acceptedRemotes", "empty", [])
negative("acceptedRemotes", "duplicate", [HTTPS, dict(HTTPS)])
negative("repositoryIdentity", "empty-remotes", {"acceptedRemotes": []})
negative("remoteExpectation", "empty-remotes", {"remoteName": "origin", "acceptedRemotes": []})
negative("scope", "duplicate-paths", {"capabilities": [], "paths": ["src/**", "src/**"]})

# Each closed branch: positive control, missing required fields, unknown member.
CLOSED_OBJECT_CASES = [
    ("metadata", "minimal", {"id": "synthetic.invalid"}, ["id"]),
    ("metadata", "full", {"id": "synthetic.invalid", "displayName": "x" * 128, "description": "x" * 1024}, ["id"]),
    ("absoluteHostPath", "posix-closed", {"platform": "posix", "value": "/"}, ["platform", "value"]),
    ("absoluteHostPath", "windows-closed", {"platform": "windows", "value": "C:\\"}, ["platform", "value"]),
    ("objectReference", "closed", REFERENCE, ["apiVersion", "kind", "id"]),
    ("gitObjectId", "sha1-closed", OID, ["algorithm", "value"]),
    ("gitObjectId", "sha256-closed", {"algorithm": "sha256", "value": "b" * 64}, ["algorithm", "value"]),
    ("branchSelection", "closed", SELECTION, ["exact", "prefixes"]),
    ("branchPolicy", "closed", {"allowed": SELECTION, "denied": {"exact": [], "prefixes": []}}, ["allowed", "denied"]),
    ("refState", "branch", {"state": "branch", "branchRef": "refs/heads/synthetic"}, ["state", "branchRef"]),
    ("refState", "detached", {"state": "detached"}, ["state"]),
    ("headState", "commit", {"state": "commit", "objectId": OID}, ["state", "objectId"]),
    ("headState", "unborn", {"state": "unborn"}, ["state"]),
    ("freshnessBoundary", "closed", FRESHNESS, ["issuedAt", "expiresAt"]),
    ("structuredRemote", "closed", HTTPS, ["transport", "host", "namespace", "repository"]),
    ("repositoryIdentity", "closed", {"acceptedRemotes": [HTTPS]}, ["acceptedRemotes"]),
    ("remoteExpectation", "closed", {"remoteName": "origin", "acceptedRemotes": [HTTPS]}, ["remoteName", "acceptedRemotes"]),
    ("scope", "closed", {"capabilities": ["inspect"], "paths": ["src/**"]}, ["capabilities", "paths"]),
]
for profile, label, value, required in CLOSED_OBJECT_CASES:
    positive(profile, label, value)
    negative(profile, label + "-unknown", {**value, "syntheticExtra": True})
    for key in required:
        negative(profile, label + "-missing-" + key, {k: v for k, v in value.items() if k != key})
negative("metadata", "display-too-long", {"id": "synthetic.invalid", "displayName": "x" * 129})
negative("metadata", "description-too-long", {"id": "synthetic.invalid", "description": "x" * 1025})
negative("metadata", "unknown-name", {"id": "synthetic.invalid", "name": "Synthetic"})
negative("objectReference", "unknown-kind", {**REFERENCE, "kind": "GovernanceBundle"})

INTEGER_BOUNDS = {
    "remotePort": (1, 65535),
    "routingPriority": (0, 1000),
    "indexStage": (0, 0),
    "sequence": (0, 4095),
    "redactionCount": (0, 4294967295),
}
for profile, (minimum, maximum) in INTEGER_BOUNDS.items():
    positive(profile, "minimum", minimum)
    if maximum != minimum:
        positive(profile, "maximum", maximum)
    for label, value in [
        ("below", minimum - 1), ("above", maximum + 1), ("fraction", 0.5),
        ("string", str(minimum)), ("bool", True), ("null", None),
    ]:
        negative(profile, label, value)


def validator(profile, formats=PROJECT_CHECKER):
    return Draft202012Validator(
        {"$ref": COMMON_ID + "#/$defs/" + profile},
        registry=REGISTRY,
        format_checker=formats,
    )


def vector_ids(vectors):
    return [profile + "-" + label for profile, label, _ in vectors]


def test_common_schema_identity_dialect_and_definition_coverage():
    assert len(POSITIVE_VECTORS) + len(TIMESTAMP_POSITIVES) == 201
    assert len(NEGATIVE_VECTORS) + len(TIMESTAMP_CALENDAR_NEGATIVES) == 793
    assert COMMON["$id"] == COMMON_ID
    assert COMMON["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert "not" not in COMMON
    Draft202012Validator.check_schema(COMMON)
    assert set(COMMON["$defs"]) == {profile for profile, _, _ in POSITIVE_VECTORS}
    assert set(COMMON["$defs"]) == {profile for profile, _, _ in NEGATIVE_VECTORS}
    assert COMMON["$defs"]["canonicalUuid"]["format"] == "uuid"
    assert COMMON["$defs"]["canonicalUtcTimestamp"]["format"] == "date-time"
    assert COMMON["$defs"]["canonicalUtcTimestamp"]["pattern"] == (
        r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
        r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$"
    )


@pytest.mark.parametrize(
    "profile,label,value", POSITIVE_VECTORS, ids=vector_ids(POSITIVE_VECTORS),
)
def test_positive_structure_and_lexical_vectors(profile, label, value):
    assert not list(validator(profile).iter_errors(value)), label


@pytest.mark.parametrize(
    "profile,label,value", NEGATIVE_VECTORS, ids=vector_ids(NEGATIVE_VECTORS),
)
def test_negative_structure_and_lexical_vectors(profile, label, value):
    assert list(validator(profile).iter_errors(value)), label


@pytest.fixture
def asserted_formats():
    return build_format_checker()


def test_uuid_format_assertion_is_enabled():
    assert PROJECT_CHECKER.conforms(UUID, "uuid")
    assert not PROJECT_CHECKER.conforms("synthetic-invalid-uuid", "uuid")


@pytest.mark.parametrize("value", TIMESTAMP_POSITIVES)
def test_timestamp_positive_with_asserted_format(value, asserted_formats):
    assert validator("canonicalUtcTimestamp", asserted_formats).is_valid(value)


@pytest.mark.parametrize("value", TIMESTAMP_CALENDAR_NEGATIVES)
def test_timestamp_calendar_negative_with_asserted_format(value, asserted_formats):
    assert not validator("canonicalUtcTimestamp", asserted_formats).is_valid(value)


# Adapter-only cases assert format without the Schema's lexical patterns, so
# the Schema cannot mask a permissive checker. The declared S2 inventory above
# remains 201 positive and 793 negative vectors.
FORMAT_NAMES = {"canonicalUuid": "uuid", "canonicalUtcTimestamp": "date-time"}
ADAPTER_POSITIVE_VECTORS = [
    (FORMAT_NAMES[profile], label, value)
    for profile, label, value in POSITIVE_VECTORS if profile in FORMAT_NAMES
] + [
    ("uuid", "version-1", "01234567-89ab-1def-8123-456789abcdef"),
    ("uuid", "version-4", "01234567-89ab-4def-8123-456789abcdef"),
    ("uuid", "version-7", "01234567-89ab-7def-8123-456789abcdef"),
    ("uuid", "all-bits", "ffffffff-ffff-ffff-ffff-ffffffffffff"),
    ("date-time", "century-leap", "2400-02-29T00:00:00Z"),
    ("date-time", "ordinary-month-end", "2001-04-30T23:59:59Z"),
]
ADAPTER_NEGATIVE_VECTORS = [
    (FORMAT_NAMES[profile], label, value)
    for profile, label, value in NEGATIVE_VECTORS if profile in FORMAT_NAMES
] + [
    ("date-time", "calendar-" + str(i), value)
    for i, value in enumerate(TIMESTAMP_CALENDAR_NEGATIVES)
] + [
    ("uuid", "short", UUID[:-1]),
    ("uuid", "long", UUID + "0"),
    ("uuid", "misplaced-hyphen", "0123456-789ab-cdef-0123-456789abcdef"),
    ("uuid", "leading-space", " " + UUID),
    ("uuid", "trailing-space", UUID + " "),
    ("uuid", "internal-space", UUID[:18] + " " + UUID[19:]),
    ("date-time", "century-non-leap", "2100-02-29T00:00:00Z"),
    ("date-time", "february-30", "2000-02-30T00:00:00Z"),
    ("date-time", "minute-60", "2000-01-01T00:60:00Z"),
    ("date-time", "short-day", "2000-01-1T00:00:00Z"),
    ("date-time", "short-hour", "2000-01-01T0:00:00Z"),
    ("date-time", "short-minute", "2000-01-01T00:0:00Z"),
    ("date-time", "short-second", "2000-01-01T00:00:0Z"),
    ("date-time", "negative-year", "-2000-01-01T00:00:00Z"),
    ("date-time", "nonzero-offset", "2000-01-01T00:00:00+01:00"),
    ("date-time", "internal-tab", "2000-01-01T00:\t0:00Z"),
    ("date-time", "non-ascii-digit", "\u0662" + "000-01-01T00:00:00Z"),
]


def test_project_format_checker_has_exact_surface_without_global_mutation():
    original = dict(FormatChecker.checkers)
    checker = build_format_checker()
    assert PROJECT_FORMATS == ("uuid", "date-time")
    assert set(checker.checkers) == {"uuid", "date-time"}
    assert FormatChecker.checkers == original


def test_project_format_checker_instances_are_independent():
    original = dict(FormatChecker.checkers)
    first = build_format_checker()
    second = build_format_checker()
    assert first is not second
    assert first.checkers is not second.checkers
    first.checks("uuid")(lambda value: True)
    first.checks("synthetic-only")(lambda value: True)
    del first.checkers["date-time"]
    assert second.checkers == build_format_checker().checkers
    assert not second.conforms("synthetic-invalid-uuid", "uuid")
    assert not second.conforms("2001-02-29T00:00:00Z", "date-time")
    assert FormatChecker.checkers == original


@pytest.mark.parametrize(
    "format_name,label,value", ADAPTER_POSITIVE_VECTORS,
    ids=vector_ids(ADAPTER_POSITIVE_VECTORS),
)
def test_project_format_checker_accepts_canonical_strings(format_name, label, value):
    checker = build_format_checker()
    assert checker.conforms(value, format_name), label
    assert Draft202012Validator(
        {"format": format_name}, format_checker=checker,
    ).is_valid(value), label


@pytest.mark.parametrize(
    "format_name,label,value", ADAPTER_NEGATIVE_VECTORS,
    ids=vector_ids(ADAPTER_NEGATIVE_VECTORS),
)
def test_project_format_checker_rejects_invalid_strings(format_name, label, value):
    checker = build_format_checker()
    assert not checker.conforms(value, format_name), label
    errors = list(Draft202012Validator(
        {"format": format_name}, format_checker=checker,
    ).iter_errors(value))
    assert len(errors) == 1 and errors[0].validator == "format", label


@pytest.mark.parametrize("format_name", PROJECT_FORMATS)
@pytest.mark.parametrize("value", [None, False, True, 0, 1.5, [], {}])
def test_project_format_checker_leaves_non_strings_to_type(format_name, value):
    checker = build_format_checker()
    assert checker.conforms(value, format_name)
    assert Draft202012Validator(
        {"format": format_name}, format_checker=checker,
    ).is_valid(value)
    errors = list(Draft202012Validator(
        {"type": "string", "format": format_name}, format_checker=checker,
    ).iter_errors(value))
    assert len(errors) == 1 and errors[0].validator == "type"


# These controls deliberately pass Schema and require another gate. They are
# not additional accepted governance instances or evidence of static acceptance.
DEFERRED_VECTORS = [
    ("displayText", "nfc-model", "e\u0301"),
    ("displayText", "unicode-scalar-model", "\ud800"),
    ("objectReference", "reference-existence-static", {**REFERENCE, "id": "absent.invalid"}),
    ("freshnessBoundary", "equal-times-static", {"issuedAt": FRESHNESS["issuedAt"], "expiresAt": FRESHNESS["issuedAt"]}),
    ("freshnessBoundary", "reverse-times-static", {"issuedAt": FRESHNESS["expiresAt"], "expiresAt": FRESHNESS["issuedAt"]}),
    ("acceptedRemotes", "canonical-order-static", [SSH, HTTPS]),
    ("scope", "pattern-language-static", {"capabilities": [], "paths": ["**"]}),
]


@pytest.mark.parametrize(
    "profile,label,value", DEFERRED_VECTORS, ids=vector_ids(DEFERRED_VECTORS),
)
def test_schema_acceptance_is_not_deferred_validation(profile, label, value):
    assert validator(profile).is_valid(value), label


@pytest.mark.parametrize("token", ["1.0", "1e0", "-0"])
def test_schema_cannot_recover_raw_numeric_spelling(token):
    # Ordinary JSON parsing is only a demonstration of information loss.
    assert validator("sequence").is_valid(json.loads(token))


def test_schema_cannot_detect_duplicate_source_keys():
    value = json.loads('{"id":"first.invalid","id":"second.invalid"}')
    assert validator("metadata").is_valid(value)
