import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const areas = [
  {id: '01', title: 'Product ontology', description: 'Establish Productness and Information Product family qualification without confusing them with maturity.', path: '/docs/ontology/overview'},
  {id: '02', title: 'Information Product characteristics', description: 'Define evidence-backed INFOPCH characteristics, applicability and agent-neutral assessment guidance.', path: '/docs/infopch/overview'},
  {id: '03', title: 'PMDD', description: 'Guide qualified Information Products through version-bound, evidence-driven maturity improvement.', path: '/docs/pmdd/overview'},
  {id: '04', title: 'HDIP & UPOS', description: 'Align information-family semantics with governed self-service discovery, compilation and consumption.', path: '/docs/integration/hdip-upos'},
];

export default function Home() {
  return (
    <Layout title="INFOPS" description="Information Product Specification - P01 Stage 4 conditional owner-reviewed research">
      <main>
        <header className={styles.hero}>
          <div className="container">
            <p className={styles.eyebrow}>KivaNura · ProductVerse · Product Family Specifications</p>
            <h1>Information Product Specification</h1>
            <p className={styles.subtitle}>INFOPS</p>
            <p className={styles.description}>
              Investigating Information Product intrinsic nature, candidate qualification rules,
              and evidence-based Product Maturity-Driven Development.
            </p>
            <div className={styles.actions}>
              <Link className="button button--primary button--lg" to="/docs/intro">Explore the project</Link>
              <Link className="button button--secondary button--lg" to="/docs/ontology/p01-stage-04-overview">S04 review status</Link>
            </div>
            <div className={styles.status}>P01 Stage 4: G01-G05 conditional research closed (8/8 G05 approved; 49 total decisions) · G06/G07 pending · No normative qualification published</div>
          </div>
        </header>
        <section className={styles.section}>
          <div className="container">
            <h2>Built on existing semantic authorities</h2>
            <p>INFOPS will reference BPS/PIN for Product semantics, GEARM for Information meaning, GEARA for Information architecture, and HDIP/UPOS for realization and self-service experiences. It will not redefine them.</p>
            <div className={styles.grid}>
              {areas.map((area) => (
                <Link key={area.id} to={area.path} className={styles.card}>
                  <span className={styles.number}>{area.id}</span>
                  <h3>{area.title}</h3>
                  <p>{area.description}</p>
                  <span className={styles.arrow}>Explore →</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
