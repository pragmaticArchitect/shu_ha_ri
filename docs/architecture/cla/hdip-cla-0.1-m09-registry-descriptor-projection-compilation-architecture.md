---
id: hdip-cla-0.1-m09-registry-descriptor-projection-compilation-architecture
title: HDIP-CLA 0.1 M09 - Registry, Descriptor, Projection & Compilation Architecture
sidebar_label: M09 - Registry, Projection & Compilation
---

# HDIP-CLA 0.1 M09 - Registry, Descriptor, Projection & Compilation Architecture

**Status:** COMPLETE

## 1. Purpose

M09 defines the canonical logical architecture by which the **Holistic Data, Information and Intelligence Platform (HDIP)** registers governed resources, projects authoritative information into operational forms, resolves dependencies and obligations, and compiles governed intent into realization-ready artifacts.

M09 sits directly on the M06-M08 architecture:

```text
P1  Governed Intent, Definition & Authority Context
        |
        v
P2  Discovery, Composition & Realization
        |
        +--> logical Registries / Catalog projections
        +--> resolution / validation / compilation
        +--> HDIP descriptors and projections
        +--> realization plans and bindings
        |
        v
P3/P4 runtime and consumption
        |
        v
P5 outcome / value / evolution

X1-X9 remain cross-cutting throughout.
```

M09 answers six architecture questions:

1. Which logical registry responsibilities are canonical in HDIP core and which remain Profile-specific?
2. What authority does a registry have, and what authority does it explicitly not have?
3. How do Registry, Catalog and Marketplace differ?
4. Which HDIP-generated descriptors/projections are canonical and what do they project?
5. What are the canonical compilation outputs and how do they relate?
6. How does HDIP preserve provenance, currentness, authority and historical meaning through resolution and compilation?

M09 does **not** prescribe physical databases, graph stores, registry products, event buses, API products, vendor tools, centralization, or one compiler implementation.

---

# 2. Derivation basis

M09 is constrained by the previous HDIP-CLA decisions:

- **M01**: HDIP is an enterprise logical realization/composition architecture; semantic and Product authority remain external where assigned externally.
- **M02**: source responsibility and provenance must be preserved; source nouns do not automatically become HDIP components.
- **M03**: ADS, Product, Schema, Policy, Capability and Blueprint registry responsibilities remain logically distinguishable; HPD and SYNCTX remain projections; Catalog/Registry/Marketplace are not synonyms.
- **M04**: projections and compilers do not acquire source authority; registries do not qualify Productness; historical meaning must be preserved.
- **M05**: RCF-27 keeps registry responsibilities co-realizable but distinct; RCF-28 makes Catalog a converged discovery projection; RCF-29 makes Marketplace a converged acquisition experience.
- **M06**: registry/discovery/compilation concerns principally participate in P1/P2 while lifecycle, governance and evidence remain cross-cutting.
- **M07**: X1, X3, X5, X6 and X7 constrain compilation and projection semantics; X4/X8/X9 remain applicable where material.
- **M08**: P2-ABB-01 through P2-ABB-04 provide the principal logical ABB boundaries; registries and first-class artifacts are not ABBs merely because they exist.

M09 therefore formalizes **logical information/coordination architecture**, not a service bill of materials.

---

# 3. Canonical M09 distinction model

M09 freezes the following hard distinction:

```text
Authoritative semantic / Product / policy / domain source
              !=
Logical Registry responsibility
              !=
Catalog discovery projection
              !=
Marketplace acquisition experience
              !=
HDIP operational projection / descriptor
              !=
Compiled realization artifact
              !=
Runtime realization
              !=
Evidence about any of the above
```

These constructs may reference one another and may be co-realized physically, but they do not inherit one another's authority.

## 3.1 Scoped registry authority

A logical HDIP registry MAY be authoritative for **registration facts inside the HDIP operating context**, for example:

- that a subject/version was registered;
- the registration identifier;
- registration lifecycle/currentness state;
- registration effective period;
- pointers to the authoritative subject definition;
- the registered interface/contract references;
- the recorded owning/accountable participant reference;
- registration provenance/evidence.

This scoped authority does **not** make the registry authoritative for the underlying subject's intrinsic meaning.

For example:

```text
Product Registry
  may establish: "Product Version PV7 is registered in HDIP"

Product Registry
  does NOT establish by registration alone: "PV7 qualifies as a Product"
```

Likewise:

```text
Policy Registry
  may establish: "Policy artifact P12/v4 is the registered reference used by HDIP"

Policy Registry
  does NOT become: the legal / regulatory / domain authority that authored the policy
```

---

# 4. Logical Registry admission model

A named logical registry identity is admitted only where all of the following hold:

1. **Distinct registered subject class** - the registry governs registration of a materially distinct kind of subject/reference.
2. **Distinct authority semantics** - registration state and the subject's semantic authority can be stated without ambiguity.
3. **Independent lifecycle/currentness need** - registered versions/currentness materially affect resolution or operation.
4. **Reusable discovery/resolution value** - P1/P2 or cross-cutting responsibilities repeatedly need the registered information.
5. **Technology neutrality** - the registry remains meaningful whether implemented by one database, several stores, APIs, knowledge graphs or federated sources.
6. **Logical independence** - consolidation with another registry is permitted only if subject identity, ownership, lifecycle and contracts remain distinguishable.
7. **Non-qualification** - registration does not manufacture semantic status, Productness, authority, trust, control effectiveness or conformance.

A logical Registry is therefore an architecture responsibility, not a mandate for a standalone registry product.

---

# 5. Canonical HDIP Registry catalogue

M09 freezes **five core logical Registry identities** and **one Data-profile Registry specialization**.

## 5.1 Core Registry identities

| ID | Canonical logical Registry | Principal responsibility | Primary architecture participation |
|---|---|---|---|
| **HDIP-REG-01** | **Product Registry** | Register qualified/intentionally constituted Product and Product Version references, Product-family identity, lifecycle/currentness, Product contracts/ports and authoritative descriptor references without qualifying Productness itself. | P1, P2, P4, X7 |
| **HDIP-REG-02** | **Schema Registry** | Register versioned structural/interface schemas and compatibility metadata required for design, compilation, binding and consumption without becoming business-semantic authority. | P1, P2, P3, P4, X7 |
| **HDIP-REG-03** | **Policy Registry** | Register governed policy/control references and machine-evaluable policy artifacts where available, preserving external policy authority and version/effective-period context. | P1, P2, X1, X7 |
| **HDIP-REG-04** | **Capability Registry** | Register discoverable platform/domain capabilities, eligibility/availability metadata and invocation/realization references without automatically classifying them as Products or AI Primitives. | P2, P3, P4, X7 |
| **HDIP-REG-05** | **Blueprint Registry** | Register reusable technology-neutral realization blueprints/patterns, applicability constraints and versioned realization metadata used by P2 binding. | P2, X7, HDIP-FND |

## 5.2 Data-profile Registry specialization

| ID | Profile | Canonical logical Registry | Status |
|---|---|---|---|
| **HDIP-REG-D01** | HDIP Data Profile | **ADS Registry** | Canonical Data-profile specialization; registers HDIP Authorized Data Source designations/references and their scoped authority/currentness evidence. It is not generalized into Information or Intelligence. |

The former **Data Product Registry** is therefore reshaped as follows:

```text
HDIP core
  Product Registry
      |
      +--> Data Product entries / Data Profile projection
      +--> Information Product entries
      +--> AI Product entries
      +--> other Product-family entries where qualified

not

one HDIP-local Product taxonomy that replaces BPS/PIN or family authority
```

## 5.3 Why ADS Registry is Profile-specific

ADS is a Data-domain specialization of Authoritative Source semantics. It therefore remains an HDIP Data Profile Registry rather than being generalized into a universal `Authoritative Source Registry` across Information and Intelligence.

Other domain/Product profiles MAY introduce additional logical registries where the M09 admission model is satisfied. Profile-specific registry admission SHALL NOT silently expand the HDIP core Registry catalogue.

---

# 6. Registry Entry Contract

Every canonical logical Registry SHALL expose a stable **Registry Entry Contract** sufficient for deterministic reference and historical reconstruction.

The contract SHOULD include, where applicable:

```text
registration identity
subject identity / IRI / stable identifier
subject kind / type
subject version or version reference
registration lifecycle state
currentness / eligibility state where applicable
effective-from / effective-to context where material
authoritative-source reference(s)
ownership / accountability reference(s)
contract / interface / port reference(s)
applicability / scope metadata
supersession / deprecation references
registration provenance / evidence reference
last governed registration-change identity
```

The contract does not require every Registry to use the same physical schema. It requires equivalent architectural meaning to remain available.

## 6.1 Latest is not current

A registry MAY contain many versions. Resolution SHALL distinguish:

```text
latest/newest
    !=
governed-current
    !=
eligible for this purpose/context
    !=
the version historically used
```

X7 lifecycle/currentness responsibilities apply to every registry subject for which version/currentness affects operation.

---

# 7. Registry, Catalog and Marketplace architecture

M09 freezes the following relationship:

```text
Registries
  governed registration + identity/currentness references
        |
        v
Catalog
  read/discovery/search projection across eligible registered resources
        |
        v
Marketplace / acquisition experience
  consumer-facing browse/evaluate/request/acquire/subscribe interaction
```

## 7.1 Registry

Registry responsibilities answer questions such as:

- What subject/version is registered?
- What is its stable identity?
- What authoritative definition is referenced?
- What lifecycle/currentness state is registered?
- What contracts or ports are associated?
- What registration evidence applies?

## 7.2 Catalog

Catalog is principally a P2 discovery projection. It MAY index or project information from multiple Registries, HPD and other governed metadata so participants can search and navigate efficiently.

Catalog indexing SHALL NOT make the Catalog authoritative for Product qualification, source authority, policy meaning, lifecycle truth or eligibility.

## 7.3 Marketplace

Marketplace is principally a P4 consumer/acquisition experience. It MAY use Catalog projections, Product Registry records, HPD and entitlement/policy context to support browse, evaluate, request, subscribe or acquire interactions.

Marketplace presence SHALL NOT itself establish:

- Productness;
- entitlement;
- Data authority;
- Fitness for Use;
- trust;
- successful access provisioning;
- value.

---

# 8. Canonical artifact taxonomy

M09 distinguishes four artifact classes.

| Class | Nature | Examples | Authority rule |
|---|---|---|---|
| **Authoritative referenced artifact** | Definition/contract governed by an external or family authority | BPS/PIN Product definition, DPROD, domain ontology, authoritative policy, schema/contract source | HDIP consumes/references; does not replace authority. |
| **HDIP operational projection** | Versioned HDIP-generated projection of authoritative/resolved information for platform operation | HPD, Resolved Realization Graph, SYNCTX specialization | Projection authority is limited to the projection and its compilation state. |
| **HDIP compiled realization artifact** | Output used to govern/drive realization | Resolved Governance Bundle, Realization Plan, Blueprint Binding | Compiles authoritative inputs; does not become source authority. |
| **HDIP compilation evidence artifact** | Evidence of what inputs/rules/versions produced a compilation result | Compilation Record | Evidences the compilation occurrence; does not prove correctness/assurance by itself. |

This taxonomy prevents documents, graphs and bundles from being mistaken for architecture components or semantic authorities.

---

# 9. HDIP Product Descriptor (HPD)

M09 confirms **HPD** as the canonical HDIP operational projection for an applicable **Product Version**.

## 9.1 Canonical role

> **HPD is a versioned HDIP operational projection bundle that makes authoritative Product/Product-Version information and resolved HDIP operational context computable for discovery, coordination, dependency/impact analysis, governance, consumption, observability and lifecycle operations.**

HPD MAY project, where applicable:

- Product and Product Version identifiers;
- Product Family / Product Kind / family-specific classification references;
- authoritative Product descriptor references;
- ownership/accountability references;
- Product Promise/intent references;
- dependency and composition references with explicit relation types;
- governed ports/contracts;
- applicable governance-context references;
- realization/binding references;
- lifecycle/currentness references;
- provenance/evidence references;
- SYNCTX reference where a realization actually uses a SYNCTX version;
- operational discovery/observability references.

## 9.2 HPD boundary

```text
HPD
  != Product qualification authority
  != BPS/PIN
  != Product-family semantic authority
  != DPROD / family-authoritative descriptor
  != DPDS / deployable specification
  != Registry
```

HPD MAY be indexed by a Catalog and referenced by a Product Registry entry, but those relationships do not merge the constructs.

## 9.3 Product scope

HPD is Product-Version scoped. Governed non-Product capabilities MAY have discoverable/operational metadata, but SHALL NOT receive an HPD merely to make the platform symmetrical.

---

# 10. Resolved Realization Graph (RRG)

M09 introduces **Resolved Realization Graph (RRG)** as the canonical family-neutral compilation projection for the resolved design/realization context.

> **RRG is a versioned HDIP compilation projection that records the resolved subjects, typed dependencies, authoritative references, applicable bindings, compatibility results and material realization relationships required to explain and drive a governed realization.**

RRG is principally produced by **HDIP-P2-ABB-03 Resolution, Validation & Compilation Boundary** and consumed by P2 realization binding and downstream evidence/lifecycle responsibilities.

## 10.1 RRG contents

An RRG MAY include, where applicable:

- governed intent/use-context references;
- subject/Product Version/capability identities;
- semantic-definition references;
- authority/accountability references;
- typed dependencies;
- composition relationships;
- compatibility findings;
- input/output/port/interface bindings;
- applicable Policy/Schema/Capability/Blueprint Registry references;
- specialized context/projection references;
- realization prerequisites;
- currentness/version state used during resolution;
- evidence links for material resolution decisions.

## 10.2 Resolved Product Graph compatibility

The historical **Resolved Product Graph** becomes a Product-scoped projection/view of the RRG model:

```text
Resolved Realization Graph
      |
      +--> Product-scoped RRG
               historical label: Resolved Product Graph
```

This preserves existing Data PDEP meaning while avoiding the incorrect conclusion that all HDIP compilation must involve a Product.

## 10.3 RRG non-authority

RRG SHALL NOT manufacture:

- Product identity;
- semantic relationships;
- source authority;
- joinability;
- policy authority;
- provenance;
- eligibility;
- compatibility findings unsupported by applicable evidence.

---

# 11. Synthetic Context (SYNCTX)

M09 confirms **SYNCTX** as a specialized HDIP operational projection, not a universal Context construct.

> **SYNCTX is a versioned relational and constraint projection compiled for a defined synthetic-generation purpose from authoritative Product Version, schema, semantic, contract and governance information.**

SYNCTX remains:

- a Data/synthetic-generation specialization;
- Product-Version-aware;
- evidence-bound for RelationshipBindings;
- constraint-projection based;
- historically versioned;
- reproducibly compilable when normalized authoritative inputs and compiler/rule versions are held constant;
- distinct from GEAIRM AI Context;
- non-authoritative for Product/Data/policy semantics.

Conceptually:

```text
RRG
  generic resolved realization context
       |
       +--> SYNCTX
            specialized relational/constraint projection
            when synthetic generation is applicable
```

SYNCTX need not exist for every Product or every synthetic-classified Product Version; applicability must be resolved from the actual generation requirement and evidence.

---

# 12. Resolved Governance Bundle (RGB)

M09 freezes **Resolved Governance Bundle (RGB)** as the canonical name for the subject/version/context-scoped projection of applicable governing obligations prepared for realization and enforcement.

> **RGB is a versioned HDIP compiled governance projection that binds the applicable policy, control, privacy, entitlement, quality/evidence and other governing obligations required for a defined subject/version/context while retaining traceability to their authoritative sources.**

RGB MAY contain or reference, where applicable:

- authoritative policy/version references;
- policy-as-code or equivalent machine-evaluable projections;
- Data/Information/AI/Product control obligations;
- access/entitlement constraints;
- privacy/purpose/residency/retention constraints;
- quality-rule obligations;
- evidence/control-evidence requirements;
- human approval/assessment obligations;
- exception/waiver references;
- effective period and applicability context;
- enforcement/binding targets.

## 12.1 Historical Unified Governance Bundle terminology

The historical term **Unified Governance Bundle (UGB)** is retained as an alias for compatibility only.

M09 prefers **Resolved Governance Bundle** because `Resolved` accurately describes the HDIP role without implying that HDIP has unified or centralized all governance authority.

```text
UGB  historical alias
RGB  canonical M09 term
```

## 12.2 RGB boundary

```text
Policy authority
      !=
Policy applicability resolution
      !=
RGB compilation
      !=
Runtime enforcement
      !=
Control Evidence / Assurance
```

RGB may carry the executable form of an obligation without becoming its legal, regulatory, domain or Product authority.

---

# 13. Realization Plan

M09 freezes **Realization Plan** as the technology-neutral logical plan that describes how the resolved design is intended to be realized before physical/platform-specific deployment details are finalized.

A Realization Plan MAY include:

- typed execution/formation/processing stages;
- dependency/input/output binding intent;
- orchestration/dependency ordering where required;
- logical control/enforcement points;
- quality/evidence checkpoints;
- runtime/serving requirements;
- resilience/failure expectations;
- observability requirements;
- cost/economic constraints;
- required capability classes;
- deployment/promotion prerequisites.

The historical **Logical Execution Plan** is a valid specialized name where the plan is execution-focused. `Realization Plan` is the family-neutral M09 term.

A Realization Plan is not executable code by definition and does not imply one orchestration technology.

---

# 14. Blueprint Binding

M09 freezes **Blueprint Binding** as the compiled relationship between a resolved realization and a selected eligible Blueprint plus the capability/environment constraints needed to instantiate it.

Blueprint Binding MAY include:

- selected Blueprint identity/version;
- applicability rationale;
- required capability bindings;
- environment/placement constraints;
- residency/location constraints where applicable;
- cost/economic constraints;
- security/secrets/identity requirements;
- deployment/promotion constraints;
- parameterization references;
- fallback/alternative binding references where permitted.

`Selected Blueprint` alone is therefore insufficient as the canonical output. The architectural result is the **binding**, including why and under which constraints that Blueprint is applicable.

Blueprint Binding does not make the Blueprint Registry a deployment authority and does not make the selected Blueprint a Product.

---

# 15. Compilation Record

M09 introduces **Compilation Record (CR)** as the canonical evidence artifact for a material P2 compilation occurrence.

> **CR records which normalized inputs, authoritative references, Registry versions, compiler/rule-set versions, decisions, exceptions and output artifacts participated in a compilation result.**

A CR SHOULD include, where applicable:

```text
compilation occurrence identity
subject / Product Version / capability identity
intent/design input versions
semantic/authority source references
Registry entry versions used
policy/control versions used
compiler / rule-set version
validation results
material resolution decisions
assessment-required decisions and accountable actor references
RRG version
HPD version where applicable
SYNCTX version where applicable
RGB version
Realization Plan version
Blueprint Binding version
warnings / unresolved conditions / exceptions
compilation outcome
created-at / effective context
provenance/evidence correlation identifiers
```

The Compilation Record provides X3/X7 historical reconstruction. It does **not** prove that the result is semantically correct, safe, fit, authorized or assured merely because compilation completed.

---

# 16. Canonical compilation architecture

The canonical M09 compilation flow is logical and non-vendor-specific:

```text
P1 governed intent / definition / authority context
        |
        v
P2-ABB-01 Governed Discovery & Navigation
        |
        +--> Registry / Catalog references
        v
P2-ABB-02 Dependency, Composition & Compatibility
        |
        v
P2-ABB-03 Resolution, Validation & Compilation
        |
        +--> RRG
        +--> RGB
        +--> HPD              [when Product applies]
        +--> SYNCTX           [when synthetic generation applies]
        +--> Realization Plan
        |
        v
P2-ABB-04 Realization & Deployment Binding
        |
        +--> Blueprint Binding
        |
        v
Compilation Record correlates the exact input/output set
        |
        v
M10/M12 governed promotion / deployment / interaction
```

This is not a mandatory physical pipeline. One implementation may perform several boundaries in-process; a federated realization may distribute them across domains/providers.

---

# 17. Compilation semantics

## 17.1 Resolve; do not invent

P2 compilation SHALL distinguish:

```text
candidate evidence
      !=
validated binding
      !=
authoritative fact
```

Naming similarity, co-location, schema shape, shared key names, graph adjacency or transitive dependency SHALL NOT by themselves establish a semantic relationship, Product composition, joinability, policy obligation or authority.

## 17.2 Deterministic and judgement-dependent portions

Compilation may contain both:

- safely machine-evaluable resolution/validation; and
- judgement-dependent decisions requiring accountable assessment.

HDIP SHALL NOT report judgement-dependent architecture/governance conclusions as machine-proven merely because automation assembled supporting evidence.

## 17.3 Reproducibility

For deterministic compilation portions, the same normalized pinned inputs, authoritative/reference versions, compiler/rule-set versions and configuration SHOULD produce semantically equivalent canonical output projections.

This does not imply runtime determinism, especially for stochastic AI execution or time-varying external systems.

## 17.4 Currentness

A compilation result is valid only for its governed input/currentness context. A newer Registry entry, policy version or Product Version SHALL NOT silently mutate an already-used RRG, HPD, SYNCTX, RGB, Plan, Binding or CR.

Material change produces a new version/revision and applicable impact/recompilation/evolution activity.

---

# 18. Projection dependency model

M09 establishes the following logical dependency pattern:

```text
Authoritative definitions / policies / Product-family artifacts
        |
        +--> logical Registry references
        |
        v
P1/P2 normalized design and resolution context
        |
        v
RRG -------------------------+
 |                            |
 +--> RGB                     |
 +--> Realization Plan        |
 +--> SYNCTX [conditional]    |
 |                            |
 +--> HPD [Product] <---------+
        |
        v
Blueprint Binding
        |
        v
Compilation Record correlates all material versions
```

The diagram expresses logical dependency, not ownership. A projection may reference another projection while each retains independent identity/version/currentness.

---

# 19. Relationship to Data PDEP Stage 8

M09 deliberately prepares M10 by reconciling the current Data PDEP Stage 8 outputs with the canonical artifact model.

| Current Data PDEP Stage 8 term | M09 canonical treatment |
|---|---|
| **Resolved Product Graph** | Product-scoped view/projection of **Resolved Realization Graph (RRG)**. |
| **Dependency Graph** | View/subprojection of RRG rather than a separate canonical authority/artifact family. |
| **SYNCTX** | Retained specialized conditional projection. |
| **HPD** | Retained canonical Product-Version operational projection. |
| **Unified Governance Bundle** | Historical alias; normalized to **Resolved Governance Bundle (RGB)**. |
| **Logical Execution Plan** | Execution-focused specialization/view of **Realization Plan**. |
| **Selected Blueprint** | Source/reference inside the stronger canonical **Blueprint Binding** artifact. |
| **Compilation Pack** | Packaging/transport composition of canonical compiled artifacts; not an independent semantic authority. |
| *(not explicit in current Stage 8 output list)* | **Compilation Record** should be added by M10 to preserve exact compilation provenance and historical reconstruction. |

M10 SHALL update the canonical PDEP architecture so the lifecycle and interactive PDEP Spec C remain synchronized with these M09 artifact semantics.

---

# 20. Relationship to M08 ABBs and M07 Overlays

## 20.1 Principal ABB participation

| M09 concern | Principal ABB(s) |
|---|---|
| Registry/Catalog discovery | P2-ABB-01 |
| Dependency/composition/compatibility | P2-ABB-02 |
| RRG/RGB/HPD/SYNCTX/Plan compilation | P2-ABB-03 |
| Blueprint Binding | P2-ABB-04 |
| semantic references | P1-ABB-02 + P2-ABB-01/02 |
| authority/accountability context | P1-ABB-03 |
| publication/port exposure references | P4-ABB-01 |
| Product/consumer discovery projection | P2-ABB-01 + P4 experience composition |

## 20.2 Principal Overlay participation

| Overlay | M09 relevance |
|---|---|
| X1 Governance/Policy/Control | policy applicability, RGB, exception/approval/control binding |
| X2 Security/Privacy/Identity/Entitlement | registry/projection protection and binding constraints |
| X3 Provenance/Evidence/Traceability | compilation evidence, source/reference lineage, CR |
| X4 Observability/Telemetry/Auditability | compiler/registry operational telemetry; not authority |
| X5 Quality/Fitness/Trust Evidence | quality/fitness inputs and projection references |
| X6 Evaluation/Assurance | assurance/evaluation findings that constrain eligibility or promotion |
| X7 Lifecycle/Version/Currentness/Change | version/currentness across every registry/artifact |
| X8 Resilience/Safety/Failure/Recovery | compilation/registry failure/degraded-state handling where material |
| X9 Economic/Cost Accountability | cost constraints/evidence used in Blueprint Binding and realization planning |

---

# 21. Historical HDIP terminology disposition after M09

| Historical term | M09 disposition |
|---|---|
| Data Product Registry | **RESHAPE** to core Product Registry with Data Product profile/view. |
| Blueprint Library | **ALIAS/RESHAPE** to canonical Blueprint Registry when the concern is governed registration; a documentation/library UI may remain a projection. |
| Data Catalog | **RETAIN AS PROJECTION** - Catalog is discovery projection, not Registry. |
| Marketplace | **RETAIN AS EXPERIENCE** - P4 acquisition/consumer experience, not Registry. |
| DPFI / Data Product Factory & Intelligence | **RETIRE AS CANONICAL COMPONENT NAME**; responsibilities resolve into P2-ABB-01..04 plus applicable Overlays. Historical alias may remain for traceability. |
| Resolved Product Graph | **SPECIALIZE** as Product-scoped RRG view. |
| Unified Governance Bundle | **ALIAS** to canonical Resolved Governance Bundle. |
| Logical Execution Plan | **SPECIALIZE/ALIAS** under canonical Realization Plan. |
| Compilation Pack | **RETAIN AS PACKAGING VIEW** if useful; it packages canonical M09 outputs but does not create a separate authority. |
| Product Knowledge Graph | **IMPLEMENTATION/PROJECTION OPTION** - graph realization is permitted but not required. |

---

# 22. M09 anti-patterns

M09 rejects the following anti-patterns:

1. **Registry equals authority** - assuming registration transfers semantic/domain/policy/Product authority.
2. **Registry equals qualification** - treating registration as Productness, ADS authority, conformance or control-effectiveness proof.
3. **Catalog equals registry** - using search/index projection as the registration authority.
4. **Marketplace equals entitlement** - assuming visible/acquirable means authorized.
5. **One physical registry per logical Registry** - turning logical independence into mandatory deployment fragmentation.
6. **Mega-registry semantic collapse** - consolidating implementation while erasing subject type/ownership/currentness distinctions.
7. **HPD becomes Product ontology** - moving BPS/PIN or family semantics into HPD-local classifications.
8. **Projection becomes truth source** - treating RRG/HPD/SYNCTX/RGB as upstream semantic authority.
9. **Compiler invents relationships** - deriving joins, dependencies, authority or obligations from weak evidence/naming similarity.
10. **Latest equals current** - selecting newest artifacts without governed currentness/eligibility resolution.
11. **Compilation success equals assurance** - treating a successful compile as correctness, safety, Fitness or approval.
12. **Graph database mandate** - assuming RRG/HPD/SYNCTX require one graph technology.
13. **SYNCTX universalization** - turning the synthetic-generation projection into generic HDIP Context or AI Context.
14. **UGB central-governance implication** - reading `Unified Governance Bundle` as proof that governance authority has been centralized.
15. **Blueprint equals deployment** - treating selection of a Blueprint as a completed runtime realization.
16. **Compilation Pack authority** - treating a packaging bundle as the source authority for its contents.
17. **Artifact equals ABB** - promoting a graph/descriptor/bundle/record into an architecture building block merely because it is first-class.
18. **Non-Product HPD inflation** - giving every capability an HPD to force symmetry.

---

# 23. Canonical M09 architecture rules

**HDIP-CLA-M09-R01 - Five-core-Registry freeze.** HDIP-CLA 0.1 SHALL use the five core logical Registry identities HDIP-REG-01 through HDIP-REG-05 defined by M09 unless changed through governed versioning.

**HDIP-CLA-M09-R02 - ADS Registry specialization.** HDIP-REG-D01 ADS Registry SHALL remain a canonical HDIP Data Profile specialization and SHALL NOT be generalized into a universal Information/Intelligence authority registry without independent evidence.

**HDIP-CLA-M09-R03 - Registry logicality.** A logical Registry SHALL define registration responsibility and contract semantics without implying one standalone physical registry system.

**HDIP-CLA-M09-R04 - Scoped registration authority.** A Registry MAY be authoritative for HDIP registration facts while remaining non-authoritative for the underlying subject's semantic, Product, policy, Data or AI meaning.

**HDIP-CLA-M09-R05 - Registration non-qualification.** Registry presence SHALL NOT by itself establish Product qualification, source authority, control effectiveness, semantic correctness, Fitness, trust, Assurance or HDIP conformance.

**HDIP-CLA-M09-R06 - Product Registry authority boundary.** HDIP-REG-01 SHALL preserve BPS/PIN and applicable Product-family authority and SHALL NOT invent an HDIP-local universal Product taxonomy.

**HDIP-CLA-M09-R07 - Product Registry family typing.** Product Registry entries SHALL preserve applicable Product Family/Kind/family-specific classification references rather than flattening Product families into one semantic type.

**HDIP-CLA-M09-R08 - Data Product Registry reshaping.** Historical Data Product Registry terminology SHALL be treated as a Data-profile view/subset of HDIP-REG-01 Product Registry rather than the HDIP-core Product Registry identity.

**HDIP-CLA-M09-R09 - Schema Registry non-semantic-authority.** HDIP-REG-02 SHALL register structural/interface schema versions and compatibility metadata without becoming the authority for business meaning merely through schema possession.

**HDIP-CLA-M09-R10 - Policy Registry authority boundary.** HDIP-REG-03 SHALL preserve the distinction between registered policy artifacts/references and the authority that creates/interprets the governing policy.

**HDIP-CLA-M09-R11 - Capability Registry non-Productness.** HDIP-REG-04 registration SHALL NOT make a capability a Product, AI Product or AI Primitive.

**HDIP-CLA-M09-R12 - Blueprint Registry abstraction.** HDIP-REG-05 SHALL register reusable realization Blueprints independently of vendor/platform-specific deployment products unless a Profile explicitly specializes them.

**HDIP-CLA-M09-R13 - Registry implementation consolidation.** Multiple logical Registries MAY share an implementation where subject identity, ownership, lifecycle, contracts and authority semantics remain distinguishable.

**HDIP-CLA-M09-R14 - Registry Entry Contract.** Every canonical logical Registry SHALL provide stable registration identity, subject/version reference and sufficient lifecycle/currentness/provenance context for deterministic reference and historical reconstruction.

**HDIP-CLA-M09-R15 - Latest/current distinction.** Registry resolution SHALL NOT assume the newest version is governed-current or eligible for a given purpose.

**HDIP-CLA-M09-R16 - Catalog projection.** Catalog SHALL remain a discovery/search projection across governed registered resources and SHALL NOT replace Registry or source authority.

**HDIP-CLA-M09-R17 - Marketplace experience.** Marketplace SHALL remain a consumer/acquisition experience and SHALL NOT independently establish Productness, entitlement, Fitness or Value.

**HDIP-CLA-M09-R18 - Registry/Catalog/Marketplace separation.** Registry, Catalog and Marketplace MAY share implementation/experience but SHALL retain distinct architectural meanings and evidence.

**HDIP-CLA-M09-R19 - Artifact class distinction.** Authoritative referenced artifacts, HDIP operational projections, compiled realization artifacts and compilation evidence artifacts SHALL remain distinguishable.

**HDIP-CLA-M09-R20 - HPD canonical status.** HPD SHALL remain the canonical HDIP operational Product-Version projection for applicable Products.

**HDIP-CLA-M09-R21 - HPD non-authority.** HPD SHALL NOT establish Product qualification, Product-family semantics, semantic authority, policy authority or deployment truth independently of the authoritative sources it references.

**HDIP-CLA-M09-R22 - HPD Product scope.** HPD SHALL NOT be assigned to a governed non-Product capability solely for architectural symmetry.

**HDIP-CLA-M09-R23 - RRG canonical status.** Resolved Realization Graph SHALL be the canonical family-neutral HDIP projection of resolved realization context produced through P2 compilation.

**HDIP-CLA-M09-R24 - Resolved Product Graph specialization.** Historical Resolved Product Graph SHALL be treated as a Product-scoped RRG projection/view and SHALL NOT constrain all HDIP realization to Products.

**HDIP-CLA-M09-R25 - RRG typed relationships.** RRG SHALL preserve dependency, composition, provenance, derivation, semantic relationship and binding distinctions where applicable.

**HDIP-CLA-M09-R26 - RRG non-invention.** RRG SHALL NOT contain material semantic, authority, policy, dependency, joinability or compatibility assertions unsupported by applicable evidence/authority.

**HDIP-CLA-M09-R27 - SYNCTX specialization.** SYNCTX SHALL remain a synthetic-generation relational/constraint projection and SHALL NOT become a universal HDIP Context or GEAIRM AI Context.

**HDIP-CLA-M09-R28 - SYNCTX version binding.** SYNCTX membership/bindings SHALL reference applicable Product Versions and authoritative evidence and SHALL preserve historical version meaning.

**HDIP-CLA-M09-R29 - RGB canonical status.** Resolved Governance Bundle SHALL be the canonical M09 term for a subject/version/context-scoped compiled governance projection.

**HDIP-CLA-M09-R30 - UGB alias.** Unified Governance Bundle MAY remain a historical alias but SHALL NOT imply centralized/unified governance authority.

**HDIP-CLA-M09-R31 - RGB authority preservation.** RGB SHALL preserve traceability to authoritative policy/control sources and SHALL NOT become their semantic/legal/regulatory authority.

**HDIP-CLA-M09-R32 - Realization Plan status.** Realization Plan SHALL remain a technology-neutral logical realization artifact and SHALL NOT require one orchestration/deployment technology.

**HDIP-CLA-M09-R33 - Logical Execution Plan specialization.** Logical Execution Plan MAY remain an execution-focused specialization/view of the canonical Realization Plan.

**HDIP-CLA-M09-R34 - Blueprint Binding status.** The canonical P2 realization output SHALL capture Blueprint Binding, including selected Blueprint/version and applicable constraints, rather than only a Blueprint name/reference.

**HDIP-CLA-M09-R35 - Blueprint selection non-deployment.** Successful Blueprint selection/binding SHALL NOT by itself prove deployment, promotion, Product publication or operational fitness.

**HDIP-CLA-M09-R36 - Compilation Record status.** A material P2 compilation occurrence SHALL produce or retain a Compilation Record sufficient to correlate material input/reference/rule/output versions and decisions.

**HDIP-CLA-M09-R37 - Compilation evidence non-assurance.** Compilation Record and successful compilation SHALL NOT by themselves establish correctness, Fitness, authorization, safety or Assurance.

**HDIP-CLA-M09-R38 - Resolve-not-invent.** Compilation SHALL resolve and validate governed evidence and SHALL NOT invent Product identity, semantic relationships, joinability, provenance, policy authority or obligations from weak evidence.

**HDIP-CLA-M09-R39 - Judgement honesty.** Judgement-dependent validation/approval/assurance SHALL retain accountable assessment and SHALL NOT be represented as machine-proven because compilation automation exists.

**HDIP-CLA-M09-R40 - Deterministic compilation reproducibility.** Deterministic compilation portions SHOULD produce semantically equivalent canonical projections when normalized pinned inputs, authoritative/reference versions, compiler/rule versions and applicable configuration are unchanged.

**HDIP-CLA-M09-R41 - Runtime stochasticity distinction.** Compilation reproducibility SHALL NOT be interpreted as a guarantee of deterministic runtime behavior for stochastic or externally variable execution.

**HDIP-CLA-M09-R42 - Historical non-mutation.** Later Product, policy, schema, capability, Blueprint or semantic changes SHALL NOT silently mutate already-used HPD/RRG/SYNCTX/RGB/Plan/Binding/Compilation Record versions.

**HDIP-CLA-M09-R43 - Material change versioning.** Material change to a compiled projection/binding SHALL create a new version/revision and trigger applicable impact/recompilation/evolution responsibility.

**HDIP-CLA-M09-R44 - Compilation Pack packaging rule.** Compilation Pack MAY package canonical M09 artifacts for transport/operation but SHALL NOT become a separate semantic/governance authority by packaging them together.

**HDIP-CLA-M09-R45 - Dependency Graph projection rule.** A Dependency Graph MAY be exposed as an RRG view/subprojection and SHALL NOT automatically become a separate canonical artifact authority.

**HDIP-CLA-M09-R46 - Graph technology neutrality.** HPD, RRG and SYNCTX MAY use graph-addressable representations but SHALL NOT require a particular graph database or RDF implementation for HDIP-CLA conformance.

**HDIP-CLA-M09-R47 - Projection reference stability.** Material cross-artifact references SHOULD use stable governed identifiers/IRIs or equivalent resolvable identifiers and preserve referenced version identity where version affects meaning.

**HDIP-CLA-M09-R48 - Evidence linkage.** Material Registry changes, resolution decisions and compilation outputs SHALL retain X3 evidence/provenance linkage sufficient for later reconstruction.

**HDIP-CLA-M09-R49 - Lifecycle participation.** Every versioned Registry entry and canonical M09 artifact SHALL participate in X7 lifecycle/version/currentness/change responsibilities where applicable.

**HDIP-CLA-M09-R50 - Security/privacy participation.** Registries and projections SHALL remain subject to X2 security/privacy/identity/entitlement obligations; metadata/provenance visibility SHALL NOT imply unrestricted access.

**HDIP-CLA-M09-R51 - Assurance participation.** Evaluation/Assurance findings MAY constrain eligibility, compilation or promotion but SHALL remain distinct from quality measures, telemetry and compilation success.

**HDIP-CLA-M09-R52 - Economic constraint participation.** X9 cost/economic constraints MAY influence realization planning and Blueprint Binding but SHALL NOT determine Product Value or Product qualification.

**HDIP-CLA-M09-R53 - DPFI component-name retirement.** Historical DPFI responsibilities SHALL remain realized through canonical P2 ABBs/Overlays, but `Data Product Factory & Intelligence` SHALL NOT be required as a canonical HDIP component or ABB identity.

**HDIP-CLA-M09-R54 - Artifact non-ABB preservation.** Registry entries, HPD, RRG, SYNCTX, RGB, Realization Plan, Blueprint Binding and Compilation Record SHALL NOT become ABBs merely because they are canonical/versioned artifacts.

**HDIP-CLA-M09-R55 - M10 reconciliation obligation.** M10 SHALL reconcile PDEP Stage 8 and related lifecycle semantics to the canonical M09 artifact model, including Compilation Record and Blueprint Binding semantics.

**HDIP-CLA-M09-R56 - No physical topology freeze.** M09 SHALL NOT prescribe registry centralization, graph/storage topology, compiler deployment topology, eventing/protocol choices, vendor products or physical service decomposition.

---

# 24. What M09 deliberately does not decide

M09 does not freeze:

- PDEP stage ordering/re-entry beyond the already accepted Data lifecycle baseline (M10);
- family-specific PDEP profiles other than preserving current Data-profile boundaries (M10);
- SSCF/CEP runtime/consumption architecture (M11);
- canonical inter-Plane Interaction Contract identities/directions (M12);
- external/adjacent-system boundary catalogue (M13);
- realization/deployment patterns (M14);
- final reference-view catalogue (M15);
- conformance assessment modes/evidence sufficiency (M16);
- concrete API schemas for Registries/HPD/RRG/RGB/CR;
- physical graph/database technology;
- mandatory centralization/federation of any Registry;
- vendor/tool selection.

---

# 25. M09 completion state

**HDIP-CLA M09 - COMPLETE.**

M09 establishes:

- **5 core logical Registry identities**;
- **1 canonical Data-profile Registry specialization (ADS Registry)**;
- scoped Registry authority limited to HDIP registration facts;
- canonical Registry/Catalog/Marketplace separation;
- a common Registry Entry Contract expectation;
- **HPD** as canonical Product-Version operational projection;
- **Resolved Realization Graph (RRG)** as canonical family-neutral resolved-realization projection;
- historical Resolved Product Graph as a Product-scoped RRG projection;
- **SYNCTX** as a specialized synthetic-generation projection;
- **Resolved Governance Bundle (RGB)** as canonical compiled governance projection, with UGB retained only as a historical alias;
- **Realization Plan** as the family-neutral logical realization artifact;
- **Blueprint Binding** as the canonical selected-blueprint plus constraint binding artifact;
- **Compilation Record** as the canonical evidence artifact for material compilation occurrences;
- explicit Stage 8 reconciliation requirements for M10;
- **18 anti-patterns**;
- **56 normative M09 rules**;
- **0 new Planes**;
- **0 new Overlays**;
- **0 new ABBs**.

### Next stage

> **M10 - Product Development & Evolution Architecture — PDEP**

M10 will apply the frozen P1-P5/X1-X9/ABB/M09 artifact model to the Product development/evolution lifecycle, reconcile the current Data PDEP Stage 0-10 baseline and progressive G0/Spec A/Spec C projections, and define the canonical cross-Plane PDEP architecture without making one Product-family lifecycle universal.
