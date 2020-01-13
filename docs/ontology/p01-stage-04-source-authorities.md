---
title: P01 Stage 4 - Source Authority and Adoption Readiness
sidebar_label: P01-S04 - Source Authorities
---

# G03 upstream source authority and conditional adoption

> **G03-D10 owner-reviewed research baseline - NOT a normative source adoption.** The candidate sources and jurisdictions below may be used for controlled INFOPS research. A candidate document path, version label, machine-run result or release manifest is not an authorized cross-specification adoption record.

## Consolidated authority register

| Source ID | Candidate reference | Authority | Current limitation |
| --- | --- | --- | --- |
| S01 | BPS Product Ontology and PIN - BPS/PIN conceptual draft | Generic Productness, Product Promise, identity, PIN, Product Family and Kind | CANONICAL NORMATIVE PIN UNRESOLVED |
| S02 | GEARM - 0.1 / GEARM-0.1-RC1 | Information and analytical semantics | EXECUTABLE RC1 CLOSED NOT ADOPTED |
| S03 | GEARA - 0.1 / GEARA-0.1-RC1 | Generic enterprise Analytics architecture | EXECUTABLE RC1 CLOSED NOT ADOPTED |
| S04 | GEDRM - 0.1 Normative Draft Baseline | Generic enterprise Data semantics | DRAFT UNPINNED |
| S05 | GEDRA - 0.1 release candidate | Generic enterprise Data architecture | A14 BLOCKED IN AVAILABLE REPORT |
| S06 | OMG DPROD - 1.0 beta 2 candidate | External Data Product ontology and competing-family reference | NORMATIVE SCOPE UNPINNED |
| S07 | Open Data Mesh DPDS - 1.0.0 candidate | External Data Product Descriptor Specification (NOT INFOPDS or deployment DPDS) | ADOPTION SCOPE UNPINNED |
| S08 | AIPS - 0.1 Stage 14 | AI Product qualification and AI-specific semantics | REPOSITORY CONFORMANT RC READY PUBLISH CHECKS OPEN |
| S09 | GEAIRM - 0.1 A15 | Generic enterprise AI semantics | WORKING DRAFT EXECUTABLE RC CLOSED |
| S10 | GEAIRA - 0.1 M17 | Generic enterprise AI architecture | WORKING DRAFT M17 HUMAN BASELINE FROZEN |
| S11 | UPOS - Conceptual; version unverified | Product-kind agnostic Productization meta-architecture | NORMATIVE VERSION UNVERIFIED |
| S12 | HDIP-CLA - 0.1 M17 / A15 | Holistic Data, Information and Intelligence platform logical architecture | M17 FROZEN A15 BOUNDED NOT CONFORMANCE |
| S13 | INFOPCH / PMDD - Future | Characteristics, maturity and operational assessment separate from Family | NOT SPECIFIED |
| S14 | INFOPROD - Proposed Information Product semantic descriptor | Versioned Information-specific Product semantic commitments | NOT NORMATIVELY SPECIFIED |
| S15 | INFOPDS - Proposed Information Product deployment specification | Applicable Product realization and deployment contract | NOT NORMATIVELY SPECIFIED |
| S16 | BPS DPP Core - candidate 0.1 | Generic cross-family Product Digital Product Passport | CORE RELEASE URI HASH UNVERIFIED |
| S17 | Information Product DPP Profile - Proposed | Information-specific BPS DPP trust/evidence specialization | NOT NORMATIVELY SPECIFIED |

## Foundational versus adjacent binding

1. **Foundational sources:** BPS/PIN owns generic Productness and the PIN boundary; GEARM owns Information and Information Proposition semantics. Normative INFOPS qualification requires authoritative versions and compatibility mappings.
2. **Competing-family authorities:** Applicable Data Product family and AIPS AI Product specifications govern their own qualifications. An INFOPS research finding may note a plausible competing family, but cannot certify a Product under an independently governed family without that authority's evidence.
3. **Supporting architectures:** GEARA, GEDRA, GEAIRA, HDIP-CLA and relevant UPOS concepts are adopted only for an applicable architecture/Profile subject. Intrinsic Product Family is not conditioned on one implementation platform.
4. **BPS DPP:** Cross-family Product trust authority is distinct from intrinsic qualification; its adopted Core version will bind future DPP compliance claims, not automatically every Information Product existence predicate.
5. **INFOPROD/INFOPDS/Information DPP Profile:** Owner approval establishes architectural direction only. These are **not yet** adopted semantic contracts, deployment schemas or trust conformance specifications.

## Reconciliation and exact-version requirements

For every binding normative dependency the future record should identify: governing authority; canonical source URI and artifact path; semantic/architecture version; immutable revision or verifiable digest; governed release status; applicable jurisdiction and scope; cross-specification version pairings; source precedence; adoption authority/decision; and change/supersession policy.

### Selected source evidence and status caveats

- **BPS/PIN:** The accessible `bps-product-ontology-pin.md` is a conceptual BPS document. Its governing immutable normative release is not pinned by this review.
- **GEARM:** `GEARM-0.1-RC1`, closed at A15, with human-readable source under `docs/tools/gearm/0.1/gearm-0.1-specification.md`. Release-candidate closure is not the same as final publication.
- **GEARA:** `GEARA-0.1-RC1`, closed at A15, with companion human-readable architectural authority. Its architecture validation does not substitute for accountable contextual assessment.
- **GEDRM:** 0.1 Normative Draft Baseline; R4 records no material semantic conflict with GEDRA but retains a Source of Authority formal-kind issue for future normalization.
- **GEDRA:** 0.1 Release Candidate; retrieved A14 closure reports the complete SHACL/Profile regression **blocked because `pyshacl` was not available**. Do not assert that a later successful gate was independently verified.
- **AIPS:** 0.1 Stage 14 repository-conformant/release-candidate ready; full connected Docusaurus build and executable SHACL checks were not completed in retrieved evidence.
- **GEAIRM:** 0.1 Working Draft, A15 executable release candidate closed; governed publication pending.
- **GEAIRA:** 0.1 Working Draft, M17 human-readable architecture baseline frozen; separate executable closure not established.
- **HDIP-CLA:** 0.1 M17 frozen; A15 closes a **bounded executable formalization package**, NOT implementation conformance, external endorsement or publication authorization.
- **UPOS:** Product-kind-agnostic conceptual reference; binding Version and immutable reference not established.
- **BPS DPP Core:** A candidate v0.1 namespace is visible in an older GRNPS BPS-oriented reference and a different shared-DPP URI is visible in GRNPS-native material. **No authoritative alias, migration, supersession or single Core release has been verified.**

## Compatibility must not be inferred by name matching

- BPS/PIN / GEARM: Productness remains independent of Information semantics.
- GEARM / GEARA: meaning remains distinct from Analytics architectural responsibility.
- GEDRM / GEDRA: separate Data semantic and architectural authorities, known formalization/release limitations retained.
- AIPS / GEAIRM / GEAIRA: AI Product qualification, AI semantics and AI architecture remain distinct.
- GEDRA / GEARA / GEAIRA / HDIP-CLA: HDIP can co-realize responsibilities without absorbing their jurisdiction or treating like-named Planes as equivalent.
- BPS DPP / family Profiles: Core authority is not replaced by the specialized Product evidence Profile.
- INFOPROD / INFOPDS / DPP / HPD: different semantic, realization, trust and operational projection responsibilities, with independently versioned subjects.

**No material incompatibility has been established that prevents conditional G04 research; this does NOT prove complete normative version-level interoperability.** Material new source evidence may reopen the affected G03 findings before adoption.

The machine-readable research index is stored at `research/p01-s04/source-authority-register.json` (not an INFOPS normative schema).
