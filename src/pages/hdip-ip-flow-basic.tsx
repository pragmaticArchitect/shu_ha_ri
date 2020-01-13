import React from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import IPFlowPlayerBasic from '../components/IPFlowPlayerBasic';

export default function InformationProductSSPDG0(): React.JSX.Element {
  return <Layout title="HDIP IP SSPD G0" description="Experimental Information Product self-service Product development G0 (HDIP PDEP specialization)">
    <main className="container margin-vert--lg">
      <BrowserOnly fallback={<p>Loading interactive Information Product G0 flow…</p>}>{()=> <IPFlowPlayerBasic/>}</BrowserOnly>
    </main>
  </Layout>;
}
