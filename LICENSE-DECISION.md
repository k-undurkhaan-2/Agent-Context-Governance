# License Decision Record

## Status

The final license for Agent Context Governance is intentionally undecided. This document records evaluation work that remains; it does not select, recommend, rank, or grant a license.

The repository MUST NOT add a license file or describe any project material as licensed under particular terms until the repository owner makes and records an explicit decision. This document is not a license and grants no permissions.

## Decision to be made

A later decision MUST define the terms under which source code, schemas, documentation, examples, tests, and other project artifacts may be used, modified, distributed, and contributed. It MUST also decide whether all artifact types use the same terms or require clearly identified, compatible terms.

The decision MUST be evaluated against evidence available when implementation and distribution plans are concrete. The current documentation-bootstrap phase does not provide enough information to resolve it.

## Evaluation dimensions

The later evaluation MUST consider at least:

- **Intended adoption:** who is expected to use the framework, in which environments, and whether broad interoperability or controlled redistribution is a project objective.
- **Use, modification, and redistribution rights:** which permissions recipients need for source and binary forms, derivative works, internal use, and redistribution.
- **Reciprocity obligations:** whether modifications or larger combined works would carry source-disclosure or licensing duties, and at what boundary those duties would apply.
- **Hosted and network use:** whether operating a modified version as a service should trigger obligations even without distributing a copy.
- **Commercial use and dual-licensing strategy:** whether commercial use, paid support, proprietary integration, exceptions, or parallel licensing models are intended.
- **Patent terms:** the scope of any express patent grant, patent-retaliation provisions, termination conditions, and the project's expected patent exposure.
- **Attribution and notices:** preservation requirements for copyright, notices, source offers, change notices, and documentation.
- **Warranty, liability, and security expectations:** disclaimer language, limitation of liability, and whether the terms fit software that influences authorization and execution decisions.
- **Trademark and project identity:** separation of copyright permissions from rights in names, marks, branding, and statements of endorsement.
- **Dependency and ecosystem compatibility:** compatibility with planned runtime dependencies, development tools, generated artifacts, packaging channels, and likely downstream projects.
- **Documentation, schemas, examples, and generated output:** whether non-code materials or generated outputs need distinct treatment and how mixed artifacts would be labeled.
- **Contribution model:** required inbound rights, contributor attestations, provenance, sign-off or agreement processes, and the ability to relicense later if needed.
- **Third-party material:** procedures for identifying, recording, and complying with dependencies, copied material, data, fonts, media, or generated content that has separate terms.
- **Jurisdiction and enforceability:** review of applicable law, organizational constraints, export or sanctions considerations where relevant, and the need for qualified legal advice.
- **Governance and change control:** who can approve the initial license, how exceptions are authorized, and whether future license changes require contributor or copyright-holder consent.
- **Operational burden:** the work needed to provide notices, source, attribution, compliance records, contributor records, and answers to downstream licensing questions.

These dimensions are questions for evaluation, not preferences for a license family or outcome.

## Evidence required before selection

Before selecting terms, the project SHOULD document its expected distribution model, contribution model, dependency inventory, artifact types, downstream integration patterns, commercial intentions, ownership of existing contributions, and responsible decision maker. Any legal assumptions SHOULD be reviewed by qualified counsel appropriate to the repository owner's circumstances.

Candidate terms MUST be compared against the same documented criteria. Compatibility claims MUST be checked against the actual dependency and distribution plan rather than assumed from a license label.

## Recording the future decision

When an explicit decision is made, it SHOULD be captured in a separate decision record that includes the chosen terms, scope, rationale, alternatives considered, compatibility analysis, approver, and effective date. The repository MAY then add the exact license text and consistent file headers or notices as required.

Until that happens, this record MUST remain neutral: it MUST NOT be interpreted as favoring a permissive, reciprocal, source-available, proprietary, dual, or other licensing model.
