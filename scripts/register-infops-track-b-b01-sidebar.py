#!/usr/bin/env python3
"""Safely add the already-approved B01 research charter page to Docusaurus navigation."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
sidebar=root/'sidebars.js'
page=root/'docs/governance/infops-p01-tb-b01-owner-approved-research-charter.md'
if not sidebar.exists() or not page.exists():
    sys.exit('Refusing sidebar update: required repository file missing')
text=sidebar.read_text()
doc='governance/infops-p01-tb-b01-owner-approved-research-charter'
if text.count(doc)==1:
    print('Sidebar already registered exactly once; no changes')
    sys.exit(0)
if doc in text:
    sys.exit('Refusing: duplicate or malformed existing B01 sidebar registration')
anchor="{type: 'category', label: 'Governance & reference', items: ["
if text.count(anchor)!=1:
    sys.exit('Refusing: expected unique Governance & reference category not found')
start=text.index(anchor)+len(anchor)
end=text.find(']},',start)
if end<0: sys.exit('Refusing: malformed governance category')
updated=text[:end]+"      '"+doc+"',\n"+text[end:]
# Idempotent, preserves all existing sidebar entries.
sidebar.write_text(updated)
print('Sidebar B01 document registered once')
