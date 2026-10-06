"""Supplied contract relationships and static transition composition."""

from ._static_baseline import (
    _TARGET_DIMENSION, _apply_simultaneous_transitions, _baseline_target_value,
    _check_baseline_consistency, _ordinary_operation_set, _ordinary_projection,
    _project_final_conditions,
)
from ._static_bundle import _branch_policy_contains, _closed_reference_indexes, _resource_key
from ._static_core import _increasing, _proof, _reference_key, _root, _s, _transition_key, _validate_shape
from ._static_overlay import _remote_key
from ._static_paths import _closed_path_membership, _prove_scope_subset


_POST_DIMENSIONS = {"ref-state": "ref", "head-state": "head", "index-state": "index",
    "tracked-state": "tracked", "untracked-state": "untracked", "ignored-state": "ignored",
    "submodule-state": "submodules", "active-operations": "activeOperations",
    "administrative-locks": "administrativeLocks"}


def _check_contract_bindings(contract, bundle, host_overlay, ctx):
    spec, overlay = contract["spec"], host_overlay["spec"]
    indexes = _closed_reference_indexes(bundle, ctx)
    project = bundle["project"]
    target = spec["target"]
    role = indexes.get(target["worktreeRoleRef"])
    domains = [indexes.get(ref) for ref in spec["domainRefs"]]
    declared = {_reference_key(ref) for ref in project["spec"]["domainRefs"]}
    matching = [binding for binding in overlay["bindings"]
                if binding["worktreeId"] == target["worktreeId"]
                and binding["roleRef"] == target["worktreeRoleRef"]]
    valid = (_reference_key(spec["projectRef"]) == _resource_key(project)
             and spec["projectRef"] == overlay["projectRef"] and role is not None
             and all(domain is not None for domain in domains) and len(matching) == 1
             and all(_reference_key(ref) in declared for ref in spec["domainRefs"]))
    if not ctx.check("CONTRACT.UPSTREAM", valid, "/spec/target", "contract-binding"):
        return
    owned = {_reference_key(ref) for ref in role["spec"]["ownedDomainRefs"]}
    ctx.check("CONTRACT.UPSTREAM", all(_reference_key(ref) in owned for ref in spec["domainRefs"])
              and role["spec"]["projectRef"] == spec["projectRef"]
              and all(domain["spec"]["projectRef"] == spec["projectRef"] for domain in domains),
              "/spec/domainRefs", "contract-binding")
    policies = [resource["spec"]["permissions"] for resource in (project, role, *domains)]
    capabilities = set(spec["authorizedScope"]["capabilities"])
    for policy in policies:
        ctx.check("CONTRACT.UPSTREAM", spec["effectiveMode"] in policy["modes"]
                  and capabilities <= set(policy["permittedCapabilities"])
                  and not capabilities.intersection(policy["prohibitedCapabilities"]),
                  "/spec/authorizedScope/capabilities", "contract-binding")
    ctx.check("CONTRACT.UPSTREAM", capabilities <= set(overlay["capabilityCeiling"]),
              "/spec/authorizedScope/capabilities", "contract-binding")
    remote_set = {_remote_key(remote) for remote in overlay["repositoryIdentity"]["acceptedRemotes"]}
    ctx.check("CONTRACT.UPSTREAM", all(_remote_key(remote) in remote_set for remote in
              spec["repositoryIdentity"]["acceptedRemotes"]), "/spec/repositoryIdentity", "contract-binding")
    baseline = spec["expectedBaseline"]
    ref = baseline["ref"]
    ctx.check("CONTRACT.UPSTREAM", ref == matching[0]["expectedRef"],
              "/spec/expectedBaseline/ref", "contract-binding")
    ctx.check("BRANCH.STATIC", ref["state"] == "branch" and
              _branch_policy_contains(role["spec"]["branchPolicy"], ref.get("branchRef", "")),
              "/spec/expectedBaseline/ref", "branch-policy")
    for dimension, rule in role["spec"]["cleanlinessPolicy"].items():
        if rule != "contract-enumerated":
            ctx.check("CONTRACT.UPSTREAM", baseline[dimension]["state"] == rule,
                      "/spec/expectedBaseline/" + dimension, "contract-binding")
    ctx.path_requirement = "CONTRACT.UPSTREAM"
    ctx.location = "/spec/authorizedScope/paths"
    scope = {"include": spec["authorizedScope"]["paths"], "exclude": []}
    _prove_scope_subset(scope, [domain["spec"]["pathScope"] for domain in domains], ctx.limits, ctx)
    _prove_scope_subset(scope, [overlay["pathCeiling"]], ctx.limits, ctx)
    del ctx.path_requirement


def _check_contract_plan(contract, materialized_baseline, limits, ctx):
    spec = contract["spec"]
    transitions = spec["permittedTransitions"]
    authorized, prohibited = spec["authorizedScope"], spec["prohibitedScope"]
    ctx.check("CONTRACT.SCOPE_DISJOINT", all(not set(authorized[field]).intersection(prohibited[field])
              for field in ("paths", "capabilities")), "/spec/authorizedScope", "contract-scope")
    ctx.check("CONTRACT.TARGETS", _increasing(transitions, _transition_key)
              and all(t["from"] != t["to"] for t in transitions),
              "/spec/permittedTransitions", "contract-transitions")
    posts = spec["requiredPostconditions"]
    ctx.check("CONTRACT.POST_UNIQUE", _increasing(posts, lambda p: _s(p["type"]))
              and sum(p["type"] == "scope-contained" for p in posts) == 1,
              "/spec/requiredPostconditions", "contract-postconditions")
    from_valid = True
    for i, transition in enumerate(transitions):
        location = f"/spec/permittedTransitions/{i}"
        ctx.location = location + "/path"
        for requirement, scope, expected in (("TA01", authorized, True), ("TA02", prohibited, False)):
            membership = _closed_path_membership(transition["path"], {"include": scope["paths"], "exclude": []}, limits, ctx)
            if membership is not None:
                ctx.check(requirement, membership is expected, ctx.location, "transition-path")
        if materialized_baseline is None:
            from_valid = False
            continue
        source = _baseline_target_value(materialized_baseline, transition, ctx)
        if not ctx.check("CONTRACT.APPLY", source == transition["from"], location + "/from", "transition-baseline"):
            from_valid = False
            continue
        relation = _proof(ctx, "PROOF.TRANSITION_JCS", "require_canonical_comparison",
            (transition["from"], "complete-value", source, "baseline-target", "jcs-equality"),
            location + "/from", "exact-transition-from")
        if relation is None:
            ctx.unevaluated = True
            from_valid = False
        else:
            from_valid = ctx.check("PROOF.TRANSITION_JCS", relation == "equal", location + "/from", "transition-baseline") and from_valid
    if materialized_baseline is None or not from_valid:
        _check_contract_postconditions(contract, spec["expectedBaseline"], None, ctx)
        return None
    final_view = _apply_simultaneous_transitions(materialized_baseline, transitions, ctx)
    final = _project_final_conditions(final_view, ctx)
    before = len(ctx.diagnostics)
    if _validate_shape(final, _root("task-contract") + "#/$defs/expectedBaseline", ctx):
        _check_baseline_consistency(final, final_view, ctx)
    else:
        ctx.check("CONTRACT.FINAL", False, "/spec/permittedTransitions", "final-composite")
    if len(ctx.diagnostics) == before:
        operations = (_ordinary_operation_set(_ordinary_projection(materialized_baseline),
                      _ordinary_projection(final_view), ctx) if spec["allowWrite"] else frozenset())
        _check_required_plan_capabilities(contract, operations, ctx)
        _check_contract_postconditions(contract, spec["expectedBaseline"], final, ctx)
        return final_view
    return None


def _check_required_plan_capabilities(contract, ordinary_operations, ctx):
    spec = contract["spec"]
    index_required = any(t["type"] == "index-entry" for t in spec["permittedTransitions"])
    required = set(ordinary_operations) | ({"git-stage"} if index_required else set())
    authorized, prohibited = set(spec["authorizedScope"]["capabilities"]), set(spec["prohibitedScope"]["capabilities"])
    ctx.check("TA03", not index_required or "git-stage" in authorized,
              "/spec/authorizedScope/capabilities", "plan-capabilities")
    ctx.check("CONTRACT.REQUIRED_CAPS", required <= authorized and not required.intersection(prohibited),
              "/spec/authorizedScope/capabilities", "plan-capabilities")


def _check_contract_postconditions(contract, baseline, final_conditions, ctx):
    spec = contract["spec"]
    changed = {_TARGET_DIMENSION[t["type"]] for t in spec["permittedTransitions"]}
    posts = {post["type"]: post for post in spec["requiredPostconditions"]}
    for post_type, dimension in _POST_DIMENSIONS.items():
        if dimension in changed:
            ctx.check("CONTRACT.POST_FINAL", post_type in posts,
                      "/spec/requiredPostconditions", "contract-postconditions")
        if post_type not in posts:
            continue
        expected = final_conditions[dimension] if final_conditions is not None else baseline[dimension] if dimension not in changed else None
        if expected is not None:
            ctx.check("CONTRACT.POST_FINAL", posts[post_type]["expected"] == expected,
                      "/spec/requiredPostconditions", "contract-postconditions")
