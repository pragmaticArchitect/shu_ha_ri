---
id: hdip-cla-0.1-m02-upstream-responsibility-intake
title: HDIP-CLA 0.1 M02 — Upstream Architecture Responsibility Intake
sidebar_label: M02 — Upstream Responsibility Intake
---

# HDIP-CLA 0.1 M02 — Upstream Architecture Responsibility Intake

**Status:** Draft baseline for review.

## 1. Purpose

M02 establishes the provenance-preserving intake corpus from the three generic reference architectures that HDIP may realize or profile:

- **GEDRA** — Generic Enterprise Data Reference Architecture;
- **GEARA** — Generic Enterprise Analytics / Information Reference Architecture;
- **GEAIRA** — Generic Enterprise AI Reference Architecture.

M02 is deliberately an **intake stage, not a convergence stage**. It records the responsibilities and cross-cutting structures that must be considered by later HDIP-CLA analysis without deciding that similarly named responsibilities are equivalent, mergeable, shared, or candidates for the same HDIP plane/ABB.

## 2. Intake principle

> **Preserve source responsibility before interpreting platform realization.**

```text
GEDRA source obligations ──┐
GEARA source obligations ──┼──> M02 provenance corpus
GEAIRA responsibilities  ──┘
                                  |
                                  v
                         M03 existing HDIP inventory
                                  |
                                  v
                         M05 convergence/separation
                                  |
                                  v
                         M06+ HDIP architecture
```

## 3. Source granularity is intentionally asymmetric

The three source architectures do not encode responsibility at identical granularity:

- GEDRA expresses much of its detailed obligation through plane definitions and minimum conformance expectations.
- GEARA expresses explicit plane responsibilities plus cross-cutting Fabric and Foundation responsibilities.
- GEAIRA freezes **96 explicitly identified canonical plane Architectural Responsibilities** and **8 Cross-Cutting Overlays**.

M02 therefore does **not** normalize source strength or granularity. Local `INTAKE` identifiers below exist only to make GEDRA/GEARA source statements traceable inside HDIP-CLA; they do not become new GEDRA/GEARA canonical identifiers.

## 4. Source architecture inventory

| Source | Primary structures ingested | Detailed responsibility/obligation corpus used by M02 |
|---|---|---:|
| GEDRA 0.1 | 6 logical planes + Cross-Cutting Governance & Control + Technology / Utility Foundation | 106 source conformance obligations |
| GEARA 0.1 | 5 responsibility planes + 5 cross-cutting Fabrics + Shared Platform / Utility Foundation | 134 responsibility/fabric/foundation statements |
| GEAIRA 0.1 | 7 planes + 8 cross-cutting overlays | 96 canonical plane Architectural Responsibilities |
| **Total intake statements** | source structures preserved independently | **336** |

The numerical total is an inventory count only. It MUST NOT be interpreted as a maturity score, weighting, coverage percentage or proof that one source architecture is more detailed/important than another.

## 5. M02 normative intake rules

**HDIP-CLA-M02-R01 — Intake Before Convergence.** M02 SHALL preserve source responsibilities before any merge, rationalization or HDIP plane assignment.

**HDIP-CLA-M02-R02 — Source Authority Preservation.** Intake SHALL NOT modify the meaning or authority of GEDRA, GEARA or GEAIRA source responsibilities.

**HDIP-CLA-M02-R03 — Provenance Required.** Every intake item SHALL retain a source architecture and source plane/fabric/overlay/foundation reference.

**HDIP-CLA-M02-R04 — Local Identifier Non-Authority.** HDIP-CLA-generated `INTAKE` identifiers for source statements without canonical upstream IDs are traceability aids only and SHALL NOT be represented as upstream canonical identifiers.

**HDIP-CLA-M02-R05 — No Label Equivalence.** Similar labels across GEDRA, GEARA and GEAIRA SHALL NOT by themselves establish equivalent responsibility.

**HDIP-CLA-M02-R06 — Granularity Preservation.** Differences in source responsibility granularity SHALL be preserved through M02 and SHALL NOT be hidden by forced normalization.

**HDIP-CLA-M02-R07 — Plane Non-Equivalence.** Source plane numbering or lexical similarity SHALL NOT imply cross-architecture plane equivalence.

**HDIP-CLA-M02-R08 — Cross-Cutting Preservation.** GEDRA cross-cutting concerns, GEARA Fabrics and GEAIRA overlays SHALL remain visible as cross-cutting source obligations rather than being silently localized into candidate HDIP planes.

**HDIP-CLA-M02-R09 — Foundation Preservation.** Source utility/foundation responsibilities SHALL remain distinguishable from semantic, Product, governance and authority responsibilities.

**HDIP-CLA-M02-R10 — Product Authority Preservation.** Product-related source responsibilities SHALL NOT transfer BPS/PIN or Product-family semantic authority to HDIP.

**HDIP-CLA-M02-R11 — Many-to-Many Mapping Allowed.** A later HDIP responsibility MAY trace to multiple source responsibilities and one source responsibility MAY be realized across multiple HDIP constructs.

**HDIP-CLA-M02-R12 — No Premature ABB Admission.** M02 source nouns, capabilities or responsibilities SHALL NOT automatically become HDIP ABBs.

**HDIP-CLA-M02-R13 — No HDIP Plane Derivation in M02.** M02 SHALL NOT freeze an HDIP plane count, plane name or source-to-HDIP plane mapping.

**HDIP-CLA-M02-R14 — Lexical Recurrence Is Evidence Only.** Recurring concerns such as governance, lifecycle, provenance, observability, discovery or consumption MAY be flagged for later analysis but SHALL NOT be merged until M05 convergence/separation analysis.

## 6. GEDRA 0.1 intake structure

GEDRA contributes six logical Data architecture planes plus one cross-cutting governance/control concern and a Technology / Utility Foundation.

| Source ID | Source structure | M02 treatment |
|---|---|---|
| `GEDRA-PL-001` | Semantic & Enterprise Ontology Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.1. |
| `GEDRA-PL-002` | Authority Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.2. |
| `GEDRA-PL-003` | Processing, Provision & Movement Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.3. |
| `GEDRA-PL-004` | Data Platform & Product Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.4. |
| `GEDRA-PL-005` | Consumption & Access Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.5. |
| `GEDRA-PL-006` | Value, Observability & Feedback Plane | Preserve as source responsibility group; intake detailed conformance obligations from section 6.6. |
| `GEDRA-XC-001` | Cross-Cutting Governance & Control | Preserve as source responsibility group; intake detailed conformance obligations from section 7. |
| `GEDRA-TF-001` | Technology / Utility Foundation | Preserve as source responsibility group; intake detailed conformance obligations from section 8. |

### 6.1 GEDRA detailed intake obligations

The items below preserve the source minimum-conformance statements as M02 responsibility-intake atoms. `INTAKE` IDs are HDIP-CLA traceability identifiers only.

#### GEDRA-PL-001 — Semantic & Enterprise Ontology Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P1-INTAKE-01` | governed business meaning is identifiable independently of physical implementation. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-02` | key enterprise/domain concepts have explicit definitions. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-03` | material semantic relationships can be represented. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-04` | semantic classifications align with GEDRM where GEDRM applies. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-05` | orthogonal GEDRM classification dimensions are not incorrectly collapsed. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-06` | mappings between materially different representations are explicit where required. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-07` | semantic ownership or stewardship can be identified under the enterprise governance model. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-08` | semantic change can be governed and impact-assessed. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-09` | the architecture distinguishes semantic authority from operational or sourcing authority. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-10` | data products and consumer interfaces can reference governed semantics. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-11` | external-standard mappings do not silently assert equivalence. | GEDRA 6.1 minimum conformance expectations |
| `GEDRA-P1-INTAKE-12` | application or technology models are not treated as the sole enterprise semantic authority by default. | GEDRA 6.1 minimum conformance expectations |

#### GEDRA-PL-002 — Authority Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P2-INTAKE-01` | material authority is explicitly scoped. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-02` | Data Originator and Data Producer are not silently assumed equivalent. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-03` | System of Record and Authoritative Source are distinguished. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-04` | Source of Authority can be identified for material authority designations. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-05` | authoritative and authorized are distinguished. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-06` | derived, mastered, replicated, or cached data does not gain authority implicitly. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-07` | authority may be distributed across lifecycle stages or attributes. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-08` | downstream consumers can identify relevant authoritative sourcing context. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-09` | authority changes can be impact-assessed. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-10` | HDIP ADS/ADO terminology is treated as specialization rather than generic GEDRA terminology. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-11` | ADD is not treated as authoritative merely because it is authorized to distribute. | GEDRA 6.2 minimum conformance expectations |
| `GEDRA-P2-INTAKE-12` | architecture documentation does not rely on vague phrases such as "single source of truth" without defining semantic and authority scope. | GEDRA 6.2 minimum conformance expectations |

#### GEDRA-PL-003 — Processing, Provision & Movement Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P3-INTAKE-01` | transformation, transport, provision, publication, distribution, and brokerage can be distinguished. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-02` | `Data Transformer` is used instead of technical misuse of `Data Processor`. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-03` | Data Provider and Data Publisher are not silently treated as equivalent. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-04` | Data Transport / Relay and Data Distributor are distinguishable. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-05` | a technical message broker is not automatically modeled as a Data Broker. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-06` | transformations preserve or explicitly map semantic meaning. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-07` | derivation is traceable where material. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-08` | processing or distribution does not confer authority implicitly. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-09` | publication and distribution can reference relevant Data Contracts and policy obligations. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-10` | copies, caches, and replicas retain explicit lineage and authority status. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-11` | movement across trust or jurisdictional boundaries can carry applicable governance obligations. | GEDRA 6.3 minimum conformance expectations |
| `GEDRA-P3-INTAKE-12` | consumer-facing changes can be impact-assessed and versioned where required. | GEDRA 6.3 minimum conformance expectations |

#### GEDRA-PL-004 — Data Platform & Product Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P4-INTAKE-01` | Data Object, Data Asset, and Data Product are distinguishable. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-02` | Data Product is treated as an intentional specialization of Data Asset. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-03` | productization is consumer- and obligation-driven rather than automatic. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-04` | platform capabilities are not silently treated as Data Products. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-05` | a Data Product has accountable ownership. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-06` | a Data Product has explicit identity and lifecycle. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-07` | material consumer-facing commitments can be expressed through a Product Promise and/or Data Contract. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-08` | output ports are distinguishable from the product itself. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-09` | discoverability does not require a marketplace. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-10` | metadata, lineage, quality, and observability responsibilities are supported. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-11` | authority status remains explicit and is not implied by productization. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-12` | policy, controls, and evidence can be integrated into product lifecycle where required. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-13` | product changes can be impact-assessed. | GEDRA 6.4 minimum conformance expectations |
| `GEDRA-P4-INTAKE-14` | business-product and data-product semantics remain distinct. | GEDRA 6.4 minimum conformance expectations |

#### GEDRA-PL-005 — Consumption & Access Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P5-INTAKE-01` | Data Recipient and Data Consumer can be distinguished. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-02` | intended consumers and use are identifiable for material data sharing. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-03` | consumer class can influence architectural obligations. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-04` | discovery and entitlement are distinct. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-05` | consumers can assess suitability using appropriate metadata. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-06` | access mechanisms do not obscure semantics or authority context. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-07` | regulatory and other high-assurance consumers can receive stronger product, lineage, and evidence treatment where required. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-08` | local consumer copies retain explicit authority and lineage status. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-09` | least-privilege or minimum-necessary access can be applied where appropriate. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-10` | purpose limitation can be represented where required. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-11` | access can be lifecycle-managed and revoked. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-12` | consumer changes and downstream dependencies can be impact-assessed. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-13` | consumer feedback can inform product and architecture evolution. | GEDRA 6.5 minimum conformance expectations |
| `GEDRA-P5-INTAKE-14` | access to data is not treated as equivalent to understanding or permission for unrestricted reuse. | GEDRA 6.5 minimum conformance expectations |

#### GEDRA-PL-006 — Value, Observability & Feedback Plane

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-P6-INTAKE-01` | material usage and operational behavior can be observed. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-02` | metrics are distinguishable from Data Controls. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-03` | observability signals are distinguishable from Control Evidence. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-04` | product health can be assessed against relevant Product Promise or contract commitments. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-05` | usage and value are not assumed equivalent. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-06` | cost and value are not assumed equivalent. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-07` | consumer feedback can be associated with affected assets, products, or interfaces. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-08` | relevant feedback can influence product, platform, governance, or architecture evolution. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-09` | product lifecycle decisions can consider active consumers and downstream dependencies. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-10` | regulatory or evidential use can retain reproducibility context where required. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-11` | optimization does not silently bypass governance or authority obligations. | GEDRA 6.6 minimum conformance expectations |
| `GEDRA-P6-INTAKE-12` | observability is treated as a decision-support capability rather than merely a dashboard layer. | GEDRA 6.6 minimum conformance expectations |

#### GEDRA-XC-001 — Cross-Cutting Governance & Control

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-XC-INTAKE-01` | governance applies across all GEDRA planes rather than only downstream. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-02` | material Data Assets and Data Products have accountable ownership. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-03` | Data Controls have Control Owners. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-04` | Data Policy, Policy as Code, Data Contract, Data Quality Rule, Data Control, and Control Evidence are distinguishable. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-05` | controls can trace to governed expectations. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-06` | Control Evidence can identify the control it substantiates. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-07` | observability metrics and dashboards are not automatically treated as controls. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-08` | exceptions are explicit and governed. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-09` | remediation and escalation can occur where obligations fail. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-10` | authority designation is governed and scoped. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-11` | classification can drive access, retention, residency, security, and control obligations. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-12` | privacy roles remain distinct from technical operational roles. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-13` | governance artifacts are versionable and currentness can be determined where required. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-14` | material policy changes can be impact-assessed and propagated. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-15` | product-local executable governance can remain traceable to authoritative policy. | GEDRA 7 minimum conformance expectations |
| `GEDRA-XC-INTAKE-16` | governance tool choices do not redefine GEDRM/GEDRA semantics. | GEDRA 7 minimum conformance expectations |

#### GEDRA-TF-001 — Technology / Utility Foundation

| Intake ID | Source obligation | Source |
|---|---|---|
| `GEDRA-TF-INTAKE-01` | data architecture roles are distinguishable from implementation technologies. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-02` | platform/runtime services are treated as enabling capabilities. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-03` | storage technology does not imply authority. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-04` | messaging products are not automatically treated as GEDRM Data Brokers. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-05` | API infrastructure does not automatically define product or publisher semantics. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-06` | IAM implements access controls without replacing entitlement semantics. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-07` | observability tools do not automatically define controls or evidence. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-08` | policy engines remain traceable to authoritative Data Policy. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-09` | operational ownership is distinct from Data Ownership and Product Ownership. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-10` | technology change can occur without unnecessary semantic redefinition. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-11` | infrastructure choices can be impact-assessed across products, consumers, controls, and evidence. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-12` | AI runtime capabilities remain subject to ordinary data governance obligations. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-13` | trust boundaries and resilience obligations can be represented where material. | GEDRA 8 minimum conformance expectations |
| `GEDRA-TF-INTAKE-14` | technology does not become a substitute for GEDRM/GEDRA semantics. | GEDRA 8 minimum conformance expectations |

## 7. GEARA 0.1 intake structure

GEARA contributes five logical responsibility planes, five cross-cutting Fabrics and a Shared Platform / Utility Foundation.

| Source ID | Source structure | Responsibility statements ingested |
|---|---|---:|
| `GEARA-PL-001` | P1 — Intent, Semantics & Design | 13 |
| `GEARA-PL-002` | P2 — Discovery, Composition & Realization | 17 |
| `GEARA-PL-003` | P3 — Analytical Runtime & Information Formation | 17 |
| `GEARA-PL-004` | P4 — Provision, Consumption & Decision Integration | 12 |
| `GEARA-PL-005` | P5 — Outcome, Value & Evolution | 12 |
| `GEARA-FAB-001` | Governance / Policy / Assurance Fabric | 10 |
| `GEARA-FAB-002` | Security / Privacy / Entitlement Fabric | 10 |
| `GEARA-FAB-003` | Provenance / Evidence / Observability Fabric | 9 |
| `GEARA-FAB-004` | Quality / Trust Fabric | 11 |
| `GEARA-FAB-005` | Lifecycle / Version / Change Fabric | 11 |
| `GEARA-FND-001` | Shared Platform / Utility Foundation | 12 |

### 7.1 GEARA detailed intake statements

The statements below preserve the source responsibility/fabric/foundation lists. `INTAKE` IDs are HDIP-CLA traceability identifiers only.

#### GEARA-PL-001 — P1 — Intent, Semantics & Design

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-P1-INTAKE-01` | Information Need capture. | GEARA 6.2 |
| `GEARA-P1-INTAKE-02` | Analytical Intent definition. | GEARA 6.2 |
| `GEARA-P1-INTAKE-03` | Analytical Use Case definition. | GEARA 6.2 |
| `GEARA-P1-INTAKE-04` | Analytical Subject and Population definition. | GEARA 6.2 |
| `GEARA-P1-INTAKE-05` | governed semantic discovery and authoring. | GEARA 6.2 |
| `GEARA-P1-INTAKE-06` | Metric, Indicator, KPI, KRI, Threshold, Classification, Score, and State definition references. | GEARA 6.2 |
| `GEARA-P1-INTAKE-07` | expected Analytical Output definition. | GEARA 6.2 |
| `GEARA-P1-INTAKE-08` | analytical dependency declaration. | GEARA 6.2 |
| `GEARA-P1-INTAKE-09` | Information Proposition design. | GEARA 6.2 |
| `GEARA-P1-INTAKE-10` | Product Intent and Product Promise reference where Productization applies. | GEARA 6.2 |
| `GEARA-P1-INTAKE-11` | Consumer and access intent. | GEARA 6.2 |
| `GEARA-P1-INTAKE-12` | policy, quality, security, provenance, and lifecycle requirements. | GEARA 6.2 |
| `GEARA-P1-INTAKE-13` | versioned design metadata. | GEARA 6.2 |

#### GEARA-PL-002 — P2 — Discovery, Composition & Realization

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-P2-INTAKE-01` | Product discovery. | GEARA 6.4 |
| `GEARA-P2-INTAKE-02` | Semantic discovery. | GEARA 6.4 |
| `GEARA-P2-INTAKE-03` | Analytics Capability discovery. | GEARA 6.4 |
| `GEARA-P2-INTAKE-04` | AI Product discovery. | GEARA 6.4 |
| `GEARA-P2-INTAKE-05` | dependency resolution. | GEARA 6.4 |
| `GEARA-P2-INTAKE-06` | input and semantic binding. | GEARA 6.4 |
| `GEARA-P2-INTAKE-07` | analytical composition. | GEARA 6.4 |
| `GEARA-P2-INTAKE-08` | rules and Threshold binding. | GEARA 6.4 |
| `GEARA-P2-INTAKE-09` | AI Product invocation binding. | GEARA 6.4 |
| `GEARA-P2-INTAKE-10` | compatibility and impact analysis. | GEARA 6.4 |
| `GEARA-P2-INTAKE-11` | semantic, policy, security, quality, and runtime validation. | GEARA 6.4 |
| `GEARA-P2-INTAKE-12` | testing and simulation. | GEARA 6.4 |
| `GEARA-P2-INTAKE-13` | intent realization / compilation. | GEARA 6.4 |
| `GEARA-P2-INTAKE-14` | runtime binding. | GEARA 6.4 |
| `GEARA-P2-INTAKE-15` | deployment generation and release preparation. | GEARA 6.4 |
| `GEARA-P2-INTAKE-16` | registry registration. | GEARA 6.4 |
| `GEARA-P2-INTAKE-17` | change-impact analysis. | GEARA 6.4 |

#### GEARA-PL-003 — P3 — Analytical Runtime & Information Formation

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-P3-INTAKE-01` | governed input acquisition. | GEARA 6.6 |
| `GEARA-P3-INTAKE-02` | batch, streaming, event-driven, interactive, scheduled, continuous, or human-assisted execution. | GEARA 6.6 |
| `GEARA-P3-INTAKE-03` | Data Product consumption. | GEARA 6.6 |
| `GEARA-P3-INTAKE-04` | Information Product consumption. | GEARA 6.6 |
| `GEARA-P3-INTAKE-05` | AI Product invocation. | GEARA 6.6 |
| `GEARA-P3-INTAKE-06` | Metric calculation. | GEARA 6.6 |
| `GEARA-P3-INTAKE-07` | Indicator and Threshold evaluation. | GEARA 6.6 |
| `GEARA-P3-INTAKE-08` | rule execution. | GEARA 6.6 |
| `GEARA-P3-INTAKE-09` | classification and scoring. | GEARA 6.6 |
| `GEARA-P3-INTAKE-10` | detection and anomaly evaluation. | GEARA 6.6 |
| `GEARA-P3-INTAKE-11` | prediction and forecasting. | GEARA 6.6 |
| `GEARA-P3-INTAKE-12` | simulation and scenario execution. | GEARA 6.6 |
| `GEARA-P3-INTAKE-13` | assessment, interpretation, explanation, and synthesis. | GEARA 6.6 |
| `GEARA-P3-INTAKE-14` | analytical state management. | GEARA 6.6 |
| `GEARA-P3-INTAKE-15` | intermediate output handling. | GEARA 6.6 |
| `GEARA-P3-INTAKE-16` | runtime quality checks. | GEARA 6.6 |
| `GEARA-P3-INTAKE-17` | provenance, evidence, and operational telemetry emission. | GEARA 6.6 |

#### GEARA-PL-004 — P4 — Provision, Consumption & Decision Integration

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-P4-INTAKE-01` | direct Analytical Output provision. | GEARA 6.8 |
| `GEARA-P4-INTAKE-02` | Information Product output provision. | GEARA 6.8 |
| `GEARA-P4-INTAKE-03` | Output Port operation. | GEARA 6.8 |
| `GEARA-P4-INTAKE-04` | API, stream, event, query, subscription, notification, file, interactive, or agent interface provision. | GEARA 6.8 |
| `GEARA-P4-INTAKE-05` | Product discovery and marketplace integration. | GEARA 6.8 |
| `GEARA-P4-INTAKE-06` | Consumer discovery and onboarding. | GEARA 6.8 |
| `GEARA-P4-INTAKE-07` | Consumer entitlement enforcement. | GEARA 6.8 |
| `GEARA-P4-INTAKE-08` | Consumption Event capture. | GEARA 6.8 |
| `GEARA-P4-INTAKE-09` | interactive analytics. | GEARA 6.8 |
| `GEARA-P4-INTAKE-10` | Recommendation integration. | GEARA 6.8 |
| `GEARA-P4-INTAKE-11` | Decision-system integration. | GEARA 6.8 |
| `GEARA-P4-INTAKE-12` | Action and workflow integration. | GEARA 6.8 |

#### GEARA-PL-005 — P5 — Outcome, Value & Evolution

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-P5-INTAKE-01` | Outcome Observation integration. | GEARA 6.11 |
| `GEARA-P5-INTAKE-02` | Consumer Feedback. | GEARA 6.11 |
| `GEARA-P5-INTAKE-03` | Recommendation disposition analysis. | GEARA 6.11 |
| `GEARA-P5-INTAKE-04` | Decision and Action Feedback. | GEARA 6.11 |
| `GEARA-P5-INTAKE-05` | false-positive and false-negative evidence. | GEARA 6.11 |
| `GEARA-P5-INTAKE-06` | analytical effectiveness assessment. | GEARA 6.11 |
| `GEARA-P5-INTAKE-07` | Information Product effectiveness assessment. | GEARA 6.11 |
| `GEARA-P5-INTAKE-08` | Value evidence and Value assessment. | GEARA 6.11 |
| `GEARA-P5-INTAKE-09` | usage interpretation. | GEARA 6.11 |
| `GEARA-P5-INTAKE-10` | Outcome attribution evidence. | GEARA 6.11 |
| `GEARA-P5-INTAKE-11` | drift evidence. | GEARA 6.11 |
| `GEARA-P5-INTAKE-12` | evolution triggers and change proposals. | GEARA 6.11 |

#### GEARA-FAB-001 — Governance / Policy / Assurance Fabric

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FAB1-INTAKE-01` | policy. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-02` | control. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-03` | regulatory constraints. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-04` | semantic governance. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-05` | Product governance integration. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-06` | approvals where judgement is required. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-07` | exception and waiver handling. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-08` | assurance. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-09` | conformance. | GEARA 6.12 |
| `GEARA-FAB1-INTAKE-10` | segregation of duties. | GEARA 6.12 |

#### GEARA-FAB-002 — Security / Privacy / Entitlement Fabric

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FAB2-INTAKE-01` | identity. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-02` | authentication. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-03` | authorization. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-04` | entitlement. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-05` | purpose limitation. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-06` | privacy. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-07` | confidentiality. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-08` | data minimization. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-09` | sensitive metadata protection. | GEARA 6.13 |
| `GEARA-FAB2-INTAKE-10` | provenance access control. | GEARA 6.13 |

#### GEARA-FAB-003 — Provenance / Evidence / Observability Fabric

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FAB3-INTAKE-01` | Definition Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-02` | Semantic Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-03` | Logic and Method Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-04` | Product and AI Product Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-05` | Execution Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-06` | Consumption Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-07` | Decision and Action Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-08` | Outcome and Feedback Provenance. | GEARA 6.14 |
| `GEARA-FAB3-INTAKE-09` | operational telemetry. | GEARA 6.14 |

#### GEARA-FAB-004 — Quality / Trust Fabric

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FAB4-INTAKE-01` | input quality. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-02` | semantic quality. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-03` | analytical quality. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-04` | AI/model quality. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-05` | Information Product quality. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-06` | freshness. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-07` | completeness. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-08` | uncertainty. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-09` | reproducibility. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-10` | known limitations. | GEARA 6.15 |
| `GEARA-FAB4-INTAKE-11` | Fitness for Use. | GEARA 6.15 |

#### GEARA-FAB-005 — Lifecycle / Version / Change Fabric

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FAB5-INTAKE-01` | identity and version. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-02` | lifecycle state. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-03` | currentness. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-04` | compatibility. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-05` | deprecation. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-06` | retirement. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-07` | migration. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-08` | rollback. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-09` | resilience. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-10` | change impact. | GEARA 6.16 |
| `GEARA-FAB5-INTAKE-11` | historical interpretability. | GEARA 6.16 |

#### GEARA-FND-001 — Shared Platform / Utility Foundation

| Intake ID | Source responsibility / capability statement | Source |
|---|---|---|
| `GEARA-FND-INTAKE-01` | compute. | GEARA 6.17 |
| `GEARA-FND-INTAKE-02` | storage. | GEARA 6.17 |
| `GEARA-FND-INTAKE-03` | network. | GEARA 6.17 |
| `GEARA-FND-INTAKE-04` | messaging and eventing. | GEARA 6.17 |
| `GEARA-FND-INTAKE-05` | orchestration. | GEARA 6.17 |
| `GEARA-FND-INTAKE-06` | scheduling. | GEARA 6.17 |
| `GEARA-FND-INTAKE-07` | runtime hosting. | GEARA 6.17 |
| `GEARA-FND-INTAKE-08` | identity infrastructure. | GEARA 6.17 |
| `GEARA-FND-INTAKE-09` | secrets and key infrastructure. | GEARA 6.17 |
| `GEARA-FND-INTAKE-10` | logging and telemetry transport. | GEARA 6.17 |
| `GEARA-FND-INTAKE-11` | API/service infrastructure. | GEARA 6.17 |
| `GEARA-FND-INTAKE-12` | deployment infrastructure. | GEARA 6.17 |

## 8. GEAIRA 0.1 intake structure

GEAIRA contributes seven canonical planes and eight cross-cutting overlays. Its M17 baseline freezes 96 canonical plane Architectural Responsibilities, so M02 preserves the source responsibility IDs directly.

### 8.1 GEAIRA planes

| Plane | Canonical responsibilities |
|---|---:|
| P1 — AI Intent, Purpose & Authority | 12 |
| P2 — Knowledge, Context & Grounding | 13 |
| P3 — Intelligence Capability & Primitive | 13 |
| P4 — AI Execution, Agentic & Environment | 14 |
| P5 — AI Serving, Product & Integration | 14 |
| P6 — Decision, Action & Human Oversight | 14 |
| P7 — Evaluation, Assurance, Observability & Evolution | 16 |
| **Total** | **96** |

### 8.2 GEAIRA cross-cutting overlays

| ID | Overlay | Source scope |
|---|---|---|
| `X1` | Security, Privacy & Trust Boundaries | Confidentiality, integrity, isolation, privacy, trust boundaries, protected processing and security-relevant failure behavior. |
| `X2` | Identity, Authority & Policy Enforcement | Actor/resource identity, authority context, policy binding, authorization inputs, delegated authority and enforcement evidence. |
| `X3` | Evidence, Provenance & Traceability | Traceable inputs, outputs, decisions, actions, dependencies, provenance references, evidence chains and historical truth. |
| `X4` | Observability, Telemetry & Auditability | Material runtime/operational signals, auditability, monitoring, diagnostic context and evidence-producing telemetry. |
| `X5` | Resilience, Safety & Failure Management | Availability, degradation, fail-safe/fail-closed behavior, containment, recovery, uncertainty handling and operational/physical safety. |
| `X6` | Lifecycle, Version, Currentness & Change | Identity/version alignment, lifecycle state, currentness, compatibility, supersession, migration and change control. |
| `X7` | Interoperability, Contracts & Semantic Compatibility | Boundary contracts, semantic compatibility, interface obligations, protocol-neutral exchange and peer-architecture alignment. |
| `X8` | Governance, Human Accountability & Compliance | Human accountability, governance participation, review/escalation, policy/control evidence and regulatory/enterprise obligation alignment. |

### 8.3 GEAIRA canonical responsibility intake

The following source IDs remain canonical GEAIRA identifiers. M02 does not rename them.

#### P1 — AI Intent, Purpose & Authority

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P1-RESP-01` | Intended Purpose Declaration | Human & Governance | Baseline-mandatory | The governed AI use has an explicit intended purpose/scope traceable to an authoritative owner or mandate. |
| `P1-RESP-02` | Permitted / Prohibited Use Boundary | Authority & Control | Baseline-mandatory | Material allowed, disallowed and constrained uses can be determined for the governed scope. |
| `P1-RESP-03` | Authority Source & Accountability Binding | Human & Governance | Baseline-mandatory | The authoritative source and accountable human/organizational role for the governed AI use are identifiable. |
| `P1-RESP-04` | Delegated Authority Envelope | Authority & Control | Conditional-mandatory | Where an Agent operates under delegated mandate, the bounded authority scope, constraints and oversight are explicit. |
| `P1-RESP-05` | Applicable Policy & Governance Obligation Projection | Contract & Interoperability | Conditional-mandatory | Applicable external policy/governance obligations can be projected to the architecture without semantic redefinition. |
| `P1-RESP-06` | Product / Risk Governance Context Association | Contract & Interoperability | Conditional-mandatory | Where BPS/AIPS Product boundaries apply, the correct Product Version, risk and governance context can be associated with the governed AI use. |
| `P1-RESP-07` | Governing Constraint Distribution | Mediation | Baseline-mandatory | Relevant P1 constraints can be made available to P2-P7 responsibility holders without requiring implicit shared state. |
| `P1-RESP-08` | Authority Currentness, Revocation & Supersession | Lifecycle & Evolution | Conditional-mandatory | Time-bounded, revocable or superseded authority/constraint state can be detected and propagated where material. |
| `P1-RESP-09` | Governing Conflict & Escalation | Human & Governance | Conditional-mandatory | Conflicting, incomplete or indeterminate governing inputs have an explicit precedence/escalation path rather than silent permissive resolution. |
| `P1-RESP-10` | Human Accountability & Escalation Envelope | Human & Governance | Baseline-mandatory | Accountable participation, review/escalation responsibilities and material exception ownership are explicit where applicable. |
| `P1-RESP-11` | Governing Evidence & Traceability | Observation & Evidence | Baseline-mandatory | Material purpose/authority/constraint decisions are traceable enough for applicable assurance, governance and audit needs. |
| `P1-RESP-12` | Assurance / Governance Feedback Intake | Evaluation & Assurance | Conditional-mandatory | Findings, currentness concerns or assurance outcomes that constrain continued use can feed back into governing intent/authority decisions. |

#### P2 — Knowledge, Context & Grounding

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P2-RESP-01` | Context Requirement Determination | — | Baseline-mandatory | Determine the categories, constraints and scope of context required for the governed execution/use. |
| `P2-RESP-02` | Context Resource Eligibility | — | Baseline-mandatory | Determine whether a candidate resource is eligible to participate in a context under applicable policy, identity, scope and quality/currentness rules. |
| `P2-RESP-03` | Knowledge Resource Access & Mediation | — | Conditional-mandatory | Obtain governed access to knowledge/resources without assuming a particular repository or access protocol. |
| `P2-RESP-04` | Retrieval Coordination | — | Conditional-mandatory | Locate/select/obtain resources where retrieval is part of context construction. |
| `P2-RESP-05` | Grounding Source Qualification | — | Conditional-mandatory | Establish when an eligible resource is intentionally used in the Grounding Source Role. |
| `P2-RESP-06` | Context Assembly & Bounding | — | Baseline-mandatory | Construct the bounded set of resources, state, conditions, prompts/instructions and other information to be made available to an execution. |
| `P2-RESP-07` | Prompt & Instruction Contextualization | — | Conditional-mandatory | Preserve applicable prompt/instruction identity, ordering, scope and context contribution without treating them as authority. |
| `P2-RESP-08` | Memory Contribution Governance | — | Conditional-mandatory | Govern retained/retrievable state contributed to context, including scope, isolation, retention and currentness. |
| `P2-RESP-09` | Source Identity, Version & Currentness | — | Baseline-mandatory where source identity matters | Preserve sufficient identity/version/currentness information for materially relevant resources. |
| `P2-RESP-10` | Context Provenance & Traceability | — | Baseline-mandatory | Record or expose enough lineage/evidence to reconstruct what resources and transformations contributed to the provided context. |
| `P2-RESP-11` | Context Provision to Execution | — | Baseline-mandatory | Provide the assembled context to P4 through a governed architecture interaction. |
| `P2-RESP-12` | Context Change, Invalidation & Refresh | — | Conditional-mandatory | React to source revocation, supersession, staleness, policy change or changed context requirements. |
| `P2-RESP-13` | Context Conflict & Degradation Handling | — | Conditional-mandatory | Handle contradictory, unavailable, insufficient, over-large or otherwise degraded context without silently converting uncertainty into certainty. |

#### P3 — Intelligence Capability & Primitive

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P3-RESP-01` | Intelligence Capability Requirement Interpretation | Enablement / Contract | Baseline-mandatory | — |
| `P3-RESP-02` | Primitive Discovery / Availability Determination | Enablement | Baseline-mandatory | — |
| `P3-RESP-03` | Capability-to-Primitive Contribution Mapping | Contract / Interoperability | Baseline-mandatory | — |
| `P3-RESP-04` | Primitive Type & Mechanism Identity Preservation | Contract / Evidence | Baseline-mandatory | — |
| `P3-RESP-05` | Primitive Eligibility Determination | Assurance / Control | Baseline-mandatory | — |
| `P3-RESP-06` | Primitive Version & Currentness Determination | Lifecycle / Evolution | Conditional-mandatory | — |
| `P3-RESP-07` | Primitive Compatibility Determination | Interoperability / Safety | Conditional-mandatory | — |
| `P3-RESP-08` | Multi-Primitive Composition Determination | Coordination | Conditional-mandatory | — |
| `P3-RESP-09` | Primitive Substitution / Fallback Governance | Resilience / Safety | Conditional-mandatory | — |
| `P3-RESP-10` | Primitive Provision to P4 | Enablement / Contract | Baseline-mandatory | — |
| `P3-RESP-11` | Primitive Evidence & Traceability | Observation / Evidence | Baseline-mandatory | — |
| `P3-RESP-12` | Primitive Change / Invalidation Propagation | Lifecycle / Evolution | Conditional-mandatory | — |
| `P3-RESP-13` | Evaluation / Assurance Feedback Intake | Evaluation / Assurance | Conditional-mandatory | — |

#### P4 — AI Execution, Agentic & Environment

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P4-RESP-01` | Execution Occurrence Establishment | Baseline-mandatory | Establish a distinct, traceable AI Execution occurrence with stable correlation identity and bounded runtime scope. | — |
| `P4-RESP-02` | Context Binding & Consumption | Baseline-mandatory | Bind the applicable P2-provided AI Context to the execution and preserve which context was made available. | — |
| `P4-RESP-03` | Primitive Realization Binding | Baseline-mandatory | Bind the execution to the P3-approved primitive realization set actually eligible for use. | — |
| `P4-RESP-04` | Execution Mode Realization | Conditional-mandatory | Realize and record the applicable AIPS Execution Mode without treating it as primitive identity or deployment topology. | — |
| `P4-RESP-05` | Runtime Invocation & Coordination | Baseline-mandatory | Invoke/enact qualifying primitives and coordinate execution steps/participants in a bounded occurrence. | — |
| `P4-RESP-06` | Agent Participation Coordination | Conditional-mandatory | Coordinate Agent participation while preserving Agent identity, Agent type, autonomy/control-mode and authority boundaries. | — |
| `P4-RESP-07` | Tool-Use Coordination | Conditional-mandatory | Coordinate use of resources playing the Tool Role with explicit runtime scope and applicable authority/control checks. | — |
| `P4-RESP-08` | Runtime Orchestration | Conditional-mandatory | Coordinate multi-step/multi-participant execution flow where orchestration is required without equating orchestration with Agent or AI Product identity. | — |
| `P4-RESP-09` | Environment Observation / Sensing | Conditional-mandatory | Acquire or receive relevant Environment observations/signals where the execution or Agent senses an Environment. | — |
| `P4-RESP-10` | Environment Interaction / Actuation Execution | Conditional-mandatory | Technically enact an authorized Environment interaction or Actuation while preserving the distinction between capability, command, Authorization and observed effect. | — |
| `P4-RESP-11` | Control-Loop Participation | Conditional-mandatory | Coordinate recurring sense-evaluate-decide/authorize-act-observe participation without inferring autonomy or Control Intelligence Capability. | — |
| `P4-RESP-12` | Occurrence-Level Effect & Outcome Recording | Baseline-mandatory | Record Intelligence Effects or relevant outcomes produced/caused by the execution without treating effect as success, authorization or Product classification. | — |
| `P4-RESP-13` | Runtime Evidence, State & Correlation | Baseline-mandatory | Emit sufficient occurrence-level evidence/state/correlation for traceability, observability, reconstruction and downstream P7 assessment. | — |
| `P4-RESP-14` | Runtime Failure, Interruption & Degradation Handling | Baseline-mandatory | Make execution failure, partial completion, cancellation, timeout, degraded mode and control interruption explicit and governable. | — |

#### P5 — AI Serving, Product & Integration

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P5-RESP-01` | Consumption Boundary Definition | Define the governed boundary through which a consumer/system accesses an AI capability or Product realization. | Baseline-mandatory where P5 applies | — |
| `P5-RESP-02` | Serving Contract Definition | Define technology-neutral request/input, response/output, interaction, error and semantic expectations. | Baseline-mandatory | — |
| `P5-RESP-03` | Product/Offering Association | Associate the serving boundary with externally established Product/Product Version/AI Product identity where applicable. | Conditional-mandatory | — |
| `P5-RESP-04` | Consumer Compatibility | Determine whether a consumer/integration contract is compatible with the exposed serving contract/version. | Baseline-mandatory | — |
| `P5-RESP-05` | Consumption Mode Realization | Support the applicable interaction mode without making one protocol mandatory. | Conditional-mandatory | — |
| `P5-RESP-06` | Invocation Admission & Validation | Validate that a consumption request satisfies the applicable contract and governing preconditions before P4 invocation. | Baseline-mandatory | — |
| `P5-RESP-07` | Invocation Routing | Route/mediate an admitted serving request toward the appropriate P4 execution path without taking over P4 execution ownership. | Baseline-mandatory | — |
| `P5-RESP-08` | Result / Effect Delivery | Deliver eligible P4 outputs/effects to the appropriate consumer boundary under the serving contract. | Baseline-mandatory | — |
| `P5-RESP-09` | Integration / Provider Mediation | Mediate external/shared provider, platform, Product or service dependencies where needed. | Conditional-mandatory | — |
| `P5-RESP-10` | Contract Version & Currentness | Maintain serving-contract version, compatibility, currentness, supersession and deprecation state. | Baseline-mandatory | — |
| `P5-RESP-11` | Product/Serving Configuration Projection | Project externally governed Product-version or offering-specific configuration into serving behavior without redefining source semantics. | Conditional-mandatory | — |
| `P5-RESP-12` | Consumption Evidence & Traceability | Preserve consumer, contract, Product/version, invocation and integration trace needed for audit/reconstruction. | Baseline-mandatory | — |
| `P5-RESP-13` | Usage / Outcome Feedback | Provide relevant serving/integration usage and outcome evidence to P7 and applicable Product/governance authorities. | Conditional-mandatory | — |
| `P5-RESP-14` | Change, Deprecation & Migration Coordination | Coordinate consumer-impacting contract/provider/Product-serving changes and migration windows. | Conditional-mandatory | — |

#### P6 — Decision, Action & Human Oversight

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P6-RESP-01` | Decision-Control Context Determination | Baseline-mandatory | Determine which decision/action control pattern applies to the occurrence, including whether P6 intervention is required at all. | — |
| `P6-RESP-02` | Decision Input & Evidence Binding | Conditional-mandatory | Bind relevant recommendations, plans, context, evidence, human input and governing constraints to the Decision Formation occurrence. | — |
| `P6-RESP-03` | Decision Formation Coordination | Conditional-mandatory | Coordinate the governed formation of a determination where AI, human or system participants contribute. | — |
| `P6-RESP-04` | Operative Decision Commitment | Conditional-mandatory | Record/commit the operative determination where a governed decision is required, preserving the distinction from AI-produced Decision effects. | — |
| `P6-RESP-05` | Authorization Requirement Determination | Baseline-mandatory | Determine whether a specific Decision, invocation or Action requires context-specific Authorization. | — |
| `P6-RESP-06` | Point-of-Use Authorization | Conditional-mandatory | Establish, consume or verify the context-bounded Authorization that permits the governed occurrence to proceed. | — |
| `P6-RESP-07` | Authorization Scope & Condition Binding | Conditional-mandatory | Bind Authorization to subject/actor, target, action/decision scope, conditions, time/currentness and applicable Delegated Authority/policy basis. | — |
| `P6-RESP-08` | Human Oversight Requirement Determination | Baseline-mandatory | Determine whether review, approval, supervision, intervention, escalation or post-hoc oversight is required and at what control point. | — |
| `P6-RESP-09` | Human Review / Approval / Intervention | Conditional-mandatory | Enable required human participation with sufficient context, time, authority and ability to approve, reject, intervene, defer or escalate. | — |
| `P6-RESP-10` | Consequential Action Commitment & Control | Conditional-mandatory | Commit, reject, constrain, defer or cancel a consequential Action before technical enactment where applicable. | — |
| `P6-RESP-11` | Escalation, Exception & Override Handling | Conditional-mandatory | Route unresolved, conflicting, exceptional or safety-sensitive cases to an applicable governed escalation/override path. | — |
| `P6-RESP-12` | Revocation, Intervention & Stop Propagation | Conditional-mandatory | Propagate authority withdrawal, human intervention, emergency stop or equivalent control to affected execution/action boundaries. | — |
| `P6-RESP-13` | Decision / Authorization / Oversight Evidence | Baseline-mandatory | Preserve traceable evidence of inputs, authority basis, decisions, approvals/rejections, conditions, human participation and action outcomes. | — |
| `P6-RESP-14` | Outcome / Assurance Feedback Intake | Conditional-mandatory | Consume P7/P4/P5 outcome, assurance, safety and currentness feedback that may affect continued decision/action permission. | — |

#### P7 — Evaluation, Assurance, Observability & Evolution

| Source ID | Architectural Responsibility | Type / category | Applicability | Source intent where stated |
|---|---|---|---|---|
| `P7-RESP-01` | Observability Requirement Determination | Baseline-mandatory | Determine which behavior, state, decisions, effects, dependencies and changes must be observable for the applicable context. | — |
| `P7-RESP-02` | Evidence Capture & Correlation | Baseline-mandatory | Preserve/refer to sufficient material evidence with identity and correlation across relevant P1-P6 occurrences. | — |
| `P7-RESP-03` | Evidence Integrity & Provenance Association | Conditional-mandatory | Preserve applicable origin, integrity, custody/provenance and transformation references needed to assess evidence fitness. | — |
| `P7-RESP-04` | Evaluation Target & Criterion Binding | Conditional-mandatory | Bind each Evaluation to an explicit target, criteria, scope and context. | — |
| `P7-RESP-05` | Evaluation Coordination | Conditional-mandatory | Coordinate or consume an Evaluation using declared methods/evidence without conflating it with Assurance. | — |
| `P7-RESP-06` | Evaluation Result Management | Conditional-mandatory | Preserve Evaluation Results, their scope, criteria, method/context and report linkage where applicable. | — |
| `P7-RESP-07` | Assurance Scope & Claim Binding | Conditional-mandatory | Define the target, property/claim, conditions and evidence expectations of an Assurance Assessment. | — |
| `P7-RESP-08` | Assurance Assessment | Conditional-mandatory | Assess whether the declared assurance scope is sufficiently supported by applicable evidence. | — |
| `P7-RESP-09` | Assurance Finding Management | Conditional-mandatory | Preserve and propagate findings including sufficient/insufficient/conditional/indeterminate outcomes. | — |
| `P7-RESP-10` | Currentness Assessment | Baseline-mandatory where currentness materially affects use | Assess whether semantics, evidence, dependencies, governance or assurance remain applicable for the stated current purpose. | — |
| `P7-RESP-11` | Lifecycle & Version State Observation | Baseline-mandatory | Observe relevant version/lifecycle/supersession state without equating latest with current. | — |
| `P7-RESP-12` | Semantic Change Intake & Impact Triggering | Conditional-mandatory | Consume Semantic Change Events/material changes and identify potentially affected architecture targets. | — |
| `P7-RESP-13` | Operational Drift / Performance / Safety Signal Intake | Conditional-mandatory | Consume operational signals that may justify Evaluation, Assurance or Currentness reassessment. | — |
| `P7-RESP-14` | Re-evaluation / Re-assurance Triggering | Conditional-mandatory | Trigger or request reassessment when change, drift, expiry or findings invalidate prior assumptions. | — |
| `P7-RESP-15` | Constraint / Finding Feedback Propagation | Conditional-mandatory | Propagate current findings/status to affected P1-P6 responsibilities with scope and effective time. | — |
| `P7-RESP-16` | Historical Evidence & Assessment Preservation | Baseline-mandatory | Preserve what was observed, evaluated, assured and considered current at the relevant historical time without mutation by later findings. | — |

## 9. Intake observations — explicitly non-convergent

M02 reveals repeated architectural vocabulary across the three sources, including intent/semantics, governance/authority, discovery/realization, runtime, provision/consumption, evidence/observability, lifecycle/change and utility/foundation concerns.

These recurrences are **not yet architecture decisions**. In particular:

```text
same word       != same responsibility
same purpose    != same semantic authority
same mechanism  != same ABB
shared platform != merged reference architecture
```

M05 will determine whether recurring responsibilities should be:

- co-realized by one HDIP responsibility/ABB;
- kept distinct but coordinated;
- preserved as source-specific specialization;
- represented as cross-cutting obligations;
- excluded from HDIP core because they belong to adjacent enterprise capabilities.

## 10. Traceability contract for downstream stages

Every later HDIP responsibility candidate SHALL retain enough provenance to answer:

1. Which GEDRA/GEARA/GEAIRA source responsibility or obligation supports it?
2. Is the source requirement baseline or conditional?
3. Does the candidate co-realize more than one source responsibility?
4. Which semantic authority remains authoritative for the meaning involved?
5. Is the candidate an HDIP-specific coordination responsibility rather than an upstream responsibility?
6. What source distinction would be lost if the candidate were merged with another responsibility?

## 11. Completion state

**HDIP-CLA M02 — DRAFT BASELINE PRODUCED.**

M02 establishes:

- 3 authoritative upstream architecture sources;
- 6 GEDRA planes, one GEDRA cross-cutting governance/control concern and one GEDRA technology/utility foundation;
- 5 GEARA planes, 5 GEARA Fabrics and one GEARA shared foundation;
- 7 GEAIRA planes and 8 GEAIRA cross-cutting overlays;
- 106 GEDRA source obligation intake atoms;
- 134 GEARA source responsibility/fabric/foundation intake statements;
- 96 GEAIRA canonical responsibility IDs;
- **336 total source responsibility/obligation statements** preserved for downstream analysis;
- 14 M02 intake rules preventing premature convergence.

M02 intentionally introduces:

- **0 HDIP canonical planes**;
- **0 HDIP canonical overlays**;
- **0 HDIP canonical ABBs**;
- **0 cross-source equivalence assertions**.

### Next stage

> **M03 — Existing HDIP Construct Inventory & Disposition**

M03 will inventory historical/current HDIP constructs such as PDEP, CEP, COVP, DPFI, HPD, SYNCTX, registries, Marketplace/Consumption concepts, Governance and Utility constructs and classify each as **retain, specialize, reshape, defer, retire or unresolved** without yet freezing the final HDIP plane model.
