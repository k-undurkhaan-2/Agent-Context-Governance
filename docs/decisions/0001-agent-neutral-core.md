# ADR 0001: Agent-neutral core

- Status: Accepted

## Context

Agent Context Governance is intended to apply the same governance decisions across different execution products. Product-specific concepts in the core would couple authorization, routing, and verification to one agent interface and would make policy behavior vary by adapter.

Phase 0 documentation bootstrap is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and Models is current, but its implementation has not yet begun. The repository remains pre-operational. This decision defines future boundaries; it does not claim that a core library, control plane, CLI, or adapter exists.

## Decision

The core architecture MUST be agent-neutral.

The core MAY define product-independent models, decision rules, and abstract ports for:

- structured governance configuration;
- project and responsibility-domain resolution;
- worktree-role routing;
- host binding;
- live runtime and Git inspection;
- write-lease coordination;
- task-contract issuance;
- scope verification; and
- execution receipts.

The core MUST NOT import, embed, or depend on an agent product's SDK, prompt format, session model, filesystem conventions, or permission vocabulary. Core policy MUST be expressed in framework terms such as domain, role, worktree, mode, scope, contract, lease, and receipt.

Product integrations MUST be adapters outside the core. An adapter MAY translate a valid `TaskContract` into a product-specific invocation and MAY translate execution observations into the framework's evidence model. An adapter MUST NOT grant authority, widen a contract, replace live inspection, or treat its own instructions as normative governance.

A future Codex integration, if created, MUST follow this adapter boundary and MUST NOT introduce Codex-specific assumptions into the core.

## Consequences

- Governance policy and lifecycle semantics can be tested independently from any agent product.
- Each integration requires an explicit adapter and adapter-level validation.
- Product capabilities that have no safe agent-neutral representation remain unavailable until the core model deliberately supports them.
- Product-specific convenience MUST NOT bypass configuration authority, role ownership, live preflight, leases, or contract scope.
- The initial documentation MUST use agent-neutral language except when identifying an integration as an external or future adapter.

## Alternatives not selected

### Product-specific core

Embedding one agent product directly in the core was not selected because it would make that product's capabilities and defaults implicit policy.

### Policy implemented independently by each adapter

Duplicating routing and authorization logic in adapters was not selected because it would permit inconsistent decisions and weaken centralized fail-closed behavior.
