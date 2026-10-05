"""S3 composition, all 54 ordering rows and immutable supplied values."""

from copy import deepcopy
from dataclasses import FrozenInstanceError
import inspect

import pytest

from contextctl_schema import _static_core as core
from contextctl_schema import static_validation as api
from tests.schema.s4_synthetic import proofs, bundle, context, codes, reference, resource


def array_cases():
    strings = ["a", "b"]
    refs = [reference("Domain", v) for v in strings]
    cases = {}
    def add(row, path, values=strings, kind=None):
        obj = {"kind": kind} if kind else {}
        node = obj
        for key in path[:-1]:
            node = node.setdefault(key, {})
        node[path[-1]] = deepcopy(values)
        cases[row] = obj, path
    for row, field in ((3, "modes"), (4, "permittedCapabilities"), (5, "prohibitedCapabilities")):
        add(row, ("permissions", field))
    for row, path in ((6, ("scope", "capabilities")), (7, ("scope", "paths")),
        (10, ("pathScope", "include")), (11, ("pathScope", "exclude")),
        (15, ("allowed", "exact")), (16, ("allowed", "prefixes")),
        (17, ("denied", "exact")), (18, ("denied", "prefixes")),
        (22, ("remoteNames",)), (25, ("capabilityCeiling",)),
        (26, ("pathCeiling", "include")), (27, ("pathCeiling", "exclude")),
        (29, ("authorizedScope", "paths")), (30, ("prohibitedScope", "paths")),
        (33, ("untracked", "paths")), (34, ("ignored", "paths")),
        (44, ("preContractEvidence", "reasonCodes")), (48, ("changedPaths",)),
        (51, ("reasonCodes",)), (52, ("delivery", "reasonCodes"))):
        add(row, path, kind="ExecutionReceipt" if row == 51 else None)
    for row, field in ((8, "domainRefs"), (9, "worktreeRoleRefs"), (12, "overlapRefs"),
                       (13, "ownedDomainRefs"), (14, "excludedDomainRefs")):
        add(row, (field,), refs)
    add(20, ("domainSet", "domainRefs"), refs)
    add(28, ("domainRefs",), refs, "TaskContract")
    add(43, ("resolvedTarget", "domainRefs"), refs)
    add(19, ("rules",), [{"id": "a", "priority": 2}, {"id": "b", "priority": 1}])
    add(21, ("bindings",), [{"roleRef": reference("WorktreeRole"), "worktreeId": v} for v in strings])
    add(23, ("remoteExpectations",), [{"remoteName": v} for v in strings])
    for row, dimension in ((31, "index"), (32, "tracked"), (35, "submodules")):
        add(row, (dimension, "entries"), [{"path": v} for v in strings])
    add(36, ("permittedTransitions",), [{"type": "untracked-path", "path": v} for v in strings])
    add(37, ("requiredPostconditions",), [{"type": v} for v in strings])
    for row, kind, field in ((38, "index-state", "entries"), (39, "tracked-state", "entries"),
        (40, "untracked-state", "paths"), (41, "ignored-state", "paths"), (42, "submodule-state", "entries")):
        vals = [{"path": v} for v in strings] if field == "entries" else strings
        cases[row] = {"requiredPostconditions": [{"type": kind, "expected": {field: deepcopy(vals)}}]}, ("requiredPostconditions", 0, "expected", field)
    add(45, ("unresolvedCoordinationWarnings",), [{"sequence": 0}, {"sequence": 1}])
    add(46, ("checks",), [{"sequence": 0, "checkId": "a"}, {"sequence": 1, "checkId": "b"}])
    cases[47] = {"checks": [{"sequence": 0, "checkId": "a", "reasonCodes": strings.copy()}]}, ("checks", 0, "reasonCodes")
    add(49, ("ordinaryOperationEvidence",), [{"path": v} for v in strings])
    cases[50] = {"ordinaryOperationEvidence": [{"path": "a", "operations": ["create", "delete"]}]}, ("ordinaryOperationEvidence", 0, "operations")
    for row, name in ((53, "domains"), (54, "worktreeRoles")):
        add(row, (name,), [{"metadata": {"id": v}} for v in strings])
    for row in (1, 24):
        remotes = [{"host": "a.invalid"}, {"host": "b.invalid"}]
        if row == 1:
            add(row, ("repositoryIdentity", "acceptedRemotes"), remotes)
        else:
            cases[row] = {"remoteExpectations": [{"remoteName": "a", "acceptedRemotes": remotes}]}, ("remoteExpectations", 0, "acceptedRemotes")
    add(2, ("namespace",), ["b", "a", "a"])
    return cases


@pytest.mark.parametrize("row", range(1, 55), ids=lambda n: f"ARRAY.{n:02d}")
def test_ordering_matrix(row, proofs):
    subject, path = array_cases()[row]
    original = deepcopy(subject)
    ctx = context(subject, proofs.context)
    core._check_canonical_arrays(subject, ctx.root_id, ctx)
    assert not ctx.failed and not ctx.required_proofs
    assert subject == original
    values = subject
    for key in path:
        values = values[key]
    if row == 2:
        return  # significant positional order and duplicates must be preserved
    values[:] = [deepcopy(values[0]), deepcopy(values[0])]
    ctx = context(subject, proofs.context)
    core._check_canonical_arrays(subject, ctx.root_id, ctx)
    assert f"S4.ARRAY.{row:02d}" in codes(ctx)


@pytest.mark.parametrize("a,b", [("a", "b"), ("\U00010000", "\ue000"), ("a", "aa")])
def test_utf16_order(a, b):
    assert core._compare_s(a, b) == -1
    assert core._compare_s(b, a) == 1
    assert core._compare_s(a, a) == 0


@pytest.mark.parametrize("kind", ["Project", "Domain", "WorktreeRole", "RoutingPolicy", "HostOverlay", "TaskContract", "ExecutionReceipt"])
def test_s3_guard_is_composed(kind, proofs):
    names = {"WorktreeRole": "worktree-role", "RoutingPolicy": "routing-policy", "HostOverlay": "host-overlay", "TaskContract": "task-contract", "ExecutionReceipt": "execution-receipt"}
    value = resource(kind)
    ctx = context(value, proofs.context, names.get(kind, kind.lower()))
    assert core._validate_shape(value, ctx.root_id, ctx)
    value["unexpected"] = "secret.example"
    assert not core._validate_shape(value, ctx.root_id, ctx)
    assert all("secret.example" not in d.message for d in ctx.diagnostics)


def test_no_repair_and_missing_trust(proofs):
    value = deepcopy(bundle())
    # Align the structural fixture's synthetic IDs with its existing references
    # so direct closed-bundle checks pass before missing proof is considered.
    for member in (value["project"], *value["domains"],
                   *value["worktreeRoles"], value["routingPolicy"]):
        member["metadata"]["id"] = reference(member["kind"])["id"]
    saved = deepcopy(value)
    result = api.validate_governance_bundle(value)
    assert result.status == "PROOF_REQUIRED"
    assert value == saved
    result = api.validate_governance_bundle(value, proof_context=proofs.context)
    assert result.status == "PASS"
    assert value == saved
    with pytest.raises(FrozenInstanceError):
        result.status = "PASS"
    with pytest.raises(TypeError):
        api.DEFAULT_PROOF_LIMITS["max_nfa_states"] = 1


def test_public_export_contract():
    assert len(api.__all__) == 10
    for name in api.__all__[4:]:
        assert inspect.signature(getattr(api, name)).parameters["proof_context"].kind == inspect.Parameter.KEYWORD_ONLY
