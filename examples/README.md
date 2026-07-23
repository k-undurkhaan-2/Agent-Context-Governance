# Example data requirements

No examples are provided in the documentation-bootstrap phase. Future examples MUST be safe to publish and MUST demonstrate concepts without reproducing an actual environment.

Every example MUST use synthetic repository names, personal and service identities, branches, paths, commit references, remotes, and secret placeholders. Values SHOULD be conspicuously fictional and non-operational. Secret placeholders MUST NOT resemble usable credentials, and examples MUST NOT contain credential-bearing URLs.

Before an example is committed, its author MUST remove or replace customer names, usernames, hostnames, filesystem layouts, repository topology, infrastructure identifiers, incidents, deployment data, and other environment-derived metadata. Examples MUST NOT copy details from any real source project or customer infrastructure.

Examples MAY illustrate restrictive governance decisions and denial paths. Repository documentation MAY contain only conspicuously synthetic, non-authoritative receipt-shaped examples. Such examples are not generated `ExecutionReceipt` records, runtime evidence, or authorization input.

Concrete `HostOverlay`, `TaskContract`, and generated `ExecutionReceipt` instances, runtime state, live leases, Git or lease-store locks, real secrets, and evidence that could identify a host MUST NOT be placed in the target worktree. Generated receipts are host-local runtime evidence and MUST remain outside portable governance.
