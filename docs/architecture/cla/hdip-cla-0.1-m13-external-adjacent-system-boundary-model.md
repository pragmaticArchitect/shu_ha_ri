---
id: hdip-cla-0.1-m13-external-adjacent-system-boundary-model
title: HDIP-CLA 0.1 M13 - External & Adjacent-System Boundary Model
sidebar_label: M13 - External & Adjacent Boundaries
---

# HDIP-CLA 0.1 M13 - External & Adjacent-System Boundary Model

**Status:** COMPLETE

## 1. Purpose

M13 defines and freezes the canonical logical boundary model between the **Holistic Data, Information and Intelligence Platform (HDIP)** and the semantic authorities, Product authorities, peer architectures, enterprise systems, external providers and downstream environments with which HDIP must interoperate.

M13 answers:

> **Where does HDIP jurisdiction stop, what responsibility remains outside HDIP, and what must an authority-preserving boundary contract carry when HDIP references, invokes, publishes to, consumes from, or co-realizes with an adjacent system or authority?**

M13 applies the M12 Interaction Contract discipline at the **edges of HDIP**. It does not introduce a second integration model.

M13 is technology-neutral. A logical boundary may exist even when both sides are physically co-located in the same cloud account, process, platform, database, enterprise tool, deployment environment or organizational team.

---

# 2. Derivation basis

M13 is constrained by the architecture frozen through M12:

- **M01** - HDIP is an enterprise logical realization/composition architecture and preserves external semantic and Product authorities;
- **M02** - source architecture responsibilities retain provenance and are not made equivalent by label similarity;
- **M03** - adjacent artifacts and external authorities are referenced rather than silently absorbed into HDIP semantics;
- **M04** - explicit contractual interoperability, federated authority preservation, topology independence and projection non-authority;
- **M05** - authority, Product-family, domain-runtime and consequential-action distinctions;
- **M06** - five logical Planes and Shared Platform / Utility Foundation;
- **M07** - nine cross-cutting Overlays;
- **M08** - twenty-two canonical logical ABBs and no component reflex;
- **M09** - Registry/projection/compilation architecture and authority-preserving references;
- **M10** - PDEP cross-Plane lifecycle;
- **M11** - SSCF / CEP consumption/runtime architecture;
- **M12** - twenty-one canonical inter-Plane interactions and one technology-neutral Interaction Contract model.

M13 also uses the adjacent-authority discipline established in the peer generic architectures as supporting evidence: semantic/reference/Product/standard/enterprise-realization boundaries remain typed and many-to-many rather than flattened into one specification hierarchy.

---

# 3. What is inside HDIP and what is not

For M13, the following are **inside the HDIP logical architecture boundary**:

```text
P1-P5 canonical Plane responsibilities
X1-X9 canonical Overlay responsibilities
HDIP-FND Shared Platform / Utility Foundation responsibility
HDIP canonical ABB responsibilities
HDIP Registry responsibilities
HPD / RRG / SYNCTX / RGB / Realization Plan / Blueprint Binding /
Compilation Record responsibilities
PDEP / SSCF / CEP lifecycle and experience responsibilities
M12 Interaction Contracts
```

The following remain **outside HDIP authority unless explicitly assigned by an applicable enterprise governance model**:

```text
semantic-model ownership
Product / PIN qualification authority
Product-family semantic authority
Data/source authority
enterprise policy/legal/regulatory authority
Decision/Action authority
external standards ownership
third-party provider authority
consumer-system business authority
peer reference-architecture authority
```

A physical implementation MAY realize responsibilities from both sides of a boundary. Physical co-location SHALL NOT erase the logical boundary.

---

# 4. Boundary model vocabulary

M13 uses four complementary concepts.

## 4.1 Boundary Class

A **Boundary Class** groups adjacent concerns that have materially different jurisdiction or interoperability semantics.

## 4.2 Boundary Family

A **Boundary Family** is a canonical HDIP boundary identity used to reason consistently about one recurring adjacent-system/authority concern.

## 4.3 Boundary Instance

A **Boundary Instance** is a concrete enterprise or provider-specific realization of a Boundary Family, for example an enterprise IAM platform, one external model provider, one system of record, or one downstream workflow system.

## 4.4 External Boundary Contract

An **External Boundary Contract (EBC)** is the M13 specialization of the M12 Interaction Contract model for a material crossing between HDIP and an adjacent boundary.

An EBC is not automatically an API, legal contract, network ACL, schema or vendor integration configuration. Those artifacts MAY realize parts of the EBC.

---

# 5. Canonical boundary classes

M13 freezes six canonical Boundary Classes.

| ID | Boundary Class | Purpose |
|---|---|---|
| **BC1** | **Authority & Specification Boundary** | Preserve externally owned semantic, Product, architecture, standard and policy jurisdiction. |
| **BC2** | **Enterprise Control-System Boundary** | Interoperate with identity, security, privacy, entitlement, policy and governance/control infrastructure without transferring authority. |
| **BC3** | **Producer / Source-System Boundary** | Ingest, reference or bind governed Data/Information/Intelligence sources while preserving source identity, authority, currentness and provenance. |
| **BC4** | **Execution / Platform Boundary** | Bind HDIP logical realization to enterprise or provider runtime/infrastructure environments without making those environments semantic authorities. |
| **BC5** | **Consumer / Consequence Boundary** | Expose Products/capabilities to consumers and downstream workflow/decision/action environments while preserving access-versus-consequence distinctions. |
| **BC6** | **Provider / Partner / Evidence Boundary** | Govern interaction with third-party providers, partners and external evidence/observability/economic systems. |

Boundary Classes are logical groupings. They do not imply six gateways, networks, platforms or teams.

---

# 6. Canonical Boundary Family catalogue

M13 freezes **twelve canonical HDIP Boundary Families**.

| ID | Boundary Family | Class | Principal jurisdiction outside HDIP |
|---|---|---|---|
| **HDIP-BND-01** | **Semantic Authority Boundary** | BC1 | GEDRM, GEARM, GEAIRM and applicable enterprise/domain semantic authorities. |
| **HDIP-BND-02** | **Product & Product-Family Authority Boundary** | BC1 | BPS/PIN and applicable Product-family authorities such as AIPS and family specifications. |
| **HDIP-BND-03** | **Peer Reference-Architecture Boundary** | BC1 | GEDRA, GEARA, GEAIRA and other independently governed peer architectures. |
| **HDIP-BND-04** | **External Standard & Vocabulary Boundary** | BC1 | External standards/vocabularies such as W3C PROV and applicable external interoperability standards. |
| **HDIP-BND-05** | **Enterprise Policy, Legal & Control-Authority Boundary** | BC1/BC2 | Enterprise policy owners, legal/regulatory interpretation, control owners, risk/compliance authorities and exception authorities. |
| **HDIP-BND-06** | **Identity, Security, Privacy & Entitlement System Boundary** | BC2 | Enterprise identity providers, IAM/PAM, consent/privacy systems, entitlement services, key/secrets systems and security infrastructure. |
| **HDIP-BND-07** | **Authoritative Producer / Source-System Boundary** | BC3 | Systems of record, ADS/source systems, upstream Products/capabilities, authoritative feeds and source-domain providers. |
| **HDIP-BND-08** | **Runtime, Processing & Infrastructure Boundary** | BC4 | Data processing engines, analytical runtimes, AI runtimes, cloud/on-prem infrastructure, schedulers, messaging and execution environments. |
| **HDIP-BND-09** | **Product / Capability Provider Boundary** | BC3/BC4 | Internal or external Product/capability providers whose governed Ports/interfaces are discovered, bound or consumed by HDIP. |
| **HDIP-BND-10** | **Consumer & Downstream Integration Boundary** | BC5 | Human consumers, applications, BI/analytical tools, APIs, agents, automation, integration and workflow systems. |
| **HDIP-BND-11** | **Decision, Action & Consequence Boundary** | BC5 | Decision engines, tool/action systems, transactional systems, physical/digital actuators and accountable human decision environments. |
| **HDIP-BND-12** | **External Provider, Partner, Evidence & Economic-System Boundary** | BC6 | Third-party data/model/API/SaaS providers, partners, audit/SIEM/observability, lineage/provenance and FinOps/economic systems. |

One concrete system MAY participate in several Boundary Families. A cloud provider, for example, may host runtime infrastructure, external AI services and economic metering. M13 classification is responsibility-based rather than vendor-based.

---

# 7. Canonical External Boundary Contract model

An EBC reuses the M12 Interaction Contract model and adds boundary-specific obligations where material.

An EBC SHOULD identify:

| Dimension | Boundary question |
|---|---|
| **Boundary family / instance** | Which `HDIP-BND-*` family and concrete adjacent party/system applies? |
| **Jurisdiction owner** | Which authority owns the external meaning, rule, Product, source, runtime or consequence? |
| **HDIP responsibility** | Which Plane / ABB / Overlay initiates or consumes the crossing? |
| **Direction** | Inbound to HDIP, outbound from HDIP, bidirectional, or reference-only? |
| **Subject / version** | Which Product, source, semantic model, policy, capability, provider or contract version applies? |
| **Authority reference** | Which external authority/reference justifies the exchanged meaning or permission? |
| **Conformance claim** | Which specification/standard conformance is claimed, by whom, for which bounded subject? |
| **Currentness / effective time** | Which external version/currentness/effective-time rules govern eligibility? |
| **Compatibility** | Which semantic, contract, protocol, capability and policy compatibility conditions apply? |
| **Identity / trust zone** | Which actor/workload identities and trust-zone assumptions are valid? |
| **Security / privacy / residency** | Which protection, purpose, legal-location or confidentiality obligations apply? |
| **Delivery / processing semantics** | Which acknowledgement, replay, ordering, retry and side-effect rules apply? |
| **Evidence / provenance** | Which source, provider, decision and occurrence evidence must survive the boundary? |
| **Failure / withdrawal** | What happens on provider failure, revocation, withdrawal, stale evidence or indeterminate state? |
| **Exit / substitution** | Can the external provider/runtime/source be replaced without changing HDIP semantics? What migration evidence is required? |
| **Economic obligations** | Which metering, licensing, quota, cost attribution or commercial constraints apply? |
| **Human/accountable obligations** | Which approvals, exceptions, escalations or accountable decisions remain outside automation? |

The EBC is conceptual and MAY be realized through several technical and governance artifacts.

---

# 8. HDIP-BND-01 - Semantic Authority Boundary

HDIP references semantics needed for P1 definition, P2 compatibility, P3 typed execution, P4 consumption and P5 interpretation. It does not become the owner of externally governed semantics merely because it stores, indexes, maps, validates or compiles them.

Canonical authorities include, where applicable:

```text
GEDRM  - Data semantics
GEARM  - Information / Analytics semantics
GEAIRM - Enterprise-AI semantics
enterprise/domain semantic authorities
```

Required boundary behavior includes:

- stable semantic identity and version reference;
- authoritative-source provenance;
- compatibility/mapping evidence where local terminology differs;
- currentness/effective-time context;
- change/supersession propagation;
- explicit treatment of unresolved semantic gaps.

```text
copy of ontology != semantic authority
mapping != equivalence
validation != ownership
shared semantic repository != merged semantic jurisdiction
```

Semantic gaps that require new meaning SHOULD be referred to the appropriate semantic authority rather than silently defined inside an HDIP projection.

---

# 9. HDIP-BND-02 - Product & Product-Family Authority Boundary

HDIP supports Product development, registration, discovery, provision, consumption and evolution but does not independently determine Productness.

Canonical external Product authorities include:

```text
BPS / PIN
applicable Product-family specifications
AIPS for AI Product qualification/classification/governance
other family authorities where adopted
```

Boundary behavior SHALL preserve:

- Product identity and Product Version identity;
- Product-family identity;
- qualification/classification provenance;
- Product Promise / contract references where applicable;
- Product ownership/accountability references;
- Product Port/interface identity;
- applicable family-specific lifecycle and conformance claims.

```text
registered != Product
published != Product
consumed != Product
composed != new Product automatically
HDIP HPD != Product ontology authority
```

---

# 10. HDIP-BND-03 - Peer Reference-Architecture Boundary

HDIP composes and realizes responsibilities from independently governed reference architectures including:

```text
GEDRA
GEARA
GEAIRA
```

M13 permits many-to-many mapping between HDIP and peer architecture responsibilities.

It does not permit:

- one-to-one Plane equivalence by label or numbering;
- one-to-one ABB equivalence without responsibility evidence;
- transferring conformance from a peer architecture to HDIP or vice versa;
- treating HDIP as a parent generic architecture of GEDRA/GEARA/GEAIRA;
- treating the peer architectures as subordinate implementation modules of HDIP.

A shared implementation may co-realize responsibilities from several architectures while conformance and jurisdiction remain independently assessable.

---

# 11. HDIP-BND-04 - External Standard & Vocabulary Boundary

HDIP MAY align with external standards/vocabularies where doing so improves interoperability or evidence portability.

Examples include provenance standards such as W3C PROV and domain/industry interoperability standards adopted by the enterprise.

Boundary rules include:

- reuse external identifiers/vocabulary without shadowing their ownership;
- record the standard/version/profile used;
- preserve mapping direction and information loss where representations differ;
- distinguish syntactic/profile conformance from semantic/HDIP conformance;
- avoid claiming that use of a standard proves quality, trust, authority or fitness.

```text
standard-compatible != semantically equivalent
standard-conformant != HDIP-conformant
PROV-compatible evidence != assurance
```

---

# 12. HDIP-BND-05 - Enterprise Policy, Legal & Control-Authority Boundary

X1 may resolve, coordinate, compile and evidence governing obligations, but authoritative policy/legal/control ownership remains outside HDIP unless enterprise governance explicitly delegates it.

The boundary includes, where applicable:

- enterprise policies and standards;
- legal/regulatory interpretation;
- risk appetite and control requirements;
- control ownership;
- exception/waiver authority;
- records of accountable approval or acceptance.

The boundary SHALL preserve:

```text
policy authority
    != policy applicability
    != policy compilation
    != runtime enforcement
    != Control Evidence
```

A machine-evaluable policy may be enforced automatically while policy authorship and accountable exception authority remain external.

---

# 13. HDIP-BND-06 - Identity, Security, Privacy & Entitlement System Boundary

X2 interoperates with enterprise security/control systems rather than redefining their underlying identity or security architecture.

Adjacent systems MAY include:

- identity providers;
- IAM/PAM;
- entitlement systems;
- consent/privacy systems;
- data-loss/prevention and security-policy systems;
- key/secrets/certificate infrastructure;
- security posture/trust-zone services.

M13 preserves:

```text
identity != authority != ownership != entitlement
Authentication != Authorization
Product-access Authorization != consequential Decision/Action Authorization
```

Entitlement or credential state received from an external system SHALL be bound to purpose, scope, version/currentness and applicable Product/Port context where required.

No transitive-entitlement assumption is permitted merely because access was valid upstream.

---

# 14. HDIP-BND-07 - Authoritative Producer / Source-System Boundary

HDIP may ingest, reference, discover or bind Data/Information/Intelligence from authoritative producer/source systems.

Examples include:

- Systems of Record;
- ADS/source systems;
- upstream Data Products;
- Information Products;
- AI/Intelligence capabilities;
- authoritative external feeds.

The boundary SHALL preserve:

- source identity;
- authoritative scope;
- source/version/currentness;
- event/effective time where relevant;
- schema/semantic references;
- lineage/provenance;
- applicable quality/control evidence;
- permitted purpose/use constraints;
- upstream revocation/supersession semantics.

```text
ingestion != ownership
copy != authority
cache != authoritative source
transformation != source rewrite
matching field names != semantic equivalence
```

A non-owning copy or cache MUST retain sufficient authority/currentness reference to avoid masquerading as the authoritative source.

---

# 15. HDIP-BND-08 - Runtime, Processing & Infrastructure Boundary

HDIP logical responsibilities may be realized on enterprise or provider runtime/infrastructure environments, including:

- Data processing/streaming engines;
- analytical runtimes;
- AI/model/agent runtimes;
- orchestration/scheduling platforms;
- messaging/event infrastructure;
- cloud/on-prem compute/storage/network;
- deployment/promotion platforms.

HDIP-FND and P2/P3 may bind to these environments without transferring semantic, Product, policy or Decision authority to the runtime.

The EBC SHOULD preserve:

- runtime/environment identity/version;
- capability and compatibility constraints;
- environment currentness/eligibility;
- deployment/binding evidence;
- residency/security constraints;
- resilience/failure semantics;
- cost attribution;
- provider/runtime substitution constraints.

```text
runs on != owned by
hosted in != semantically governed by
runtime success != Product qualification
runtime health != assurance
```

---

# 16. HDIP-BND-09 - Product / Capability Provider Boundary

A Product/capability provider exposes governed functionality or information to HDIP through an externally owned Port/interface/contract.

The provider may be internal or external to the enterprise.

HDIP SHALL preserve:

- provider identity and accountability;
- Product/capability identity and version;
- interface/Port contract identity;
- supported purpose/use constraints;
- availability/currentness;
- compatibility assumptions;
- evidence and provenance obligations;
- failure/degradation behavior;
- entitlement/access boundary;
- provider lifecycle/supersession events.

Discovery or successful invocation SHALL NOT imply qualification, fitness, trust or entitlement.

---

# 17. HDIP-BND-10 - Consumer & Downstream Integration Boundary

P4 exposes governed Products/capabilities to consumers and downstream systems.

Adjacent consumers include:

- human users;
- business applications;
- BI/analytical tools;
- APIs and integration services;
- automated workloads;
- agents and agentic workflows;
- downstream Products/capabilities.

The boundary SHALL preserve:

- PCON/consumer identity;
- CIR/purpose context where applicable;
- Access Decision;
- Access Descriptor;
- Usage Contract;
- Product/Port identity;
- current entitlement state;
- usage/evidence correlation;
- downstream handling obligations where contractually required.

The consumer does not inherit upstream authority merely by consuming a Product.

```text
consumer access != Product ownership
consumer access != Data authority
consumer access != policy authority
consumer access != permission for every downstream use
```

---

# 18. HDIP-BND-11 - Decision, Action & Consequence Boundary

M13 freezes an explicit boundary between ordinary Product/capability consumption and downstream consequential Decision/Action environments.

Adjacent environments may include:

- Decision engines;
- case/workflow systems;
- order/transaction systems;
- tools invoked by agents;
- digital-action services;
- physical actuators;
- accountable human decision processes.

The boundary preserves the M05/M11 distinction:

```text
Recommendation != Decision != Authorization != Action
Product-access Authorization != point-of-use consequential Authorization
```

HDIP may provide evidence/context into a Decision/Action environment, but the downstream authority responsible for the consequence remains independently governed.

Where GEAIRA applies, its Decision, Action and Human Oversight responsibilities remain authoritative for the applicable AI/consequential-action profile.

---

# 19. HDIP-BND-12 - External Provider, Partner, Evidence & Economic-System Boundary

HDIP may depend on external organizations or enterprise systems that supply Data, models, APIs, SaaS capabilities, audit evidence, observability or economic information.

Examples include:

- external data providers;
- foundation/model providers;
- SaaS/API providers;
- market/reference-data providers;
- delivery/business partners;
- SIEM/audit platforms;
- lineage/provenance systems;
- observability platforms;
- FinOps/cost systems.

The boundary SHALL make explicit, where material:

- provider identity and jurisdiction;
- commercial/licensing constraints;
- data-use/training/reuse restrictions;
- provider/runtime/model version;
- residency/privacy constraints;
- service-level and failure semantics;
- provenance/evidence sufficiency;
- metering/cost attribution;
- provider withdrawal/substitution/exit strategy;
- currentness and change notification obligations.

A provider's assurance, certification or SLA MAY be evidence but does not automatically establish HDIP, Product or use-case assurance.

---

# 20. Boundary direction model

M13 distinguishes four boundary directions:

| Direction | Meaning |
|---|---|
| **REFERENCE-ONLY** | HDIP references an external authority/standard without operationally invoking it for each occurrence. |
| **INBOUND** | An external system/authority supplies data, definitions, state, evidence or capability into HDIP. |
| **OUTBOUND** | HDIP publishes/provisions information, Products, requests, evidence or results to an adjacent system. |
| **BIDIRECTIONAL** | Material state, request/result, clarification, feedback, change or evidence flows cross both ways. |

Direction does not imply authority direction.

```text
information flows into HDIP != authority transfers into HDIP
HDIP sends instruction outward != HDIP owns external action authority
```

---

# 21. Boundary currentness and version model

Every material external boundary MUST be capable of distinguishing, where applicable:

```text
known version
latest version
governed-current version
eligible version
effective version at occurrence time
superseded version
revoked/withdrawn version
unknown/indeterminate version
```

M13 therefore prohibits the assumption:

```text
latest == current == eligible
```

External change MAY require:

- P1 intent/authority review;
- P2 compatibility/impact analysis;
- recompilation/rebinding;
- P3 runtime migration;
- P4 consumer/contract change;
- P5 outcome reassessment;
- X6 assurance re-evaluation;
- X7 lifecycle/currentness update.

Historical occurrences retain the versions and authority context valid at the time they occurred.

---

# 22. Caching, projection and local-copy boundary rules

HDIP MAY cache or project external information to reduce interaction distance where contracts permit it.

A local copy/projection SHOULD retain, where material:

- external authoritative identity;
- source/version/currentness;
- retrieval/effective time;
- expiry/TTL or invalidation semantics;
- transformation/projection provenance;
- permitted use restrictions;
- synchronization/reconciliation status.

A local copy SHALL NOT silently become authoritative merely because the external source is temporarily unavailable.

Where freshness/currentness cannot be established, the state SHOULD become explicit (`STALE`, `UNKNOWN`, `INDETERMINATE`, or equivalent) rather than being assumed current.

---

# 23. Cross-boundary conformance model

Conformance claims remain independently scoped.

```text
HDIP conformance
    != GEDRA conformance
    != GEARA conformance
    != GEAIRA conformance
    != BPS/PIN Product qualification
    != Product-family conformance
    != provider certification
    != external-standard conformance
```

A composite solution MAY hold several claims simultaneously, but each claim SHALL identify:

- subject;
- version;
- specification/profile;
- assessor/authority;
- scope;
- evidence;
- currentness.

Mapping or co-realization does not make conformance transitive.

---

# 24. Cross-boundary security and trust-zone model

M13 does not prescribe network zones, but every material boundary crossing SHOULD identify relevant trust assumptions.

These may include:

- actor/workload identity;
- authentication method;
- entitlement scope;
- confidentiality/integrity requirements;
- purpose limitation;
- tenant/domain boundary;
- residency constraints;
- secret/key/certificate requirements;
- data minimization/exposure shaping;
- external provider trust posture;
- audit/evidence requirements.

Security posture is evidence for access/control decisions, not semantic or Product authority.

---

# 25. External provider failure, withdrawal and substitution

M13 treats external dependency failure as an architecture concern rather than a procurement-only issue.

For material dependencies, the EBC SHOULD specify:

- failure detection;
- timeout/degraded-mode semantics;
- retries/idempotency;
- fallback/substitution eligibility;
- data/model/API version compatibility;
- cached-state behavior;
- unknown-side-effect handling;
- consumer notification where relevant;
- evidence preservation;
- recovery/reconciliation;
- provider withdrawal/end-of-life handling;
- migration/exit strategy.

Substitution is not assumed semantically safe merely because two providers expose similar APIs.

---

# 26. Relationship to M12 canonical interactions

M13 does not create another internal interaction catalogue. Instead, an M12 interaction MAY terminate at or traverse an M13 boundary.

Examples:

```text
P1 semantic reference
  -> BND-01 Semantic Authority Boundary

P1/P2 policy resolution
  -> BND-05 Policy/Control Authority Boundary

P2 source discovery/binding
  -> BND-07 Producer / Source-System Boundary

P2 realization binding
  -> BND-08 Runtime / Infrastructure Boundary

P4 Product access
  -> BND-10 Consumer Boundary

P4 downstream integration
  -> BND-11 Decision / Action Boundary

P3 external model/API execution
  -> BND-12 External Provider Boundary

X3/X4/X9 evidence exchange
  -> BND-12 Evidence / Economic-System Boundary
```

The same M12 identity/correlation/evidence discipline remains applicable where material.

---

# 27. Boundary applicability across HDIP Planes

The following matrix is indicative, not exclusive.

| Boundary | P1 | P2 | P3 | P4 | P5 |
|---|:---:|:---:|:---:|:---:|:---:|
| BND-01 Semantic Authority | **P** | **P** | S | S | S |
| BND-02 Product / Family Authority | **P** | **P** | S | **P** | S |
| BND-03 Peer Reference Architecture | **P** | **P** | **P** | **P** | **P** |
| BND-04 External Standard / Vocabulary | S | S | S | S | S |
| BND-05 Policy / Legal / Control Authority | **P** | **P** | S | **P** | S |
| BND-06 Identity / Security / Privacy / Entitlement | S | S | S | **P** | S |
| BND-07 Producer / Source System | S | **P** | **P** | S | S |
| BND-08 Runtime / Processing / Infrastructure | S | **P** | **P** | S | S |
| BND-09 Product / Capability Provider | S | **P** | **P** | **P** | S |
| BND-10 Consumer / Downstream Integration | S | S | S | **P** | S |
| BND-11 Decision / Action / Consequence | S | S | S | **P** | **P** |
| BND-12 Provider / Partner / Evidence / Economic | S | S | **P** | S | **P** |

Legend:

```text
P = principal boundary participation
S = supporting / contextual participation
```

---

# 28. Representative cross-boundary scenarios

## 28.1 Data Product from authoritative ADS

```text
Authoritative source / ADS              HDIP
      BND-07                              |
        |                                v
        +---- source identity -------> P2 discovery/binding
        +---- data/events -----------> P3 Data runtime
        +---- schema/semantics ------> BND-01 references via P1/P2
        +---- source provenance -----> X3
                                         |
                                         v
                                   P4 Product Port
```

HDIP processing and Product realization do not transfer source Data authority.

## 28.2 Information Product using Data Products and analytical runtime

```text
Data Products --BND-09--> P2 composition
                               |
                               v
analytical runtime --BND-08--> P3 Information Formation
                               |
                               v
                         P4 Information Product Port
```

The runtime provider does not become Information semantic authority or Product owner.

## 28.3 AI Product using an external model provider

```text
AIPS / Product-family authority --BND-02--> P1/P2
GEAIRA responsibilities ---------BND-03--> HDIP profile mapping
External model provider ---------BND-12--> P3 Intelligence Execution
Enterprise IAM ------------------BND-06--> P4 access
```

Model-provider availability or certification does not establish AI Product qualification, point-of-use action authority or HDIP assurance.

## 28.4 Consumer access followed by consequential action

```text
PCON --BND-10--> P4 Product access
                     |
                     | governed Product result
                     v
Decision / Action environment --BND-11--> consequential effect
```

Product entitlement does not automatically authorize the consequential effect.

## 28.5 Enterprise policy revocation

```text
Policy authority --BND-05--> X1/P1
                               |
                               +--> M12 INT-08 governing revocation
                               +--> P2 recompilation/invalidations
                               +--> P4 access change
```

Historical occurrences retain the policy/version that governed them at occurrence time.

## 28.6 External provider outage or withdrawal

```text
Provider --BND-12--> P3/P2
         failure / withdrawal
                |
                +--> X8 degraded/failure handling
                +--> X7 lifecycle/currentness change
                +--> P2 substitution analysis
                +--> P4/P5 consumer/outcome impact
```

Substitution requires compatibility evidence rather than API similarity alone.

## 28.7 External provenance standard alignment

```text
HDIP X3 evidence model
        |
        +-- maps to --> BND-04 external provenance vocabulary
```

Mapping improves interoperability but does not transfer evidence ownership or make provenance equivalent to assurance.

---

# 29. Boundary anti-patterns

M13 rejects the following anti-patterns:

1. **Physical-perimeter fallacy** - treating only network boundaries as architecture boundaries.
2. **Shared-platform authority collapse** - assuming co-hosted systems share semantic or governance authority.
3. **One namespace to rule them all** - forcing every adjacent authority into one HDIP-owned identifier namespace.
4. **Conformance transitivity** - treating conformance to one specification as conformance to another.
5. **Mapping-equals-equivalence** - treating a cross-model mapping as proof of semantic identity.
6. **Registry-as-external-authority** - letting HDIP Registry state replace an external authority source.
7. **Cache-as-source** - allowing a local cache/projection to masquerade as authoritative source state.
8. **Latest-is-current** - adopting the newest external version without governed currentness/eligibility.
9. **IAM-is-authority** - treating authentication/entitlement infrastructure as Product/Data/policy/Decision authority.
10. **Access-is-action-authority** - using Product access permission as downstream consequential authorization.
11. **Provider-certification-is-assurance** - treating provider certification/SLA as complete use-case assurance.
12. **API-shape compatibility** - substituting providers because endpoints/schemas look similar while ignoring semantics/effects/policy.
13. **External-success-is-Productness** - inferring Product status from successful external provisioning or invocation.
14. **Provider-version opacity** - failing to record external provider/model/runtime version and occurrence-time context.
15. **Silent provider drift** - accepting external changes without compatibility/impact analysis.
16. **Silent policy drift** - changing resolved policy/control behavior without preserving effective-time/version evidence.
17. **External evidence equals truth** - treating logs/certificates/claims as self-validating proof.
18. **Dependency without provenance** - consuming external sources/providers without reconstructible source identity.
19. **Unlimited downstream reuse** - assuming an authorized consumer may repurpose outputs without contract/purpose constraints.
20. **External failure as implementation detail** - omitting architectural degraded/fallback/recovery semantics for material dependencies.
21. **Vendor lock-in by architecture name** - naming a provider product as the canonical HDIP boundary/ABB.
22. **Peer-architecture flattening** - replacing GEDRA/GEARA/GEAIRA distinctions with one HDIP-local architecture model.
23. **Product-family flattening** - treating all Product families as semantically identical at the boundary.
24. **Boundary checkbox** - documenting a boundary name without its authority, version, contract, evidence and failure obligations.

---

# 30. Canonical M13 architecture rules

**HDIP-CLA-M13-R01 - Boundary-model status.** HDIP-BND-01 through HDIP-BND-12 SHALL be the canonical HDIP-CLA 0.1 external/adjacent Boundary Families unless changed through governed versioning.

**HDIP-CLA-M13-R02 - Logical-boundary semantics.** A canonical boundary SHALL represent a jurisdiction/responsibility/contract distinction and SHALL NOT require a physical network perimeter or separate deployable system.

**HDIP-CLA-M13-R03 - M12 contract reuse.** Material external crossings SHALL reuse the M12 Interaction Contract discipline through an External Boundary Contract rather than creating an incompatible integration model.

**HDIP-CLA-M13-R04 - Typed boundary.** A material adjacent relationship SHALL identify its Boundary Family and SHALL NOT rely solely on a generic `integrates with` assertion.

**HDIP-CLA-M13-R05 - Many-to-many boundary mapping.** One adjacent system MAY participate in several Boundary Families and one Boundary Family MAY be realized by several systems/providers.

**HDIP-CLA-M13-R06 - Authority preservation.** Reference, mapping, ingestion, storage, compilation, execution or publication across a boundary SHALL NOT transfer external semantic, Product, Data, policy, Decision or standards authority to HDIP.

**HDIP-CLA-M13-R07 - Co-location non-collapse.** Physical co-location or shared implementation SHALL NOT erase a logical boundary or make conformance/authority shared.

**HDIP-CLA-M13-R08 - Independent conformance.** HDIP and adjacent specifications/standards/providers SHALL retain independently scoped conformance/qualification claims.

**HDIP-CLA-M13-R09 - No namespace consolidation requirement.** M13 SHALL NOT require one global HDIP namespace or Registry for all adjacent authorities.

**HDIP-CLA-M13-R10 - External-version explicitness.** Material boundary interactions SHALL identify applicable external versions/currentness where the result depends on them.

**HDIP-CLA-M13-R11 - Historical boundary truth.** Later external change, revocation, migration or provider substitution SHALL NOT rewrite which external version/authority governed a historical occurrence.

**HDIP-CLA-M13-R12 - Latest/current distinction.** The latest external version SHALL NOT automatically be treated as governed-current, eligible or compatible.

**HDIP-CLA-M13-R13 - Compatibility beyond syntax.** Schema/protocol/API compatibility SHALL NOT by itself prove semantic, capability, effect, policy, Product-family or assurance compatibility.

**HDIP-CLA-M13-R14 - Mapping non-equivalence.** A semantic/architecture mapping SHALL NOT by itself establish equivalence, ownership transfer or conformance transfer.

**HDIP-CLA-M13-R15 - Semantic-authority boundary.** HDIP-BND-01 SHALL preserve GEDRM/GEARM/GEAIRM and applicable enterprise/domain semantic authority independently of HDIP projections and tooling.

**HDIP-CLA-M13-R16 - Semantic-gap referral.** A material semantic gap SHALL be referred to the appropriate semantic authority rather than silently invented by an HDIP compiler/projection.

**HDIP-CLA-M13-R17 - Product-authority boundary.** HDIP-BND-02 SHALL preserve BPS/PIN and applicable Product-family qualification/classification authority.

**HDIP-CLA-M13-R18 - No external Productness inference.** Successful provider invocation, publication, Registry presence, interface exposure or repeated use SHALL NOT independently establish Product status.

**HDIP-CLA-M13-R19 - Peer-architecture independence.** HDIP-BND-03 SHALL preserve GEDRA, GEARA and GEAIRA as independently governed reference architectures rather than HDIP submodules.

**HDIP-CLA-M13-R20 - Peer mapping many-to-many.** HDIP-to-peer Plane/ABB mappings MAY be many-to-many; similar labels or numbering SHALL NOT create one-to-one equivalence.

**HDIP-CLA-M13-R21 - External-standard ownership.** HDIP-BND-04 SHALL reuse external standards/vocabularies without shadowing or redefining their ownership.

**HDIP-CLA-M13-R22 - Standard conformance independence.** Conformance to an external standard SHALL NOT automatically establish HDIP conformance, semantic correctness, Product status, trust or assurance.

**HDIP-CLA-M13-R23 - Policy-authority boundary.** HDIP-BND-05 SHALL preserve policy/legal/control ownership independently of applicability resolution, compilation and enforcement performed by HDIP.

**HDIP-CLA-M13-R24 - Judgement preservation.** Legal, policy, risk, waiver or exception determinations requiring accountable judgement SHALL NOT be represented as machine-proven merely because supporting rules/metadata exist.

**HDIP-CLA-M13-R25 - Identity-authority separation.** HDIP-BND-06 SHALL preserve identity, authority, ownership and entitlement as distinct concepts.

**HDIP-CLA-M13-R26 - Authentication/authorization separation.** Successful authentication SHALL NOT by itself establish authorization, entitlement or permitted purpose.

**HDIP-CLA-M13-R27 - No entitlement transitivity.** Entitlement valid in one upstream/downstream context SHALL NOT automatically be inherited across another Product, Port, purpose or consequence boundary.

**HDIP-CLA-M13-R28 - Source-authority preservation.** HDIP-BND-07 SHALL preserve producer/source identity, scope, version/currentness and provenance when data/information/intelligence enters HDIP.

**HDIP-CLA-M13-R29 - Copy non-authority.** Local ingestion, persistence, caching or projection SHALL NOT silently transfer source authority to HDIP.

**HDIP-CLA-M13-R30 - Stale-state honesty.** If source/provider currentness cannot be established, HDIP SHALL expose an explicit stale/unknown/indeterminate condition rather than assume currentness.

**HDIP-CLA-M13-R31 - Runtime non-authority.** HDIP-BND-08 runtimes/infrastructure SHALL NOT acquire semantic, Product, policy or Decision authority merely by executing or hosting HDIP workloads.

**HDIP-CLA-M13-R32 - Runtime binding evidence.** Material P2/P3 binding to an external runtime/environment SHALL retain version, eligibility, configuration and evidence sufficient for reconstruction.

**HDIP-CLA-M13-R33 - Runtime success non-qualification.** Successful execution/deployment SHALL NOT prove Product qualification, correctness, fitness or assurance.

**HDIP-CLA-M13-R34 - Provider identity preservation.** HDIP-BND-09 SHALL preserve provider, Product/capability, Port/interface and contract identity where an external or internal provider is consumed.

**HDIP-CLA-M13-R35 - Discovery non-trust.** Discovery/ranking/availability of a provider SHALL NOT by itself prove entitlement, trust, fitness or assurance.

**HDIP-CLA-M13-R36 - Consumer-context preservation.** HDIP-BND-10 SHALL preserve consumer identity, purpose, access/contract context and Product/Port identity where applicable.

**HDIP-CLA-M13-R37 - Downstream-purpose restraint.** Consumer access SHALL NOT be interpreted as unrestricted downstream reuse beyond applicable purpose, contract, policy or legal constraints.

**HDIP-CLA-M13-R38 - Decision/action boundary.** HDIP-BND-11 SHALL preserve Recommendation, Decision, Authorization and Action as distinct responsibilities where consequential effects arise.

**HDIP-CLA-M13-R39 - Product-access/action-authority separation.** An SSCF/Product access decision SHALL NOT by itself authorize downstream consequential Decision, Tool use, Digital Action or Physical Action.

**HDIP-CLA-M13-R40 - External-provider explicitness.** HDIP-BND-12 material providers SHALL expose sufficient provider/version/currentness/contract/evidence context to support governed use and reconstruction.

**HDIP-CLA-M13-R41 - Provider certification non-assurance.** Provider certification, SLA, benchmark or self-attestation MAY contribute evidence but SHALL NOT automatically establish use-case or HDIP assurance.

**HDIP-CLA-M13-R42 - Economic-context preservation.** Provider licensing, quotas, metering and cost attribution SHALL remain explicit where they materially constrain use or evolution.

**HDIP-CLA-M13-R43 - External failure model.** Material external dependencies SHALL define degraded, failure, indeterminate, recovery and reconciliation semantics where applicable.

**HDIP-CLA-M13-R44 - No exactly-once assumption.** External Boundary Contracts SHALL NOT assume exactly-once processing or side-effect certainty unless the concrete contract demonstrably provides it.

**HDIP-CLA-M13-R45 - Retry safety explicitness.** Retry/idempotency/side-effect semantics SHALL be explicit where replay can create material duplicate or consequential effects.

**HDIP-CLA-M13-R46 - Provider-substitution discipline.** Provider substitution SHALL require applicable semantic/capability/effect/policy/contract compatibility evidence rather than API similarity alone.

**HDIP-CLA-M13-R47 - Provider withdrawal handling.** Material provider/source withdrawal or end-of-life SHALL trigger applicable X7 lifecycle and P2 impact/rebinding responsibilities.

**HDIP-CLA-M13-R48 - Cached-authority reference.** A permitted local cache/projection SHOULD retain authoritative-source identity, source version/currentness, retrieval/effective time and invalidation/expiry semantics.

**HDIP-CLA-M13-R49 - Evidence provenance across boundary.** Material external evidence SHALL retain provider/source identity and occurrence/version context sufficient to assess its meaning and limitations.

**HDIP-CLA-M13-R50 - Evidence non-truth.** Externally supplied evidence, logs, certificates or claims SHALL NOT be treated as self-validating proof of correctness, trust or assurance.

**HDIP-CLA-M13-R51 - Boundary security applicability.** X2 security/privacy/identity/entitlement obligations SHALL apply to external crossings according to context and SHALL NOT be reduced to network encryption alone.

**HDIP-CLA-M13-R52 - Boundary governance applicability.** X1 governing obligations, exceptions and accountable decisions SHALL remain visible at material external boundaries.

**HDIP-CLA-M13-R53 - Boundary evidence applicability.** X3/X4 evidence and observability obligations SHALL preserve sufficient cross-boundary correlation without requiring one universal identity or evidence store.

**HDIP-CLA-M13-R54 - Boundary quality/assurance applicability.** X5/X6 quality/fitness/trust/assurance obligations SHALL remain contextual and SHALL NOT collapse into provider reputation or one score.

**HDIP-CLA-M13-R55 - Boundary lifecycle applicability.** X7 currentness/version/change obligations SHALL apply to material external specifications, providers, sources, runtimes and consumer contracts.

**HDIP-CLA-M13-R56 - Boundary resilience applicability.** X8 failure/recovery obligations SHALL cover material external-system/provider dependencies, not only HDIP-FND infrastructure.

**HDIP-CLA-M13-R57 - Boundary economic applicability.** X9 SHALL preserve cost/licensing/economic accountability independently of Product value or usage volume.

**HDIP-CLA-M13-R58 - No boundary-to-ABB reflex.** A canonical Boundary Family SHALL NOT imply a dedicated gateway, adapter, proxy, Registry, service or ABB with the same name.

**HDIP-CLA-M13-R59 - No vendor naming.** Provider/vendor products SHALL NOT become canonical HDIP Boundary Family or ABB names merely because they are current implementations.

**HDIP-CLA-M13-R60 - Profile specialization.** Data-, Information-, Intelligence-, Product-family-, jurisdiction- and industry-specific boundary obligations MAY specialize M13 but SHALL NOT weaken applicable core authority/currentness/evidence rules.

**HDIP-CLA-M13-R61 - Boundary traceability.** Material M13 boundary mappings SHOULD trace to relevant M01-M12 responsibilities, external authority/specification, contracts and evidence.

**HDIP-CLA-M13-R62 - No new internal topology.** M13 SHALL NOT introduce a sixth Plane, a tenth Overlay, a new internal ABB catalogue or a mandatory external gateway topology.

**HDIP-CLA-M13-R63 - No boundary bus.** M13 Boundary Families SHALL NOT be interpreted as requiring one enterprise integration bus, API gateway, mesh or broker through which all external crossings pass.

**HDIP-CLA-M13-R64 - M14 handoff.** M14 realization/profile patterns SHALL preserve the M13 boundary identities and rules while demonstrating multiple valid centralized, federated, distributed, embedded and provider-based realizations.

---

# 31. What M13 deliberately does not decide

M13 does not freeze:

- concrete API/protocol/message/event schemas;
- network/security-zone topology;
- enterprise identity or policy product selection;
- vendor/cloud/provider choice;
- physical gateway/proxy/broker deployment;
- legal/commercial contract wording;
- final enterprise Product-family specification catalogue;
- source-system inventory;
- provider allowlist;
- physical observability/evidence-store topology;
- exact realization/profile patterns (M14);
- canonical stakeholder/reference views (M15);
- final conformance assessment modes/evidence sufficiency rules (M16).

---

# 32. M13 completion state

**HDIP-CLA M13 - COMPLETE.**

M13 establishes:

- **6 canonical Boundary Classes**;
- **12 canonical Boundary Families (`HDIP-BND-01` through `HDIP-BND-12`)**;
- a canonical **External Boundary Contract (EBC)** model reusing M12 Interaction Contract discipline;
- explicit authority boundaries for semantics, Product qualification, peer architectures, standards, policy/control, identity/security, source systems, runtimes/providers, consumers and downstream consequence environments;
- explicit currentness/version, caching, conformance, trust-zone, failure, withdrawal and provider-substitution rules;
- a Plane-to-boundary applicability matrix;
- **7 representative cross-boundary scenarios**;
- **24 boundary anti-patterns**;
- **64 normative M13 rules**;
- **0 new canonical Planes**;
- **0 new canonical Overlays**;
- **0 new canonical ABBs**.

### Next stage

> **M14 - HDIP Realization / Profile Patterns**

M14 will demonstrate how the same frozen HDIP Plane, Overlay, ABB, Interaction and Boundary architecture can be realized through different enterprise patterns without making any one deployment topology canonical.
