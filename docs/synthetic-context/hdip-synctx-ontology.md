---
id: hdip-synctx-ontology
title: HDIP SYNCTX (Synthetic Context) Ontology
sidebar_label: HDIP © SYNCTX Ontology
---

# 📘 1. SYNCTX Ontology (TTL)

This ontology defines the **HDIP-owned Synthetic Context vocabulary** used to represent a platform-generated, versioned relational and constraint projection for synthetic-data generation.

SYNCTX is deliberately **referential**. It does not redefine generic Product, Product Version, Data Product, schema, policy, provenance, or enterprise semantic concepts owned by BPS/PIN, GEDRM/GEDRA, W3C PROV, or other authoritative specifications.

> **Core principle:** SYNCTX compiles and correlates authoritative Product Version, semantic, schema, contract, constraint and governance references for a defined synthetic-generation purpose. It does not become the source authority for those referenced semantics.

---

```turtle
@prefix synctx: <https://kivanura.org/spec/hdip/synctx#> .
@prefix bps:    <https://kivanura.org/spec/bps/0.1/> .
@prefix gedrm:  <https://specs.kivanura.org/gedrm#> .
@prefix hpd:    <https://kivanura.org/spec/hdip/hpd#> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

##################################################
# Ontology Declaration
##################################################

synctx:Ontology a owl:Ontology ;
    rdfs:label "HDIP Synthetic Context Ontology" ;
    rdfs:comment "Defines the HDIP-owned Synthetic Context projection used to bind Product Versions, validated relational bindings, constraints and generation requirements for governed synthetic-data generation." .

##################################################
# Core Class
##################################################

synctx:SyntheticContext a owl:Class ;
    rdfs:label "Synthetic Context" ;
    rdfs:comment "A platform-generated, versioned relational and constraint projection compiled for a defined synthetic-generation purpose from authoritative Product Version and governance information." .

##################################################
# Membership
##################################################

synctx:hasMemberVersion a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range bps:ProductVersion ;
    rdfs:label "has member Product Version" ;
    rdfs:comment "Binds the specific Product Versions whose resolved schema, semantic and constraint state participates in this Synthetic Context." .

##################################################
# Relationship Binding
##################################################

synctx:hasRelationshipBinding a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range synctx:RelationshipBinding ;
    rdfs:label "has relationship binding" .

synctx:RelationshipBinding a owl:Class ;
    rdfs:label "Synthetic Context Relationship Binding" ;
    rdfs:comment "A validated relationship projection between member Product Versions. It may reference an authoritative semantic relationship, a technical join/key binding, or both; neither is inferred solely from naming similarity." .

synctx:fromVersion a owl:ObjectProperty ;
    rdfs:domain synctx:RelationshipBinding ;
    rdfs:range bps:ProductVersion ;
    rdfs:label "from Product Version" .

synctx:toVersion a owl:ObjectProperty ;
    rdfs:domain synctx:RelationshipBinding ;
    rdfs:range bps:ProductVersion ;
    rdfs:label "to Product Version" .

synctx:relationshipKindRef a owl:ObjectProperty ;
    rdfs:domain synctx:RelationshipBinding ;
    rdfs:range rdfs:Resource ;
    rdfs:label "relationship kind reference" ;
    rdfs:comment "References a controlled relationship-kind concept rather than encoding material relationship semantics as an arbitrary string." .

synctx:semanticRelationshipRef a owl:ObjectProperty ;
    rdfs:domain synctx:RelationshipBinding ;
    rdfs:range rdfs:Resource ;
    rdfs:label "semantic relationship reference" ;
    rdfs:comment "Optional reference to the authoritative semantic relationship governing the participating concepts." .

synctx:joinBindingRef a owl:ObjectProperty ;
    rdfs:domain synctx:RelationshipBinding ;
    rdfs:range rdfs:Resource ;
    rdfs:label "join or key binding reference" ;
    rdfs:comment "Optional reference to the governed schema/key/contract binding used to realize the relationship technically." .

##################################################
# Purpose & Generation Requirements
##################################################

synctx:hasPurpose a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range bps:Purpose ;
    rdfs:label "has purpose" ;
    rdfs:comment "References the governed purpose for which the Synthetic Context is compiled." .

synctx:hasFidelityLevelRef a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "fidelity level reference" ;
    rdfs:comment "References a controlled HDIP or enterprise fidelity concept where fidelity classification is applicable." .

synctx:generationModeRef a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "generation mode reference" ;
    rdfs:comment "References a controlled generation-mode concept where generation mode is applicable." .

##################################################
# Constraint Projection
##################################################

synctx:hasConstraintProjection a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range synctx:ConstraintProjection ;
    rdfs:label "has constraint projection" .

synctx:ConstraintProjection a owl:Class ;
    rdfs:label "Synthetic Context Constraint Projection" ;
    rdfs:comment "A SYNCTX projection of an authoritative policy, contract, privacy, quality, semantic or generation constraint relevant to the synthetic-generation context." .

synctx:constraintKindRef a owl:ObjectProperty ;
    rdfs:domain synctx:ConstraintProjection ;
    rdfs:range rdfs:Resource ;
    rdfs:label "constraint kind reference" .

synctx:constraintRef a owl:ObjectProperty ;
    rdfs:domain synctx:ConstraintProjection ;
    rdfs:range rdfs:Resource ;
    rdfs:label "authoritative constraint reference" ;
    rdfs:comment "References the authoritative policy, contract, rule or control obligation from which this projection is derived." .

synctx:constraintValue a owl:DatatypeProperty ;
    rdfs:domain synctx:ConstraintProjection ;
    rdfs:range xsd:string ;
    rdfs:label "projected constraint value" ;
    rdfs:comment "Optional typed lexical value used only where the authoritative constraint requires a value in the compiled context." .

##################################################
# Governance / Request Context
##################################################

synctx:requestedBy a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "requested by" ;
    rdfs:comment "Identifies the actor or governed role requesting compilation of the Synthetic Context." .

synctx:requestedFor a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "requested for" ;
    rdfs:comment "Identifies the domain, Product development context or governed initiative for which the Synthetic Context is compiled." .

synctx:appliedBy a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "applied by" ;
    rdfs:comment "Identifies the HDIP platform capability that applies the compiled Synthetic Context. This does not transfer semantic or policy authority to that capability." .

##################################################
# Generation / Output References
##################################################

synctx:usedByGeneration a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "used by generation activity" ;
    rdfs:comment "Optional reference to a synthetic-generation execution/activity that used this context. The Synthetic Context itself does not perform generation." .

synctx:associatedGeneratedAsset a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "associated generated asset" ;
    rdfs:comment "References generated data/assets associated with generation under this context. Presence of this relationship does not establish Product status." .

##################################################
# Lifecycle & Version
##################################################

synctx:createdOn a owl:DatatypeProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range xsd:dateTime ;
    rdfs:label "created on" .

synctx:versionIdentifier a owl:DatatypeProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range xsd:string ;
    rdfs:label "version identifier" .

synctx:statusRef a owl:ObjectProperty ;
    rdfs:domain synctx:SyntheticContext ;
    rdfs:range rdfs:Resource ;
    rdfs:label "lifecycle or currentness status reference" .

# For revisions, use W3C PROV revision semantics rather than mutating
# the historical meaning of an already-used Synthetic Context version.
# Example: <SYNCTX-v2> prov:wasRevisionOf <SYNCTX-v1> .
```

---

# 🧠 Key Design Notes (TTL)

## ✔ SYNCTX is a first-class HDIP-owned construct

```turtle
synctx:SyntheticContext a owl:Class
```

SYNCTX owns the **context projection and binding semantics** required by HDIP synthetic-data generation. It does not own the generic Product, Product Version, Data Product, policy, provenance or enterprise semantic concepts it references.

---

## ✔ Members are Product Versions

```text
SYNCTX
   +--> Payment Data Product Version v3
   +--> Party Data Product Version v5
```

The operative membership is Product-Version-specific because schema, semantics, contracts and constraints may change between versions.

Parent Product identity remains available through BPS `isVersionOf` / `hasVersion` relationships.

> **Historical rule:** a later Product Version does not silently rewrite an already-compiled SYNCTX version.

---

## ✔ Relationship bindings are explicit and typed

Instead of an arbitrary literal such as:

```text
relationshipType = "foreign_key"
```

SYNCTX represents a validated binding that may separately reference:

```text
semantic relationship
technical join/key binding
controlled relationship kind
```

Therefore:

```text
same field name != relationship
same datatype != foreign key
semantic relationship != executable join automatically
```

---

## ✔ Constraints are projections of authoritative obligations

SYNCTX does not create a second policy vocabulary.

A `ConstraintProjection` points to the authoritative policy, contract, rule or control obligation and carries only the information required to compile/apply it within the synthetic-generation context.

---

## ✔ SYNCTX does not produce Products

SYNCTX is declarative context. It does not itself perform generation.

```text
SYNCTX
   |
   v
Synthetic-generation activity / execution
   |
   v
Generated Data / Data Asset
   |
   | intentional Product constitution, if applicable
   v
Synthetic Data Product
```

Therefore:

```text
generated output != Product automatically
Synthetic classification != mandatory SYNCTX realization
```

If a Product realization uses SYNCTX, the applicable HPD/operational projection should reference the SYNCTX version used.

---

## ✔ Request context and platform application are distinct

```text
requestedBy
requestedFor
appliedBy
```

replace the earlier overloaded `contextOwner` / `enforcedBy` formulation.

The HDIP capability applying SYNCTX does not thereby become the owner of the underlying policy, Product or Data semantics.

---

## ✔ SYNCTX versions preserve historical meaning

Once a SYNCTX version has been used for generation, material changes to its member Product Versions, relationship bindings, constraints, purpose or generation requirements should result in a **new SYNCTX version**, not silent mutation of the historical context.

```text
identity != version
version != currentness
revision != deletion
```

---

## ✔ Authority boundaries

```text
BPS / PIN
  -> Product and Product Version semantics

GEDRM / GEDRA
  -> Data and Data Product semantics / architecture

W3C PROV
  -> generic provenance / revision semantics

HDIP SYNCTX
  -> Synthetic Context projection and binding semantics
```

And explicitly:

```text
HDIP SyntheticContext != GEAIRM AI Context
```

A generated asset governed by SYNCTX may later participate as a resource in an AI Context, but the two context concepts are not equivalent.

---

# 📦 2. JSON-LD Context for SYNCTX

The following JSON-LD context is valid JSON and mirrors the revised referential ontology.

```json
{
  "@context": {
    "synctx": "https://kivanura.org/spec/hdip/synctx#",
    "bps": "https://kivanura.org/spec/bps/0.1/",
    "gedrm": "https://specs.kivanura.org/gedrm#",
    "hpd": "https://kivanura.org/spec/hdip/hpd#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "id": "@id",
    "type": "@type",

    "SyntheticContext": "synctx:SyntheticContext",
    "RelationshipBinding": "synctx:RelationshipBinding",
    "ConstraintProjection": "synctx:ConstraintProjection",

    "members": {
      "@id": "synctx:hasMemberVersion",
      "@type": "@id"
    },

    "relationships": {
      "@id": "synctx:hasRelationshipBinding",
      "@container": "@set"
    },
    "fromVersion": {
      "@id": "synctx:fromVersion",
      "@type": "@id"
    },
    "toVersion": {
      "@id": "synctx:toVersion",
      "@type": "@id"
    },
    "relationshipKindRef": {
      "@id": "synctx:relationshipKindRef",
      "@type": "@id"
    },
    "semanticRelationshipRef": {
      "@id": "synctx:semanticRelationshipRef",
      "@type": "@id"
    },
    "joinBindingRef": {
      "@id": "synctx:joinBindingRef",
      "@type": "@id"
    },

    "purpose": {
      "@id": "synctx:hasPurpose",
      "@type": "@id"
    },
    "fidelityLevelRef": {
      "@id": "synctx:hasFidelityLevelRef",
      "@type": "@id"
    },
    "generationModeRef": {
      "@id": "synctx:generationModeRef",
      "@type": "@id"
    },

    "constraints": {
      "@id": "synctx:hasConstraintProjection",
      "@container": "@set"
    },
    "constraintKindRef": {
      "@id": "synctx:constraintKindRef",
      "@type": "@id"
    },
    "constraintRef": {
      "@id": "synctx:constraintRef",
      "@type": "@id"
    },
    "constraintValue": "synctx:constraintValue",

    "requestedBy": {
      "@id": "synctx:requestedBy",
      "@type": "@id"
    },
    "requestedFor": {
      "@id": "synctx:requestedFor",
      "@type": "@id"
    },
    "appliedBy": {
      "@id": "synctx:appliedBy",
      "@type": "@id"
    },

    "usedByGeneration": {
      "@id": "synctx:usedByGeneration",
      "@type": "@id"
    },
    "associatedGeneratedAssets": {
      "@id": "synctx:associatedGeneratedAsset",
      "@type": "@id",
      "@container": "@set"
    },

    "createdOn": {
      "@id": "synctx:createdOn",
      "@type": "xsd:dateTime"
    },
    "versionIdentifier": "synctx:versionIdentifier",
    "statusRef": {
      "@id": "synctx:statusRef",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    }
  }
}
```

---

# 📄 3. Example SYNCTX Instance (JSON-LD)

This example binds specific Product Versions and references governed relationship/constraint resources. The identifiers are illustrative.

```json
{
  "@context": "https://kivanura.org/context/synctx.jsonld",

  "id": "https://kivanura.org/data/synctx/SYNCTX-AI-TRAINING-001/v1",
  "type": "SyntheticContext",

  "purpose": "https://kivanura.org/purpose/model-training",
  "fidelityLevelRef": "https://kivanura.org/hdip/vocab/fidelity/high",
  "generationModeRef": "https://kivanura.org/hdip/vocab/generation-mode/coordinated",

  "members": [
    "https://kivanura.org/data/product/PaymentDataProduct/version/3",
    "https://kivanura.org/data/product/PartyDataProduct/version/5"
  ],

  "relationships": [
    {
      "id": "https://kivanura.org/data/synctx/SYNCTX-AI-TRAINING-001/v1/relationship/payment-party",
      "type": "RelationshipBinding",
      "fromVersion": "https://kivanura.org/data/product/PaymentDataProduct/version/3",
      "toVersion": "https://kivanura.org/data/product/PartyDataProduct/version/5",
      "relationshipKindRef": "https://kivanura.org/hdip/vocab/relationship-kind/key-binding",
      "semanticRelationshipRef": "https://kivanura.org/enterprise/semantics/payment-party-relationship",
      "joinBindingRef": "https://kivanura.org/data/contracts/payment-party-key-binding/v2"
    }
  ],

  "constraints": [
    {
      "id": "https://kivanura.org/data/synctx/SYNCTX-AI-TRAINING-001/v1/constraint/privacy-1",
      "type": "ConstraintProjection",
      "constraintKindRef": "https://kivanura.org/hdip/vocab/constraint-kind/privacy",
      "constraintRef": "https://kivanura.org/policy/no-direct-identifiers/v4",
      "constraintValue": "no_direct_identifiers"
    }
  ],

  "requestedBy": "https://example.org/org/AIEngineering",
  "requestedFor": "https://example.org/initiative/FraudModelTraining",
  "appliedBy": "https://kivanura.org/platform/DPFI",

  "associatedGeneratedAssets": [
    "https://kivanura.org/data/asset/synthetic-payment-batch/2026-10-09",
    "https://kivanura.org/data/asset/synthetic-party-batch/2026-10-09"
  ],

  "createdOn": "2026-10-09T18:00:00Z",
  "versionIdentifier": "1.0.0",
  "statusRef": "https://kivanura.org/hdip/vocab/context-status/current"
}
```

The generated assets above are **not inferred to be Products** merely because they were generated under SYNCTX. If they are intentionally constituted as Products, BPS/PIN and the applicable Data Product semantics determine that Product status separately.

---

# 🔥 Final Mental Model

## 🔹 SYNCTX in HDIP

```text
Authoritative Product Versions
+ schemas / semantic relationships
+ contracts / controls / policy references
+ governed synthetic-generation purpose
                 |
                 v
              PDEP
         DPFI compilation
                 |
                 v
             SYNCTX vN
   relational + constraint projection
                 |
                 v
     Synthetic-generation activity
                 |
                 v
          Generated Data
                 |
          [if productized]
                 v
      Synthetic Data Product
```

---

## 🔹 Interaction with HPD

```text
HPD for Product Version
        |
        +--> references applicable SYNCTX version

SYNCTX
        |
        +--> references Product Versions
        +--> references validated relationship bindings
        +--> references authoritative constraints
        +--> may reference generation activity / generated assets
```

SYNCTX does **not** replace HPD, DPROD, DPDS, Product Version semantics, Data Contracts, policy authority or provenance. It is the HDIP projection that binds the subset of those authoritative references required for governed synthetic-data generation.

---
