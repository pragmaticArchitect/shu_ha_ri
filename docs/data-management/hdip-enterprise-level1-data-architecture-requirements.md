---
id: hdip-enterprise-level1-data-architecture-requirements
title: Enterprise Data Management Requirements Catalogue
sidebar_label: HDIP © DM Level 1 Requirements
---

# Enterprise Data Management Principles & Mandatory Requirements

## 1. Purpose

This document defines the minimum Data Management expectations that apply to enterprise initiatives which create, change, move, store, expose, consume, govern, or retire enterprise data.

It is intended to provide a concise and reusable requirement baseline for initiatives such as:

- regulatory change;
- regional transformation;
- data localisation;
- cloud migration;
- platform transformation;
- new product or service initiatives;
- enterprise data programmes;
- analytics and AI initiatives.

This document is the **Level 1 entry point**.

Detailed requirement wording, applicability rules, evidence expectations, control obligations, and exception handling are defined in the companion **Enterprise Data Management Requirements Catalogue**.

---

## 2. Core Principle

> An initiative may own the delivery of a change, but it does not independently redefine the enterprise data architecture.

The Enterprise Data Architecture / Data Management function defines the Data Management requirements and architectural guardrails that must be satisfied where enterprise data is materially affected.

The programme and its architecture teams remain accountable for designing and delivering a compliant solution.

---

## 3. Normative Language

The following terminology is used throughout this document:

- **MUST** — mandatory requirement. Non-compliance requires an explicitly approved exception.
- **MUST NOT** — prohibited practice unless an approved exception exists.
- **SHOULD** — expected practice unless a justified alternative is documented.
- **MAY** — optional where appropriate.

---

## 4. Mandatory Data Management Principles

![Diagram](/img/hdip/lvl1edmr.png)

### Principle 1 — Data Must Have Clear Ownership

Every material data domain, dataset, Authoritative Source, Data Asset, and Data Product must have an identified accountable owner.

Programme ownership must not become a substitute for enduring BAU ownership.

### Principle 2 — Authoritative Sources Must Be Protected

For material data, authoritative operational state and authoritative sourcing must be identifiable for the relevant governed scope.

Initiatives must not create competing sources of truth without explicit governance or authority designation.

Persistent non-owning copies must be justified, traceable, owned, synchronized where necessary, and lifecycle-managed.

Where the distinction is material, initiatives must distinguish the System of Record, Authoritative Source, and Source of Authority; these roles may coincide but must not be assumed equivalent.

### Principle 3 — Data Meaning Must Remain Consistent

Existing enterprise and domain semantics must be reused where appropriate.

Material new concepts, mappings, and transformations must be explicitly defined and governed.

Technical implementation convenience must not result in loss of important business meaning.

The Enterprise Ontology, domain ontologies, business vocabulary, canonical semantics, and mappings to external standards should be used where applicable.

### Principle 4 — Data Must Be Governed Through Explicit Contracts

Material data interfaces must have explicit contracts.

Contracts must define the structure, meaning, ownership, compatibility expectations, and relevant Data Quality commitments of the data being exchanged.

Breaking changes must be controlled and version-managed.

### Principle 5 — Data Must Be Fit for Its Intended Use

Material data must have defined Data Quality expectations aligned to consumer need and business purpose.

Quality failures must be measurable, observable, owned, and remediable.

### Principle 6 — Data Must Be Discoverable and Traceable

Material data must have sufficient business and technical metadata.

Lineage must enable traceability from authoritative source through material transformation to significant consumption points.

Regulatory and critical data must provide the level of lineage necessary for auditability and reconstruction.

### Principle 7 — Persistence Must Be Intentional

Every material persistent store must have a defined purpose, owner, retention period, and lifecycle.

Data must not be retained indefinitely simply because deletion or retirement was not designed.

### Principle 8 — Data Location and Movement Must Be Known

Where jurisdictional restrictions apply, initiatives must understand:

- where data is stored;
- where it is processed;
- where it is replicated;
- where it is backed up;
- where it is accessed;
- where derived data, metadata, and logs may travel.

Data residency assessment must consider the full lifecycle, not only the primary production database.

### Principle 9 — Consumers Must Be Explicit

Material data consumers and their intended purposes must be identified.

Consumer needs must inform:

- Data Quality;
- latency;
- availability;
- support;
- retention;
- contract design;
- access and entitlement design;
- productization decisions.

### Principle 10 — Reusable Data Must Be Assessed for Productization

Where an initiative creates or materially changes a reusable Data Asset, it must assess whether that asset should be managed as a Data Product.

The question is not merely:

> Can this data be technically consumed?

The more important question is:

> Should this data be governed and operated as a Data Product?

### Principle 11 — Data Products Must Carry an Explicit Product Promise

Where data is productized, the Data Product must have:

- identity;
- accountable ownership;
- an explicit Product Promise;
- governed interfaces and Data Contract where required;
- defined source and authority dependencies;
- versioning;
- discoverability;
- observability;
- lifecycle management.

### Principle 12 — Data Change Must Be Designed for Evolution

Initiatives must consider how their data capabilities will evolve after go-live.

This includes:

- upstream schema change;
- semantic change;
- new consumer requirements;
- new enrichment sources;
- versioning;
- compatibility;
- deprecation;
- migration.

### Principle 13 — Data Architecture Must Align to Enterprise Strategy and Strategic Data Architecture

Material initiatives must assess alignment with:

- Enterprise Data Strategy;
- target enterprise data architecture;
- **GEDRA**, where adopted as the generic enterprise data reference architecture;
- approved data architecture patterns;
- strategic data platforms and capabilities;
- cross-domain architecture;
- **HDIP**, where adopted as the enterprise **Holistic Data, Information and Intelligence Platform**; for the purposes of this Data Management catalogue, the relevant HDIP Data responsibilities should align with and specialize or realize GEDRA.

Local programme optimisation must not knowingly create material enterprise fragmentation without explicit architectural acceptance.

### Principle 14 — Regulatory and Evidential Data Must Be Reproducible

Where data supports regulatory or evidential use, the organisation must be able to explain:

- where the data came from;
- what transformations were applied;
- what rules and assumptions were used;
- what output was produced;
- how historical states can be reconstructed where required.

### Principle 15 — AI Consumption Does Not Remove Data Governance Obligations

Data used for AI, ML, analytics, model training, evaluation, grounding, or inference remains subject to Data Management requirements.

Where an AI Product is created or materially changed, applicable enterprise AI governance and relevant **AIPS** requirements should also be assessed.

### Principle 16 — Data Obligations Must Be Supported by Effective Controls

Material Data Management obligations must be supported by appropriate preventive, detective, and/or corrective Data Controls.

Controls must have:

- a defined control objective;
- clear ownership;
- defined operating frequency or trigger;
- measurable thresholds or rules where applicable;
- evidence of operation;
- exception handling;
- escalation and remediation arrangements.

Applicable controls may include:

- Data Quality control patterns;
- reconciliation controls;
- schema and contract validation;
- completeness controls;
- access and entitlement controls;
- residency controls;
- retention and deletion controls;
- lineage completeness controls;
- metadata completeness controls;
- integrity controls;
- distribution controls;
- regulatory controls;
- Data Product promise / SLA controls.

> Policy, standards, architecture requirements, and product promises define what is expected. Data Controls operationalise, test, enforce, and evidence those expectations.

---

## 5. Minimum Mandatory Requirement Set

Every materially data-impacting initiative must, at minimum, address the following questions:

1. What data is being created, changed, moved, consumed, or retired?
2. Who owns it?
3. Where is authoritative operational state maintained, what is the Authoritative Source, and who or what designates that authority where applicable?
4. Is a new copy being created, and why?
5. What is the business meaning of the data?
6. What interfaces or contracts expose it?
7. What are the relevant Data Quality expectations?
8. What lineage and metadata are required?
9. How long is it retained?
10. Where is it stored, processed, replicated, backed up, and accessed?
11. Who consumes it and for what purpose?
12. Is it a Data Asset that should become a Data Product?
13. How will schema, semantics, and product promises evolve?
14. Does it align with Enterprise Data Strategy, target data architecture, and HDIP where applicable?
15. Are there regulatory, evidential, or AI-specific implications?
16. What material Data Controls are required, who owns them, how do they operate, what evidence demonstrates their operation and outcomes, and how is effectiveness assessed where required?
17. Are existing controls dependent on data being changed by the initiative?
18. What exceptions or architectural divergences remain?

---

## 6. Required Initiative Outputs

Depending on scope and materiality, the initiative must provide:

- Data Management Applicability Assessment;
- Data Architecture Assessment;
- ownership and accountability model;
- authority mapping, including System of Record, Authoritative Source, and Source of Authority where applicable;
- source-to-target semantic mapping;
- data-flow and lineage view;
- contract/schema definition;
- Data Quality requirements;
- Data Controls inventory and control evidence model;
- retention and lifecycle definition;
- residency and cross-border assessment;
- consumer inventory;
- access and entitlement model where applicable;
- Data Asset / Data Product assessment;
- architecture alignment assessment;
- requirements traceability;
- documented exceptions where applicable.

---

## 7. Architecture Engagement Points

### Intake

Confirm applicability and material data impact.

### Architecture Definition

Confirm authority and sourcing, semantics, data movement, consumers, Data Assets, strategic alignment, and material control obligations.

### Detailed Design

Confirm contracts, lineage, Data Quality, retention, residency, access, entitlements, Data Controls, lifecycle, and observability.

### Pre-Production Readiness

Confirm requirements are satisfied, controls are operational where required, exceptions are approved, and enduring ownership exists.

### Post-Implementation

Confirm temporary arrangements are retired, control obligations remain effective, and the enduring data capability remains governed.

---

## 8. Relationship to the Detailed Catalogue

This document establishes the mandatory principles and minimum questions.

Detailed obligations are defined in:

> **Enterprise Data Management Requirements Catalogue**

The detailed catalogue contains:

- requirement identifiers;
- MUST / SHOULD / MAY wording;
- applicability criteria;
- rationale;
- evidence expectations;
- Data Control obligations;
- exception handling;
- requirement ownership;
- architecture assessment status.

Where there is ambiguity, the detailed catalogue is authoritative.

---

## 9. Relationship to GEDRM, GEDRA, BPS, UPOS, ProductVerse, HDIP and AIPS

This framework can be used independently, but it is compatible with the broader semantic, architecture, productization, and Data & AI concepts represented by:

- **GEDRM** — generic enterprise data semantic reference model;
- **GEDRA** — generic enterprise data reference architecture;
- **BPS** — universal product grammar;
- **UPOS** — universal productization architecture;
- **ProductVerse** — interconnected product relationship model;
- **HDIP** — enterprise **Holistic Data, Information and Intelligence Platform** architecture; its Data responsibilities may specialize and realize GEDRA while remaining subject to this enterprise Data Management baseline;
- **AIPS** — AI Product-specific productization and governance requirements.

These concepts provide useful architecture context where an enterprise adopts them, while the Data Management requirements remain applicable at enterprise level. Analytics and AI initiatives may additionally be subject to applicable Information/Analytics and AI semantic, architecture, Product, and governance frameworks; those additional obligations do not replace this enterprise Data Management baseline.

---

## 10. Foundational Statement

> Enterprise data must remain understandable, owned, trustworthy, governed, traceable, appropriately controlled, and intentionally consumable throughout its lifecycle.
