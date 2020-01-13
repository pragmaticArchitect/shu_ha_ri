import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const cards = [
  {
    title: 'Canonical Logical Architecture',
    body: 'Follow HDIP-CLA 0.1 as Data, Information and Intelligence responsibilities are composed into a canonical enterprise logical platform architecture.',
    to: '/docs/architecture/hdip-cla-0.1-programme',
  },
  {
    title: 'Product Development',
    body: 'Explore the HDIP Product Development and Evolution Process and its governed platform compilation model.',
    to: '/docs/product-development/hdip-data-product-development-stages',
  },
  {
    title: 'Product Consumption',
    body: 'Explore SSCF and the HDIP product-consumption lifecycle across supported Product families.',
    to: '/docs/product-consumption/hdip-product-consumption-stages',
  },
  {
    title: 'Synthetic Context',
    body: 'Read the SYNCTX concept, ontology and DPFI resolution/compilation rules for governed synthetic-data generation contexts.',
    to: '/docs/synthetic-context/hdip-synthetic-context',
  },
];

export default function Home(): React.JSX.Element {
  return (
    <Layout
      title="Holistic Data, Information and Intelligence Platform"
      description="HDIP — Holistic Data, Information and Intelligence Platform">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <div className={styles.brandRow}>
            <img src="/img/hdip/logo.svg" alt="HDIP" className={styles.logo} />
            <div>
              <h1 className="hero__title">HDIP</h1>
              <p className="hero__subtitle">Holistic Data, Information and Intelligence Platform</p>
            </div>
          </div>
          <p className={styles.lead}>
            An enterprise logical platform architecture for governed, interoperable and product-oriented capabilities across Data, Information and Intelligence.
          </p>
          <div className={styles.actions}>
            <Link className="button button--primary button--lg" to="/docs/introduction">
              Start with HDIP
            </Link>
            <Link className="button button--outline button--primary button--lg" to="/docs/architecture/hdip-cla-0.1-programme">
              HDIP-CLA 0.1
            </Link>
          </div>
        </div>
      </header>

      <main>
        <section className={styles.wormholeSection} aria-labelledby="dii-wormhole-heading">
          <div className="container">
            <div className={styles.wormholeHeading}>
              <h2 id="dii-wormhole-heading">The Data–Info–Intel (DII) Wormhole</h2>
              <p className={styles.wormholeTagline}>
                <strong>Short-circuiting interaction distance. Realising intrinsic product value with evidencable trust.</strong>
              </p>
            </div>

            <figure className={styles.wormholeFigure}>
              <img
                src="/img/hdip/dii-wormhole-concept.png"
                alt="DII Wormhole Concept showing HDIP as a shortcut across a U-folded interaction space between Product Owner Symbiants and consumers"
                className={styles.wormholeImage}
                loading="eager"
              />
              <figcaption className={styles.wormholeCaption}>
                Figure: The long conventional interaction route (red) is contrasted with the shorter, trusted HDIP interaction route (green) through the conceptual wormhole (blue).
              </figcaption>
            </figure>

            <div className={styles.wormholeProse}>
              <p>
                The DII Wormhole is a conceptual representation of the interaction paradigm enabled by HDIP (Holistic Data, Information and Intelligence Platform), a specialised logical architecture of the Universal Product Operating System (UPOS).
              </p>
              <p>
                Inspired by the theoretical concept of a spacetime wormhole, HDIP creates an architectural shortcut between Data, Information and Intelligence Product Owner Symbiants and their consumers.
              </p>
              <p>
                In conventional enterprise environments, consumers must often traverse extensive organisational, technological, semantic and governance boundaries to obtain useful product capabilities. This introduces avoidable friction, dependencies, coordination effort and delivery delays.
              </p>
              <p>
                HDIP reduces this effective interaction distance through discoverable and independently governed products, explicit product contracts, authoritative registries, interoperable interfaces, policy-aware consumption and evidencable trust.
              </p>
              <p>
                The objective is not merely the exchange of products, but the <strong>realisation of their intrinsic utility in the consumer&apos;s context</strong>. Product owners preserve ownership and accountability, while consumers gain direct, governed access to the capabilities they need.
              </p>
              <p>
                As a specialised embodiment of UPOS within the wider Productverse, HDIP enables the DII Wormhole experience: bridging formerly distant product participants, reducing unnecessary intermediaries and allowing useful product capabilities to be consumed at the <em>speed of need</em>.
              </p>
              <p className={styles.wormholePrinciple}>
                <strong>The DII Wormhole does not eliminate the distance between independent participants; it makes that distance substantially less consequential to their ability to interact and realise value.</strong>
              </p>
            </div>
          </div>
        </section>

        <section className={styles.section}>
          <div className="container">
            <h2>One platform, preserved authorities</h2>
            <p className={styles.sectionIntro}>
              GEDRA, GEARA and GEAIRA define generic architectural responsibilities. HDIP composes and realizes those responsibilities as one enterprise platform while preserving semantic and Product authority boundaries.
            </p>
            <div className={styles.grid}>
              {cards.map((card) => (
                <article className="card" key={card.title}>
                  <div className="card__header"><h3>{card.title}</h3></div>
                  <div className="card__body"><p>{card.body}</p></div>
                  <div className="card__footer">
                    <Link className="button button--primary button--sm" to={card.to}>Open</Link>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className={styles.philosophy}>
          <div className="container">
            <h2>shu_ha_ri</h2>
            <p>
              The repository name reflects the martial-arts progression from preserving sound foundations, through deliberate adaptation, to fluent creation beyond inherited form. HDIP applies the same discipline to enterprise platform architecture.
            </p>
          </div>
        </section>
      </main>
    </Layout>
  );
}
