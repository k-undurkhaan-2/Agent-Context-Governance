# Planned `contextctl` package boundaries

This directory is reserved for a future Python package. No Python modules, packaging metadata, command-line executable, or operational framework behavior exists in this bootstrap phase.

The planned package boundaries are:

- **Models and decoding:** typed representations of public configuration objects and strict input decoding.
- **Validation:** schema-independent semantic checks and cross-object invariants.
- **Resolution and routing:** deterministic project and domain resolution followed by worktree-role selection.
- **Runtime inspection:** live, read-only observation of repository, worktree, branch, HEAD, dirty-state, and active-operation state.
- **Leases:** acquisition, revalidation, and release of exclusive runtime write leases.
- **Contracts:** issuance and verification of bounded Task Contracts.
- **Scope verification:** comparison of observed changes with the contract's permitted scope.
- **Receipts:** generation of execution evidence that MUST NOT be accepted as authorization input.
- **Adapter interfaces:** narrow boundaries through which future agent-specific integrations MAY invoke the agent-neutral core.
- **Application orchestration:** a future command-line layer that composes the boundaries above without embedding policy in presentation code.

Dependencies SHOULD point inward toward models and policy rules. The core MUST remain independent of any particular agent product. Runtime inspection and persistence SHOULD be isolated behind explicit interfaces so deterministic policy logic can be tested without a live repository.

The default authorization state will be `mode: plan-only` with `allowWrite: false`. Customer governance MAY restrict permissions, and a local Host Overlay MAY restrict them further but MUST NOT widen them. A write operation will require both correct worktree role ownership and a valid runtime write lease; those are separate controls.

