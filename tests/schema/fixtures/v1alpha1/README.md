# Synthetic v1alpha1 fixture corpus

This directory is the persistent S5 fixture corpus for `contextctl.dev/v1alpha1`.
All fixtures are conspicuously synthetic test assets. No fixture grants operational
authority, proves that an event occurred, or constitutes a production receipt.
Schema acceptance and static acceptance are not authorization, and a correct digest
does not establish event truth.

`manifest.json` uses inventory format version 2. It separates executable or
explicitly deferred case rows from non-executable coverage-obligation records.
The corpus contains 138 physical assets: 135 case-pack assets and three
`coverage-obligation-pack` assets. Together with this README and the manifest,
the corpus contains 140 paths.

The manifest has 2,166 case rows: 516 `ACCEPT`, 1,535 `REJECT`, and 115
`DEFERRED`. Their inventory dispositions are 1,566 `DIRECT_SCHEMA`, 485
`DIRECT_STATIC`, and 115 `DEFERRED`; the direct executable total is 2,051.
Fourteen additional `TRACE_ONLY` observations are retained for their approved
later operational owners, producing the corrected inventory total of 2,180:

```text
1566 DIRECT_SCHEMA + 485 DIRECT_STATIC = 2051 DIRECT_TOTAL
2051 DIRECT_TOTAL + 14 TRACE_ONLY + 115 DEFERRED = 2180 TOTAL
```

The two SG-001 aggregate matrix packs contain 50 non-executable obligations, not
cases. Forty-two are `COVERAGE_LEDGER_OPEN` Phase-1 coverage gaps and remain
OPEN; eight are `FUTURE_MODEL_OBLIGATION` records. None is automatically
satisfied by the existence of an aggregate row, and the eight future-model
obligations are not part of the 115 deferred case identities.

The runtime-structure pack contains exactly 14 non-authorizing `TRACE_ONLY`
observations owned by Phase 3 live validation, with later Phase-4 evidence use.
It does not claim Phase-1 validation execution or operational authority. Generic
Phase-1 active-operation and administrative-lock shape coverage remains OPEN
through SG-001 rows 06 and 07.

Model-owned vectors remain expectations only. S5 does not implement the strict
decoder, canonical representation, RFC 8785 JCS, hashing, replay, or the
cross-runtime model. S5 also does not implement Phase-2 routing, Phase-3 live
Git or lease checks, or Phase-4 trusted issuance and receipt generation.
Executable conformance belongs to S6 or to the explicitly assigned future owner.

Physical assets and logical cases are separate: one deterministic asset may
carry multiple non-additive cases. Raw decoder and exact-golden assets preserve
their bytes and must not be normalized. Case-row `expectedDisposition` remains
`ACCEPT`, `REJECT`, or `DEFERRED`; `inventoryDisposition` records whether the row
is `DIRECT_SCHEMA`, `DIRECT_STATIC`, or `DEFERRED`.

The former values 2,115 and 2,230 are withdrawn as, respectively, an executable
acceptance count and a corrected case-inventory count. They are retained only as
historical withdrawn claims in manifest v2.

Historical S5 integration provenance is preserved:

```text
schemaSetRevision:
v1alpha1-r1

design:
docs/schema-contract-v1alpha1.md

design blob:
c77bbc39da8a631918bde5cf4041659ddada8998

implementation baseline:
3619ce3f21731241ccec6b989452e57da2f14e12

post-integration correction source:
44b41272b56ebadb4ddb557e23593c22f6b0c2b9
```
