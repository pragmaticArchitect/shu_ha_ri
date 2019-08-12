# shu_ha_ri — HDIP

This repository is the source for **HDIP — Holistic Data, Information and Intelligence Platform** and the site at **https://hdip.kivanura.org**.

The repository name **shu_ha_ri** evokes the Japanese martial-arts learning model:

- **Shu** — learn and preserve sound foundations;
- **Ha** — examine, adapt and break beyond inherited forms;
- **Ri** — internalise the principles and create fluently beyond the form.

That progression reflects the intent of HDIP: preserve authoritative semantic and architectural boundaries, compose them deliberately, and evolve toward a coherent enterprise platform architecture.

## Project status

This initial repository baseline establishes the home for the **HDIP Canonical Logical Architecture programme (HDIP-CLA 0.1)** and imports only HDIP material that has already been reconciled from the BPS repository.

The imported baseline includes:

- HDIP introductory architecture material;
- Data PDEP lifecycle;
- Product consumption / SSCF lifecycle;
- Enterprise Data Management Level-1 requirements;
- HDIP Product Descriptor (HPD);
- Synthetic Context (SYNCTX) concept, ontology and PDEP/DPFI compilation rules.

Unreviewed BPS-era HDIP material is intentionally not migrated in this initial commit.

## Local development

```bash
npm install
npm start
```

Production build:

```bash
npm run build
npm run serve
```

## Architecture programme

See:

- `docs/architecture/hdip-cla-0.1-programme.md`

## Authority model

HDIP is an enterprise logical platform architecture. It consumes and composes responsibilities from authoritative semantic and reference-architecture bodies rather than replacing them.

In particular, HDIP preserves the authority of BPS/PIN for generic Product semantics and the relevant Data, Information/Analytics and AI semantic/reference architecture specifications.
