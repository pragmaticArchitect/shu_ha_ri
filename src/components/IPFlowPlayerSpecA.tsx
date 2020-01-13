import React, {useEffect, useMemo, useRef, useState} from 'react';
import {saLanes, saPaths, saPathTitles, saMoments, visibleSANodes, visibleSAEdges, type SAPath} from '../data/IPSpecAFlow';
import './IPFlowPlayerSpecA.css';

const rates=[0.5,1,1.5,2];
type Inspector={type:'node'|'edge';id:string}|null;
export default function IPFlowPlayerSpecA():React.JSX.Element {
 const [path,setPath]=useState<SAPath>('create');
 const [index,setIndex]=useState(0);
 const [playing,setPlaying]=useState(false);
 const [rate,setRate]=useState(1);
 const [inspect,setInspect]=useState<Inspector>(null);
 const [allEdges,setAllEdges]=useState(false);
 const steps=useMemo(()=>saMoments(path),[path]);
 const nodes=useMemo(()=>visibleSANodes(path),[path]);
 const edges=useMemo(()=>visibleSAEdges(path),[path]);
 const step=steps[index]||steps[0];
 const activeNodes=new Set(step.nodeIds); const activeEdges=new Set(step.edgeIds);
 const rootRef=useRef<HTMLDivElement|null>(null);
 const nodeRefs=useRef<Record<string,HTMLButtonElement|null>>({});
 const [routes,setRoutes]=useState<Record<string,string>>({});
 const [size,setSize]=useState({width:1,height:1});
 const changePath=(p:SAPath)=>{setPath(p);setIndex(0);setPlaying(false);setInspect(null);setAllEdges(false);};
 const go=(n:number)=>{setIndex(Math.max(0,Math.min(steps.length-1,n)));setPlaying(false);};
 useEffect(()=>{if(!playing)return;if(index>=steps.length-1){setPlaying(false);return;}const timer=window.setTimeout(()=>setIndex(i=>Math.min(i+1,steps.length-1)),Math.round(1900/rate));return()=>window.clearTimeout(timer);},[playing,index,steps.length,rate]);
 useEffect(()=>{
   const panel=rootRef.current;if(!panel)return;let raf=0;
   const measure=()=>{window.cancelAnimationFrame(raf);raf=window.requestAnimationFrame(()=>{
     const rect=panel.getBoundingClientRect(),paths:Record<string,string>={};
     edges.forEach(e=>{const f=nodeRefs.current[e.from]?.getBoundingClientRect(),t=nodeRefs.current[e.to]?.getBoundingClientRect();if(!f||!t)return;
       const fx=f.left+f.width/2-rect.left,fy=f.top+f.height/2-rect.top,tx=t.left+t.width/2-rect.left,ty=t.top+t.height/2-rect.top;
       const dx=tx-fx,dy=ty-fy;
       if(Math.abs(dx)>90){const sx=fx+(dx>0?f.width/2:-f.width/2),ex=tx+(dx>0?-t.width/2:t.width/2);paths[e.id]=`M ${sx} ${fy} C ${sx+dx*.38} ${fy}, ${ex-dx*.38} ${ty}, ${ex} ${ty}`;}
       else {const sy=fy+(dy>0?f.height/2:-f.height/2),ey=ty+(dy>0?-t.height/2:t.height/2);paths[e.id]=`M ${fx} ${sy} C ${fx+30} ${sy+dy*.35}, ${tx-30} ${ey-dy*.35}, ${tx} ${ey}`;}
     });setRoutes(paths);setSize({width:Math.max(1,rect.width),height:Math.max(1,rect.height)});
   });};
   measure();const observer=typeof ResizeObserver!=='undefined'?new ResizeObserver(measure):null;
   if(observer){observer.observe(panel);Object.values(nodeRefs.current).forEach(n=>{if(n)observer.observe(n);});}
   window.addEventListener('resize',measure);return()=>{window.cancelAnimationFrame(raf);observer?.disconnect();window.removeEventListener('resize',measure);};
 },[path]);
 const selected=inspect?.type==='node'?nodes.find(n=>n.id===inspect.id):inspect?.type==='edge'?edges.find(e=>e.id===inspect.id):undefined;
 const selectedEdge=inspect?.type==='edge'?edges.find(e=>e.id===inspect.id):undefined;
 const drawnEdges=edges.filter(e=>routes[e.id]&&(allEdges||activeEdges.has(e.id)||inspect?.id===e.id));
 return <section className="ipsa" aria-label="Information Product SSPD Spec A interactive architecture">
   <header className="ipsa-heading"><div><p className="ipsa-kicker">HDIP PDEP · Information Product SSPD · Spec A</p><h2>Creator, HDIP & independent authority interactions</h2><p>One detailed interaction projection of deployed G0; not a new Product lifecycle.</p></div><span className="ipsa-status">Experimental E0 · Non-normative</span></header>
   <div className="ipsa-toolbar"><fieldset className="ipsa-paths"><legend>Product path</legend>{saPaths.map(p=><label className={p===path?'is-selected':''} key={p}><input type="radio" name="ipsa-path" checked={path===p} onChange={()=>changePath(p)}/>{saPathTitles[p]}</label>)}</fieldset>
   <div className="ipsa-controls" role="group" aria-label="Spec A playback controls"><button type="button" onClick={()=>go(0)}>Reset</button><button type="button" disabled={index===0} onClick={()=>go(index-1)}>Previous</button><button type="button" onClick={()=>setPlaying(v=>!v)}>{playing?'Pause':'Play'}</button><button type="button" disabled={index===steps.length-1} onClick={()=>go(index+1)}>Next</button><label>Speed <select aria-label="Playback speed" value={rate} onChange={e=>setRate(Number(e.target.value))}>{rates.map(r=><option key={r} value={r}>{r}×</option>)}</select></label><button type="button" onClick={()=>{setAllEdges(v=>!v);setInspect(null);}} aria-pressed={allEdges}>{allEdges?'Focus active links':'Show all links'}</button><button type="button" onClick={()=>window.print()}>Print view</button></div></div>
   <div className="ipsa-story" aria-live="polite" aria-atomic="true"><div><strong>{step.id} — {step.title}</strong><span>{index+1} / {steps.length}</span></div><p>{step.narrative}</p><small>M15-V03 shared PDEP grouping: {step.grouping}. Presentation moments are non-mandatory, iterative and branch-aware.</small>{step.reentryTo&&<button type="button" className="ipsa-reenter" onClick={()=>go(1)}>Explore discovery re-entry ↶</button>}</div>
   <div className="ipsa-progress" aria-label="Select Spec A presentation moment">{steps.map((s,i)=><button type="button" key={s.id} onClick={()=>go(i)} className={i===index?'is-current':''} aria-current={i===index?'step':undefined} aria-label={`${s.id} ${s.title}`}>{i+1}</button>)}</div>
   <div className="ipsa-content"><div className="ipsa-diagram" ref={rootRef}>
   <svg className="ipsa-connections" width={size.width} height={size.height} viewBox={`0 0 ${size.width} ${size.height}`} aria-hidden="true"><defs><marker id="ipsa-arr" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6Z" fill="#8591a5"/></marker><marker id="ipsa-arr-current" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6Z" fill="#0d9488"/></marker></defs>{drawnEdges.map(e=><path key={e.id} d={routes[e.id]} className={activeEdges.has(e.id)?'is-active':''} markerEnd={`url(#${activeEdges.has(e.id)?'ipsa-arr-current':'ipsa-arr'})`}/>)}</svg>
   {saLanes.map(l=><div key={l.id} className="ipsa-lane"><div className="ipsa-lane-title"><h3>{l.title}</h3><p>{l.description}</p></div><div className="ipsa-nodelist">{nodes.filter(n=>n.lane===l.id).map(n=><button type="button" key={n.id} ref={el=>{nodeRefs.current[n.id]=el;}} className={'ipsa-node '+(activeNodes.has(n.id)?'is-active ':'')+(inspect?.id===n.id?'is-inspected ':'')+'ipsa-kind-'+n.kind} onClick={()=>{setInspect({type:'node',id:n.id});setPlaying(false);}} aria-pressed={inspect?.type==='node'&&inspect.id===n.id}><strong>{n.title}</strong><span>{n.subtitle}</span><small>{n.kind==='authority'?'Independent determination':n.kind==='service'?'Shared supporting service':n.kind}</small></button>)}</div></div>)}
   </div><aside className="ipsa-inspector" aria-label="Architecture detail inspector"><h3>Inspect architecture</h3>{selected?<><span className="ipsa-inspector-type">{inspect?.type==='node'?'Node':'Typed interaction'}</span><h4>{'title' in selected?selected.title:selected.label}</h4><p>{selected.description}</p>{'boundary' in selected && selected.boundary&&<p><strong>Authority boundary: </strong>{selected.boundary}</p>}{selectedEdge&&<><p><strong>Relationship: </strong>{selectedEdge.kind.toUpperCase()}</p><p><strong>From → To: </strong>{selectedEdge.from} → {selectedEdge.to}</p>{selectedEdge.conditional&&<p>Conditional applicability — no automatic approval.</p>}</>}<button type="button" onClick={()=>setInspect(null)}>Close details</button></>:<><p>Select a node below its lane to inspect responsibilities. Select an interaction to inspect its typed relationship.</p><div className="ipsa-edges"><h4>Relationships in this moment</h4>{edges.filter(e=>activeEdges.has(e.id)).map(e=><button type="button" key={e.id} onClick={()=>{setInspect({type:'edge',id:e.id});setPlaying(false);}}><strong>{e.label}</strong><small>{e.kind.replaceAll('_',' ')} · {e.from} → {e.to}</small></button>)}</div></>}{inspect?.type==='node'&&<div className="ipsa-edges"><h4>Related interactions</h4>{edges.filter(e=>e.from===inspect.id||e.to===inspect.id).map(e=><button type="button" key={e.id} onClick={()=>setInspect({type:'edge',id:e.id})}><strong>{e.label}</strong><small>{e.kind.replaceAll('_',' ')} · {e.from} → {e.to}</small></button>)}</div>}</aside></div>
   <footer className="ipsa-notes"><p><strong>Product and meaning:</strong> BPS/PIN Productness and Product-family/Compound qualification, GEARA/GEARM semantic and analytical authority and policy/assurance decisions remain independently competent. HDIP lookup, compilation and orchestration cannot grant them.</p><p><strong>Distinct identities:</strong> Product/Version, semantic-definition version, analytical-method definition, informational Promise, INFOPROD, INFOPDS, DPP, consumption contract, PFI realization, compilation evidence, registry projection and runtime occurrences are not interchangeable.</p><p><strong>Economic and consumption boundary:</strong> X9 supports progressively indicative economics; P5 observes actual costs and value. Funding/investment decisions are enterprise-specific. Publication does not confer entitlement; the Consume path hands off to generic SSCF/CEP.</p><p><strong>Research status:</strong> Experimental E0. Seven M15-V03 PDEP groupings and ten SA playback moments are presentation constructs, not mandatory gates. No simulated control performs Product qualification, semantic approval, deployment, funding approval or runtime execution.</p><a href="/hdip-ip-flow-basic">Return to Information Product SSPD G0</a></footer>
 </section>;
}
