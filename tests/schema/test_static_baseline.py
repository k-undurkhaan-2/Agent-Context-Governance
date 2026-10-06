"""Complete supplied baseline relationships and ordinary-operation projection."""

from copy import deepcopy
from types import MappingProxyType
import pytest
from contextctl_schema._static_baseline import (
    _check_baseline_consistency, _ordinary_operation_set, _apply_simultaneous_transitions,
    _baseline_target_value, _project_final_conditions, _MaterializedBaselineView,
)
from contextctl_schema.static_validation import validate_task_contract_static
from tests.schema.s4_synthetic import proofs, context, codes, contract_bundle, reference, OID, DIGEST


def _inventory_context(b, o, proofs):
    marker = object()
    proofs.snapshots[o["spec"]["hostId"], id(marker)] = (((o, b),), ())
    return marker


def explicit_baseline():
    b, o, c = contract_bundle()
    base = c["spec"]["expectedBaseline"]
    base["index"] = {"state": "exact", "entries": [{"path": "synthetic/file", "mode": "100644", "objectId": deepcopy(OID)}]}
    base["tracked"] = {"state": "exact", "entries": [{"path": "synthetic/file", "status": "modified", "indexMode": "100644", "indexObjectId": deepcopy(OID), "worktreeMode": "100644", "contentDigest": DIGEST}]}
    return c


@pytest.mark.parametrize("fault,code", [(None, None), ("mode", "BASE.TRACKED_INDEX"), ("object", "BASE.TRACKED_INDEX"), ("coverage", "BASE.COVERAGE"), ("duplicate", "BASE.PATH_IDENTITIES"), ("untracked", "BASE.DISJOINT"), ("ignored", "BASE.DISJOINT"), ("clean", "BASE.TRACKED_EXACT"), ("gitlink", "BASE.SUBMODULE_INDEX")])
def test_explicit_cross_dimensions(fault, code):
    c = explicit_baseline()
    base = c["spec"]["expectedBaseline"]
    entry = base["tracked"]["entries"][0]
    if fault == "mode":
        entry["indexMode"] = "100755"
    elif fault == "object":
        entry["indexObjectId"]["value"] = "b" * 40
    elif fault == "coverage":
        entry["path"] = "synthetic/other"
    elif fault == "duplicate":
        base["index"]["entries"].append(deepcopy(base["index"]["entries"][0]))
    elif fault in ("untracked", "ignored"):
        base[fault] = {"state": "exact", "paths": ["synthetic/file"]}
    elif fault == "clean":
        entry["status"] = "clean"
    elif fault == "gitlink":
        base["index"]["entries"][0]["mode"] = "160000"
    ctx = context(c)
    _check_baseline_consistency(base, None, ctx)
    if code:
        assert "S4." + code in codes(ctx)
    else:
        assert not ctx.failed


@pytest.mark.parametrize("before,after,expected", [({}, {}, set()), ({}, {"a": None}, {"create"}), ({"a": None}, {}, {"delete"}), ({"a": None}, {"a": None}, {"modify"}), ({"a": ("100644", "x")}, {"a": ("100644", "x")}, set()), ({"a": ("100644", "x")}, {"a": ("100755", "x")}, {"modify"}), ({"a": None}, {"b": None}, {"create", "delete"})])
def test_ordinary_operation_projection(before, after, expected):
    assert _ordinary_operation_set(before, after, context()) == expected


def test_simultaneous_composition_preserves_input(proofs):
    _, _, c = contract_bundle(True)
    materialized = proofs.baseline(c)
    transitions = [{"type": "untracked-path", "path": "synthetic/file", "from": "absent", "to": "present"}]
    ctx = context(c)
    assert _baseline_target_value(materialized, transitions[0], ctx) == "absent"
    result = _apply_simultaneous_transitions(materialized, transitions, ctx)
    assert result.values["untracked"] == ("synthetic/file",)
    assert materialized.values["untracked"] == ()
    final = _project_final_conditions(result, ctx)
    assert final["untracked"] == {"state": "exact", "paths": ["synthetic/file"]}
    assert final["head"] == c["spec"]["expectedBaseline"]["head"]

    def coherent_case(status="clean"):
        b, o, c = contract_bundle(True)
        for resource in (b["project"], *b["domains"], *b["worktreeRoles"], b["routingPolicy"]):
            resource["metadata"]["id"] = reference(resource["kind"])["id"]
        index = {"path": "synthetic/file", "stage": 0, "mode": "100644", "objectId": deepcopy(OID),
                 "intentToAdd": False, "skipWorktree": False, "assumeUnchanged": False}
        tracked = {"path": "synthetic/file", "status": status, "indexMode": "100644", "indexObjectId": deepcopy(OID)}
        baseline = c["spec"]["expectedBaseline"]
        if status == "clean":
            baseline["head"] = {"state": "commit", "objectId": deepcopy(OID)}
            head_entries = (deepcopy(index),)
        else:
            tracked.update(worktreeMode="100644", contentDigest=DIGEST)
            baseline["index"] = {"state": "exact", "entries": [index]}
            baseline["tracked"] = {"state": "exact", "entries": [tracked]}
            b["worktreeRoles"][0]["spec"]["cleanlinessPolicy"].update(index="contract-enumerated", tracked="contract-enumerated")
            head_entries = ()
        initial = proofs.baseline(c)
        view = _MaterializedBaselineView(c, MappingProxyType(dict(initial.values, index=(index,), tracked=(tracked,))),
            head_entries, MappingProxyType({}), MappingProxyType({("synthetic/file", id(tracked)): ("100644", DIGEST)}))
        proofs.materializations[id(c)] = view
        return b, o, c, view, index, tracked

    # S4-INDEPENDENT-001: each contradiction starts from its own coherent copy
    # of the same semantic baseline and changes only the final index target.
    for variant in ("object-id", "mode", "remove-index-path"):
        b, o, c, view, index, tracked = coherent_case()
        control = validate_task_contract_static(c, bundle=b, host_overlay=o,
            inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
        assert control.status == "PASS" and control.full_static_acceptance, control
        assert _project_final_conditions(view, context(c))["tracked"] == {"state": "clean"}
        replacement = deepcopy(index)
        if variant == "object-id":
            replacement["objectId"]["value"] = "b" * 40
        elif variant == "mode":
            replacement["mode"] = "100755"
        removed = variant == "remove-index-path"
        c["spec"]["permittedTransitions"] = [{"type": "index-entry", "path": index["path"],
            "from": {"state": "present", "value": {k: v for k, v in index.items() if k != "path"}},
            "to": {"state": "absent"} if removed else {"state": "present", "value": {k: v for k, v in replacement.items() if k != "path"}}}]
        c["spec"]["requiredPostconditions"] = [
            {"type": "index-state", "expected": {"state": "exact", "entries": [] if removed else [replacement]}},
            {"type": "lease-state", "expected": "owned"}, {"type": "scope-contained"},
            {"type": "tracked-state", "expected": {"state": "clean"}}]
        before = deepcopy(c)
        final_view = _apply_simultaneous_transitions(view, c["spec"]["permittedTransitions"], context(c))
        assert final_view.values["tracked"] == (tracked,)
        assert final_view.values["index"] == (() if removed else (replacement,))
        assert all(final_view.values[key] == view.values[key] for key in view.values if key != "index")
        result = validate_task_contract_static(c, bundle=b, host_overlay=o,
            inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
        assert result.status == "INVALID" and not result.full_static_acceptance, (variant, result)
        assert codes(result) == {"S4.BASE.TRACKED_INDEX"} | ({"S4.BASE.COVERAGE"} if removed else set())
        assert all(d.instance_pointer == "/spec/expectedBaseline/tracked" and d.predicate_family == "baseline"
                   for d in result.diagnostics)
        assert c == before and view.values["index"] == (index,) and view.values["tracked"] == (tracked,)

    # Matching explicit inventories still pass, and a coherent tracked-entry
    # transition can still collapse modified records to canonical tracked.clean.
    b, o, c, view, index, tracked = coherent_case("modified")
    exact = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
    assert exact.status == "PASS" and exact.full_static_acceptance, exact
    clean = {k: v for k, v in tracked.items() if k not in ("worktreeMode", "contentDigest")}
    clean["status"] = "clean"
    c["spec"]["permittedTransitions"] = [{"type": "tracked-entry", "path": tracked["path"],
        "from": {"state": "present", "value": {k: v for k, v in tracked.items() if k != "path"}},
        "to": {"state": "present", "value": {k: v for k, v in clean.items() if k != "path"}}}]
    c["spec"]["requiredPostconditions"].append({"type": "tracked-state", "expected": {"state": "clean"}})
    before = deepcopy(c)
    clean_final = _apply_simultaneous_transitions(view, c["spec"]["permittedTransitions"], context(c))
    assert _project_final_conditions(clean_final, context(c))["tracked"] == {"state": "clean"}
    collapsed = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
    assert collapsed.status == "PASS" and collapsed.full_static_acceptance, collapsed
    assert c == before and view.values["tracked"] == (tracked,)


@pytest.mark.parametrize("operations,locks,valid", [(["merge", "rebase"], [], True), (["rebase", "merge"], [], False), ([], [{"type": "index"}, {"type": "index"}], False)])
def test_reusable_observation_order(operations, locks, valid):
    _, _, c = contract_bundle()
    base = c["spec"]["expectedBaseline"]
    base["activeOperations"] = {"operations": operations}
    base["administrativeLocks"] = {"locks": locks}
    ctx = context(c)
    _check_baseline_consistency(base, None, ctx)
    assert (not ctx.failed) is valid
