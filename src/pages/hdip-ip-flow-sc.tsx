import React from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import IPFlowPlayerSpecC from '../components/IPFlowPlayerSpecC';
export default function InformationProductSSPDSpecC():React.JSX.Element{
 return <Layout title="HDIP Information Product SSPD Spec C" description="Experimental detailed Information Product evidence, identity and responsibility interactions"><main className="container margin-vert--lg"><BrowserOnly fallback={<p>Loading experimental Spec C architecture view…</p>}>{()=> <IPFlowPlayerSpecC/>}</BrowserOnly></main></Layout>;
}
