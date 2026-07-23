# Example data requirements

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and no examples or fixtures exist yet.

## Phase 1 fixtures

Phase 1 Schema fixtures MUST be conspicuously synthetic positive and negative
examples owned by `schema-contracts`. They MUST exercise only the approved
Schema contract and Phase 1 structural or static configuration-integrity
boundary. Model fixtures and Schema/model conformance data begin later, in the
distinct `model-implementation` worktree, only after the approved Schema
baseline has been committed, reviewed, and integrated into `main`.

Every example or fixture MUST use synthetic repository names, personal and
service identities, branches, paths, commit references, remotes, and secret
placeholders. Values SHOULD be conspicuously fictional and non-operational.
Secret placeholders MUST NOT resemble usable credentials, and examples MUST
NOT contain credential-bearing URLs.

Before an example is committed, its author MUST remove or replace customer
names, usernames, hostnames, filesystem layouts, repository topology,
infrastructure identifiers, incidents, deployment data, and other
environment-derived metadata. Examples MUST NOT copy details from a real source
project or customer infrastructure.

Examples MAY illustrate restrictive governance decisions and denial paths.
Repository documentation MAY contain only conspicuously synthetic,
non-authoritative receipt-shaped examples. Such examples are not generated
`ExecutionReceipt` records, runtime evidence, or authorization input.

Concrete `HostOverlay`, `TaskContract`, and generated `ExecutionReceipt`
instances, concrete host-local or runtime configuration, live leases, Git or
lease-store locks, real secrets, and evidence that could identify a host MUST
NOT be placed in the target worktree. Generated receipts are host-local runtime
evidence and MUST remain outside portable governance.
