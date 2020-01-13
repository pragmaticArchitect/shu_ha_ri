---
id: hdip-cla-0.1-a2-canonical-relationship-traceability-registry
title: HDIP-CLA 0.1 A2 - Canonical Relationship & Traceability Registry
sidebar_label: A2 - Relationship & Traceability Registry
---

# HDIP-CLA 0.1 A2 — Canonical Relationship & Traceability Registry

**Status:** COMPLETE  
**Programme:** HDIP-CLA 0.1 machine-readable / executable formalization  
**Human-readable authority:** M01-M17 frozen baseline  
**Identity baseline:** A1 Canonical Architecture Element Registry  
**Primary machine artifact:** `/specs/hdip-cla/0.1/a2/relationship-traceability-registry.json`

## 1. Purpose

A2 establishes the canonical machine-readable **relationship and traceability layer** over the 209 stable identities registered by A1.

A2 answers:

> **How are frozen HDIP-CLA architecture identities connected, projected, hosted, classified, specialized, traversed and traced without turning mapping into equivalence or reference into authority transfer?**

The governing distinction is:

```text
relationship
   != equivalence
   != ownership
   != authority transfer
   != automatic transitivity
   != runtime call
```

A2 therefore defines typed edges and provenance. It does **not** create new Planes, Overlays, ABBs, Registries, lifecycle stages, interactions, Boundary Families, Patterns, Views, Flows or Invariants.

---

# 2. Source authority and A1 dependency

A2 is downstream from the frozen M17 human-readable baseline and from A1 machine identity registration.

A2 MUST use A1 identifiers as endpoints wherever a frozen HDIP element already has an A1 identity. External authorities and derivation identifiers are kept in separate reference scopes so they do not silently become HDIP architecture elements.

If an A2 edge conflicts with the frozen human-readable source, the human-readable source governs and the A2 edge must be corrected.

---

# 3. A2 relationship metamodel

Each canonical relationship record contains:

| Field | Meaning |
|---|---|
| `id` | Stable A2 relationship-record identifier. |
| `type` | Typed relationship from the A2 relationship-type catalogue. |
| `source` | A1 element ID or explicitly marked historical compatibility term. |
| `target` | A1 element ID, external reference or derivation identifier. |
| `targetScope` | `A1_ELEMENT`, `EXTERNAL_REFERENCE`, or `DERIVATION_REFERENCE`. |
| `assertionClass` | Why the edge exists: structure, projection, flow, profile, authority, traceability, compatibility, etc. |
| `modality` | Canonical/required, principal, representative, conditional or historical character of the assertion. |
| `sourceDocument` | Human-readable document supporting the edge. |
| `note` | Optional clarification where the relation is intentionally scoped. |

Relationship records are **assertions**, not implementation messages.

---

# 4. Endpoint scopes

A2 uses three endpoint scopes.

```text
A1_ELEMENT
  frozen machine identity from A1

EXTERNAL_REFERENCE
  external semantic/Product/architecture/policy/source/provider authority
  retained outside the A1 element inventory

DERIVATION_REFERENCE
  upstream derivation identifiers such as M04-Ixx or RCF-xx
  used for provenance, not runtime architecture
```

Historical compatibility terms use an explicitly marked `HIST::` source form. They are not added to the A1 canonical element registry.

---

# 5. Relationship-type catalogue

A2 freezes **32 relationship types** across structural, lifecycle, interaction, boundary, profile, view/flow, conformance, authority, traceability and compatibility concerns.

Principal types include:

```text
PRIMARY_HOSTED_BY
PARTICIPATES_IN
CONTAINS_STAGE
PROJECTS_LIFECYCLE
PRODUCES_ARTIFACT / CONSUMES_ARTIFACT
CONTAINS_INTERACTION
HAS_SOURCE_PLANE / HAS_TARGET_PLANE
CLASSIFIED_BY_BOUNDARY_CLASS
SPECIALIZES_ELEMENT / STRENGTHENS_ELEMENT
PROJECTS_ELEMENT
FLOW_USES_INTERACTION
FLOW_CROSSES_BOUNDARY
FLOW_USES_PROFILE_PATTERN
FLOW_USES_REALIZATION_PATTERN
GOVERNS_ELEMENT
REFERENCES_EXTERNAL_AUTHORITY
PRESERVES_SOURCE_INVARIANT
DERIVED_FROM_RCF
```

A2 also preserves the nine **typed** M17 compatibility mappings. Multi-target mappings are serialized as 13 edge records. `HISTORICAL_ALIAS_OF`, `DECOMPOSED_TO`, `SPECIALIZED_VIEW_OF` and `RESPONSIBILITIES_MAP_TO` remain different meanings.

No A2 relationship type implies semantic equivalence or authority transfer.

---

# 6. Canonical structural relationships

## 6.1 ABB primary hosting

All 22 canonical ABBs receive one `PRIMARY_HOSTED_BY` relation to their frozen Plane or Overlay host.

Examples:

```text
HDIP-P2-ABB-03  PRIMARY_HOSTED_BY  HDIP-P2
HDIP-P3-ABB-02  PRIMARY_HOSTED_BY  HDIP-P3
HDIP-X6-ABB-01  PRIMARY_HOSTED_BY  HDIP-X6
```

Primary hosting is logical. It does not require a separate deployment unit for each ABB.

## 6.2 Registry participation

M09 Registry participation is represented with `PARTICIPATES_IN`, preserving multi-Plane/Overlay participation.

For example:

```text
HDIP-REG-01 Product Registry
  -> P1 / P2 / P4 / X7

HDIP-REG-05 Blueprint Registry
  -> P2 / X7 / HDIP-FND
```

Participation does not make a Registry authoritative for the semantics it references.

## 6.3 Boundary classification

Each Boundary Family is related to its M13 Boundary Class using `CLASSIFIED_BY_BOUNDARY_CLASS`. Multi-class boundaries remain multi-class rather than being forced into a single parent.

---

# 7. Lifecycle and projection relationships

A2 encodes lifecycle membership without turning lifecycle into topology.

```text
PDEP  CONTAINS_STAGE  Stage 0 .. Stage 10
SSCF  CONTAINS_STAGE  Stage 1 .. Stage 8

PDEP G0 / Spec A / Spec C  PROJECTS_LIFECYCLE  PDEP
CEP                         PROJECTS_LIFECYCLE  SSCF
```

PDEP Stage 8 is related to the canonical compilation artifacts it produces; Stage 9 is related to the canonical realization artifacts it consumes. SYNCTX remains conditional where applicable.

This does not imply that all lifecycle stages are mandatory synchronous runtime hops.

---

# 8. M12 interaction relationships

Every canonical M12 interaction is related to:

1. exactly one interaction family;
2. exactly one source Plane;
3. one or more target/affected Planes.

Fan-out interactions remain explicit:

```text
INT-08  P1 -> affected P2 / P3 / P4 / P5
INT-16  P2 -> affected P3 / P4 / P5
```

A2 does not infer missing direct interactions merely because two Planes can communicate in an implementation.

---

# 9. Profile and realization traceability

A2 records only profile relations explicitly supported by M14.

Examples:

```text
PP-01 Data / Data Product Profile
  SPECIALIZES_ELEMENT ADS Registry
  SPECIALIZES_ELEMENT P3-ABB-01
  SPECIALIZES_ELEMENT PDEP
  SPECIALIZES_ELEMENT SYNCTX where applicable

PP-05 Regulated / High-Assurance Profile
  STRENGTHENS_ELEMENT X1 / X2 / X3 / X5 / X6 / X7 / X8
```

A Profile relation does not weaken baseline obligations or transfer external authority.

Realization Patterns remain topology choices. A2 does not assign every ABB to a Pattern because M14 intentionally makes realization mapping contextual and many-to-many.

---

# 10. Reference View relationships

M15 view coverage is formalized through `PROJECTS_ELEMENT`.

This is projection metadata only:

```text
View projects element
   != view owns element
   != element is unique to view
   != omission from another view means non-applicable
```

The same A1 identity is reused across all ten views.

---

# 11. Representative flow relationships

M15 flow coverage is formalized using:

```text
FLOW_USES_INTERACTION
FLOW_CROSSES_BOUNDARY
FLOW_USES_PROFILE_PATTERN
FLOW_USES_REALIZATION_PATTERN
```

These relations preserve the exact M12/M13/M14 identities used by a scenario. They do not turn a representative flow into a new lifecycle or universal runtime pipeline.

---

# 12. Invariant coverage relationships

A2 records selected explicit invariant-to-element coverage required for later A3/A6/A12 formalization.

Examples:

```text
M16-I41 -> P1-P5 / FND / X1-X9 / all 22 ABBs
M16-I42 -> INT-01..21
M16-I43 -> BND-01..12
M16-I45 -> PDEP / SSCF / CEP
M16-I48 -> PP-01..06
```

This is **scope traceability**, not proof that an invariant is satisfied.

M16-I01..I40 additionally retain explicit ancestry to M04-I01..I40.

---

# 13. External-authority references

A2 defines **18 external reference identities** for traceability only. They are not A1 architecture elements.

This keeps relations such as the following explicit:

```text
Product Lens  REFERENCES_EXTERNAL_AUTHORITY  BPS/PIN
P3-ABB-01     REFERENCES_EXTERNAL_AUTHORITY  GEDRA / GEDRM
P3-ABB-02     REFERENCES_EXTERNAL_AUTHORITY  GEARA / GEARM
P3-ABB-03     REFERENCES_EXTERNAL_AUTHORITY  GEAIRA / GEAIRM
BND-01        REFERENCES_EXTERNAL_AUTHORITY  GEDRM / GEARM / GEAIRM
```

A reference edge does not import the external authority into HDIP ownership.

---

# 14. Derivation traceability

A2 retains two explicit derivation lineages required by the frozen baseline:

- the 22 ABBs to their M05 RCF ancestry;
- M16-I01..I40 to M04-I01..I40.

A2 also serializes A1 `sourceDocuments` as separate traceability records for every registered element.

Derivation references remain provenance. They do not become additional runtime Planes, ABBs or services.

---

# 15. Closed-world and inference restraint

A2 is **not a closed-world ontology**.

Absence of an edge means:

> A2 does not assert that canonical relationship.

It does **not** mean:

> the relationship is impossible in every conformant implementation.

Similarly, A2 does not infer:

```text
A -> B and B -> C
therefore A -> C
```

unless a later formalization explicitly establishes a safe transitive rule. None of the A2 relationship types is marked as authority-transferring or equivalence-producing.

---

# 16. A2 machine artifacts

Canonical JSON:

```text
/specs/hdip-cla/0.1/a2/relationship-traceability-registry.json
```

CSV projections:

```text
/specs/hdip-cla/0.1/a2/relationship-registry.csv
/specs/hdip-cla/0.1/a2/traceability-registry.csv
```

The CSV files are convenience projections. The JSON document is the canonical A2 machine artifact.

---

# 17. A2 anti-patterns

A2 rejects the following formalization anti-patterns:

1. **Generic-edge collapse** — replacing typed relations with a universal `relatedTo` edge.
2. **Mapping-equals-equivalence** — treating `mapsTo`, projection or specialization as identity equivalence.
3. **Reference-equals-ownership** — importing external authority because HDIP references it.
4. **Host-equals-deployment** — treating ABB primary hosting as one service/container per ABB.
5. **Participation-equals-authority** — assuming Registry participation in a Plane grants Plane/domain authority.
6. **Lifecycle-edge pipeline** — treating stage containment as a mandatory synchronous runtime sequence.
7. **Projection-equals-copy** — minting duplicate canonical identities inside a view or lifecycle projection.
8. **Flow-equals-lifecycle** — turning an M15 flow into a second lifecycle definition.
9. **Fan-out erasure** — forcing INT-08 or INT-16 to a single target.
10. **Boundary-single-parent reflex** — erasing legitimate multi-class Boundary Families.
11. **Profile-as-fork** — using specialization edges to redefine parent semantics.
12. **Pattern-assignment absolutism** — binding canonical ABBs permanently to one M14 topology.
13. **Invariant-edge proof** — treating `GOVERNS_ELEMENT` as proof of invariant satisfaction.
14. **Source-lineage runtime promotion** — turning RCF or M04 ancestry into runtime components.
15. **External-ref annexation** — registering GEDRM/GEARM/GEAIRM/BPS/etc. as HDIP-owned A1 elements.
16. **Alias-resurrection** — turning historical compatibility terms into active canonical identities.
17. **Unsafe transitive inference** — deriving new authority/ownership/compatibility edges from edge chains.
18. **Schema-shape equivalence** — inferring semantic equivalence from matching relationship endpoint kinds.
19. **View omission as N/A** — treating absence from a view as conformance non-applicability.
20. **Traceability without provenance** — emitting an edge without identifying the human-readable source that supports it.

---

# 18. Canonical A2 normative rules

**HDIP-CLA-A2-R01 — Human-readable precedence.** A2 SHALL remain downstream from the frozen M17 human-readable baseline; conflicting machine relationships SHALL be corrected rather than redefining the baseline.

**HDIP-CLA-A2-R02 — A1 identity reuse.** A2 SHALL use A1 canonical IDs for HDIP endpoints whenever the endpoint is already registered by A1.

**HDIP-CLA-A2-R03 — No new architecture identity.** A2 relationship records SHALL NOT create new canonical Planes, Overlays, ABBs, Registries, lifecycle identities, interactions, Boundary Families, Patterns, Views, Flows or Invariants.

**HDIP-CLA-A2-R04 — Typed-edge requirement.** Every A2 relationship SHALL carry an explicit relationship type; a generic untyped related-to edge SHALL NOT substitute for a canonical type.

**HDIP-CLA-A2-R05 — Relationship non-equivalence.** No A2 relationship SHALL imply identity or semantic equivalence unless a future governed formalization explicitly defines such semantics; A2 defines none.

**HDIP-CLA-A2-R06 — No authority transfer.** No A2 relationship SHALL transfer semantic, Product, policy, Data/source, Decision or architecture authority merely by reference, hosting, mapping, composition or projection.

**HDIP-CLA-A2-R07 — Endpoint scope.** Every relationship target SHALL declare A1_ELEMENT, EXTERNAL_REFERENCE or DERIVATION_REFERENCE scope.

**HDIP-CLA-A2-R08 — External-reference non-element.** External authorities SHALL remain in the A2 external-reference registry and SHALL NOT become A1 elements merely for graph convenience.

**HDIP-CLA-A2-R09 — Derivation-reference non-runtime.** RCF and M04 ancestry identifiers SHALL remain derivation references and SHALL NOT become runtime architecture elements.

**HDIP-CLA-A2-R10 — Closed-world restraint.** Absence of an A2 edge SHALL mean no canonical A2 assertion, not proof that an implementation relation is impossible.

**HDIP-CLA-A2-R11 — Transitivity restraint.** A2 SHALL NOT infer transitive relationships unless the relationship type explicitly permits it; A2 0.1 defines no authority-bearing transitive inference.

**HDIP-CLA-A2-R12 — Deterministic relationship IDs.** Relationship record IDs SHALL be assigned deterministically from a stable ordering so regression tooling can detect drift.

**HDIP-CLA-A2-R13 — Source provenance.** Every canonical A2 relationship SHALL identify at least one human-readable source document.

**HDIP-CLA-A2-R14 — ABB hosting.** Each of the twenty-two canonical ABBs SHALL have exactly one PRIMARY_HOSTED_BY edge to its M08 Plane or Overlay host.

**HDIP-CLA-A2-R15 — Host non-topology.** PRIMARY_HOSTED_BY SHALL describe logical responsibility placement and SHALL NOT prescribe a deployment unit, service, process, team or network tier.

**HDIP-CLA-A2-R16 — Registry participation.** M09 Registry participation SHALL be represented as potentially multi-Plane/Overlay/Foundation rather than forced into exclusive hosting.

**HDIP-CLA-A2-R17 — Registry non-authority.** Registry participation relationships SHALL NOT establish semantic/Product/policy authority.

**HDIP-CLA-A2-R18 — ADS profile scope.** HDIP-REG-D01 SHALL retain explicit association with the Data/Data Product Profile and SHALL NOT be generalized to Information or Intelligence.

**HDIP-CLA-A2-R19 — Lifecycle membership.** PDEP and SSCF SHALL contain exactly their frozen registered stages: PDEP Stage 0 plus Stages 1-10, and SSCF Stages 1-8.

**HDIP-CLA-A2-R20 — Projection preservation.** PDEP G0, Spec A and Spec C SHALL project PDEP rather than form competing lifecycle identities.

**HDIP-CLA-A2-R21 — CEP projection.** CEP SHALL remain a Consumer Experience Projection over SSCF responsibilities and SHALL NOT become a Plane.

**HDIP-CLA-A2-R22 — Lifecycle non-runtime.** Lifecycle containment/projection edges SHALL NOT imply mandatory synchronous runtime sequencing.

**HDIP-CLA-A2-R23 — Compilation artifact output.** A2 SHALL preserve the M10 Stage-8 relationship to RRG, HPD, conditional SYNCTX, RGB, Realization Plan, Blueprint Binding and Compilation Record.

**HDIP-CLA-A2-R24 — Realization artifact input.** A2 SHALL preserve the Stage-9 use of applicable realization/compilation artifacts without making successful deployment proof of Productness or assurance.

**HDIP-CLA-A2-R25 — Interaction family membership.** Every HDIP-M12-INT-01..21 SHALL belong to exactly one frozen M12 interaction family.

**HDIP-CLA-A2-R26 — Interaction source.** Every canonical interaction SHALL have exactly one HAS_SOURCE_PLANE edge.

**HDIP-CLA-A2-R27 — Interaction target.** Every canonical interaction SHALL have at least one HAS_TARGET_PLANE edge; fan-out interactions MAY have several.

**HDIP-CLA-A2-R28 — Fan-out preservation.** INT-08 and INT-16 target multiplicity SHALL be preserved and SHALL NOT be flattened to one target for schema convenience.

**HDIP-CLA-A2-R29 — Interaction non-API.** Interaction direction relationships SHALL NOT imply a specific API, queue, broker, topic, synchronous call or protocol.

**HDIP-CLA-A2-R30 — Boundary classification.** Every M13 Boundary Family SHALL retain its canonical Boundary Class classification, including legitimate multi-class membership.

**HDIP-CLA-A2-R31 — Boundary non-gateway.** Boundary classification SHALL NOT imply one physical gateway, perimeter or integration component per Boundary Family/Class.

**HDIP-CLA-A2-R32 — Profile specialization.** Profile relationships SHALL preserve monotonic specialization and SHALL NOT redefine parent architecture meaning.

**HDIP-CLA-A2-R33 — High-assurance strengthening.** PP-05 strengthening edges SHALL express possible tightened obligations rather than mandatory centralized approval components.

**HDIP-CLA-A2-R34 — Realization mapping contextuality.** A2 SHALL NOT assign every canonical responsibility permanently to an M14 Realization Pattern; concrete Realization Mapping remains subject-specific.

**HDIP-CLA-A2-R35 — View projection identity.** M15 views SHALL project existing A1 identities rather than create view-specific clones.

**HDIP-CLA-A2-R36 — View omission non-waiver.** Absence of an element from a particular view SHALL NOT imply non-applicability or waiver.

**HDIP-CLA-A2-R37 — Flow interaction reuse.** Representative flows SHALL reuse canonical M12 interaction identities and SHALL NOT mint scenario-specific interaction identities.

**HDIP-CLA-A2-R38 — Flow boundary reuse.** Material flow crossings SHALL reuse M13 Boundary Family identities rather than generic provider/integration edges.

**HDIP-CLA-A2-R39 — Flow non-universality.** Flow relationships SHALL remain representative scenario coverage and SHALL NOT create a universal HDIP lifecycle or runtime pipeline.

**HDIP-CLA-A2-R40 — Pattern/profile flow context.** Flow-to-Pattern/Profile relationships SHALL retain illustrative/scoped semantics and SHALL NOT make the selected pattern/profile universally required.

**HDIP-CLA-A2-R41 — Invariant scope non-proof.** GOVERNS_ELEMENT SHALL record invariant scope/coverage only and SHALL NOT assert SATISFIED, CONFORMANT or assurance status.

**HDIP-CLA-A2-R42 — M04 ancestry.** M16-I01..I40 SHALL retain explicit traceability to M04-I01..I40.

**HDIP-CLA-A2-R43 — ABB RCF ancestry.** Canonical ABBs SHALL retain traceability to their M05 RCF responsibility basis as recorded by M08.

**HDIP-CLA-A2-R44 — External authority reference.** Key Product, semantic, peer-architecture and Boundary constructs SHALL preserve explicit references to applicable external authorities.

**HDIP-CLA-A2-R45 — External authority non-annexation.** REFERENCES_EXTERNAL_AUTHORITY SHALL NOT copy or own the target authority semantics inside HDIP.

**HDIP-CLA-A2-R46 — Compatibility typing.** The nine M17 historical terminology mappings SHALL retain their distinct relationship types.

**HDIP-CLA-A2-R47 — Historical source non-element.** Historical terms SHALL remain compatibility sources and SHALL NOT be added to the A1 canonical element set.

**HDIP-CLA-A2-R48 — Alias non-resurrection.** A historical alias or earlier term SHALL NOT regain canonical status because it participates in an A2 relationship.

**HDIP-CLA-A2-R49 — Document traceability.** A2 SHALL serialize A1 source-document provenance for registered elements as traceability records.

**HDIP-CLA-A2-R50 — Traceability separation.** Traceability records SHALL be distinguishable from canonical architecture relationships so provenance does not become architecture topology.

**HDIP-CLA-A2-R51 — CSV non-authority.** A2 CSV outputs SHALL be deterministic convenience projections of the canonical JSON registry and SHALL NOT diverge semantically.

**HDIP-CLA-A2-R52 — A3 handoff.** A3 SHALL use A2 invariant coverage and traceability but SHALL define executable invariant/conformance semantics independently of relationship existence.

**HDIP-CLA-A2-R53 — A4 graph handoff.** A4 RDF/OWL formalization SHALL project A2 typed relationships without introducing stronger equivalence, transitivity or authority semantics.

**HDIP-CLA-A2-R54 — A5 IRI deferral.** A2 record identifiers and external-reference IDs SHALL NOT be treated as final IRIs; canonical namespace/IRI design remains A5 scope.

**HDIP-CLA-A2-R55 — A6/A8 constraint deferral.** A2 SHALL describe relationship meaning but SHALL NOT prematurely convert every relation into SHACL/schema cardinality or runtime validation.

**HDIP-CLA-A2-R56 — A13/A14 reconciliation readiness.** A2 JSON/CSV relationships, traceability records, counts and endpoint references SHALL be deterministic enough for later cross-artifact reconciliation and regression testing.

---

# 19. A2 completion state

**HDIP-CLA A2 — COMPLETE.**

A2 establishes:

- one canonical Relationship & Traceability Registry;
- **32** typed relationship kinds;
- **911** canonical relationship records;
- **332** traceability records;
- **18** external authority/adjacent reference identities;
- complete 22-ABB primary-host mapping;
- M09 logical Registry participation mapping;
- exact PDEP/SSCF stage membership and projection relationships;
- Stage-8/Stage-9 compilation/realization artifact relationships;
- complete M12 interaction-family and source/target Plane mapping;
- complete M13 Boundary Family -> Boundary Class mapping;
- selected explicit M14 Profile specialization/strengthening relationships;
- M15 View and Flow coverage relationships using existing canonical identities;
- selected M16 invariant scope relationships plus M04 invariant ancestry;
- ABB -> M05 RCF derivation traceability;
- explicit external-authority reference edges without authority capture;
- the nine typed M17 compatibility mappings serialized as 13 edge records;
- **20** A2 anti-patterns;
- **56** normative A2 rules.

A2 introduces no new human-readable HDIP architecture semantics. It formalizes relationships and provenance over the A1 identity set.

### Next stage

> **A3 — Invariant & Conformance Catalogue**

A3 will formalize the M16 invariant catalogue, assessment modes, applicability/result semantics, conformance subject/claim/outcome model and evidence-package requirements while preserving the A2 relationship/traceability graph and the M16 boundary between machine-decidable structure and accountable human judgement.
