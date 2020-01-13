import React,{useState} from 'react';
import {scIdentities} from '../data/IPSpecCFlow';
export default function IPSpecCIdentityInspector():React.JSX.Element {
 const [id,setId]=useState(scIdentities[0].id);const item=scIdentities.find(i=>i.id===id)||scIdentities[0];
 return <section className="ipsc-inspector" aria-label="Spec C identity and version inspector"><h3>Identity & version inspector</h3><p className="ipsc-muted">Conceptual dimensions, not mandatory schema keys or adopted identifiers.</p><label htmlFor="ipsc-identity">Identity / evidence dimension</label><select id="ipsc-identity" value={id} onChange={e=>setId(e.target.value)}>{scIdentities.map(i=><option key={i.id} value={i.id}>{i.title}</option>)}</select><dl><dt>Meaning</dt><dd>{item.meaning}</dd><dt>Not equivalent to</dt><dd>{item.notSameAs}</dd><dt>Applicable authority</dt><dd>{item.authority}</dd></dl><h4>Illustrative distinctions</h4><ul>{item.examples.map(s=><li key={s}>{s}</li>)}</ul></section>
}
