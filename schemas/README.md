# Public configuration schemas

This directory is reserved for future public, machine-readable schemas. The repository is in its documentation-bootstrap phase, so it contains no schema files yet.

The initial public configuration API version will be `contextctl.dev/v1alpha1`. Its schemas will live under `schemas/v1alpha1/`. Configuration API versions MUST evolve independently of package release versions, which will use Semantic Versioning.

Schema definitions for all seven kinds—`Project`, `Domain`, `WorktreeRole`, `HostOverlay`, `RoutingPolicy`, `TaskContract`, and `ExecutionReceipt`—MAY later live here. Schema location does not determine concrete-instance trust or storage. Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Host-local and runtime instances MUST remain outside the target worktree, and generated receipts MUST never become portable governance.

Machine-readable structured customer governance will be authoritative for portable policy. Markdown MAY explain or mirror that configuration, but it MUST NOT independently grant authority.

## Planned validation behavior

Future schema processing MUST:

- reject unknown fields;
- reject missing required fields, invalid types, and unsupported API versions;
- apply strict format and value constraints; and
- fail closed when configuration is malformed, ambiguous, stale, or mismatched.

JSON Schema validation alone will not be sufficient. Semantic validation MUST also enforce cross-object references and invariants. Task resolution MUST produce exactly one `Project` and a non-empty deterministic `Domain` set; exactly one selected `WorktreeRole` MUST own every `Domain` in that set; and a `TaskContract` MUST bind the same set. `RoutingPolicy` consumes the already-resolved project and complete domain set to select the one covering role; it does not resolve or discover them. Permission bounds and expected repository state also require semantic validation. A `HostOverlay` MAY further restrict customer governance but MUST NOT widen it. Runtime Git state MUST be inspected live rather than inferred from configuration.

See the [configuration model](../docs/configuration-model.md) for the planned objects and trust boundaries.
