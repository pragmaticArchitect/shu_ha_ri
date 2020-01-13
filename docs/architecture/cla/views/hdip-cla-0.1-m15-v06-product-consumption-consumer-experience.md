---
id: hdip-cla-0.1-m15-v06-product-consumption-consumer-experience
title: HDIP-CLA 0.1 — M15-V06 Product Consumption & Consumer Experience
sidebar_label: M15-V06 — Product Consumption & Consumer Experience Diagram
description: Product-consumption and consumer-experience view showing the frozen eight-stage SSCF lifecycle, CEP experience projection, multiple entry modes and the optional governed transition from consumption into PDEP.
---

# HDIP-CLA 0.1 — M15-V06 Product Consumption & Consumer Experience

**Status:** Presentation-only M15-V06 visual; no change to the frozen architecture.  
**Authority:** [M11 — Product Consumption & Runtime Architecture — SSCF / CEP](/docs/architecture/cla/hdip-cla-0.1-m11-sscf-cep-architecture) · [M12 — Inter-Plane Interaction Model](/docs/architecture/cla/hdip-cla-0.1-m12-canonical-inter-plane-interaction-model) · [M15 — Canonical Reference Views](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views) · [M17 — Frozen Baseline](/docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze).

**Question addressed:** How does a Product Consumer move from intent to governed consumption, evidence and feedback through SSCF and CEP, while preserving the optional path from discovery/consumption into intentional Product creation or evolution?

[![HDIP M15-V06 Product Consumption & Consumer Experience: SSCF and CEP across the five Planes, with three entry modes, eight canonical stages, CEP channels and optional PDEP transition](/img/hdip/cla/hdip-cla-0.1-m15-v06-product-consumption-consumer-experience-preview.png)](/img/hdip/cla/hdip-cla-0.1-m15-v06-product-consumption-consumer-experience.svg)

**Resources:** [Full-resolution SVG](/img/hdip/cla/hdip-cla-0.1-m15-v06-product-consumption-consumer-experience.svg) · [Editable draw.io XML](/diagrams/hdip-cla/0.1/hdip-cla-0.1-m15-v06-product-consumption-consumer-experience.drawio.xml) · [Frozen M15-V06 view definition](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views).

## What the view makes explicit

- **Eight-stage SSCF lifecycle:** Consumption Intent → Discovery & Resolution → Fit & Access Decision → Access Establishment → Consumption Execution → Evidence & Usage Record → Outcome & Feedback → Continuation / Re-entry / Evolution.
- **Three valid entry modes:** intent-first, browse-first and established-state reuse.
- **Consumer-facing CEP:** a projection/experience composition spanning P2 discovery, P4 access/consumption and P5 feedback, not a sixth Plane.
- **Purpose-neutral discovery:** discovery may lead either to pure consumption or to an accountable decision to enter PDEP for a new/evolved Product.
- **Governed consumption artifacts:** CIR, Product Resolution Set, Access Decision, Access Descriptor, Usage Contract, runtime/usage evidence and feedback signals.
- **Authority preservation:** consumption, discovery and output reuse do not automatically constitute a new Product or confer delegated consequential Decision/Action authority.

## P2 and P4 discovery distinction

The view intentionally shows both:

- **P2 governed discovery/resolution** responsibilities, where candidate Products, fit and constraints are resolved in architecture-governed terms; and
- **P4 consumer-facing discovery/selection/access/consumption** experiences, where those capabilities are presented through CEP in human, system or agent-mediated channels.

This avoids the false choice between “discovery is only creation-side” and “discovery is only consumption-side.” In HDIP, discovery supports **both** product-creation journeys and pure consumption journeys.

## Optional transition to PDEP

A Consumer may simply access and use an existing Product. Equally, discovery, repeated use or feedback may reveal the need for a richer or different Product. In that case the accountable participant may intentionally enter **PDEP (M10)**. That transition is **optional and governed**; SSCF itself does not qualify or constitute the new Product.
