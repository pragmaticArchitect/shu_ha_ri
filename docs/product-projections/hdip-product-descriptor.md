---
id: hdip-product-descriptor
title: HDIP Product Descriptor (HPD)
sidebar_label: HDIP© Product Descriptor
---

# 1. Introduction

The **HDIP© Product Descriptor (HPD)** is a platform-generated HDIP artifact that projects authoritative Data Product and Product Version information into a computable form used for **discovery, coordination, dependency and impact analysis, governance, usage, observability, and lifecycle operations** within the **Holistic Data, Information and Intelligence Platform (HDIP)**.

HPD is additive to the canonical Product and Data Product specifications. It does **not** determine whether something is a Product, does **not** establish Product Family or family-specific intrinsic classifications, and does **not** replace the authoritative Product or Data Product semantic models.

HPD enables:

- Platform coordination and orchestration (including DPFI)
- Product discovery and experience (CEP)
- Consumer Observability & Value (COVP)
- Dependency and impact analysis
- Governance and policy-context evaluation
- Usage and observability projection
- Graph-based querying, reasoning, and analysis capabilities

---

# 2. Positioning in HDIP

HPD is **not a replacement** for DPROD or DPDS.

It exists as a **separate, additive operational projection**:

```text
DPROD
  -> governed Data Product semantic descriptor

DPDS
  -> deployment / realization specification

HPD
  -> HDIP operational Product projection for discovery,
     coordination, governance, dependency, usage,
     observability and lifecycle
```

HPD references authoritative semantics; it does not re-author them.

---

# 3. Design Principles

### 3.1 Non-invasive
HPD does **not modify or redefine DPROD, DPDS, BPS/PIN, or applicable Data Product semantics**.

### 3.2 Referential
Relationships and classifications are represented through **URI/IRI-based references** to authoritative resources wherever those resources exist.

### 3.3 Ontology-driven
HPD is compatible with RDF/OWL and JSON-LD representations, while remaining independent of a particular graph database or storage technology.

### 3.4 Computable
HPD is machine-readable for:

- Platform coordination and orchestration (including DPFI)
- Product discovery and experience (CEP)
- Consumer Observability & Value (COVP)
- Dependency and impact analysis
- Governance and policy-context evaluation
- Graph-based querying, reasoning, and analysis capabilities

### 3.5 Projection-ready
HPD supports multiple governed views and representations, including UI, API, registry/catalog, document, and graph projections.

### 3.6 Authority-preserving
HPD **projects** authoritative Product identity, Product Version, classification, ownership, dependency, provenance, governance, and lifecycle information. Projection does not transfer semantic or governance authority to HPD.

---

# 4. Referencing Contract Alignment

HPD follows the **HDIP Referencing Contract**:

- HPD, Products, Product Versions, classifications, dependencies, owners, providers, and related resources are represented through stable identifiers / IRIs where available.
- Product classification is **referenced from authoritative Product semantics** rather than recreated as an HPD-local taxonomy.
- Product Family, Product Kind, and family-specific Intrinsic Type remain governed by BPS/PIN and the applicable Product-family specification.
- Dependency, provenance, derivation, and composition remain distinct relationships and MUST NOT be collapsed into one generic `basedOn` relationship.
- External ontologies are allowed for domains, organizations, policies, provenance, and related governed concepts.

---

# 5. Core Structure

Conceptually:

```text
HPD =
HPD identity +
described Product reference +
described Product Version reference +
authoritative classification references +
owner / provider references +
typed dependency / provenance references +
context references +
governance references +
usage +
observability +
lifecycle / currentness
```

Important identity distinction:

```text
HPD identity
  != Product identity
  != Product Version identity
```

HPD is a descriptor/projection **about** a Product Version. It is not the Product itself.

---

# 6. Ontology Alignment (TTL)

The following is a minimal HPD alignment illustrating the authority boundary. BPS remains authoritative for generic Product and Product Version semantics; HPD introduces only descriptor/projection relationships required by HDIP.

```turtle
@prefix bps: <https://kivanura.org/spec/bps/0.1/> .
@prefix hpd: <https://kivanura.org/spec/hdip/hpd#> .
@prefix dprod: <https://example.org/ikgf/dprod#> .
@prefix synctx: <https://kivanura.org/spec/hdip/synctx#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

##################################################
# HPD Class
##################################################

hpd:ProductDescriptor a owl:Class ;
    rdfs:label "HDIP Product Descriptor"@en .

##################################################
# HPD Projection Properties
##################################################

hpd:describesProduct a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range bps:Product .

hpd:describesProductVersion a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range bps:ProductVersion .

hpd:classificationRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range bps:Classification .

hpd:productOwnerRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .

hpd:providerRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .

hpd:dependencyRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .

hpd:provenanceRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .

hpd:derivationRef a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .

hpd:hasSyntheticContext a owl:ObjectProperty ;
    rdfs:domain hpd:ProductDescriptor ;
    rdfs:range rdfs:Resource .
```

The relationship resources referenced through `dependencyRef`, `provenanceRef`, and `derivationRef` SHOULD use the applicable authoritative semantics rather than HPD inventing substitute relationship meanings.

---

# 7. JSON-LD Context

Illustrative HPD context:

```json
{
  "@context": {
    "bps": "https://kivanura.org/spec/bps/0.1/",
    "hpd": "https://kivanura.org/spec/hdip/hpd#",
    "synctx": "https://kivanura.org/spec/hdip/synctx#",
    "dprod": "https://example.org/ikgf/dprod#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",

    "id": "@id",
    "type": "@type",
    "label": "rdfs:label",

    "describesProduct": {
      "@id": "hpd:describesProduct",
      "@type": "@id"
    },

    "describesProductVersion": {
      "@id": "hpd:describesProductVersion",
      "@type": "@id"
    },

    "classificationRefs": {
      "@id": "hpd:classificationRef",
      "@type": "@id",
      "@container": "@set"
    },

    "domain": {
      "@id": "dprod:domain",
      "@type": "@id"
    },

    "productOwnerRef": {
      "@id": "hpd:productOwnerRef",
      "@type": "@id"
    },

    "providerRef": {
      "@id": "hpd:providerRef",
      "@type": "@id"
    },

    "dependencyRefs": {
      "@id": "hpd:dependencyRef",
      "@type": "@id",
      "@container": "@set"
    },

    "provenanceRefs": {
      "@id": "hpd:provenanceRef",
      "@type": "@id",
      "@container": "@set"
    },

    "derivationRefs": {
      "@id": "hpd:derivationRef",
      "@type": "@id",
      "@container": "@set"
    },

    "syntheticContext": {
      "@id": "hpd:hasSyntheticContext",
      "@type": "@id"
    }
  }
}
```

---

# 8. Example HPD (JSON-LD Instance)

The example below illustrates a descriptor for one Product Version. Classification and dependency resources are referenced rather than redefined by HPD.

```json
{
  "@context": "https://kivanura.org/context/hdip.jsonld",

  "id": "https://kivanura.org/data/hpd/SynthPaymentProduct/v1",
  "type": "hpd:ProductDescriptor",

  "label": "Synthetic Payment Data Product - HPD v1",

  "describesProduct": "https://kivanura.org/data/product/SynthPaymentProduct",
  "describesProductVersion": "https://kivanura.org/data/product/SynthPaymentProduct/version/1",

  "domain": "https://example.org/domain/Payments",

  "classificationRefs": [
    "https://example.org/classification/product-family/data-product",
    "https://example.org/classification/product-kind/synthetic-payment-data",
    "https://example.org/classification/data-product-intrinsic-type/synthetic"
  ],

  "productOwnerRef": "https://example.org/org/PaymentsUBR",
  "providerRef": "https://example.org/org/AIEngineering",

  "dependencyRefs": [
    "https://example.org/dependency/SynthPayment-v1-to-PaymentData-v4",
    "https://example.org/dependency/SynthPayment-v1-to-PartyData-v2"
  ],

  "provenanceRefs": [
    "https://example.org/provenance/SynthPayment-v1-generation"
  ],

  "syntheticContext": "https://kivanura.org/data/synctx/SYNCTX-AI-TRAINING-001"
}
```

The example uses SYNCTX because this particular realization does. A Product being classified as `Synthetic` does **not** by itself require SYNCTX.

---

# 9. PDEP Lifecycle Integration

## 9.1 Creation Stage

HPD is **NOT authored by DPRO**.

It is generated by the platform at:

### Stage 8 — Platform Compilation Pack

```text
Intent + Product Identity/Version + Semantics + Governance
        + Usage + Dependency/Provenance State
                         |
                         v
               Stage 8: Compilation Pack
                         |
                         v
                    HPD generated
```

HPD generation projects resolved authoritative state; it does not independently establish Product qualification or classification.

---

## 9.2 Inputs to HPD Generation

HPD may project/reference:

- Product identity and Product Version
- Intent Record
- Semantic Descriptor (DPROD)
- authoritative Product classifications
- applicable Product owner/provider identities
- dependency, derivation, and provenance state
- authoritative governance/policy and compiled control bindings
- Usage Contract
- lifecycle/currentness state
- SYNCTX, where the Product realization actually uses SYNCTX

---

## 9.3 Output Role

HPD becomes an **HDIP platform coordination and operational projection** used for:

- DPFI coordination and orchestration
- CEP discovery and Product experience
- COVP usage/value/observability projection
- queryable Product knowledge
- dependency analysis
- impact assessment
- governance and policy-context evaluation
- lifecycle/currentness analysis

HPD being queryable or graph-addressable does not make it the semantic authority for the underlying Product concepts it references.

---

# 10. Relationship to Other Artifacts

| Artifact | Role |
|---|---|
| DPROD | Governed Data Product semantic descriptor |
| DPDS | Deployment / realization specification |
| SYNCTX | Synthetic relational context, where applicable |
| Digital Product Passport (DPP) | Trust / signed Product projection, where applicable |
| **HPD** | HDIP operational Product projection |

The exact authority and lifecycle relationship between these artifacts remains governed by their respective specifications.

---

# 11. Key Rules

## Rule 1 — Separation of Concerns

HPD MUST NOT redefine DPROD, DPDS, BPS/PIN, or the applicable Product-family semantics.

---

## Rule 2 — Descriptor / Product Identity Separation

HPD MUST have its own descriptor identity and MUST explicitly reference the Product and Product Version it describes.

```text
HPD identity != Product identity != Product Version identity
```

---

## Rule 3 — Authoritative Classification Projection

HPD MUST reference authoritative Product classifications where required. It MUST NOT invent an HPD-local generic `productType` taxonomy as a substitute for Product Family, Product Kind, or family-specific Intrinsic Type.

---

## Rule 4 — Typed Dependency / Provenance Semantics

Dependency, provenance, derivation, and composition MUST remain distinguishable. HPD MUST NOT collapse them into a single generic `basedOn` relationship.

---

## Rule 5 — Conditional SYNCTX Reference

Where a Product Version is realized using SYNCTX, HPD MUST reference the applicable SYNCTX. Synthetic classification alone does not make SYNCTX mandatory.

---

## Rule 6 — Domain Flexibility

HPD MAY reference the Product's governed domain through `dprod:domain` or a successor authoritative domain relationship without constraining the domain ontology itself.

---

## Rule 7 — Authority Preservation

Product ownership, provider/operational responsibility, Data ownership, source authority, and Authoritative Source status MUST NOT be inferred from one another merely because HPD references them together.

---

## Rule 8 — Historical Versioning

HPD projections SHOULD be versioned/currentness-aware so that later Product, dependency, governance, or lifecycle changes do not rewrite the state that applied to an earlier Product Version.

---

# 12. Storage & Runtime

HPD is technology-neutral at the logical architecture level.

It MAY be materialized through mechanisms such as:

- RDF / graph stores
- registry or catalog storage
- JSON / document stores
- version-controlled artifacts
- other conformant enterprise metadata or knowledge platforms

The choice of graph database, document store, source-control system, or other persistence technology does not define HPD semantics.

---

# 13. Summary

```text
DPROD
  -> defines the governed Data Product semantic descriptor

DPDS
  -> defines deployment / realization requirements

SYNCTX
  -> defines the applicable synthetic relational context, where used

HPD
  -> projects authoritative Product, Product Version,
     classification, dependency/provenance, governance,
     usage, observability and lifecycle state for HDIP operation
```

HPD **projects classification; it does not define Product classification**.

---

# 14. Final Insight

> HPD is an **HDIP platform-level operational projection of a Data Product Version** and may be represented as a first-class node in an HDIP Product knowledge graph or equivalent governed metadata/knowledge capability.

It enables HDIP to move from:

```text
static metadata
```

to:

```text
computable, queryable Product knowledge and operational context
```

without turning the descriptor into the semantic authority for the Product it describes.

---
