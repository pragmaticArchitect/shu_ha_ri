---
id: hdip-cla-0.1-m03-existing-hdip-construct-inventory
title: HDIP-CLA 0.1 M03 - Existing HDIP Construct Inventory & Disposition
sidebar_label: M03 - Existing HDIP Constructs
---

# HDIP-CLA 0.1 M03 - Existing HDIP Construct Inventory & Disposition

**Status:** COMPLETE

## 1. Purpose

M03 inventories architecturally material constructs already present in the HDIP body of work and records a controlled disposition for each before canonical planes, overlays or ABBs are derived.

M03 is deliberately **not** an architecture-design stage. A construct may survive in meaning while its historical label, scope or diagram position changes. Conversely, a familiar service/component label does not earn canonical ABB status merely because it exists in an older HDIP flow.

## 2. Source baseline

The inventory is derived from the reconciled HDIP material now carried by `shu_ha_ri`, including:

- `docs/foundations/hdip-brief.md`;
- `docs/product-development/hdip-data-product-development-stages.md`;
- `docs/product-consumption/hdip-product-consumption-stages.md`;
- `docs/product-projections/hdip-product-descriptor.md`;
- the three reconciled SYNCTX documents;
- the Enterprise Data Management Level-1 baseline;
- M01 and M02 of HDIP-CLA;
- the established GEDRA/HDIP specialization/profile reconciliation used as evidence for legacy HDIP construct mappings and the six prerequisite registries.

M03 inventories **architecturally material constructs**, not every glossary noun or every illustrative service name. Implementation-style service labels are grouped explicitly rather than being promoted one-by-one into architecture.

## 3. Disposition vocabulary

| Disposition | Meaning in M03 |
|---|---|
| **RETAIN** | The construct/responsibility remains materially valid and should continue into later HDIP-CLA analysis. Retain does not automatically mean retain its historical Plane/Layer placement. |
| **SPECIALIZE** | The construct is valid only for a defined domain, Product family, profile or use case and must not be generalized into HDIP core without evidence. |
| **RESHAPE** | The underlying responsibility remains valid, but name, scope, authority boundary, grouping or topological status requires redesign. |
| **DEFER** | The construct remains relevant, but canonical admission/structure belongs to a later HDIP-CLA stage or to an adjacent authority. |
| **RETIRE** | The term/structure should not be carried forward as a canonical HDIP architecture construct, although historical compatibility or the underlying responsibility may remain. |
| **UNRESOLVED** | Evidence is insufficient or contradictory; no architectural conclusion is permitted yet. |

## 4. Canonical M03 inventory

| ID | Existing construct | Concern | Current authority / nature | Disposition | M03 decision | Principal source |
|---|---|---|---|---|---|---|
| **M03-C01** | DII Wormhole Concept | Conceptual framing | HDIP | **RETAIN** | Keep as the evocative interaction-distance philosophy of HDIP. It is explanatory/non-normative and does not create an ABB, Plane or conformance obligation. | Homepage / HDIP philosophy |
| **M03-C02** | Product Development Experience Plane (PDEP) | Lifecycle / experience | HDIP | **RESHAPE** | Preserve the intent-driven Product development/evolution responsibility and experience. Do not freeze the word Plane or a universal family-neutral lifecycle yet; M06/M10 determine topology and profiles. | hdip-brief; Data PDEP Spec C |
| **M03-C03** | Self-Service Product Development (SSPD) | Lifecycle / experience | HDIP historical alias | **RETIRE** | Retire SSPD as a competing canonical architecture label. Preserve it as a historical/self-service philosophy alias where useful; use PDEP as the programme term. | Data PDEP glossary |
| **M03-C04** | Data PDEP Stage 0-10 lifecycle | Lifecycle / experience | HDIP Data specialization | **SPECIALIZE** | Keep as the current HDIP Data Product development profile. It must not be assumed to be the universal lifecycle for Information or AI Products. | hdip-data-product-development-stages |
| **M03-C05** | Self-Service Product Consumption Flow (SSCF) | Lifecycle / experience | HDIP | **RETAIN** | Keep the eight-stage logical Product-consumption lifecycle. It is a lifecycle model, not a mandatory synchronous runtime pipeline. | hdip-product-consumption-stages |
| **M03-C06** | Consumption Intent Record (CIR) | Lifecycle artifact | HDIP | **RETAIN** | Keep as the governed purpose/context artifact for HDIP consumption, subject to M11 contract and lifecycle reconciliation. | hdip-product-consumption-stages |
| **M03-C07** | Product Resolution Set | Lifecycle artifact | HDIP | **RETAIN** | Keep as an explainable candidate-resolution artifact; ranking/fit evidence does not establish Product qualification or access authority. | hdip-product-consumption-stages |
| **M03-C08** | Marketplace & Consumption Layer | Experience / provision | HDIP | **RESHAPE** | Preserve discovery, onboarding, acquisition and governed provision responsibilities, but re-evaluate overlap with CEP, Catalog/Registry and serving/provision responsibilities before retaining a separate Layer. | hdip-brief; GEDRA HDIP profile |
| **M03-C09** | Product Marketplace | Discovery / experience | HDIP | **RETAIN** | Keep as an HDIP discovery/acquisition experience construct. Marketplace listing is not Product qualification, authority or conformance. | hdip-brief; hdip-product-consumption-stages |
| **M03-C10** | Product Catalog | Discovery / metadata | HDIP projection of authoritative metadata | **RETAIN** | Keep the catalog/discovery responsibility while preserving a distinction from authoritative Registry responsibilities and from Marketplace experience. | hdip-product-consumption-stages |
| **M03-C11** | Consumer Experience Plane (CEP) | Experience / consumption | HDIP | **RETAIN** | Preserve the persona/context-aware governed consumption experience responsibility. Whether CEP remains a literal Plane is deferred to M06/M11. | hdip-brief; hdip-product-consumption-stages |
| **M03-C12** | COVP | Value / observability | HDIP | **RESHAPE** | Preserve usage, cost, value, outcome/feedback responsibilities. Normalize the current naming/scope conflict between Consumer Observability & Value Plane and Cost, Observability & Value Platform before plane/overlay derivation. | hdip-brief; GEDRA HDIP profile |
| **M03-C13** | Product Signal Bundle | Value / observability artifact | HDIP | **RETAIN** | Keep as an aggregation/projection of governed usage, cost, value and related signals. It is not Product classification and does not prove causal value. | hdip-product-consumption-stages |
| **M03-C14** | Resolved / Product-Local Governance Bundle (including current UGB term) | Governance projection | HDIP realization of authoritative governance | **RESHAPE** | Preserve the pattern of resolving applicable policy, contract, quality, control and evidence obligations and binding them to an exact Product Version. Normalize UGB terminology toward an authority-preserving resolved governance projection. | Data PDEP; GEDRA HDIP specialization |
| **M03-C15** | DPFI resolver/compiler capability | Compilation / realization | HDIP | **RESHAPE** | Preserve the governed resolution, validation and compilation responsibilities. Revisit the expansion Data Product Factory & Intelligence because it is Data-centric and Intelligence is now a formal architecture domain; exact ABB/name is deferred to M08/M09. | Data PDEP; SYNCTX inference |
| **M03-C16** | HDIP Product Descriptor (HPD) | Projection / descriptor | HDIP | **RETAIN** | Keep as a platform-generated operational projection bundle about a Product Version. Current formalization is Data-Product-oriented; any generic/family profiles are decided in M09. | hdip-product-descriptor |
| **M03-C17** | Synthetic Context (SYNCTX) | Synthetic-generation projection | HDIP Data/synthetic specialization | **SPECIALIZE** | Keep as the versioned relational/constraint projection for governed synthetic generation. It is not a generic HDIP context model and is not GEAIRM AI Context. | hdip-synthetic-context; SYNCTX ontology |
| **M03-C18** | Resolved Product Graph | Compilation artifact | HDIP | **DEFER** | Keep visible as a candidate compiled projection, but defer its exact canonical structure, authority and relationship to HPD/registries until M09/M10. | Data PDEP Stage 8 |
| **M03-C19** | Compilation Pack | Compilation artifact | HDIP Data PDEP | **DEFER** | Preserve as a useful packaging pattern, but do not freeze its current sub-artifact inventory as canonical HDIP architecture before M09/M10. | Data PDEP glossary |
| **M03-C20** | Logical Execution Graph (LEG) | Execution-plan artifact | HDIP Data PDEP | **DEFER** | Preserve the need for deployment-neutral logical execution representation where applicable; exact cross-family semantics and relationship to GEARA/GEAIRA runtime constructs remain to be derived. | Data PDEP glossary |
| **M03-C21** | Blueprint Binding / Selected Blueprint | Realization artifact | HDIP | **DEFER** | Preserve governed blueprint selection/binding as a realization pattern; exact blueprint contract and registry architecture are M09/M10 concerns. | Data PDEP glossary |
| **M03-C22** | Governed Runtime Views | Data runtime specialization | HDIP Data specialization | **SPECIALIZE** | Keep as a Data-domain realization pattern for policy-shaped views/interfaces. Do not generalize the term to all Information or Intelligence consumption. | Data PDEP glossary |
| **M03-C23** | Usage Contract | Product interaction contract | HDIP with upstream Product semantics | **RETAIN** | Keep as an explicit governed interaction contract, while deferring generic/family semantic authority to BPS/PIN and applicable Product-family specifications. | Data PDEP; SSCF |
| **M03-C24** | Access Decision / Access Descriptor | Consumption artifacts | HDIP | **RETAIN** | Keep Product/Port access decision and materialized access context as distinct lifecycle artifacts. They do not imply downstream consequential Decision/Action Authorization. | hdip-product-consumption-stages |
| **M03-C25** | ADS Registry | Registry | HDIP Data specialization | **SPECIALIZE** | Keep as the HDIP Data-domain registry for Authoritative Data Source specialization. It is not a universal DII authority registry. | GEDRA HDIP profile |
| **M03-C26** | Product Registry (current prerequisite is Data Product Registry) | Registry | HDIP | **RESHAPE** | Preserve Product registration/discovery responsibility, but broaden or profile the current Data Product Registry so HDIP can support Data, Information, AI and other applicable Product families without collapsing family semantics. | GEDRA HDIP profile; SSCF |
| **M03-C27** | Schema Registry | Registry | HDIP/shared | **RETAIN** | Keep logical schema-registration responsibility. Registry participation does not create semantic authority and one physical registry is not mandated. | GEDRA HDIP profile; Data PDEP |
| **M03-C28** | Policy Registry | Registry | HDIP/shared | **RETAIN** | Keep logical policy-registration/discovery/version responsibility while preserving external policy authority and authorship. | GEDRA HDIP profile; Data PDEP |
| **M03-C29** | Capability Registry | Registry | HDIP/shared | **RETAIN** | Keep logical capability discovery/eligibility responsibility; later M09 must reconcile Data, Information and Intelligence capability vocabularies without semantic collapse. | GEDRA HDIP profile; Data PDEP |
| **M03-C30** | Blueprint Registry / Blueprint Library | Registry / realization | HDIP | **RESHAPE** | Preserve governed blueprint discovery/versioning. Normalize Registry vs Library terminology and keep blueprint identity distinct from deployment/runtime instances. | GEDRA HDIP profile; Data PDEP |
| **M03-C31** | Environment Registry | Registry candidate | HDIP Data PDEP | **DEFER** | Retain as a candidate realization-support registry. It is not part of the established six-registry prerequisite set and requires M09 justification before canonical admission. | Data PDEP glossary |
| **M03-C32** | HDIP Governance Plane | Cross-cutting governance | HDIP | **RESHAPE** | Preserve governance/control responsibilities but do not freeze governance as a literal Plane. Upstream architectures strongly treat governance as cross-cutting; final HDIP form is derived in M07. | hdip-brief; GEDRA HDIP profile; M02 |
| **M03-C33** | HDIP Infrastructure / Utility Plane | Foundation / utility | HDIP | **RESHAPE** | Preserve enabling compute/storage/network/identity/messaging/orchestration/runtime responsibilities, but treat Plane status as provisional; foundation classification is tested in M06/M07. | GEDRA HDIP profile; M02 |
| **M03-C34** | ADS / ADO / ADD role specializations | Data-domain roles | HDIP Data specialization | **SPECIALIZE** | Keep as Data-domain specializations of GEDRM/GEDRA roles. They must not become universal DII producer/provider/authority roles. | GEDRA HDIP specialization |
| **M03-C35** | DPROD semantic descriptor | Adjacent Product/Data artifact | Applicable Data Product specification | **DEFER** | HDIP consumes/references DPROD but does not own its underlying Product/Data semantics. Keep outside HDIP core architecture ownership. | Data PDEP; HPD |
| **M03-C36** | DPDS deployment/realization specification | Adjacent Product deployment artifact | Applicable Product deployment specification | **DEFER** | HDIP may generate/use DPDS in a Data Product realization, but deployment semantics remain external/family-specific rather than HDIP core semantics. | Data PDEP; HPD |
| **M03-C37** | Digital Product Passport (DPP) | Adjacent trust/passport artifact | Applicable Product/trust specification | **DEFER** | HDIP may consume/pass through DPP trust evidence but should not redefine the passport or make it mandatory for every Product family without external authority. | HPD; SSCF |
| **M03-C38** | Data Mesh operating-model profile | Operating-model profile | Optional HDIP Data profile | **DEFER** | Keep Data Mesh as an optional Data-domain realization/operating-model profile, not as the definition of HDIP core. Revisit under M14. | hdip-brief; GEDRA HDIP specialization |
| **M03-C39** | Product Ports | Product interaction boundary | BPS/Product-family semantics + HDIP realization | **RETAIN** | Keep governed Product Ports as the principal consumption/serving boundary. HDIP provisions access to applicable ports; onboarding does not create the ports. | SSCF |
| **M03-C40** | Implementation-style service/component labels | Implementation labels | HDIP historical documents | **RETIRE** | Do not carry service labels such as Intent Service, Policy Service, Assertion Compiler, CEP Renderer, Product Resolution Engine, Blueprint Resolver, Deployer, Observability Engine or Value Computation Engine forward as canonical ABBs by name. Their responsibilities may be rediscovered and admitted later through M08. | Data PDEP and SSCF glossaries |

## 5. Disposition summary

M03 records **40 architecturally material existing constructs/groups**. The disposition distribution is:

| Disposition | Count |
|---|---:|
| RETAIN | 15 |
| SPECIALIZE | 5 |
| RESHAPE | 9 |
| DEFER | 9 |
| RETIRE | 2 |
| UNRESOLVED | 0 |

No final HDIP Plane, Overlay or ABB is created by these dispositions. `RETAIN` means “carry the responsibility/construct forward for analysis,” not “freeze the old box in the new architecture.”

## 6. Key M03 findings

### 6.1 The lifecycle/experience model survives, but not its historical topology

PDEP, SSCF and CEP remain strong HDIP concepts. However, historical words such as **Plane** and **Layer** are not architecture facts. M05-M07 must determine whether the relevant responsibilities converge into Planes, Overlays, experience surfaces, lifecycle views, or ABB groupings.

```text
PDEP / SSCF / CEP survive as responsibilities and experience/lifecycle constructs

!=

their historical boxes are automatically canonical HDIP Planes
```

### 6.2 COVP requires explicit normalization

The existing material uses COVP with two different expansions: **Consumer Observability & Value Plane** and **Cost, Observability & Value Platform**. Both point to a common responsibility family around usage, cost, value, observability, feedback and evolution, but the acronym must not be frozen until M04-M07 normalize its meaning and topology.

### 6.3 DPFI responsibility is stronger than its historical name

The reconciled material establishes a valuable HDIP resolver/compiler responsibility: resolve authoritative references, validate applicability, compile governed projections/plans and preserve evidence. The historical expansion **Data Product Factory & Intelligence** is now problematic because HDIP spans Data, Information and Intelligence and because Intelligence has a formal GEAIRM/GEAIRA meaning. M03 therefore preserves the capability but sends naming/ABB admission to M08/M09.

### 6.4 HPD and SYNCTX remain first-class projections, but with different scope

HPD remains an operational Product-Version projection bundle. SYNCTX remains a specialised synthetic-generation relational/constraint projection. Neither becomes semantic authority and neither should be generalized merely because both are graph-addressable compiled artifacts.

### 6.5 The registry model survives as logical responsibilities

The established HDIP prerequisite set remains important:

```text
ADS Registry
Data Product Registry
Schema Registry
Policy Registry
Capability Registry
Blueprint Registry
```

M03 does **not** require six separately deployed registry products. M09 must derive the canonical logical registry architecture and may permit shared realization while preserving distinct semantics. The current **Data Product Registry** also requires reshaping so that a holistic HDIP can support multiple Product families without treating them as one semantic type.

### 6.6 Catalog, Registry and Marketplace are not synonyms

```text
Registry
  authoritative/governed registration responsibility

Catalog
  discovery/search/projection responsibility

Marketplace
  consumer-facing discovery/acquisition experience
```

They may share implementation, but M03 preserves their logical distinction.

### 6.7 Governance and Utility responsibilities survive; their “Plane” labels do not pre-decide topology

GEDRA, GEARA and GEAIRA all provide strong evidence that governance, security, evidence, quality, lifecycle and utility concerns frequently cut across primary responsibility groupings. Accordingly, HDIP Governance and Infrastructure/Utility are retained as responsibility families but **RESHAPE** is the correct M03 disposition until M06/M07.

### 6.8 Data-specific HDIP specializations stay Data-specific

ADS/ADO/ADD, Data PDEP stages, SYNCTX and governed runtime-view patterns remain valuable HDIP Data specializations. HDIP-CLA must not generalize them into Information or Intelligence simply because the enterprise platform co-realizes all three domains.

### 6.9 Historical implementation labels do not become ABBs by inheritance

Older HDIP flows contain useful labels such as `Policy Service`, `Assertion Compiler`, `Blueprint Resolver`, `CEP Renderer`, `Product Resolution Engine`, `Deployer`, `Observability Engine` and `Value Computation Engine`. M03 retires those labels **as automatic architecture components**. M08 may rediscover one or more of the underlying responsibilities and admit a technology-neutral ABB if justified.

## 7. Existing construct map after M03

```text
                         HDIP-CLA input after M03
                                  |
       +--------------------------+--------------------------+
       |                          |                          |
       v                          v                          v
 Lifecycle / Experience     Compilation / Projection    Shared Platform Concerns
       |                          |                          |
 PDEP  [reshape]             DPFI   [reshape]            Governance [reshape]
 SSCF  [retain]              HPD    [retain]             Utility    [reshape]
 CEP   [retain]              SYNCTX [specialize]         Registries [retain/reshape]
 COVP  [reshape]             Packs/Graphs [defer]        Catalog/Marketplace [distinct]
       |                          |                          |
       +--------------------------+--------------------------+
                                  |
                                  v
                      M04 principles/invariants
                                  |
                                  v
                  M05 convergence/separation analysis
                                  |
                                  v
                 M06/M07/M08 canonical architecture
```

## 8. M03 normative rules

**HDIP-CLA-M03-R01 - Inventory before redesign:** Existing HDIP constructs SHALL be inventoried and dispositioned before canonical Plane, Overlay or ABB derivation.

**HDIP-CLA-M03-R02 - Meaning may survive topology:** A retained construct MAY preserve its responsibility while changing historical Plane, Layer, service or component placement.

**HDIP-CLA-M03-R03 - No legacy-box inheritance:** A legacy HDIP diagram box SHALL NOT become a canonical HDIP-CLA element solely because it existed in a prior diagram.

**HDIP-CLA-M03-R04 - PDEP preservation without Plane freeze:** PDEP SHALL remain a core HDIP development/evolution concept, but M03 SHALL NOT freeze it as a canonical Plane.

**HDIP-CLA-M03-R05 - Family-specific lifecycle boundary:** The current Data PDEP Stage 0-10 lifecycle SHALL remain a Data Product specialization and SHALL NOT be generalized to all Product families without family-specific evidence.

**HDIP-CLA-M03-R06 - SSCF logical-lifecycle boundary:** SSCF SHALL remain a logical consumption lifecycle and SHALL NOT be interpreted as a mandatory synchronous runtime pipeline.

**HDIP-CLA-M03-R07 - CEP responsibility preservation:** CEP SHALL preserve governed consumer-experience responsibilities without requiring a mandatory CEP Renderer component or a frozen Plane boundary.

**HDIP-CLA-M03-R08 - COVP normalization required:** COVP SHALL NOT be frozen into HDIP-CLA until its name, scope and relationship among usage, cost, value, outcome, observability and feedback are reconciled.

**HDIP-CLA-M03-R09 - Governance topology restraint:** Governance/control responsibility SHALL remain cross-cutting-capable and SHALL NOT be frozen as a standalone HDIP Plane merely because historical HDIP diagrams depicted one.

**HDIP-CLA-M03-R10 - Foundation topology restraint:** Infrastructure/utility responsibility SHALL be preserved without assuming it is a peer business-responsibility Plane.

**HDIP-CLA-M03-R11 - DPFI responsibility/name separation:** The DPFI resolver/compiler responsibility MAY survive even if the historical DPFI name or expansion changes; architecture meaning SHALL take precedence over acronym preservation.

**HDIP-CLA-M03-R12 - Projection non-authority:** HPD, SYNCTX, resolved graphs, governance bundles and other compiled projections SHALL NOT override the semantic or governance authorities from which they are derived.

**HDIP-CLA-M03-R13 - SYNCTX specialization boundary:** SYNCTX SHALL remain a synthetic-generation specialization and SHALL NOT be treated as a universal HDIP Context or as GEAIRM AI Context.

**HDIP-CLA-M03-R14 - Logical-registry independence:** ADS, Product, Schema, Policy, Capability and Blueprint registry responsibilities SHALL remain logically distinguishable even where one implementation realizes several of them.

**HDIP-CLA-M03-R15 - Catalog/Registry/Marketplace separation:** Catalog, Registry and Marketplace responsibilities SHALL NOT be treated as semantic synonyms.

**HDIP-CLA-M03-R16 - Registry non-qualification:** Registration or marketplace/catalog presence SHALL NOT by itself establish authority, Product status, control effectiveness or HDIP conformance.

**HDIP-CLA-M03-R17 - No cross-domain inheritance:** A Data-specific HDIP construct SHALL NOT automatically become an Information- or Intelligence-domain construct through platform co-realization.

**HDIP-CLA-M03-R18 - Adjacent-authority preservation:** DPROD, DPDS, DPP and other externally governed Product/family artifacts SHALL remain referenced authorities/dependencies rather than being silently absorbed into HDIP core semantics.

**HDIP-CLA-M03-R19 - Service-name non-admission:** Historical service/component labels SHALL NOT become canonical ABBs without the M08 responsibility-based admission test.

**HDIP-CLA-M03-R20 - Data Mesh profile boundary:** Data Mesh SHALL remain an optional HDIP Data-domain profile/operating-model concern and SHALL NOT define HDIP core architecture.

**HDIP-CLA-M03-R21 - Historical alias restraint:** Historical aliases such as SSPD MAY be preserved for traceability but SHALL NOT compete with the canonical terminology selected by HDIP-CLA.

**HDIP-CLA-M03-R22 - No M03 architecture freeze:** M03 dispositions SHALL NOT create final HDIP Planes, Overlays, ABBs, physical services, deployment topology or registry consolidation decisions.

## 9. M03 completion state

**HDIP-CLA M03 - COMPLETE.**

M03 establishes:

- **40** architecturally material existing constructs/groups with explicit dispositions;
- **15 RETAIN** dispositions;
- **5 SPECIALIZE** dispositions;
- **9 RESHAPE** dispositions;
- **9 DEFER** dispositions;
- **2 RETIRE** dispositions;
- **0 UNRESOLVED** dispositions;
- explicit preservation of PDEP, SSCF, CEP, HPD, SYNCTX and the registry responsibilities without freezing their final topology;
- explicit normalization requirements for COVP, DPFI, Product Registry, Blueprint Registry/Library, Governance and Utility;
- explicit retirement of SSPD as a competing canonical architecture label and of implementation-style service names as automatic ABBs;
- **22 normative M03 rules**;
- **0 new canonical HDIP Planes**;
- **0 new canonical HDIP Overlays**;
- **0 canonical HDIP ABBs**.

### Next stage

> **M04 - Canonical Architecture Principles & Design Invariants**

M04 will turn the M01 authority contract, M02 upstream responsibility corpus and M03 construct dispositions into the canonical design principles/invariants that M05-M08 must obey.
