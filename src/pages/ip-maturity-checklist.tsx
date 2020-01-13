import React from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import IPChecklist from '@site/src/components/IPChecklist';

export default function InformationProductMaturityChecklistPage() {
  return (
    <Layout title="Information Product Maturity Checklist" description="Experimental, non-normative INFOPS 0.1 IPCH self-assessment worksheet">
      <main className="container margin-vert--lg">
        <BrowserOnly fallback={<p>Loading the experimental assessment worksheet…</p>}>
          {() => <IPChecklist />}
        </BrowserOnly>
      </main>
    </Layout>
  );
}
