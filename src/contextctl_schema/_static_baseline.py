"""Closed baseline consistency and simultaneous state projection only."""

from dataclasses import dataclass
from types import MappingProxyType

from ._static_core import _increasing, _lock_key, _proof, _s


_DIMENSIONS = ("ref", "head", "index", "tracked", "untracked", "ignored",
               "submodules", "activeOperations", "administrativeLocks")
_TARGET_DIMENSION = {"index-entry": "index", "tracked-entry": "tracked",
                     "untracked-path": "untracked", "ignored-path": "ignored"}


@dataclass(frozen=True, slots=True)
class _MaterializedBaselineView:
    """Private proof payload view, not a governance resource or producer."""
    contract: object
    values: object
    head_entries: tuple
    leaf_kinds: object
    ordinary_identities: object


def _check_baseline_consistency(baseline, supplied_materialization, ctx):
    index, tracked, submodules = (baseline[key] for key in ("index", "tracked", "submodules"))
    # Clean wire branches are tentative projections, not permission to discard
    # the supplied inventories. Consume their repeated fields and coverage with
    # the same predicates before confirming the canonical branches below.
    entry_lists = {key: (supplied_materialization.values[key] if supplied_materialization is not None
                        else baseline[key].get("entries", ()))
                   for key in ("index", "tracked", "submodules")}
    inventories = {key: {entry["path"]: entry for entry in entries}
                   for key, entries in entry_lists.items()}
    for key in inventories:
        entries = entry_lists[key]
        ctx.check("BASE.PATH_IDENTITIES", len(inventories[key]) == len(entries)
                  and _increasing(entries, lambda e: _s(e["path"])),
                  f"/spec/expectedBaseline/{key}", "baseline")
    if tracked["state"] == "exact":
        ctx.check("BASE.TRACKED_EXACT", bool(tracked["entries"])
                  and any(entry["status"] != "clean" for entry in tracked["entries"]),
                  "/spec/expectedBaseline/tracked", "baseline")
    if supplied_materialization is not None or index["state"] == "exact":
        regular = {path: entry for path, entry in inventories["index"].items() if entry["mode"] != "160000"}
        gitlinks = {path: entry for path, entry in inventories["index"].items() if entry["mode"] == "160000"}
        if supplied_materialization is not None or tracked["state"] == "exact":
            for path, entry in inventories["tracked"].items():
                peer = regular.get(path)
                ctx.check("BASE.TRACKED_INDEX", peer is not None
                          and entry["indexMode"] == peer["mode"]
                          and entry["indexObjectId"] == peer["objectId"],
                          "/spec/expectedBaseline/tracked", "baseline")
            ctx.check("BASE.COVERAGE", set(regular) == set(inventories["tracked"]),
                      "/spec/expectedBaseline/tracked", "baseline")
        ctx.check("BASE.SUBMODULE_INDEX", set(gitlinks) == set(inventories["submodules"])
                  and all(entry["recordedObjectId"] == gitlinks[path]["objectId"]
                          for path, entry in inventories["submodules"].items() if path in gitlinks)
                  and ((submodules["state"] == "none") == (not gitlinks)),
                  "/spec/expectedBaseline/submodules", "baseline")
        ctx.check("BASE.COVERAGE", not set(inventories["tracked"]).intersection(inventories["submodules"]),
                  "/spec/expectedBaseline", "baseline")
    sets = {key: set(inventories[key]) for key in inventories}
    sets.update({key: set(supplied_materialization.values[key] if supplied_materialization is not None
                          else baseline[key].get("paths", ())) for key in ("untracked", "ignored")})
    explicit_tracked = sets["index"] | sets["tracked"] | sets["submodules"]
    ctx.check("BASE.DISJOINT", not sets["untracked"].intersection(sets["ignored"])
              and not (sets["untracked"] | sets["ignored"]).intersection(explicit_tracked)
              and not sets["tracked"].intersection(sets["submodules"]),
              "/spec/expectedBaseline", "baseline")
    if supplied_materialization is not None:
        view = supplied_materialization
        projected = _project_final_conditions(view, ctx)
        ctx.check("BASE.CANONICAL", all(baseline[key] == projected[key] for key in _DIMENSIONS),
                  "/spec/expectedBaseline", "baseline")
        for path in sets["untracked"] | sets["ignored"]:
            kind = view.leaf_kinds.get(path)
            if kind is None:
                ctx.unavailable("PROOF.DIRECTORY_CLASS", "/spec/expectedBaseline", "leaf-only-inventory")
            else:
                ctx.check("PROOF.DIRECTORY_CLASS", kind in ("100644", "100755", "120000"),
                          "/spec/expectedBaseline", "baseline-leaf-kind")
    elif baseline["head"]["state"] == "unborn" and index["state"] == "exact":
        ctx.check("BASE.CANONICAL", bool(index["entries"]), "/spec/expectedBaseline/index", "baseline")
    operations = baseline["activeOperations"].get("operations", ())
    locks = baseline["administrativeLocks"].get("locks", ())
    ctx.check("BASE.OBSERVATIONS", _increasing(operations, _s) and _increasing(locks, _lock_key),
              "/spec/expectedBaseline", "observation-order")


def _consume_materialized_baseline(contract, baseline_context, ctx):
    """No observation, fallback inventory, inferred HEAD or new trust source."""
    view = _proof(ctx, "PROOF.BASELINE", "require_baseline_materialization",
                  (contract, _DIMENSIONS), "/spec/expectedBaseline", "complete-baseline-materialization")
    if (not isinstance(view, _MaterializedBaselineView) or view.contract is not contract
            or (baseline_context is not None and view is not baseline_context)
            or set(view.values) != set(_DIMENSIONS)):
        if view is not None:
            ctx.unavailable("PROOF.BASELINE", "/spec/expectedBaseline", "complete-baseline-materialization")
        ctx.unevaluated = True
        return None
    return view


def _baseline_target_value(materialized, transition_target, ctx):
    dimension = _TARGET_DIMENSION.get(transition_target["type"])
    if dimension is None:
        ctx.check("CONTRACT.TARGETS", False, "/spec/permittedTransitions", "transition-shape")
        return None
    path = transition_target["path"]
    values = materialized.values[dimension]
    if dimension in ("untracked", "ignored"):
        return "present" if path in values else "absent"
    entry = next((entry for entry in values if entry["path"] == path), None)
    return ({"state": "absent"} if entry is None else
            {"state": "present", "value": {key: value for key, value in entry.items() if key != "path"}})


def _apply_simultaneous_transitions(materialized, transitions, ctx):
    # Fresh derived containers preserve every original value. They are static
    # projections, not codec/canonical representations and never rewrite input.
    values = dict(materialized.values)
    records = {dimension: {entry["path"]: entry for entry in values[dimension]}
               for dimension in ("index", "tracked")}
    paths = {dimension: set(values[dimension]) for dimension in ("untracked", "ignored")}
    for transition in transitions:
        dimension = _TARGET_DIMENSION[transition["type"]]
        path, target = transition["path"], transition["to"]
        if dimension in records:
            if target["state"] == "absent":
                records[dimension].pop(path, None)
            else:
                records[dimension][path] = {"path": path, **target["value"]}
        elif target == "present":
            paths[dimension].add(path)
        else:
            paths[dimension].discard(path)
    # Ordering a derived projection is required by Apply's representation. No
    # supplied array is sorted, repaired or accepted because of this ordering.
    for dimension, entries in records.items():
        values[dimension] = tuple(entries[path] for path in sorted(entries, key=_s))
    for dimension, inventory in paths.items():
        values[dimension] = tuple(sorted(inventory, key=_s))
    return _MaterializedBaselineView(materialized.contract, MappingProxyType(values),
                                    materialized.head_entries, materialized.leaf_kinds,
                                    materialized.ordinary_identities)


def _project_final_conditions(materialized_final, ctx):
    values = materialized_final.values
    result = {key: values[key] for key in ("ref", "head", "activeOperations", "administrativeLocks")}
    index = list(values["index"])
    result["index"] = {"state": "clean"} if index == list(materialized_final.head_entries) else {"state": "exact", "entries": index}
    tracked = list(values["tracked"])
    result["tracked"] = ({"state": "clean"} if all(entry["status"] == "clean" for entry in tracked)
                         else {"state": "exact", "entries": tracked})
    for dimension in ("untracked", "ignored"):
        inventory = list(values[dimension])
        result[dimension] = {"state": "exact", "paths": inventory} if inventory else {"state": "none"}
    submodules = list(values["submodules"])
    result["submodules"] = {"state": "exact", "entries": submodules} if submodules else {"state": "none"}
    return result


def _ordinary_projection(view):
    result = {}
    for entry in view.values["tracked"]:
        if entry["status"] == "deleted":
            continue
        if entry["status"] in ("modified", "type-changed"):
            identity = (entry["worktreeMode"], entry["contentDigest"])
        else:
            # A supplied trusted identity may include the checkout/filter
            # information absent from clean wire values. Never invent it.
            identity = view.ordinary_identities.get((entry["path"], id(entry)))
        result[entry["path"]] = identity
    for path in (*view.values["untracked"], *view.values["ignored"]):
        result[path] = None
    return result


def _ordinary_operation_set(baseline_paths, final_paths, ctx):
    operations = set()
    for path in set(baseline_paths) | set(final_paths):
        if path not in baseline_paths:
            operations.add("create")
        elif path not in final_paths:
            operations.add("delete")
        elif (baseline_paths[path] is None or final_paths[path] is None
              or baseline_paths[path] != final_paths[path]):
            operations.add("modify")
    return frozenset(operations)
