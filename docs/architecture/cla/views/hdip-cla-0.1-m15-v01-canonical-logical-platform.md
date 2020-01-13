---
id: hdip-cla-0.1-m15-v01-canonical-logical-platform
title: HDIP-CLA 0.1 — M15-V01 Canonical Logical Platform View
sidebar_label: M15-V01 — Canonical Platform Diagram
description: Illustration of the frozen HDIP canonical logical architecture, preserving semantic, Product, and enterprise authorities.
---

# HDIP-CLA 0.1 — M15-V01 Canonical Logical Platform View

**Status:** HDIP-CLA 0.1 canonical Reference View illustration — presentation-only companion.  
**Architecture authority:** Frozen [M15 Reference View](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views) and [M17 architecture baseline](/docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze).

The following diagram presents **one holistic enterprise logical architecture across Data, Information and Intelligence**, composing GEDRA, GEARA and GEAIRA responsibilities while preserving the independent semantic, Product, policy, source and Decision authorities that HDIP references.

[![HDIP-CLA M15-V01 canonical logical platform diagram with five logical Planes, nine cross-cutting Overlays, one Foundation, and external authorities](/img/hdip/cla/hdip-cla-0.1-m15-v01-canonical-logical-platform-preview.png)](/img/hdip/cla/hdip-cla-0.1-m15-v01-canonical-logical-platform.svg)

**Diagram resources:** [Open full-size SVG](/img/hdip/cla/hdip-cla-0.1-m15-v01-canonical-logical-platform.svg) · [Download editable draw.io XML](/diagrams/hdip-cla/0.1/hdip-cla-0.1-m15-v01-canonical-logical-platform.drawio.xml) · [Read the normative M15 view description](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views).

## How to read the diagram

| Region | Architectural meaning |
|---|---|
| External authority context | GEDRM, GEARM, GEAIRM, GEDRA, GEARA, GEAIRA, and applicable enterprise/adjacent authorities remain outside HDIP ownership. |
| BPS/PIN and Product-family ribbon | Orthogonal Product semantics and qualification lens; not an additional Plane. |
| P1 — Governed Intent, Definition & Authority Context | Governed intent, semantic reference/design context, and authority/accountability context. |
| P2 — Discovery, Composition & Realization | Discovery, dependency/composition, validation/compilation, and realization binding. |
| P3 — Runtime, Formation & Execution | Separately identifiable Data processing, Information formation, and Intelligence execution responsibilities within one Plane. |
| P4 — Provision, Consumption & Integration | Interface exposure, governed consumer access and consumption, and downstream integration. |
| P5 — Outcome, Value & Evolution | Outcome/effectiveness/feedback and value assessment/evolution. |
| X1–X9 | Nine orthogonal cross-cutting responsibilities, applicable across the logical architecture; not nine centralized services. |
| HDIP-FND | Shared Platform / Utility Foundation enabling realization without creating semantic or governance authority. |

The visual presents the frozen **five Planes, nine Overlays, 22 logical ABBs, and one shared Foundation**. Data, Information and Intelligence colours distinguish responsibility emphasis; they do **not** partition HDIP into three separate architectures.

## Modelling boundaries

- A **Plane** is not a deployment tier; an **ABB** is not a physical application or service.
- The displayed arrangement is **not** a mandatory sequential execution pipeline. Canonical logical interactions are defined separately in M12.
- PDEP is Product Development & Evolution; CEP is Consumer Experience Projection. Neither is a canonical HDIP Plane.
- A Registry, Marketplace, operational projection or compiled artifact does not automatically acquire authority or establish Product qualification.
- Shared realization, co-location and presentation do not transfer semantic, Product, source, policy or consequential Decision/Action jurisdiction.
- The diagram is a **projection of** the frozen architecture; it neither adds requirements nor establishes M16 implementation conformance.

## Provenance and revision policy

This presentation companion preserves the user-refined SVG and editable draw.io source. Visual refinements may adjust legibility, spacing or colour without changing architecture meaning. Any change to canonical identifiers, invariant meaning, jurisdiction or logical architecture remains governed by the frozen M17 baseline and its amendment policy.

The legacy high-level HDIP images remain in the [executive HDIP introduction](/docs/foundations/hdip-brief) for conceptual and historical context; they must not be read as substitutes for M15-V01.

**Visual notice:** Copyrighted material 2017-2019 kivanura.org Kaizen (also displayed in the figure footer).
