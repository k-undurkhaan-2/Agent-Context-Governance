# ADR 0003: Versioning model

- Status: Accepted

## Context

The distributable package and the public configuration API evolve for different reasons. Coupling their version numbers would make ordinary implementation releases appear to change policy syntax, or force configuration-version changes when no public configuration contract changed.

The project has not yet published a package release or finished a public schema. This decision establishes the versioning contract for future work.

## Decision

Product and package releases MUST use Semantic Versioning. The first planned package release is `0.1.0`; this documentation bootstrap MUST NOT be represented as an already published release.

Public configuration API versions MUST be independent from package versions. The initial configuration API identifier is:

```text
contextctl.dev/v1alpha1
```

Future schema files for that API MUST live under `schemas/v1alpha1/`. Schema implementation is planned for Phase 1 and MUST NOT be added during Phase 0.

The following rules apply:

- A package release MAY add fixes or implementation features without changing the configuration API identifier when it remains compatible with that API.
- A configuration API change MUST be evaluated and named according to its own compatibility boundary; it MUST NOT be inferred from the package version.
- Implementations MUST validate the declared configuration API version and MUST reject missing, malformed, ambiguous, or unsupported versions.
- Implementations MUST NOT guess a version from file location, package version, field shape, Markdown, or prior successful execution.
- Support for multiple API versions, when introduced, MUST be explicit. Conversion or migration MUST be deliberate and MUST NOT silently reinterpret policy.
- Because `v1alpha1` is an alpha API, incompatible schema changes may still be necessary. Such changes MUST be documented and accompanied by explicit validation and migration handling; the alpha label does not permit silent semantic changes.

Package compatibility describes the distributed implementation. Configuration API compatibility describes the machine-readable governance contract. Documentation MUST state which boundary it discusses.

## Consequences

- Package delivery can proceed without manufacturing configuration API revisions.
- Configuration authors can identify the policy contract without interpreting package release numbers.
- A package MUST explicitly declare which configuration API versions it supports.
- Schema directories can coexist when future API versions require parallel validation or migration.
- Release notes and compatibility documentation will need to report package and configuration API support separately.

## Alternatives not selected

### One shared version number

Using a package version as the configuration API version was not selected because code releases and policy-contract changes have different compatibility lifecycles.

### Unversioned configuration

Inferring configuration semantics from fields or filenames was not selected because it makes validation ambiguous and prevents deterministic compatibility handling.
