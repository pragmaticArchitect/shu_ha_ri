---
title: P01 Stage 4 - Information Product Artifact Authority Boundaries
sidebar_label: P01-S04 - Artifact Boundaries
---

# Information-native artifacts and the BPS Digital Product Passport

> **APPROVED ARCHITECTURAL RESEARCH DIRECTION, NOT ADOPTED ARTIFACT SCHEMAS.** G03-D01 was approved as amended to prefer **INFOPROD** and **INFOPDS** as Information-native specifications. G03-D04/D09 preserve **BPS DPP cross-family applicability**. G03-D08 preserves **HPD** as an HDIP operational projection.

## Four independently governed artifact responsibilities

| Artifact | Governing question | Authority boundary |
|---|---|---|
| **INFOPROD** | What governed informational value does this Product Version promise, and which authoritative meanings constitute that Promise? | Information-specific semantic descriptor; refer to BPS/PIN, GEARM and adopted INFOPS classification rather than redefining them. |
| **INFOPDS** | How may this qualified Information Product Version be realized and provided through eligible mechanisms? | Realization/deployment contract; may bind dependencies and architecture Profiles but cannot confer intrinsic Family. |
| **BPS DPP with future Information Profile** | What attributable, current and verifiable evidence or trust assertions apply to the exact Product subject/Version? | Cross-family passport Core remains under BPS; Information extension specializes trust/evidence, not Product ontology. |
| **HDIP Product Descriptor (HPD)** | What authoritative Product/Version and runtime context does HDIP project to coordinate discovery, binding, observability and lifecycle? | Platform-owned operational projection; never Product qualification, INFOPROD, INFOPDS or the DPP. |

## Authority lattice

```text
BPS/PIN Productness and PIN + GEARM Information meaning
                |                
                v                
  future INFOPS family qualification
                |
        qualified Product Version
                |
     +----------+-------------+
     |          |             |
  INFOPROD   INFOPDS     BPS DPP Core
  semantic    realization     |
  reference    contract       + Information DPP Profile
     |          |             |
     +----------+-------------+
                |
       HDIP HPD projection (where applicable)
                |
        eligible PFI realization
```

This is an **authority/evidence sketch**, not a mandatory chronological process. DPP evidence or INFOPDS realization may reference INFOPROD, Product and dependency versions without introducing mandatory one-to-one cardinalities. HDIP usage is not necessary to constitute an Information Product.

## Accepted boundaries and non-equivalences

- `INFOPROD != INFOPDS`: semantic governing intent/Promise is distinct from deployable realization.
- `INFOPROD != HPD`: authoritative Product-family semantic descriptor is not the HDIP operational projection.
- `BPS DPP != HPD`: verifiable Passport assertions and lifecycle are distinct from discovery/operational metadata.
- `DPP != INFOPROD != INFOPDS`: trust attestation does not replace semantics or deployment obligations.
- `DPP valid != Product qualified`: signature and integrity cannot prove semantic truth, sufficiency of qualification evidence, fitness, or entitlement.
- `INFOPDS deployment pass != BPS Productness or INFOPS qualification`: technical realization cannot manufacture intrinsic nature.
- `AIPS AIPROD/AIPDS precedent != adoption of AI concepts`: INFOPS adopts the *separation of concerns*, not AIPS AI-specific qualification predicates.
- `Open Data Mesh DPDS != INFOPDS`: ODM DPDS means Data Product **Descriptor** Specification; no name collision may create a false Information deployment dependency.

## Exact subjects and history

A Product, Product Version, semantic descriptor Version, deployment specification Version, passport issuance/subject, information occurrence and HDIP projection have distinct identity and currentness concerns. A newer passport or a changed runtime does not automatically create a new Product Version; a changed governing information definition may require reassessment even if output values remain identical. No universal cardinality, passport issuance gate, or exact schema field set is adopted in G03.

## Digital Product Passport applicability

The BPS DPP Core provides cross-family identity, issuance, issuer, integrity and trust/evidence conventions. A future Information-specific Profile may attest to INFOPS qualification provenance, GEARM semantic reference Versions, applicable interpretation/limitations, Data/AI dependencies, governance and assurance evidence. It must not impose a universal model, active analytics engine, real-time API or specific publication format.

A dependent AI Product's or Data Product's Passport concerns a different Product subject. Trust/evidence references may cross Product boundaries; **family membership, issuer identity and authority do not transfer transitively**.

A mandatory DPP at Product release/distribution time, if established by applicable BPS/Product governance, is an independent lifecycle obligation, not an extra intrinsic Information-family predicate. Canonical BPS DPP namespace and source Version must be verified before a normative Information DPP Profile is issued.

## Future specification work

INFOPROD, INFOPDS and the Information DPP Profile are **proposed specifications only** as of 19 October 2026. Their fields, JSON-LD vocabularies, SHACL Shapes, JSON Schemas, examples, Profiles, validation and publication need independent adoption. Information Product Characteristics (INFOPCH), PMDD maturity, independent conformance and consequential-action authorization must remain separate from intrinsic family assessment.
