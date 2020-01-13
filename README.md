# INFOPS — Information Product Specification

**Status: INFOPS-P01 STAGE 3 CONDITIONAL QUALIFICATION RESEARCH DRAFT (NON-NORMATIVE).** This is a new Docusaurus project for developing INFOPS 0.1. It is **not** a published, normative Information Product specification.

## Purpose

INFOPS will define Information Product family qualification consistent with **BPS/PIN**, **GEARM** and **GEARA**, with its own **INFOPCH** characteristics and evidence-based **Product Maturity-Driven Development (PMDD)** guidance for human and AI assessors. It will align with **HDIP/UPOS** without absorbing their distinct architectural responsibilities.

The original P01 Stage 1 baseline and review remain preserved. Stage 2 (`docs/ontology/p01-stage-02-pin-differentiation-falsification.md`) contains 36 conditional case dispositions, ten PFI thought experiments and 16 falsification tests. Stage 3 adds `docs/ontology/p01-stage-03-candidate-qualification-rules.md`, a review procedure, 20 additional boundary cases, a PFI invariance protocol and explicit owner review decisions. The original and refined KivaNura crude-oil-to-driver analogy is retained at `docs/foundations/crude-oil-to-driver-teaching-analogy.md` as **informative only**. The `research/p01-s02/` and `research/p01-s03/` files are non-normative evidence/traceability records and scripts do **not** certify any Product or PFI. **Joint sufficiency of candidate qualification conditions is unproven**; no INFOPCH maturity assessment, descriptor contract or conformance claim has been issued.

The initial structure deliberately resembles the AIPS Docusaurus approach: documentation, characteristics/guidance, descriptors, machine-readable `static/spec` assets, validation scripts and CI.

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

If this is an **existing INFOPS repository already deployed on Netlify**, apply the **P01-S03 overlay ZIP** rather than replacing the checkout. Its repository-relative paths contain only files added or modified since the S02 PIN falsification cumulative baseline; retain your own `package-lock.json`, repository-specific configuration and independent files. Run `npm run validate` and `npm run build`, review and commit the changes.

If creating an entirely fresh INFOPS checkout from the cumulative archive, it contains repository-relative paths at the ZIP root and no `.git` directory. Extract it into your local repository checkout:

```bash
git add .
git commit -m "Add INFOPS P01 Stage 3 candidate qualification research"
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
├── scripts/                        # Scaffold/research validation (NOT conformance)
├── .github/workflows/             # Docs build CI
├── docusaurus.config.js
└── sidebars.js
```

## Authority and release rules

The existing authority boundaries are explicitly respected: generic Productness belongs to BPS/PIN; Information/Analytics meaning to GEARM; analytical architecture to GEARA; HDIP and UPOS provide separate platform/operating concepts. Data Product DPROD/DPDS and AI Product AIPS/AIPROD/AIPDS are **referenced external/adjacent Product-family sources**, not copied into INFOPS.

The Stage 2 and Stage 3 research ledgers are **not semantic conformance engines** and does not establish any live Product qualification. The scaffold must not be treated as evidence of qualification, maturity, deployment readiness or conformance. Do not label INFOPCH characteristics or INFOPS schemas normative until those decisions have been reviewed.

## Licence

**No public licence selected yet.** Before public redistribution or contribution acceptance, the repository owner should decide and publish explicit copyright, reuse and contribution terms. This scaffold does not copy the AIPS licence or grant its permissions by implication.
