# INFOPS — Information Product Specification

**Status: INFOPS-P01 STAGE 4 OWNER-REVIEWED CONDITIONAL RESEARCH (NON-NORMATIVE).** This is a new Docusaurus project for developing INFOPS 0.1. It is **not** a published, normative Information Product specification.

## Purpose

INFOPS will define Information Product family qualification consistent with **BPS/PIN**, **GEARM** and **GEARA**, with its own **INFOPCH** characteristics and evidence-based **Product Maturity-Driven Development (PMDD)** guidance for human and AI assessors. It will align with **HDIP/UPOS** without absorbing their distinct architectural responsibilities.

The original P01 Stage 1 baseline and review remain preserved. Stage 2 (`docs/ontology/p01-stage-02-pin-differentiation-falsification.md`) contains 36 conditional case dispositions, ten PFI thought experiments and 16 falsification tests. Stage 3 adds `docs/ontology/p01-stage-03-candidate-qualification-rules.md`, a review procedure, 20 additional boundary cases, a PFI invariance protocol and explicit owner review decisions. The original and refined KivaNura crude-oil-to-driver analogy is retained at `docs/foundations/crude-oil-to-driver-teaching-analogy.md` as **informative only**. The `research/p01-s02/` and `research/p01-s03/` files are non-normative evidence/traceability records and scripts do **not** certify any Product or PFI. **Joint sufficiency of candidate qualification conditions is unproven**; no INFOPCH maturity assessment, descriptor contract or conformance claim has been issued.

## Owner-reviewed Stage 4 consolidation (20 October 2026)

**G01 (15/15), G02 (7/7), G03 (10/10), and G04 (9/9) have completed conditional owner-reviewed research.** G04-D09-F01 approved `CLOSED_CONDITIONAL_RESEARCH` closure on 20 October 2026. This gives **41 distinct approved research decisions**, counting the fifteen S02/S03 antecedents once as the G01 closure basis. **G05-G07 are PENDING and NOT STARTED.** INFOPS 0.1 is NOT a normative qualification standard and all G03-R01-R12 release holds remain open.

Primary source and decision pages:

- [S04 overview](docs/ontology/p01-stage-04-overview.md), [G01-G04 owner decision register](docs/ontology/p01-stage-04-owner-decisions.md).
- [G04 owner-approved decisions D01-D09](docs/ontology/p01-stage-04-g04-owner-approved-decisions.md) - full reviewed research findings.
- [G04 final closure record](docs/ontology/p01-stage-04-g04-closure-record.md) - approval, case/test reconciliation, Q0-Q5, normative holds and next-gate limits.
- [Source authority](docs/ontology/p01-stage-04-source-authorities.md), [artifact boundaries](docs/ontology/p01-stage-04-artifact-boundaries.md), [release holds](docs/ontology/p01-stage-04-release-holds.md).

Machine-readable G04 approvals are in `research/p01-s04/g04-owner-approved-decisions.json`. Reconciliation ledgers cover **36 original S02 cases**, **16 original S02 tests**, and **20 original S03 cases**, without modifying those earlier research files. The earlier G04 proposal plan and G01-G03 manifest remain historical snapshots; current approved dispositions reside in separate registers.

**Q0** remains independently assessed BPS Productness; **Q1-Q4 universal necessity** and **Q0-Q4 joint sufficiency** remain **NOT ESTABLISHED**. **Q5** is a procedural competing-family and Compound review gate, not intrinsic Product nature. Cross-family overlaps and BPS Compound authority remain unresolved. No empirical classifier metrics or real Product certifications are claimed.

Architectural research direction: **INFOPROD** = future Information-specific semantic descriptor; **INFOPDS** = future realization/deployment specification; **BPS DPP Core** = cross-family trust with future Information Profile; **HDIP HPD** = operational Product-Version projection. All remain independently governed and do not become normative by G04 approval.

### Applying the G04 incremental owner-decision overlay

Apply the new G04 ZIP **on top of exactly the previously delivered `INFOPS-P01-S04-G01-G03-owner-approvals-complete.zip` repository state**. The ZIP paths are relative to the INFOPS checkout root. Preserve `.git`, your existing `package-lock.json`, site deployment settings and independently changed files. Examine the overlay manifest before committing.

```bash
unzip -o INFOPS-P01-S04-G04-D01-D09-owner-closure-overlay.zip
npm run validate
npm run build
```

The G04 overlay neither updates remote GitHub nor writes normative Product qualification schemas. `npm run validate` checks previous S01-S03 research and current S04/G04 owner-approved research. The full Docusaurus build requires dependencies installed in the local or CI environment.

## Run locally

Requirements: Node.js 20+; npm; Python 3 for the scaffold validator.

```bash
npm install
npm run validate
npm start
```

Open the local URL displayed by Docusaurus (normally http://localhost:3000).

For a production build:

```bash
npm run build
npm run serve
```

`npm install` produces a `package-lock.json` file. **Commit that lockfile** to the GitHub repository after the first successful install; CI automatically switches to `npm ci` when present. Dependency installation requires network access to npm unless dependencies are already cached.

## GitHub / stage overlays

For an INFOPS repository already containing the G01-G03 owner-approved consolidation, apply the **G04 incremental overlay** at checkout root. For a repository still at original `INFOPS.zip`, use the earlier owner-baseline-to-G01-G03 overlay first, then this G04 overlay; do not substitute one for the other. Preserve `package-lock.json`, `.git`, environment settings and independently changed files. Run `npm run validate` and `npm run build` before committing.

The full updated repository ZIP retains your original top-level `shu_ha_ri/` folder; the smaller overlay is rooted at the repo root. See `INFOPS-P01-S04-MERGE-NOTES.md` for the actual baseline-specific deployment instructions. After validating your local checkout:

```bash
git add .
git commit -m "Record INFOPS P01 S04 G04 D01-D09 conditional research closure"
git push -u origin HEAD
```

If you have not yet cloned/connected the remote, first clone the empty repository from its real URL and copy the contents into it. There is no assumed repository URL in this scaffold.

## Deployment settings

`docusaurus.config.js` uses `https://example.org` and `/` as safe *placeholders*, not deployment commitments. Before publishing, configure:

- `SITE_URL` to the actual website origin (for example `https://docs.example.org`);
- `BASE_URL` to `/` for a site root, or `/<repository-name>/` for project-style GitHub Pages;
- `organizationName` / `projectName` to the actual account and repository name;
- publisher-approved copyright and licensing conditions.

For example:

```bash
SITE_URL=https://docs.example.org BASE_URL=/ npm run build
```

## Layout

```text
├── docs/                           # Proposed specification and PMDD docs
│   ├── specification/              # Status, programme, roadmap
│   ├── foundations/                # Authority map and informative oil/driver analogy
│   ├── ontology/                   # Reserved P01 subject
│   ├── infopch/                    # Reserved P02 characteristic catalogue
│   ├── pmdd/                       # Reserved P03/P04 guidance and maturity
│   ├── descriptors/                # Reserved P05 descriptor strategy
│   ├── conformance/                # Reserved P06 conformance
│   └── integration/                # UPOS and HDIP boundaries
├── src/pages/                      # Homepage and agent guidance entry
├── static/spec/infops/0.1/         # Reserved machine-readable artifact namespace
├── templates/                      # Future characteristics/qualification/agent cases
├── research/p01-s02/                # Preserved S02 falsification research ledgers
├── research/p01-s03/                # S03 candidate rules, cases, analogy and decision ledger
├── research/p01-s04/                # S04 conditional owner-review and adoption-hold ledgers
├── scripts/                        # Scaffold/research validation (NOT conformance)
├── .github/workflows/             # Docs build CI when configured in your checkout
├── docusaurus.config.js
└── sidebars.js
```


### Owner-approved S02/S03 research decisions and S04-G01 closure

The owner subsequently approved **S02-D01 to D06 (6)** and **S03-D01 to D09 (9)**, incorporating reviewed refinements. These **15 antecedent approvals** form the **S04-G01 research closure basis**, without creating another set of G01 decision IDs or double-counting the 32 S04-G01/G02/G03 owner-reviewed research decisions.

- [S02 approval addendum](docs/ontology/p01-stage-02-owner-approved-decisions.md)
- [S03 approval addendum](docs/ontology/p01-stage-03-owner-approved-decisions.md)
- [S04-G01 closure basis](docs/ontology/p01-stage-04-g01-closure-basis.md)
- Machine register: `research/p01-s04/s02-s03-owner-approvals.json`

The original S02/S03 `PROPOSED` research files remain unchanged as historical source snapshots; **they no longer describe the current owner disposition**. The later approvals are non-normative, leave Q1–Q4 necessity and joint sufficiency unproven, and do not authorize Product certification, INFOPROD, INFOPDS, BPS DPP Profile or INFOPS 0.1 normative release.

## Authority and release rules

The existing authority boundaries are explicitly respected: generic Productness belongs to BPS/PIN; Information/Analytics meaning to GEARM; analytical architecture to GEARA; HDIP and UPOS provide separate platform/operating concepts. Data Product DPROD/DPDS and AI Product AIPS/AIPROD/AIPDS are **referenced external/adjacent Product-family sources**, not copied into INFOPS.

The Stage 2 and Stage 3 research ledgers are **not semantic conformance engines** and does not establish any live Product qualification. The scaffold must not be treated as evidence of qualification, maturity, deployment readiness or conformance. Do not label INFOPCH characteristics or INFOPS schemas normative until those decisions have been reviewed.

## Licence

**Uploaded repository licensing note:** The attached `INFOPS.zip` includes a `LICENSE` file containing GNU General Public License Version 3 text. The S04 integration preserves that file unchanged. The repository owner should confirm whether this is the intended licence and ensure applicable notices and redistribution conditions are met. No further licence is granted or modified by this research overlay.
