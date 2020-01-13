---
id: hdip-cla-0.1-a4-rdf-owl-architecture-graph
title: HDIP-CLA 0.1 A4 - RDF/OWL Architecture Graph
sidebar_label: A4 - RDF/OWL Architecture Graph
---

# HDIP-CLA 0.1 A4 — RDF/OWL Architecture Graph

**Status:** COMPLETE (structural RDF/OWL representation).  
**Authority:** Frozen M17 human-readable architecture (semantic precedence).  
**Input baselines:** A1 (209 element identities), A2 (32 typed relationships; 911 edges; 332 trace records), A3 (48 invariants and conformance vocabulary).  
**Primary graph:** `/specs/hdip-cla/0.1/a4/architecture-graph.ttl`

## Purpose and authority

A4 represents the frozen HDIP logical architecture as a navigable RDF graph with a conservative OWL vocabulary. It is a **projection of source assertions**, not an authority to redefine meaning. A1/A2/A3 remain source machine records; M17 human-readable architecture has semantic precedence.

## Model

- A1 registered elements are resources with stable source identifiers and source definitions.
- A2 relationship types are OWL object properties; A2 relationships are direct RDF edges **and** separately identified relationship assertion nodes retaining modality, scope and provenance.
- A2 external references remain separately scoped external resources. HIST:: compatibility terms remain historical resources. M04/RCF references remain derivation identifiers, not HDIP elements.
- A2 traceability records are individually identified nodes, not implicit identity or authority transfers.
- A3 invariants retain literal canonical conditions, assessment modes, ancestry, and governed-element references; controlled vocabulary tokens are represented without converting statements into automatic machine proofs.
- The graph's URNs are **provisional reversible identifiers** used only for A4 serialization. A5 owns canonical IRI rules and JSON-LD context.

## Safe semantics

`relationship != equivalence != authority transfer != transitive closure != runtime invocation`. The graph intentionally does **not** assert `owl:sameAs`, property transitivity, inverse inference, closed-world completeness, `owl:equivalentClass`, or domain/range inferences that could misclassify external authorities. Vocabulary representation does not create new semantic authority.

A4 does not claim to machine-prove `HYBRID` or `ASSESSMENT` invariants. It does not implement SHACL (A6), detailed schema constraints (A7/A8), or the conformance engine (A12).

## Files

| Artifact | Purpose |
|---|---|
| `architecture-graph.ttl` | Human-readable RDF Turtle graph / OWL declarations |
| `architecture-graph.nt` | N-Triples export for deterministic triple-level inspection |
| `provisional-resource-map.json` | Reversible URN namespaces, expressly subordinate to A5 |
| `a4-validation.json` | Cross-input referential and roundtrip checks |

## Graph validation

A4 validated **209 A1 resources**, **911 A2 relationship assertion records**, **332 A2 traceability assertion records**, **48 A3 canonical invariant conditions**, and **13727 RDF triples**. Turtle parse roundtrip succeeded.

## No redesign principle

Where any machine graph assertion conflicts with M17, the machine graph must be corrected. This stage adds **zero** canonical Planes, Overlays, ABBs, Registries, interactions, boundary families, patterns, flows, and invariants.
