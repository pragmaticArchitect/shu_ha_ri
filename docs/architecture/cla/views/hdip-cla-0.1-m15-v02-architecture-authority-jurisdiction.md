---
id: hdip-cla-0.1-m15-v02-architecture-authority-jurisdiction
title: HDIP-CLA 0.1 — M15-V02 Architecture Authority & Jurisdiction View
sidebar_label: M15-V02 — Authority & Jurisdiction Diagram
description: Presentation-only view of HDIP composition of GEDRA, GEARA and GEAIRA while preserving external semantic, Product and enterprise authority.
---

# HDIP-CLA 0.1 — M15-V02 Architecture Authority & Jurisdiction View

**Status:** Canonical Reference View **illustration** — presentation-only companion to frozen M15-V02.  
**Architecture authority:** [M15 — Canonical Reference Views](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views) · [M13 — External & Adjacent-System Boundary Model](/docs/architecture/cla/hdip-cla-0.1-m13-external-adjacent-system-boundary-model) · [M17 — Frozen Architecture](/docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze).

**Question answered by M15-V02:** Which authority remains outside HDIP, what responsibility belongs to HDIP, and where do the jurisdiction boundaries meet?

The illustration shows **GEDRA, GEARA and GEAIRA as independently governed peer reference architectures**, with externally governed **GEDRM, GEARM and GEAIRM semantic authorities**. HDIP composes and realizes their applicable Data, Information and Intelligence architectural responsibilities as **one enterprise logical platform**; composition does not transfer semantic, Product, policy, source or consequential Decision/Action authority.

[![HDIP-CLA M15-V02: external semantic and Product authorities, peer GEDRA/GEARA/GEAIRA reference architectures, and their composition in one HDIP logical platform](/img/hdip/cla/hdip-cla-0.1-m15-v02-architecture-authority-jurisdiction-preview.png)](/img/hdip/cla/hdip-cla-0.1-m15-v02-architecture-authority-jurisdiction.svg)

**Diagram resources:** [Open full-size SVG](/img/hdip/cla/hdip-cla-0.1-m15-v02-architecture-authority-jurisdiction.svg) · [Download editable draw.io XML](/diagrams/hdip-cla/0.1/hdip-cla-0.1-m15-v02-architecture-authority-jurisdiction.drawio.xml) · [Read the frozen M15-V02 definition](/docs/architecture/cla/hdip-cla-0.1-m15-canonical-reference-views).

## How to read the jurisdictions

| Region | What it means — and does not mean |
|---|---|
| GEDRM · GEARM · GEAIRM | Independently governed semantic references for Data, Information/Analytics and Intelligence. HDIP references and operationalizes them; it does not annex their semantics. |
| BPS/PIN and applicable Product-family authorities | Generic Product ontology, Intrinsic Nature and qualification remain external. Registration, compilation and deployment do not qualify a Product automatically. The left-hand Product lens is a **visual perspective**, not an HDIP authority transfer or sixth Plane. |
| GEDRA · GEARA · GEAIRA | Independent peer architecture jurisdictions for Data, Information/Analytics and Intelligence responsibilities, respectively. HDIP co-realization does not merge them. |
| Enterprise / adjacent authorities | Legal/policy/control, authoritative producers/sources, identity/security/entitlements, consequential Decision/Action and standards remain independently governed. |
| HDIP P1–P5 | The five logical Planes compose and realize the applicable responsibilities; they are **not** sequential deployment tiers. |
| HDIP X1–X9 | Nine cross-cutting Overlays apply across their relevant logical responsibilities; they do not denote nine central services. |
| HDIP-FND | Shared Platform / Utility Foundation enables realization, not semantics, qualification or enterprise accountability. |

## Principal jurisdiction crossings

M15-V02 draws primarily on the M13 Boundary Families below; the visual's short boundary captions are not replacements for their full frozen definitions.

| Boundary | External jurisdiction |
|---|---|
| `HDIP-BND-01` — Semantic Authority | GEDRM, GEARM, GEAIRM and applicable semantic authorities |
| `HDIP-BND-02` — Product & Product-Family Authority | BPS/PIN and applicable Product-family specifications |
| `HDIP-BND-03` — Peer Reference Architecture | GEDRA, GEARA, GEAIRA |
| `HDIP-BND-04` — External Standard & Vocabulary | Applicable externally governed standards and vocabularies |
| `HDIP-BND-05` — Enterprise Policy, Legal & Control Authority | Policy, risk, legal, regulatory and control owners |
| `HDIP-BND-06` — Identity, Security, Privacy & Entitlement | Enterprise identity, security and entitlement systems |
| `HDIP-BND-07` — Authoritative Producer / Source System | Systems of record and authoritative producer/source domains |
| `HDIP-BND-11` — Decision, Action & Consequence | Point-of-use consequential authorization and accountable Decision/Action systems |

The figure does **not** exhaust the twelve M13 Boundary Families or specify the complete M12 Interaction Contract topology. A boundary is a jurisdiction/responsibility/contract distinction, not necessarily a network gateway or physically separate system.

## Interpretation safeguards

- **Semantic projection ≠ semantic authority.** HDIP may store, map and compile externally governed semantics without becoming their owner.
- **Product registration ≠ Product qualification.** Product identity and eligibility follow BPS/PIN and applicable family specifications.
- **Source authority ≠ Product ownership.** An authoritative upstream source and a governed Product are distinct constructs.
- **Policy resolution/enforcement ≠ policy ownership.** IAM and entitlement infrastructure do not automatically acquire delegated policy or consequential Decision authority.
- **Product access ≠ consequential Decision/Action authorization.** They are separately governed and must be checked at appropriate points of use.
- **Architecture composition ≠ equivalence or jurisdiction transfer.** Peer reference architecture responsibilities remain traceable and independently governed.

## Relationship to M15-V01

[M15-V01 — Canonical Logical Platform View](/docs/architecture/cla/views/hdip-cla-0.1-m15-v01-canonical-logical-platform) answers **what constitutes HDIP** (five Planes, nine Overlays, 22 ABBs and Foundation). **M15-V02** answers **which independent authorities and peer architectures HDIP composes with**. The two are complementary projections of the **same frozen M17 architecture**.

## Visual status and provenance

The **user-refined SVG and editable draw.io XML are preserved exactly as supplied**; the optimized PNG is only a website preview. The diagram is a presentation projection of frozen M15/M17, **not** a new normative architecture, a vendor topology, a mandatory runtime sequence, or evidence of M16 implementation conformance.

**Visual notice:** Copyrighted material 2017-2019 kivanura.org Kaizen (also shown in the figure footer).
