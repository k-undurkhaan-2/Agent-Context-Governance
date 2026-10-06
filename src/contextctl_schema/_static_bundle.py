"""Closed portable reference integrity; never match or route an actual task."""

from types import MappingProxyType

from ._static_core import _increasing, _proof, _reference_key, _s


def _resource_key(resource):
    return tuple(_s(value) for value in (resource["apiVersion"], resource["kind"], resource["metadata"]["id"]))


class _ClosedReferenceIndexes:
    def __init__(self, resources):
        self.by_ref = MappingProxyType(resources)

    def get(self, ref):
        return self.by_ref.get(_reference_key(ref))


def _closed_reference_indexes(bundle, ctx):
    resources = {}
    for resource in (bundle["project"], *bundle["domains"],
                     *bundle["worktreeRoles"], bundle["routingPolicy"]):
        key = _resource_key(resource)
        if not ctx.check("BUNDLE.IDS", key not in resources, "", "closed-bundle"):
            continue
        resources[key] = resource
    return _ClosedReferenceIndexes(resources)


def _check_bundle_references(bundle, indexes, ctx):
    project = bundle["project"]
    project_key = _resource_key(project)
    project_spec = project["spec"]
    for field in ("domainRefs", "worktreeRoleRefs"):
        for i, ref in enumerate(project_spec[field]):
            ctx.check("BUNDLE.REFERENCES", indexes.get(ref) is not None,
                      f"/project/spec/{field}/{i}", "closed-bundle")
    policy = bundle["routingPolicy"]
    ctx.check("BUNDLE.PROJECT_POLICY",
              _reference_key(project_spec["routingPolicyRef"]) == _resource_key(policy)
              and _reference_key(policy["spec"]["projectRef"]) == project_key,
              "/routingPolicy/spec/projectRef", "closed-bundle")
    for collection in ("domains", "worktreeRoles"):
        for i, resource in enumerate(bundle[collection]):
            spec = resource["spec"]
            ctx.check("BUNDLE.REFERENCES", _reference_key(spec["projectRef"]) == project_key,
                      f"/{collection}/{i}/spec/projectRef", "closed-bundle")
            fields = ("overlapRefs",) if collection == "domains" else ("ownedDomainRefs", "excludedDomainRefs")
            for field in fields:
                for j, ref in enumerate(spec[field]):
                    target = indexes.get(ref)
                    ctx.check("BUNDLE.REFERENCES", target is not None and target["kind"] == "Domain"
                              and _reference_key(target["spec"]["projectRef"]) == project_key,
                              f"/{collection}/{i}/spec/{field}/{j}", "closed-bundle")
            if collection == "worktreeRoles":
                owned = {_reference_key(ref) for ref in spec["ownedDomainRefs"]}
                excluded = {_reference_key(ref) for ref in spec["excludedDomainRefs"]}
                ctx.check("BUNDLE.ROLE_OWNERSHIP", not owned.intersection(excluded),
                          f"/{collection}/{i}/spec/ownedDomainRefs", "closed-bundle")
    for resource in (project, *bundle["domains"], *bundle["worktreeRoles"]):
        permissions = resource["spec"]["permissions"]
        ctx.check("BUNDLE.PERMISSIONS", not set(permissions["permittedCapabilities"]).intersection(
            permissions["prohibitedCapabilities"]), "", "closed-bundle")


def _check_overlap_symmetry(bundle, indexes, ctx):
    for i, domain in enumerate(bundle["domains"]):
        identity = _resource_key(domain)
        for j, ref in enumerate(domain["spec"]["overlapRefs"]):
            target = indexes.get(ref)
            if target is None:
                continue  # The unresolved reference owns this finding.
            reverse = {_reference_key(r) for r in target["spec"]["overlapRefs"]}
            ctx.check("BUNDLE.OVERLAP", _reference_key(ref) != identity and identity in reverse,
                      f"/domains/{i}/spec/overlapRefs/{j}", "closed-bundle")


def _check_rule_static_relations(bundle, indexes, ctx):
    rules = bundle["routingPolicy"]["spec"]["rules"]
    project_key = _resource_key(bundle["project"])
    ctx.check("ROUTING.RULE_IDS",
        len({rule["id"] for rule in rules}) == len(rules)
        and _increasing(rules, lambda r: (-r["priority"], _s(r["id"]))),
        "/routingPolicy/spec/rules", "routing-static")
    for i, rule in enumerate(rules):
        location = f"/routingPolicy/spec/rules/{i}"
        refs = rule["match"]["domainSet"]["domainRefs"]
        valid = _reference_key(rule["match"]["projectRef"]) == project_key
        valid = valid and all(indexes.get(ref) is not None and
            _reference_key(indexes.get(ref)["spec"]["projectRef"]) == project_key for ref in refs)
        decision = rule["decision"]
        if decision["type"] == "route":
            target = indexes.get(decision["worktreeRoleRef"])
            valid = valid and target is not None and _reference_key(target["spec"]["projectRef"]) == project_key
            if target is not None:
                owned = {_reference_key(r) for r in target["spec"]["ownedDomainRefs"]}
                valid = valid and all(_reference_key(ref) in owned for ref in refs)
        ctx.check("ROUTING.PROJECT", valid, location, "routing-static")
        for earlier in rules[:i]:
            duplicate = _proof(ctx, "PROOF.RULE_PROJECTION", "require_canonical_comparison",
                (earlier, "RuleProjection", rule, "RuleProjection", "jcs-equality"),
                location, "RuleProjection")
            if duplicate is None:
                ctx.unevaluated = True
                continue
            if duplicate == "equal":
                ctx.check("PROOF.RULE_PROJECTION", False, location, "duplicate-rule-projection")
                continue
            if duplicate != "unequal":
                ctx.unavailable("PROOF.RULE_PROJECTION", location, "RuleProjection")
                continue
            if rule["priority"] == earlier["priority"]:
                same_match = _proof(ctx, "PROOF.RULE_PROJECTION", "require_canonical_comparison",
                    (earlier, "MatchProjection", rule, "MatchProjection", "jcs-equality"),
                    location, "MatchProjection")
                if same_match is None:
                    ctx.unevaluated = True
                elif same_match not in ("equal", "unequal"):
                    ctx.unavailable("PROOF.RULE_PROJECTION", location, "MatchProjection")
                else:
                    ctx.check("PROOF.RULE_PROJECTION", same_match == "unequal",
                              location, "identical-match-projection")


def _branch_policy_contains(policy, supplied_branch):
    def matches(side):
        return supplied_branch in side["exact"] or any(
            supplied_branch == prefix or supplied_branch.startswith(prefix + "/")
            for prefix in side["prefixes"])
    return matches(policy["allowed"]) and not matches(policy["denied"])
