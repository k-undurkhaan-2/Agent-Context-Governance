"""Individual narrowing and complete-snapshot union checks; no host I/O."""

from ._static_bundle import _resource_key
from ._static_core import _proof, _reference_key
from ._static_paths import _prove_scope_subset


def _remote_key(remote):
    return (remote["transport"], remote["host"],
            remote.get("port", 443 if remote["transport"] == "https" else 22),
            tuple(remote["namespace"]), remote["repository"])


def _check_overlay_individual(overlay, bundle, indexes, limits, ctx):
    spec, project = overlay["spec"], bundle["project"]
    project_spec = project["spec"]
    project_key = _resource_key(project)
    ctx.check("D10.project-mismatch", _reference_key(spec["projectRef"]) == project_key,
              "/spec/projectRef", "overlay-narrowing")
    declared_roles = {_reference_key(ref) for ref in project_spec["worktreeRoleRefs"]}
    project_remotes = {_remote_key(remote) for remote in project_spec["repositoryIdentity"]["acceptedRemotes"]}
    ctx.check("D10.repository-widening", all(_remote_key(remote) in project_remotes
              for remote in spec["repositoryIdentity"]["acceptedRemotes"]),
              "/spec/repositoryIdentity/acceptedRemotes", "overlay-narrowing")
    expectations = {}
    for i, expectation in enumerate(spec["remoteExpectations"]):
        name = expectation["remoteName"]
        ctx.check("REMOTE.NAME", name not in expectations,
                  f"/spec/remoteExpectations/{i}/remoteName", "remote-identity")
        expectations.setdefault(name, []).append(expectation)
        ctx.check("D10.remote-widening", all(_remote_key(remote) in project_remotes
                  for remote in expectation["acceptedRemotes"]),
                  f"/spec/remoteExpectations/{i}/acceptedRemotes", "overlay-narrowing")
    for i, binding in enumerate(spec["bindings"]):
        location = f"/spec/bindings/{i}"
        key = _reference_key(binding["roleRef"])
        ctx.check("D10.role-not-in-project", key in declared_roles, location + "/roleRef", "overlay-narrowing")
        role = indexes.get(binding["roleRef"])
        if role is None:
            ctx.check("D10.role-project-mismatch", False, location + "/roleRef", "overlay-narrowing")
        else:
            role_spec = role["spec"]
            ctx.check("D10.role-project-mismatch", _reference_key(role_spec["projectRef"]) == project_key,
                      location + "/roleRef", "overlay-narrowing")
            pp, pr = project_spec["permissions"], role_spec["permissions"]
            ceiling = (set(pp["permittedCapabilities"]) & set(pr["permittedCapabilities"])) - (
                set(pp["prohibitedCapabilities"]) | set(pr["prohibitedCapabilities"]))
            ctx.check("D10.capability-widening", set(spec["capabilityCeiling"]) <= ceiling,
                      "/spec/capabilityCeiling", "overlay-narrowing")
        for j, name in enumerate(binding["remoteNames"]):
            candidates = expectations.get(name, ())
            ctx.check("D10.remote-unresolved", len(candidates) == 1 and bool(candidates[0]["acceptedRemotes"]),
                      location + f"/remoteNames/{j}", "overlay-narrowing")
    scopes = []
    for ref in project_spec["domainRefs"]:
        domain = indexes.get(ref)
        if domain is None:
            ctx.unevaluated = True
            return
        scopes.append(domain["spec"]["pathScope"])
    ctx.location = "/spec/pathCeiling"
    _prove_scope_subset(spec["pathCeiling"], scopes, limits, ctx)


def _consume_complete_host_inventory(host_id, inventory_context, ctx):
    """Request the exact checkpoint-bound, producer-validated snapshot."""
    return _proof(ctx, "PROOF.SNAPSHOT", "require_complete_host_snapshot",
                  (host_id, inventory_context), "", "trusted-complete-host-snapshot")


def _exact_absolute_root_relation(left, right):
    if left["platform"] != right["platform"]:
        return "unrelated"
    a, b = left["value"], right["value"]
    if a == b:
        return "equal"
    separator = "/" if left["platform"] == "posix" else "\\"
    prefix = b if b.endswith(separator) else b + separator
    return "descendant" if a.startswith(prefix) else "unrelated"


def _check_same_host_union(validated_members, supplied_coordination_roots, ctx):
    """Call only after every exact snapshot member passes individual validation."""
    bindings = []
    worktrees, roots = set(), set()
    for overlay in validated_members:
        for binding in overlay["spec"]["bindings"]:
            root = binding["repositoryRoot"]
            root_key = root["platform"], root["value"]
            ctx.check("HX.A1", binding["worktreeId"] not in worktrees, "/spec/bindings", "same-host-union")
            ctx.check("HX.A2", root_key not in roots, "/spec/bindings", "same-host-union")
            worktrees.add(binding["worktreeId"])
            roots.add(root_key)
            bindings.append(root)
    for kind, root in supplied_coordination_roots:
        equal_requirement, descendant_requirement = ("HX.B1", "HX.B2") if kind == "stateRoot" else ("HX.B3", "HX.B4")
        for binding_root in bindings:
            relation = _exact_absolute_root_relation(root, binding_root)
            ctx.check(equal_requirement, relation != "equal", "/spec/" + kind, "same-host-roots")
            ctx.check(descendant_requirement, relation != "descendant", "/spec/" + kind, "same-host-roots")
