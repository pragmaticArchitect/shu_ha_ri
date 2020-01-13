import React from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import IPFlowPlayerSpecA from '../components/IPFlowPlayerSpecA';
export default function InformationProductSSPDSpecA():React.JSX.Element{
 return <Layout title="HDIP Information Product SSPD Spec A" description="Experimental Information Product self-service development Spec A architecture interaction model"><main className="container margin-vert--lg"><BrowserOnly fallback={<p>Loading interactive architecture…</p>}>{()=> <IPFlowPlayerSpecA/>}</BrowserOnly></main></Layout>;
}
