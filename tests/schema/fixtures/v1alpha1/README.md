# Synthetic v1alpha1 fixture corpus

This directory is the persistent S5 fixture corpus for `contextctl.dev/v1alpha1`.
All fixtures are conspicuously synthetic test assets. No fixture grants operational
authority, no fixture is evidence that an event occurred, and no fixture is a
production receipt. Schema acceptance is not authorization. Static acceptance is
not authorization. A mathematically correct digest is neither event truth nor
authority.

Model-owned vectors are retained as expectations only. S5 does not implement the
strict decoder, canonical representation, RFC 8785 JCS, hashing, replay, or the
cross-runtime model. S5 also does not implement Phase-2 routing, Phase-3 live Git
or lease checks, or Phase-4 trusted issuance and receipt generation. Executable
corpus conformance belongs to S6 or to the explicitly assigned future owner.

The authoritative inventory is `manifest.json`. Physical assets and logical cases
are separate: one deterministic asset may carry multiple non-additive cases. Raw
decoder and exact-golden assets preserve their bytes and must not be normalized.
The `expectedDisposition` and `expectedStage` fields state the assigned owner; a
future-owner `DEFERRED` row must never be promoted merely because its JSON shape
validates.

```text
schemaSetRevision:
v1alpha1-r1

design:
docs/schema-contract-v1alpha1.md

design blob:
c77bbc39da8a631918bde5cf4041659ddada8998

implementation baseline:
3619ce3f21731241ccec6b989452e57da2f14e12
```
