---
id: hdip-cla-0.1-m15-v04-registry-resolution-projection-compilation
title: HDIP-CLA 0.1 — M15-V04 Registry, Resolution, Projection & Compilation
sidebar_label: M15-V04 — Registry & Compilation Diagram
description: Enterprise semantic corpus, canonical logical Registries, governed resolution, HDIP projections and applicable Product-family descriptors.
---

# HDIP-CLA 0.1 — M15-V04 Registry, Resolution, Projection & Compilation

**Status:** Presentation-only illustration of **M15-V04**; not an amendment to frozen normative architecture.  
**Architecture authority:** [M09 — Registry, Descriptor, Projection & Compilation](/docs/architecture/cla/hdip-cla-0.1-m09-registry-descriptor-projection-compilation-architecture) · [M15 — Canonical Reference Views](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views) · [M17 — Frozen Authority](/docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze).

**Question answered:** How does HDIP ground an intent in externally governed meaning, resolve authoritative references, and produce operational projections and realization instructions **without becoming the source of semantic, Product or policy authority**?

[![M15-V04: external Enterprise Semantic Corpus, five core HDIP logical registries and Data-profile ADS Registry, P1/P2 resolution, canonical HDIP outputs, applicable Product-family descriptors and Intelligence Product ontology boundaries](/img/hdip/cla/hdip-cla-0.1-m15-v04-registry-resolution-projection-compilation-preview.png)](/img/hdip/cla/hdip-cla-0.1-m15-v04-registry-resolution-projection-compilation.svg)

**Diagram resources:** [Open full-size SVG](/img/hdip/cla/hdip-cla-0.1-m15-v04-registry-resolution-projection-compilation.svg) · [Download editable draw.io XML](/diagrams/hdip-cla/0.1/hdip-cla-0.1-m15-v04-registry-resolution-projection-compilation.drawio.xml) · [Read frozen M15-V04 definition](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views).

## Semantic grounding: governed meaning precedes compilation

The **Enterprise Semantic Corpus** in the illustration encompasses applicable authoritative enterprise and domain ontologies, business dictionaries/glossaries, capability models, semantic relationships, constraints, reference/domain models and semantic mappings. These assets make business-native intent intelligible by providing **versioned meanings, typed relationships and governed context**, rather than by guessing relationships from similarly named data fields.

The Corpus is an **illustrative external authority context**, **not** an additional canonical HDIP Registry, Plane, physical knowledge graph or new HDIP authority. Applicable source semantics remain governed by GEDRM, GEARM, GEAIRM and enterprise/domain authorities. HDIP P1/P2 references and resolves these definitions; uncertain or contradictory interpretations require governed validation, not silent invention.

## Core Registries versus Data-profile ADS

M09 freezes **five core logical Registries**: **HDIP-REG-01 Product**, **REG-02 Schema**, **REG-03 Policy**, **REG-04 Capability** and **REG-05 Blueprint**. **HDIP-REG-D01 ADS Registry** is a **Data Profile only** specialization. A single physical technology may implement several logical Registry responsibilities, but it does not collapse their registration contracts or authority boundaries.

A Registry can be authoritative about its own governed **registration fact**, identifier, version and currentness without becoming the author of the registered subject's Product qualification, semantic definition, policy meaning or source authority.

**Registry ≠ Catalog ≠ Marketplace.** A Catalog is a discovery projection; a Marketplace is a consumption/acquisition experience. **Latest** and **governed-current** are also separate states.

## P1/P2 reference resolution and compilation

The five coloured workflow boxes are **illustrative responsibility groupings** mapped to **P1** and **P2**, not additional Planes, lifecycle stages or a mandatory physical process pipeline. They emphasize context grounding, governed discovery, typed dependency and compatibility assessment, projection formation, compilation and Blueprint binding.

The seven canonical M09 artifacts have deliberately distinct responsibilities:

| HDIP artifact | Architectural meaning |
|---|---|
| **RRG** | Resolved Realization Graph; typed resolved dependencies, bindings and authoritative references |
| **HPD** | HDIP Product Descriptor; operational projection *about* an applicable Product Version, not the Product or Product qualification authority |
| **RGB** | Resolved Governance Bundle; compiled applicable governance context |
| **SYNCTX** | Synthetic context/projection **only when justified and applicable** |
| **Realization Plan** | Governed family-neutral logical realization instructions |
| **Blueprint Binding** | Explicit versioned realization/capability/Blueprint binding, distinct from merely selecting a Blueprint |
| **Compilation Record** | Correlation of material source/reference versions, rules, decisions and outputs for historical reconstruction |

These outputs may have different production and reference dependencies. Their side-by-side display **does not mandate a single execution ordering**. Compilation is not automatically assurance or authority approval.

## Product-family descriptors, realization and trust

The separate **PROD / PDS / DPP** grouping is **applicability-driven** and belongs to relevant Product-family and adjacent specifications, not to an invented uniform HDIP document taxonomy:

- **PROD — Product Semantic Descriptor:** a *descriptive umbrella label* in this view for applicable family-specific semantic descriptors such as **DPROD** or **AIPROD**, where those specifications define them. It is not a new mandatory generic descriptor introduced by HDIP.
- **PDS — Product Deployment Specification:** a family/profile realization/deployment descriptor such as **DPDS** or **AIPDS**, as defined by its applicable specification.
- **DPP — Digital Product Passport:** family/trust-specific provenance, qualification, governance or attestation context where applicable; it is not universally required simply because a Product is present in HDIP.

**HPD is the canonical HDIP operational Product projection**, not generic **PD**, and does not replace PROD, PDS or DPP. The figure therefore places HPD with the canonical M09 outputs and family descriptors in a different bounded group. The Product Registry may reference HPD and family-authoritative artifacts without acquiring their semantic authority.

## Intelligence Product versus Model Product

Intelligence is **not synonymous with trained ML model execution**. Applicable AI Product ontologies include model-based, symbolic, knowledge reasoning, planning, search and hybrid primitives, with independent qualification and evidence requirements. A governed downloadable model may constitute a **Model Product** without independently qualifying as an **AI Product**. Equally, AI used as one constituent does not automatically reclassify a Data, Information, Service or Compound Product into the AI Product Family.

The Intelligence/AI panel is consequently capability-oriented: **intelligence proposition, qualifying primitive constitution and dependencies, reasoning/inference/planning/agency, evaluation, family descriptor and realization references**. This visual **does not** define AI Product qualification; BPS/PIN, AIPS and applicable family authorities do.

## Architecture and preservation notes

- **P1–P5** are the existing five canonical Planes. **X1–X9** are cross-cutting obligations. **HDIP-FND** is an enabling Foundation, not an authority.
- The illustration makes no physical topology or single-registry implementation prescription and does not certify an HDIP realization.
- The presentation-only V04 asset and companion page do **not modify** M09, M15, M17 or any A1–A15 executable specifications.
- This view complements [M15-V03 — Symbiant-led PDEP](/docs/architecture/cla/views/hdip-cla-0.1-m15-v03-product-development-evolution): V03 depicts the Product creation experience; V04 depicts the semantic/reference/compilation responsibilities supporting it. The [M15-V01 logical architecture](/docs/architecture/cla/views/hdip-cla-0.1-m15-v01-canonical-logical-platform) remains the principal platform overview.
