---
title: IPCH01 Experimental Guidance — Evidence and Status
---

# IPCH01 — Supporting research and assessment boundaries

> **Research-only overlay.** This document reports the conversation-level owner decisions D01–D10. It is not an institutional adoption, executed conformance assessment, or final characteristic approval.

## References

- [IPCH catalogue](./overview.md): sixteen experimental characteristics.
- [IPCH01 — Domain-Owned](./IPCH01.md): sixteen-section `IPCH01-PMDD-GUIDE-01 / DRAFT-02` guide.
- `DPCH01` and `AIPCH01` canonical source guidance: cited in the IPCH01 guide; not imported or amended by this overlay.

## Assessment decision and enterprise choice

The guide specifies **five mandatory core positive ownership claims (OWN-M01–M05)**, **seven failure conditions (OWN-N01–N07)** and **seven evidence rules (ES-D01–D07)**. All five applicable core ownership claims must be adequately demonstrated for MET. A demonstrated foundational absence can support NOT_MET; evidenced but non-foundational incompleteness can support PARTIAL. Material uncertainty must not be disguised as a zero or a fifth maturity state.

Enterprises choose implementation mechanisms and proportionate evidence/assurance stringency, **not silent removal or redefinition of mandatory claims**. Manual, deterministic and agent-assisted assessments follow the same characteristic meaning. The guide does not prescribe platforms, APIs, evidence file formats or automation architecture.

## Review status

| Gate or evidence | Status |
| --- | --- |
| G1 | `BOUNDED_INTAKE_ACCEPTED` (D06) |
| DRAFT-01 | Preserved; D08 G2 `PASS_WITH_QUALIFICATIONS`, G3 `REVIEWED_REMEDIATION_REQUIRED` |
| DRAFT-02 | `EXPERIMENTAL_DRAFT_PREPARED` (D09) |
| G2 / DRAFT-02 | `PASS` (D10) |
| G3 / DRAFT-02 | `PASS_WITH_QUALIFICATIONS` (D10) |
| DR-01–DR-08 | `DOCUMENTARY_REMEDIATION_VERIFIED` only (D10) |
| G4 | `NOT_EXECUTED`; G4-C01/C02 proposed, unexecuted |
| DO-01–DO-15 | Unexecuted research cases |
| G5 / final guide | `NOT_EXECUTED` / `NOT_APPROVED` |
| G6 | `NOT_EXECUTED` |
| R01–R04 | `OPEN` |
| Upstream BPS/PIN, GEARA/GEARM independent audit | `NOT_ESTABLISHED` |
| IPCH L0/L1/L2 bands | `NOT_ADOPTED` |
| Empirical Product assessments | Zero |

## Provenance and change control

- `INFOPS-0.1-IPCH-P01-D01-F01` through `D10-F01`: conversation-level owner approval only; G4 not initiated.
- Original `DRAFT-01`, D08 findings and source qualification tension remain historical research evidence; this overlay does not replace them or reclassify parent decisions.
- `sidebars.js` in this overlay is drawn from the supplied MVP-P01 D08 overlay, with the single `infopch/IPCH01` entry added. Merge against the live branch if that file has diverged.
- This package does not add normative schemas, implementation code, automated evaluation runs, policy controls or release credentials.
