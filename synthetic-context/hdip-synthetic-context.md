---
id: hdip-synthetic-context
title: HDIP Synthetic Context
sidebar_label: HDIP © Synthetic Context
---

# 1. What is SYNCTX (Formal Positioning)

> **SYNCTX (Synthetic Context Specification)** is an HDIP-generated, versioned relational and constraint projection compiled for a defined synthetic-generation purpose from authoritative Product Version, schema, semantic, contract and governance information.

SYNCTX makes the applicable generation context explicit by projecting:

- the participating **Data Product Versions**;
- validated cross-member **RelationshipBindings** where applicable;
- generation requirements such as fidelity and coordination expectations;
- applicable **ConstraintProjections**;
- purpose/request context;
- lifecycle and traceability information.

SYNCTX does **not** itself generate data, guarantee correctness, establish Product status, or redefine the authoritative semantics it references.

> **Authority boundary:** BPS/PIN owns generic Product and Product Version semantics; GEDRM/GEDRA and applicable enterprise/domain authorities govern Data semantics and Data architecture; HDIP SYNCTX owns the synthetic-generation context projection only.

> **AI-context boundary:** **HDIP SyntheticContext != GEAIRM AI Context.** A generated asset may later participate in an AI Context, but SYNCTX itself is not an AI execution/context semantic construct.

---

# 2. Critical Clarification (Very Important)

> **Synthetic Context is NOT created or semantically authored by the DPRO.**

Instead:

> **Synthetic Context is resolved, compiled and versioned by HDIP through PDEP/DPFI from governed intent, Product Version, semantic, schema/contract, policy and generation-requirement evidence.**

This preserves the core HDIP principle:

> **The requester/producer expresses intent and governed requirements. The platform compiles the operational projection.**

DPFI may discover candidate dependencies, relationships or constraints, but candidate evidence does not automatically become a SYNCTX fact. Material bindings require authoritative or sufficiently validated evidence.

---

# 3. Nature of SYNCTX (Important Positioning)

SYNCTX is:

✔ A **first-class HDIP construct**  
✔ A **platform-generated relational and constraint projection**  
✔ A **graph-addressable resource (IRI-based)**  
✔ A **versioned context for governed synthetic generation**  
✔ A **projection of authoritative references and resolved bindings**

SYNCTX is NOT:

❗ A Data Product  
❗ A source of Product qualification  
❗ A substitute for authoritative Data, schema, contract or policy semantics  
❗ A user-authored execution specification  
❗ A guarantee that all member data is joinable  
❗ A GEAIRM AI Context

SYNCTX may be exposed read-only in PDEP or governance tooling for explanation, diagnostics, audit or impact analysis, but users do not manually author its compiled semantic content.

---

# 4. Design Principles of SYNCTX

### 1. Declarative and compiled, not procedural

SYNCTX expresses the **resolved generation context and governed requirements**. It does not prescribe a particular synthetic-data algorithm or implementation technology.

---

### 2. Relational claims require validated bindings

A SYNCTX boundary does **not** by itself guarantee joinability.

Cross-member relational compatibility or joinability may only be relied upon where:

- applicable `RelationshipBinding`s have been validated from sufficient authoritative evidence; and
- the generation requirements explicitly require the relevant relationships to be preserved.

A semantic relationship is not automatically an executable join, and matching field names do not establish a foreign key.

---

### 3. Product-Version-aware membership

A SYNCTX may contain **one or more applicable Data Product Versions**.

The operative member is the Product Version because schemas, semantics, contracts and constraints can change between versions.

> A dependency path does not automatically make every upstream Product Version a SYNCTX member. Membership requires applicability to the synthetic-generation context.

---

### 4. Versioned and reproducibly compilable

SYNCTX compilation is intended to be reproducible.

Given the same normalized authoritative inputs, Product Versions, governing semantic/policy versions, and compiler/rule-set version, DPFI should produce **semantically equivalent canonical SYNCTX projection content**.

This does **not** imply deterministic synthetic-data generation. A generation activity may legitimately be stochastic.

---

### 5. Emergent from governed evidence

SYNCTX is not manually declared as a finished artifact. It is compiled from applicable evidence such as:

- intent and approved synthetic-generation requirement;
- Product and Product Version identity;
- semantic descriptors;
- schemas and Data Contracts;
- authoritative relationship evidence;
- policy/control obligations;
- business assertions;
- generation and evaluation requirements;
- usage/accountability context.

---

### 6. Historical meaning is preserved

Once a SYNCTX version has been used, material changes to its membership, relationship bindings, constraints, purpose or generation requirements result in a **new SYNCTX version/revision**, rather than silently mutating the historical context.

---

# 5. Conceptual Structure of SYNCTX

SYNCTX is modeled conceptually as:

```text
SyntheticContext =
    identity / version
  + purpose
  + member Product Versions
  + RelationshipBindings
  + generation requirements
  + ConstraintProjections
  + requester / governance context
  + lifecycle / currentness
  + optional generation-activity references
  + optional generated-asset references
```

> This is a **logical structure**, not a prescribed serialization format.

SYNCTX may later reference a generation activity or generated assets associated with its use. Those references do not imply that SYNCTX itself performed the generation.

---

# 6. Representation (Important)

SYNCTX is represented as:

- **Canonical semantic form**: RDF / JSON-LD or another conformant graph projection;
- **Optional projections**: YAML, JSON or UI views for documentation, diagnostics or governance.

> SYNCTX is logically graph-addressable. A particular storage technology is not mandated by the concept.

---

# 7. Conceptual Fields (Illustrative Only)

Below is an illustrative, non-canonical projection:

```yaml
syntheticContext:
  identity:
  versionIdentifier:
  purposeRef:
  memberVersions:
  relationshipBindings:
  generationRequirements:
  constraintProjections:
  requestedBy:
  requestedFor:
  appliedBy:
  lifecycle:
  generationActivities:
  associatedGeneratedAssets:
```

---

# 8. Key Components (Refined)

## 8.1 Identity and Version

- stable SYNCTX identity;
- explicit version identifier;
- platform-generated/managed;
- historical versions retain their original meaning.

Identity, version and currentness are distinct concerns.

---

## 8.2 Purpose

Purpose is resolved from governed intent and usage/accountability context, for example:

- model training;
- external sharing;
- testing;
- simulation;
- other approved synthetic-generation purposes.

Purpose alone does **not** prove that synthetic generation is required. Synthetic generation may be selected or required only after applicable intent, policy, Data Contract, privacy and control evidence is resolved.

Where available, SYNCTX should reference the governed purpose/intent rather than encode important purpose semantics only as free text.

---

## 8.3 Member Product Versions

A SYNCTX references the specific Data Product Versions whose data, schemas, contracts, semantics or constraints materially participate in the compiled generation context.

> Membership MUST use stable Product Version identifiers and MUST NOT be inferred merely from a transitive dependency path.

Parent Product identities may also be referenced for navigation, but the operative membership is version-specific.

---

## 8.4 RelationshipBindings (Core)

A `RelationshipBinding` captures a validated relationship relevant to the generation context.

Evidence may include:

- authoritative semantic relationships;
- schema/key metadata;
- Data Contracts;
- enterprise/domain Data models;
- governed ontology relations;
- validated technical bindings.

Important distinctions:

```text
semantic relationship
    !=
technical join binding

matching attribute names
    !=
foreign-key proof

relationship existence
    !=
referential-integrity requirement
```

Where a join/key binding is required, the technical relationship must be supported by sufficient evidence rather than inferred from naming similarity alone.

---

## 8.5 Generation Requirements

Generation requirements may define, where applicable:

- coordinated vs independent generation;
- fidelity requirements;
- relational-preservation requirements;
- temporal or scenario consistency;
- statistical characteristics to preserve or intentionally alter;
- quality/evaluation expectations.

These requirements are resolved from governed evidence. They are not universal hard-coded consequences of purpose or relationship count.

For example, statistical distributions may intentionally be altered for class balancing, rare-event augmentation, stress testing or privacy objectives.

---

## 8.6 ConstraintProjections

A `ConstraintProjection` references an authoritative policy, contract, assertion, regulatory obligation or control requirement and carries the information needed to apply it within the synthetic-generation context.

```text
ConstraintProjection
    !=
policy authority
```

Not every policy obligation is fully machine-executable. Some constraints may require assessment or human governance rather than compilation into an automated control.

---

## 8.7 Generation Activities and Generated Assets

SYNCTX does not define or automatically create Synthetic Data Products.

The correct separation is:

```text
SYNCTX
   |
   v
Synthetic-generation activity
   |
   v
Generated Data / Data Assets
   |
   | if intentionally constituted and qualified
   v
Synthetic Data Product
```

Generated assets should preserve traceability to the SYNCTX version and generation activity under which they were produced.

If a generated asset is subsequently constituted as a Product, Product qualification and Product-family semantics are governed separately by BPS/PIN and the applicable Data Product lifecycle/specification.

Output cardinality is not determined by the number of SYNCTX members. One SYNCTX may support one generated asset, many assets, a consolidated dataset, a graph, a simulation bundle or other governed outputs.

---

## 8.8 Governance and Authority

SYNCTX coordinates governed references; it does not collapse authority into DPFI.

| Concern | Governing source |
| --- | --- |
| Generic Product / Product Version semantics | BPS / PIN |
| Data Product and Data semantics | GEDRM / applicable Data Product and enterprise/domain authorities |
| Schema / Data Contract meaning | authoritative schema and contract sources |
| Policy / regulatory / control obligations | applicable policy, regulatory and governance authorities |
| Product ownership/accountability | authoritative Product role/ownership model |
| Request purpose and usage accountability | requesting/consuming domain or governed intent |
| Generation-requirement resolution | PDEP / DPFI compilation from governed inputs |
| SYNCTX lifecycle and projection management | HDIP platform governance |

DPFI may apply compiled constraints, but application does not make DPFI the source of policy authority.

---

## 8.9 Lifecycle

SYNCTX is:

- system-generated;
- versioned;
- reproducibly compilable;
- historically preserved once used;
- superseded by new versions when material context changes.

A later Product Version does not silently rewrite the membership or meaning of an existing SYNCTX version.

---

# 9. Referencing Contract Alignment

SYNCTX follows HDIP referencing principles:

✔ Stable entities and governed resources are referenced by **IRIs/URIs or equivalent stable identifiers**  
✔ Members reference **specific Product Versions**, not arbitrary strings  
✔ RelationshipBindings are explicit and evidence-backed  
✔ ConstraintProjections reference their authoritative source  
✔ Generation/activity and generated-asset references preserve traceability  
✔ No semantic or technical relationship is established merely from naming similarity

---

# 10. How SYNCTX Emerges in PDEP

## ❌ Incorrect Model

```text
DPRO -> defines finished SYNCTX
```

or:

```text
DPFI sees matching names
     -> invents joins
     -> creates Synthetic Data Products
```

---

## ✅ Correct Model

```text
Intent / approved synthetic-generation requirement
        |
        v
Product Version + semantics + schema/contracts
+ policy/governance + assertions + purpose
        |
        v
DPFI Resolution & Compilation
        |
        v
Versioned SYNCTX projection
```

DPFI may discover candidates during compilation, but candidate evidence becomes a material SYNCTX assertion only when the applicable authority/evidence supports it.

---

# 11. Inputs That Drive SYNCTX

SYNCTX may be compiled from the following governed inputs.

### 1. Intent / Request Context

- purpose;
- requester/consumer context;
- approved synthetic-generation requirement where applicable.

### 2. Product and Product-Version State

- Product identity;
- Product Version identity;
- lifecycle/currentness information relevant to compilation;
- applicable dependency candidates.

### 3. Semantic Descriptor / Data Semantics

- governed entities/concepts;
- semantic relationships;
- applicable Data Product descriptor information.

### 4. Schemas and Data Contracts

- attributes/fields;
- key semantics;
- compatibility information;
- contractual constraints and obligations.

### 5. Business Assertions

- rules;
- constraints;
- validation conditions;
- material relationship assertions.

### 6. Governance / Policy Sources

- privacy requirements;
- sharing constraints;
- regulatory obligations;
- applicable controls.

### 7. Generation and Evaluation Requirements

- fidelity expectations;
- coordination requirements;
- characteristics that must be preserved or may be intentionally changed;
- quality/evaluation criteria.

### 8. Usage / Accountability Context

- audience;
- usage mode;
- downstream accountability conditions.

Usage signals may contribute evidence but do not by themselves create Product, semantic, relationship or policy facts.

---

# 12. How SYNCTX Works in HDIP Flow

```text
Intent / approved synthetic-generation requirement
        |
        v
Governed Product Version + semantic + schema/contract
+ policy + generation/evaluation evidence
        |
        v
PDEP / DPFI Resolution & Compilation
        |
        v
SYNCTX
        |
        v
Synthetic-generation activity
        |
        v
Generated Data / Data Assets
        |
        +--> optional Product constitution / qualification
             through the applicable Product lifecycle
```

This flow deliberately separates:

```text
context compilation
    !=
generation execution
    !=
Product constitution
```

---

# 13. Relationship to Other Artifacts

| Artifact | Role |
| --- | --- |
| DPROD | Governed Data Product semantic descriptor |
| DPDS | Deployment / realization specification |
| HPD | HDIP operational Product projection bundle |
| SYNCTX | Versioned relational / constraint projection for synthetic generation |
| Digital Product Passport (DPP) | Trust/evidence-oriented Product artifact where applicable |

SYNCTX may be referenced by HPD or other operational projections when a Product realization uses a particular SYNCTX version.

---

# 14. Very Important Rules

### Rule 1 — Joinability is evidence-bound

Relational compatibility or joinability may only be claimed where supported by validated `RelationshipBinding`s and applicable generation requirements.

A SYNCTX boundary alone does not guarantee joinability.

---

### Rule 2 — Preserve generation traceability

Generated assets SHOULD preserve traceability to the SYNCTX version and generation activity under which they were produced.

Where a generated asset is intentionally constituted as a Product, the resulting Product Version SHOULD preserve that traceability.

---

### Rule 3 — No cross-context compatibility inference

Different SYNCTX instances are **not assumed to be joinable, compatible or mutually substitutable** unless an explicit governed compatibility relation establishes that fact.

---

### Rule 4 — Not user-authored, but may be visible

SYNCTX is not a mandatory user-authored PDEP artifact.

It MAY be exposed read-only where transparency, diagnostics, audit, governance review or impact analysis require it.

---

### Rule 5 — Minimum membership

A SYNCTX MUST reference at least one valid, resolvable Data Product Version applicable to the synthetic-generation context.

---

### Rule 6 — No Product inference

A generated Data Asset does not become a Data Product merely because it was produced under SYNCTX.

Product constitution and Product-family qualification occur separately under BPS/PIN and the applicable Data Product lifecycle/specification.

---

### Rule 7 — Historical non-mutation

Material changes to member Product Versions, RelationshipBindings, ConstraintProjections, purpose or generation requirements MUST produce a new SYNCTX version/revision rather than silently changing the meaning of an already-used version.

---

# 15. Key Insight

> **Synthetic Context captures a governed relational and constraint projection for a specific synthetic-generation context; it does not encode universal relational truth and does not contain the generated data itself.**

It allows HDIP to make explicit which Product Versions, relationships, requirements and constraints were relied upon when a generation activity was prepared or executed.

---

# 16. Final Position

SYNCTX is:

✔ Platform-generated  
✔ Graph-addressable  
✔ Versioned  
✔ Reproducibly compilable  
✔ Governed  
✔ Product-Version-aware  
✔ Relationally explicit where evidence supports it  
✔ Traceable to authoritative inputs

But:

❗ Not user-authored  
❗ Not a Product  
❗ Not a policy authority  
❗ Not a guarantee of correctness or joinability  
❗ Not necessarily deterministic at synthetic-generation runtime  
❗ Not a GEAIRM AI Context

---

# 17. Summary

```text
Authoritative Product / Data semantics
        -> define governed meaning

PDEP / DPFI
        -> resolves governed evidence and compiles context

SYNCTX
        -> projects applicable Product Versions,
           validated relationship bindings,
           generation requirements and constraints

HDIP platform
        -> validates, applies and evidences
           the compiled context

Synthetic-generation activity
        -> produces generated Data / Data Assets

Product constitution
        -> occurs separately where applicable
```

> **Platform validation and enforcement provide evidence of conformance to the compiled context; they do not amount to a universal guarantee of semantic or business correctness.**

---
