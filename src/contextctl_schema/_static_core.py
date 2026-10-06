"""Private S4 diagnostics, structural composition, ordering and proof consumers.

No proof producer is installed here. The private context has no successful
default implementation; the synthetic tests replace its methods explicitly.
These records describe validation, never governance resources or authority.
"""

from dataclasses import dataclass
from types import MappingProxyType

from jsonschema import Draft202012Validator

from .catalog import CATALOG, SCHEMA_SET_REVISION, get_resource
from .formats import build_format_checker
from .registry import build_registry


@dataclass(frozen=True, slots=True)
class StaticDiagnostic:
    code: str
    subject_id: str | None
    instance_pointer: str
    predicate_family: str
    message: str
    schema_id: str | None
    schema_pointer: str | None
    keyword: str


@dataclass(frozen=True, slots=True)
class ProofObligation:
    requirement_id: str
    profile: str
    subject_id: str | None
    instance_pointer: str
    required_binding: tuple


@dataclass(frozen=True, slots=True)
class StaticValidationResult:
    status: str
    validation_scope: str
    diagnostics: tuple[StaticDiagnostic, ...]
    required_proofs: tuple[ProofObligation, ...]
    direct_checks_passed: bool | None
    full_static_acceptance: bool


DEFAULT_PROOF_LIMITS = MappingProxyType({
    "max_nfa_states": 16384,
    "max_product_states": 250000,
    "max_transition_steps": 2000000,
    "max_nfc_refinements": 1024,
    "max_work_units": 4000000,
})


class _ProofContext:
    """Unbound future integration port; constructing it supplies no proof.

    No public registration or trusted producer exists in S4. In particular,
    duck-typed caller objects, maps and booleans are never proof contexts.
    """

    __slots__ = ()

    def require_input_provenance(self, subject, root_id, schema_set_revision):
        return None

    def require_canonical_comparison(self, left_subject, left_projection,
                                     right_subject, right_projection,
                                     comparison_kind):
        return None

    def require_digest(self, subject, fixed_profile, exact_projection,
                       prerequisite_subjects):
        return None

    def require_complete_host_snapshot(self, host_id, checkpoint_context):
        return None

    def require_baseline_materialization(self, contract_subject,
                                         required_dimensions):
        return None

    def require_completed_static_validation(self, subject, validation_scope,
                                            prerequisite_subjects):
        return None

    def _validate_handle(self, handle, operation, bound_operands):
        # A future producer must validate integrity, binding, stage and
        # immutable-input/snapshot continuity. S4 cannot create that evidence.
        return None


class _ValidationContext:
    def __init__(self, subject, root_id, proof_context=None):
        self.subject = subject
        self.root_id = root_id
        self.proof_context = proof_context
        self.diagnostics = []
        self.required_proofs = []
        self.failed = False
        self.unevaluated = False
        self.requirement_id = "PROOF.INPUT"
        self.location = ""
        self.family = "input-provenance"
        self.proof_profile = "prepared-input"
        self.registry = None
        self.schema_locations = {}
        self.safe_keys = set()
        self.proofs = []
        self.path_metrics = []

    @property
    def subject_id(self):
        if isinstance(self.subject, dict):
            metadata = self.subject.get("metadata", {})
            if isinstance(metadata, dict):
                identifier = metadata.get("id")
                if (isinstance(identifier, str) and len(identifier) <= 128
                        and all(c.isascii() and (c.isalnum() or c in "._-")
                                for c in identifier)):
                    return identifier
        return None

    def check(self, requirement_id, condition, location="", family=None):
        if not condition:
            self.failed = True
            diagnostic = _diagnostic(requirement_id, self.subject_id,
                                     location, family or requirement_id.split(".")[0])
            self.diagnostics.append(diagnostic)
        return bool(condition)

    def unavailable(self, requirement_id, location="", profile="dependency",
                    binding=(), *, direct=True):
        if direct:
            self.unevaluated = True
        obligation = ProofObligation(requirement_id, profile, self.subject_id,
                                     location, tuple(binding))
        self.required_proofs.append(obligation)
        self.diagnostics.append(_diagnostic(requirement_id, self.subject_id,
                                            location, "proof-required"))


def _diagnostic(requirement_id, subject_id, location, predicate_family):
    code = ("reason.overlay." + requirement_id.removeprefix("D10.")
            if requirement_id.startswith("D10.") else "S4." + requirement_id)
    return StaticDiagnostic(code, subject_id, location[:1024], predicate_family,
                            "The required static predicate or bound proof was not satisfied.",
                            None, None, requirement_id)


def _compare_s(left, right):
    """Unsigned UTF-16 order; no locale, normalization or input repair."""
    a, b = _s(left), _s(right)
    return (a > b) - (a < b)


def _s(value):
    return value.encode("utf-16-be", errors="surrogatepass")


def _reference_key(ref):
    return tuple(_s(ref[k]) for k in ("apiVersion", "kind", "id"))


def _transition_key(transition):
    return _s(transition["type"]), _s(transition["path"])


def _lock_key(lock):
    kind = lock["type"]
    return ((_s(kind), _s(lock["ref"])) if kind == "ref" else
            (_s(kind), _s(lock["identifier"])) if kind == "other" else (_s(kind),))


def _pointer(parts, safe_keys=None):
    result = []
    for part in parts:
        if isinstance(part, int):
            text = str(part)
        elif safe_keys is None or part in safe_keys:
            text = part
        else:
            text = "[unrecognized-property]"
        result.append(text.replace("~", "~0").replace("/", "~1"))
    return ("/" + "/".join(result))[:1024] if result else ""


def _index_schema(value, root, parts, ctx):
    if isinstance(value, dict):
        ctx.schema_locations[id(value)] = (root, _pointer(parts))
        ctx.safe_keys.update(value.get("properties", {}))
        for key, child in value.items():
            _index_schema(child, root, (*parts, key), ctx)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            _index_schema(child, root, (*parts, i), ctx)


def _validate_shape(subject, root_id, ctx):
    """Compose the unchanged S3 resources and project format checker."""
    try:
        if ctx.registry is None:
            ctx.registry = build_registry()
            for record in CATALOG:
                _index_schema(ctx.registry.contents(record.schema_id),
                              record.schema_id, (), ctx)
        validator = Draft202012Validator({"$ref": root_id},
            registry=ctx.registry, format_checker=build_format_checker())
        errors = tuple(validator.iter_errors(subject))
    except Exception:
        ctx.unavailable("VALIDATOR.STRUCTURED_ERRORS", profile="structural-validator")
        return False
    for error in errors:
        ctx.failed = True
        schema_id, pointer = ctx.schema_locations.get(id(error.schema), (root_id, ""))
        ctx.diagnostics.append(StaticDiagnostic(
            "S4.VALIDATOR.STRUCTURED_ERRORS", ctx.subject_id,
            _pointer(error.absolute_path, ctx.safe_keys), "structural",
            "The supplied value does not satisfy the selected structural constraint.",
            schema_id, pointer, str(error.validator)))
    return not errors


def _proof_binding(ctx, operation, bound_operands):
    return (operation, ctx.root_id, SCHEMA_SET_REVISION,
            id(ctx.subject), tuple(id(v) for v in bound_operands))


def _require_proof(ctx, operation, bound_operands):
    """Consume an opaque producer-validated handle, or retain an obligation."""
    provider = ctx.proof_context
    if type(provider) is _ProofContext:
        try:
            handle = getattr(provider, operation)(*bound_operands)
            value = provider._validate_handle(handle, operation, bound_operands)
            if value is not None:
                ctx.proofs.append((operation, bound_operands, handle))
                return value
        except Exception:
            pass
    ctx.unavailable(ctx.requirement_id, ctx.location, ctx.proof_profile,
                    _proof_binding(ctx, operation, bound_operands),
                    direct=False)
    return None


def _proof(ctx, requirement, operation, operands, location="", profile="dependency"):
    ctx.requirement_id, ctx.location, ctx.proof_profile = requirement, location, profile
    return _require_proof(ctx, operation, operands)


def _increasing(values, key):
    keys = [key(value) for value in values]
    return all(a < b for a, b in zip(keys, keys[1:]))


def _finish_result(validation_scope, ctx):
    # Re-check every consumed handle at the last boundary. A changed input or
    # snapshot cannot retain acceptance from an earlier proof in this call.
    for operation, operands, handle in ctx.proofs:
        try:
            current = ctx.proof_context._validate_handle(handle, operation, operands)
        except Exception:
            current = None
        if current is None:
            ctx.unavailable("PROOF.INPUT", profile="proof-continuity",
                binding=_proof_binding(ctx, "require_input_provenance",
                    (ctx.subject, ctx.root_id, SCHEMA_SET_REVISION)), direct=False)
    diagnostics = tuple(sorted(set(ctx.diagnostics), key=lambda d: tuple(
        _s(value or "") for value in (d.instance_pointer, d.schema_id,
        d.schema_pointer, d.keyword, d.code, d.subject_id))))
    obligations = tuple(sorted(set(ctx.required_proofs), key=lambda p: (
        _s(p.instance_pointer), _s(p.requirement_id), _s(p.profile),
        _s(p.subject_id or ""))))
    status = "INVALID" if ctx.failed else "PROOF_REQUIRED" if obligations or ctx.unevaluated else "PASS"
    direct = False if ctx.failed else None if ctx.unevaluated else True
    return StaticValidationResult(status, validation_scope, diagnostics,
                                  obligations, direct, status == "PASS")


def _root(name):
    return get_resource(name + ".schema.json").schema_id


def _check_canonical_arrays(subject, root_id, ctx):
    """Apply the frozen 54-row matrix to shaped values without sorting them."""
    def check_array(values, row, key, path, unique=None):
        valid = _increasing(values, key)
        if unique is not None:
            identities = [unique(v) for v in values]
            valid = valid and len(set(identities)) == len(identities)
        ctx.check(f"ARRAY.{row:02d}", valid, _pointer(path), "canonical-arrays")

    def remotes(values, row, path):
        location = _pointer(path)
        duplicate = any(a == b for i, a in enumerate(values) for b in values[:i])
        ctx.check(f"ARRAY.{row:02d}", not duplicate, location, "canonical-arrays")
        if duplicate:
            return
        for i in range(1, len(values)):
            relation = _proof(ctx, f"ARRAY.{row:02d}", "require_canonical_comparison",
                (values[i - 1], "complete-remote", values[i], "complete-remote",
                 "unsigned-jcs-byte-order"), location, "PROOF.REMOTE_ORDER")
            if relation is None:
                ctx.unevaluated = True
            else:
                ctx.check(f"ARRAY.{row:02d}", type(relation) is int and relation < 0,
                          location, "canonical-arrays")

    def walk(value, path=(), kind=None, post_type=None):
        if not isinstance(value, dict):
            return
        kind = value.get("kind", kind)
        parent = path[-1] if path else ""
        for field, child in value.items():
            at = (*path, field)
            if isinstance(child, list):
                row, key, unique = None, _s, None
                if field == "acceptedRemotes":
                    remotes(child, 24 if "remoteExpectations" in path else 1, at)
                elif field == "namespace":
                    # ARRAY.02 preserves significant position and repetition.
                    pass
                elif parent == "permissions":
                    row = {"modes": 3, "permittedCapabilities": 4,
                           "prohibitedCapabilities": 5}.get(field)
                elif parent in ("scope", "authorizedScope", "prohibitedScope"):
                    row = ({"capabilities": 6, "paths": 7}[field]
                           if parent == "scope" else 29 if parent == "authorizedScope" else 30)
                elif field == "domainRefs":
                    row = (20 if parent == "domainSet" else 43 if parent == "resolvedTarget"
                           else 28 if kind == "TaskContract" else 8)
                    key = _reference_key
                elif field in ("worktreeRoleRefs", "overlapRefs", "ownedDomainRefs", "excludedDomainRefs"):
                    row = {"worktreeRoleRefs": 9, "overlapRefs": 12,
                           "ownedDomainRefs": 13, "excludedDomainRefs": 14}[field]
                    key = _reference_key
                elif parent in ("pathScope", "pathCeiling"):
                    row = (10 if field == "include" else 11) if parent == "pathScope" else (26 if field == "include" else 27)
                elif parent in ("allowed", "denied") and field in ("exact", "prefixes"):
                    row = (15 if field == "exact" else 16) if parent == "allowed" else (17 if field == "exact" else 18)
                elif field == "rules":
                    row, key, unique = 19, lambda r: (-r["priority"], _s(r["id"])), lambda r: _s(r["id"])
                elif field == "bindings":
                    row, key = 21, lambda b: (_reference_key(b["roleRef"]), _s(b["worktreeId"]))
                elif field == "remoteNames":
                    row = 22
                elif field == "remoteExpectations":
                    row, key = 23, lambda r: _s(r["remoteName"])
                elif field == "capabilityCeiling":
                    row = 25
                elif field == "entries":
                    dimension = parent if parent != "expected" else {
                        "index-state": "index", "tracked-state": "tracked",
                        "submodule-state": "submodules"}.get(post_type)
                    row = ({"index": 31, "tracked": 32, "submodules": 35} if post_type is None
                           else {"index": 38, "tracked": 39, "submodules": 42}).get(dimension)
                    key = lambda entry: _s(entry["path"])
                elif field == "paths":
                    dimension = parent if parent != "expected" else {
                        "untracked-state": "untracked", "ignored-state": "ignored"}.get(post_type)
                    row = ({"untracked": 33, "ignored": 34} if post_type is None
                           else {"untracked": 40, "ignored": 41}).get(dimension)
                elif field == "permittedTransitions":
                    row, key = 36, _transition_key
                elif field == "requiredPostconditions":
                    row, key = 37, lambda entry: _s(entry["type"])
                elif field == "reasonCodes":
                    row = (44 if parent == "preContractEvidence" else 47 if "checks" in path
                           else 51 if kind == "ExecutionReceipt" else 52)
                elif field in ("checks", "unresolvedCoordinationWarnings"):
                    sequence_row = 46 if field == "checks" else 45
                    ctx.check(f"ARRAY.{sequence_row:02d}",
                              all(v["sequence"] == i for i, v in enumerate(child)),
                              _pointer(at), "canonical-arrays")
                    if field == "checks":
                        ids = [v["checkId"] for v in child]
                        ctx.check("ARRAY.46", len(set(ids)) == len(ids), _pointer(at), "canonical-arrays")
                elif field == "changedPaths":
                    row = 48
                elif field == "ordinaryOperationEvidence":
                    row, key = 49, lambda entry: _s(entry["path"])
                elif field == "operations" and "ordinaryOperationEvidence" in path:
                    row = 50
                elif field in ("domains", "worktreeRoles"):
                    row = 53 if field == "domains" else 54
                    key = lambda resource: _s(resource["metadata"]["id"])
                if row is not None:
                    check_array(child, row, key, at, unique)
                for i, item in enumerate(child):
                    selected_post = item["type"] if field == "requiredPostconditions" else post_type
                    walk(item, (*at, i), kind, selected_post)
            elif isinstance(child, dict):
                walk(child, at, kind, post_type)
    walk(subject)
