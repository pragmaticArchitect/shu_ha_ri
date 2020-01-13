---
id: hdip-cla-0.1-a6-shacl-constraint-layer
title: HDIP-CLA 0.1 A6 — SHACL Constraint Layer
sidebar_label: A6 — SHACL Constraint Layer
---

# HDIP-CLA 0.1 — A6: SHACL Constraint Layer

**State:** A6 implemented (structural graph checks); independent full SHACL-engine execution not available in this build environment.  
**Governing authority:** Frozen M17 human-readable baseline; A1 identities, A2 edges, A3 invariant vocabulary, A4 graph and A5 canonical IRIs.

## Scope and authority

A6 adds five portable SHACL Core node shapes for specification-graph data quality: architecture elements, invariants, relationship assertions, traceability assertions and external references. These are **not** tests proving that a concrete HDIP implementation satisfies architectural invariants. A6 introduces no new semantic, Product, Data, policy, Decision, external or reference-architecture authority.

SHACL Core constraints use `sh:targetClass`, `sh:property`, `sh:path`, `sh:minCount`, `sh:maxCount`, `sh:datatype`, and `sh:nodeKind`. Neither inferencing nor `owl:sameAs` is required. The graph remains open-world for architecture semantics, although the shipped specification snapshot is reconciled with closed-inventory counts in a separate validation manifest.

## Invariant applicability and judgement

- **STRUCTURAL (7):** suitable only for specific demonstrably decidable structural checks; metadata presence alone never proves satisfaction.
- **HYBRID (37):** machine evidence may support but cannot replace accountable architecture assessment.
- **ASSESSMENT (4):** substantive accountable judgement is required.

No automatic `SATISFIED`, `CONFORMANT` or `CONDITIONALLY_CONFORMANT` claims are emitted by these shapes. `NOT_APPLICABLE` requires accepted scoped rationale; unassessed material obligations remain `INDETERMINATE`. A4/A5 graph validity is not conformance certification. Applicability, temporal claim identity and evidence acceptance belong to subsequent executable material and governed human assessments.

## Machine deliverables

- `/specs/hdip-cla/0.1/a6/architecture-structural-shapes.ttl` — portable SHACL Core shape declarations.
- `/specs/hdip-cla/0.1/a6/a6-constraint-policy.json` — scope, authority, and evaluation limitations.
- `/specs/hdip-cla/0.1/a6/fixture-positive.ttl` and three `fixture-negative-*.ttl` — targeted shape fixtures.
- `/specs/hdip-cla/0.1/a6/a6-validation.json` — source preservation, graph reconciliation and local limited-evaluator results.

## Evaluation scope and limits

The A6 checks exercised a local evaluator restricted to exactly the portable SHACL Core property constraints used in this A6 shapes file. It is **not** a complete standards-conformant SHACL engine. No independent `pySHACL`, Jena or RDF4J validation is claimed. Full engine cross-validation and broader positive/negative corpus are recommended for A10–A12. No Docusaurus build is claimed.

## Preservation

Predecessor A1–A5 files are unchanged. Repository programme status and sidebar are the only modified predecessor paths. The step overlay contains only added A6 artifacts and those two updates. M17 retains authority precedence over RDF shapes, JSON metadata and interpretation.
