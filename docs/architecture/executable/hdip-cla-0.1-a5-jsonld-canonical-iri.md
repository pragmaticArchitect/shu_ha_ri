---
id: hdip-cla-0.1-a5-jsonld-canonical-iri
title: HDIP-CLA 0.1 A5 - JSON-LD Context & Canonical IRI Model
sidebar_label: A5 - JSON-LD & Canonical IRIs
---

# HDIP-CLA 0.1 A5 — JSON-LD Context & Canonical IRI Model

**Status:** COMPLETE — serialization and identity projection.  
**Authority:** M17 frozen human-readable baseline; A1-A4 are machine representations.  
**Stable identity base:** `https://kivanura.org/specs/hdip-cla/0.1/id/` (logical canonical naming policy; HTTP hosting/dereferencing not verified).

## Scope

A5 fixes canonical HTTP(S) IRI naming and supplies a protected JSON-LD 1.1 context for A4 graph assertions. It exports the same source assertions as a canonical Turtle, N-Triples, and JSON-LD graph. **No architectural meaning is introduced or redefined.** Existing A4 provisional URNs are not overwritten in their original A4 files.

## IRI identity contract

Each A4 resource IRI is mapped bijectively to the corresponding A5 scope, preserving the original percent-encoded source identifier as a suffix. These scopes remain distinct: element, external-reference, derivation-reference, historical-term, relationship-assertion, traceability-assertion, relationship predicate, vocabulary, and ontology metadata. A2 relationship assertions remain both direct predicate edges and reified provenance nodes. Historical terms do not become canonical architecture elements.

The authority base is under the KivaNura domain for the HDIP-CLA published specification **only**. This is not a declaration that HDIP gains semantic, Product, Data, policy, external-standard, or consequential Decision authority. HTTP resolvability and domain publishing are deployment obligations, not silently assumed.

## JSON-LD context

`hdip-cla-context.jsonld` supplies scoped protected vocabulary prefixes, with `source`, `target`, `subject`, `relationshipType`, `governedElement`, `sourceInvariant` as IRI-typed properties. All other source literals remain literal; numeric-looking and version-looking identifiers are never coerced.

## Versioning and history

Version `0.1` remains part of the resource identity. Future governed revisions must preserve historical interpretability. Alias does not mean `owl:sameAs`. No transitivity, equivalence, inverse property, OWL restrictions or closed-world inference is invented by this stage. A4's provisional graph metadata is retained as a source historical note in the mapped graph; the active A5 IRI policy is recorded separately.

## Files

- `hdip-cla-context.jsonld` — protected JSON-LD 1.1 context
- `canonical-iri-policy.json` — namespace, identity, version, authority and publication governance
- `iri-migration-map.csv` — one-to-one A4 provisional to A5 canonical IRI scope mapping
- `canonical-architecture-graph.ttl` — canonical IRI Turtle graph
- `canonical-architecture-graph.nt` — canonical IRI N-Triples graph
- `canonical-architecture-graph.jsonld` — lossless expanded JSON-LD graph; companion protected A5 context published separately
- `a5-validation.json` — graph equivalence and regression evidence

## Boundaries

A5 does not implement SHACL A6, structural validation A7/A8, conformance runner A12, or web-hosting/redirect deployment. `STRUCTURAL`, `HYBRID`, and `ASSESSMENT` retain M16 meanings; RDF parsing is not architectural conformance proof.
