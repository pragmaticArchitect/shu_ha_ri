---
id: hdip-cla-0.1-a7-structural-json-jsonld-schemas
title: HDIP-CLA 0.1 A7 — Structural JSON / JSON-LD Schemas
sidebar_label: A7 — Structural JSON/JSON-LD Schemas
---

# HDIP-CLA 0.1 — A7 Structural JSON / JSON-LD Schemas

**Status:** COMPLETE — static schema checks, negative mutation fixtures and repository integrity verified.  
**Authority:** frozen M17 human-readable architecture; A1–A6 are downstream representations.  
**Dialect:** JSON Schema Draft 2020-12.  
**Scope:** artifact serialization only, **not** conformance certification.

## 1. Purpose and boundaries

A7 specifies structural shapes for the A1 identity registry, A2 relationship/traceability registry, A3 invariant/conformance catalogue, A5 IRI policy, A5 JSON-LD context, and A5 expanded canonical RDF graph serialization. It does not amend source artifacts or introduce architectural identities. It does not replace A6 SHACL, A8 lifecycle/contract schemas, A12 conformance execution, or authoritative semantic/Product/policy decisions.

## 2. Published structural schemas

All files are located under `/specs/hdip-cla/0.1/a7/`:

| Schema | Subject |
|---|---|
| `a1-architecture-elements.schema.json` | Canonical element-registry document and 209-item inventory |
| `a2-relationship-traceability.schema.json` | Relationship and traceability serialization; fixed source counts |
| `a3-invariant-conformance.schema.json` | Catalogue with 48 invariants and approved assessment modes |
| `a5-canonical-iri-policy.schema.json` | A5 IRI policy structure and canonical base |
| `a5-jsonld-context.schema.json` | JSON-LD context envelope with version/protection declarations |
| `a5-expanded-graph.schema.json` | Expanded JSON-LD node and object serialization, canonical resource IRI form |

`a7-schema-policy.json` states the scope, authority and explicit non-goals. These schemas are structural contracts for the frozen *current* serialized baselines; a future change of canonical count requires a governed version change, not an informal weakening of the schema.

## 3. Machine-checkability boundary

JSON Schema validity is not a positive M16 invariant result. In particular, a JSON object containing an authority reference does not establish that the authority approved it; a serializable policy does not prove policy enforcement; and a well-formed graph does not prove correctness of implementation or consequential decision authority. A6 SHACL remains the graph-constraint layer. Cross-document referential integrity, RDF-equivalence and content-hash preservation are validated separately from JSON Schema.

## 4. Fixture and reconciliation contract

Each canonical source is validated against the corresponding schema with Draft 2020-12. Six negative mutations each must fail. Referential checks compare A2 A1-scoped relationship endpoints and A3 invariant IDs against the actual A1 identity set. A7 must leave all A1–A6 artifact bytes unchanged except the executable programme document and sidebar navigation.

## 5. Further formalization

A8 may extend these structures to lifecycle, contracts and profiles only by preserving M17 source meaning and A1–A7 fidelity. No implicit default PASS, `CONDITIONALLY_CONFORMANT` outcome, ontology reinterpretation or Product-status inference is permitted.
