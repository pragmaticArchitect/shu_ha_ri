import React,{useEffect,useMemo,useRef,useState} from 'react';
import {sscfModel,type ConsumptionView,type ConsumptionScenario} from '../data/IPConsumptionFlow';
import './IPConsumptionFlow.css';
const titles:Record<ConsumptionView,string>={basic:'G0 — Consumer Experience',sa:'Spec A — Structured Interactions',sc:'Spec C — Detailed Consumption Architecture'};
const viewSummary:Record<ConsumptionView,string>={basic:'What does the consumer need, and how can an existing Product deliver value?',sa:'Which consumer, SSCF, independent authority and artifact responsibilities interact?',sc:'Which exact identities, competent decisions, occurrences and evidence support the consumption context?'};
const views:[ConsumptionView,string][]=[['basic','G0'],['sa','Spec A'],['sc','Spec C']];
const pathFor:Record<ConsumptionView,string>={basic:'/hdip-product-consumption-basic',sa:'/hdip-product-consumption-sa',sc:'/hdip-product-consumption-sc'};
const scenarioKeys=Object.keys(sscfModel.scenarios) as ConsumptionScenario[];
export default function IPConsumptionFlowPlayer({view}:{view:ConsumptionView}):React.JSX.Element {
 const moments=sscfModel.moments[view];
 const [moment,setMoment]=useState(0),[playing,setPlaying]=useState(false);
 const [family,setFamily]=useState<string>(sscfModel.families[1]);
 const [persona,setPersona]=useState<string>(sscfModel.personas[1]);
 const [scenario,setScenario]=useState<ConsumptionScenario>('direct');
 const [focus,setFocus]=useState<string|null>(null),[all,setAll]=useState(false);
 const [inspector,setInspector]=useState<'nodes'|'identities'|'evidence'>('nodes');
 const active=moments[moment]||moments[0];
 const nodeIds=useMemo(()=>new Set<string>([...active.nodeIds,...sscfModel.scenarios[scenario].focus]),[active,scenario]);
 const focused=sscfModel.nodes.find(n=>n.id===focus);
 const links=sscfModel.links.filter(l=>all||nodeIds.has(l.source)&&nodeIds.has(l.target)||focus===l.source||focus===l.target);
 const diagramRef=useRef<HTMLElement|null>(null);
 const nodeRefs=useRef<Record<string,HTMLButtonElement|null>>({});
 const [geometry,setGeometry]=useState<{width:number;height:number;paths:Record<string,string>}>({width:1,height:1,paths:{}});
 useEffect(()=>{
   const diagram=diagramRef.current;
   if(!diagram)return;
   let frame=0;
   const measure=()=>{
     window.cancelAnimationFrame(frame);
     frame=window.requestAnimationFrame(()=>{
       const diagramBox=diagram.getBoundingClientRect();
       const paths:Record<string,string>={};
       for(const relation of sscfModel.links){
         const source=nodeRefs.current[relation.source]?.getBoundingClientRect();
         const target=nodeRefs.current[relation.target]?.getBoundingClientRect();
         if(!source||!target)continue;
         const sx=source.left+source.width/2-diagramBox.left;
         const sy=source.top+source.height/2-diagramBox.top;
         const tx=target.left+target.width/2-diagramBox.left;
         const ty=target.top+target.height/2-diagramBox.top;
         const dx=tx-sx,dy=ty-sy;
         // Paths end at card edges; a curve, not a straight line through the cards.
         if(Math.abs(dx)>80){
           const startX=sx+(dx>0?source.width/2:-source.width/2);
           const endX=tx+(dx>0?-target.width/2:target.width/2);
           const bend=(endX-startX)*.43;
           paths[relation.id]=`M ${startX} ${sy} C ${startX+bend} ${sy}, ${endX-bend} ${ty}, ${endX} ${ty}`;
         }else{
           const startY=sy+(dy>0?source.height/2:-source.height/2);
           const endY=ty+(dy>0?-target.height/2:target.height/2);
           const bend=(endY-startY)*.42;
           paths[relation.id]=`M ${sx} ${startY} C ${sx+24} ${startY+bend}, ${tx-24} ${endY-bend}, ${tx} ${endY}`;
         }
       }
       setGeometry({width:Math.max(1,diagramBox.width),height:Math.max(1,diagramBox.height),paths});
     });
   };
   measure();
   const observer=typeof ResizeObserver!=='undefined'?new ResizeObserver(measure):null;
   if(observer){observer.observe(diagram);Object.values(nodeRefs.current).forEach(node=>{if(node)observer.observe(node);});}
   window.addEventListener('resize',measure);
   return()=>{window.cancelAnimationFrame(frame);observer?.disconnect();window.removeEventListener('resize',measure);};
 },[]);
 const activeLinkIds=new Set(sscfModel.links.filter(l=>nodeIds.has(l.source)&&nodeIds.has(l.target)).map(l=>l.id));

 useEffect(()=>{if(!playing)return;if(moment>=moments.length-1){setPlaying(false);return;}const t=window.setTimeout(()=>setMoment(n=>Math.min(n+1,moments.length-1)),2000);return()=>window.clearTimeout(t);},[moment,moments.length,playing]);
 const move=(value:number)=>{setMoment(Math.max(0,Math.min(moments.length-1,value)));setPlaying(false);setFocus(null);};
 return <main className="ipcon">
 <header className="ipcon-header"><p className="ipcon-eyebrow">INFOPS 0.1 · ACT2 · HDIP SSCF · Experimental E0</p><h1>Generic HDIP Product Consumption — {titles[view]}</h1><p>{viewSummary[view]}</p><div className="ipcon-badges"><span>Product-family agnostic</span><span>Illustrative, not a mandatory lifecycle</span><span>Independent authority retained</span></div></header>
 <nav className="ipcon-views" aria-label="SSCF architecture views">{views.map(([key,text])=><a key={key} href={pathFor[key]} aria-current={view===key?'page':undefined}>{text}</a>)}</nav>
 <section className="ipcon-controls" aria-label="Consumer context and illustrative compatibility"><div><label htmlFor="ipcon-family">Product Family</label><select id="ipcon-family" value={family} onChange={e=>setFamily(e.target.value)}>{sscfModel.families.map(x=><option key={x}>{x}</option>)}</select></div><div><label htmlFor="ipcon-persona">CEP / persona example</label><select id="ipcon-persona" value={persona} onChange={e=>setPersona(e.target.value)}>{sscfModel.personas.map(x=><option key={x}>{x}</option>)}</select></div><p role="note">Illustration: <strong>{family}</strong> viewed through a <strong>{persona}</strong> experience. This selection does not establish compatibility, supported Product ports, entitlement, Product Family or fitness.</p></section>
 <section className="ipcon-scenarios" aria-label="Consumption condition"><label htmlFor="ipcon-scenario">Illustrative consumption condition</label><select id="ipcon-scenario" value={scenario} onChange={e=>{setScenario(e.target.value as ConsumptionScenario);setFocus(null);}}>{scenarioKeys.map(k=><option key={k} value={k}>{sscfModel.scenarios[k].name}</option>)}</select><p>{sscfModel.scenarios[scenario].description}</p></section>
 <section className="ipcon-story" aria-label="Illustrative narration"><div className="ipcon-play"><button onClick={()=>move(0)}>Reset</button><button onClick={()=>move(moment-1)} disabled={moment===0}>Previous</button><button onClick={()=>setPlaying(v=>!v)}>{playing?'Pause':'Play'}</button><button onClick={()=>move(moment+1)} disabled={moment===moments.length-1}>Next</button><span>Moment {moment+1} of {moments.length}</span></div><p className="ipcon-eyebrow">{active.id} · Illustrative logical interaction</p><h2>{active.title}</h2><p>{active.summary}</p><div className="ipcon-moments" aria-label="Narrative moment selector">{moments.map((x,i)=><button key={x.id} onClick={()=>move(i)} aria-current={i===moment?'step':undefined}>{i+1}</button>)}</div></section>
 <div className="ipcon-toolbar"><label><input type="checkbox" checked={all} onChange={e=>setAll(e.target.checked)}/> Show every logical relationship</label><button onClick={()=>{setFocus(null);setAll(false);}}>Clear inspection</button></div>
 <div className="ipcon-layout"><section className="ipcon-lanes" ref={diagramRef} aria-label="Four-lane shared SSCF model"><svg className="ipcon-connectors" width={geometry.width} height={geometry.height} viewBox={`0 0 ${geometry.width} ${geometry.height}`} aria-hidden="true"><defs><marker id="ipcon-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#64748b"/></marker><marker id="ipcon-arrow-highlight" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#0e766f"/></marker></defs>{links.filter(l=>Boolean(geometry.paths[l.id])).map(l=><path key={l.id} d={geometry.paths[l.id]} className={activeLinkIds.has(l.id)?'ipcon-connector-active':''} markerEnd={`url(#${activeLinkIds.has(l.id)?'ipcon-arrow-highlight':'ipcon-arrow'})`}/>)}</svg>{sscfModel.lanes.map(l=><div className="ipcon-lane" key={l.id}><header><h3>{l.title}</h3><p>{l.hint}</p></header><div className="ipcon-node-list">{sscfModel.nodes.filter(n=>n.lane===l.id).map(n=><button key={n.id} ref={el=>{nodeRefs.current[n.id]=el;}} className={'ipcon-node '+(nodeIds.has(n.id)?'ipcon-active ':'')+(focus===n.id?'ipcon-focused':'')} aria-pressed={focus===n.id} onClick={()=>{setFocus(n.id);setInspector('nodes');setPlaying(false);}}><strong>{n.title}</strong><small>{n.subtitle}</small><span>{n.kind==='authority'?'Independent authority':n.kind==='service'?'Shared service':n.kind}</span></button>)}</div></div>)}</section><aside className="ipcon-inspector"><div className="ipcon-tabs" role="group" aria-label="Inspect SSCF architecture"><button aria-pressed={inspector==='nodes'} onClick={()=>setInspector('nodes')}>Interactions</button><button aria-pressed={inspector==='identities'} onClick={()=>setInspector('identities')}>Identities</button><button aria-pressed={inspector==='evidence'} onClick={()=>setInspector('evidence')}>Evidence</button></div>
 {inspector==='nodes'?<><h3>{focused?focused.title:'Typed relationships'}</h3>{focused?<p>{focused.description}</p>:<p>Select a node or inspect the typed links below. A reference does not establish independent authority.</p>}<div className="ipcon-edges">{links.map(e=><button key={e.id} onClick={()=>{setFocus(e.source);setPlaying(false);}}><strong>{e.interaction}</strong><small>{e.source} → {e.target}</small><span>{e.annotation} · {e.id}</span></button>)}</div></>:null}
 {inspector==='identities'?<><h3>Identity & version boundaries</h3>{sscfModel.identities.map((x,i)=><details key={x.title} open={i===0}><summary>{x.title}</summary><p>{x.meaning}</p></details>)}</>:null}
 {inspector==='evidence'?<><h3>Evidence inspection — illustrative</h3><dl><dt>Exact subject and claim</dt><dd>Which Product/Version, context and assertion are in scope?</dd><dt>Governing references</dt><dd>Product-family, semantics, source, policy and applicable assurance independently competent.</dd><dt>Evidence provenance</dt><dd>Declaration, reference, authentic execution, delivered Information and observation are distinct.</dd><dt>Evaluation</dt><dd>Unknown, absent, insufficient, contradicted and historical do not collapse into pass/fail.</dd><dt>Decision/currentness</dt><dd>Competent decision, purpose and time separately attributable; access does not authorize consequential action.</dd><dt>E0 / E1 / E2</dt><dd>E0 visualization only. Parent G06: 62 E0 designs unexecuted; E1 = 0; E2 = 0. Playback creates no empirical evidence.</dd></dl></>:null}</aside></div>
 <footer className="ipcon-footer"><h3>Non-normative architectural boundaries</h3><p><strong>Consumer is not Owner:</strong> PCON does not automatically become PRO, DPRO, IPRO or AIPRO. Product Family and CEP are orthogonal.</p><p><strong>No automatic approvals:</strong> Discovery is not Productness, contract is not entitlement, enforcement is not consequential action authorization, and multi-Product use is not independently qualified Compound Product.</p><p><strong>Information integrity:</strong> Product/Version, Promise, semantic method, contract, port/provider, invocation, execution occurrence, delivered Information occurrence, evidence, assessment and currentness remain distinct.</p><p><strong>Economics:</strong> X9 indicative cost versus P5 actual observed value. Enterprise funding authority remains external.</p><p><strong>Governance:</strong> Frozen M15-V03; D42 deferred to 1.0; Q0–Q5 research limits; F06/F14/F16 unresolved; 24 OPEN obligations; First Pass ACTIVE_NOT_CLOSED; Second Pass NOT_STARTED; normative release NOT_AUTHORIZED.</p><nav aria-label="PDEP views"><a href="/hdip-ip-flow-basic">ACT1 G0</a><a href="/hdip-ip-flow-sa">ACT1 Spec A</a><a href="/hdip-ip-flow-sc">ACT1 Spec C</a></nav></footer>
 </main>;
}
