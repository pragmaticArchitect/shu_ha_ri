#!/usr/bin/env python3
"""Repository/bootstrap checks (not a normative INFOPS conformance runner)."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
problems = []

def require(relative):
    path = ROOT / relative
    if not path.is_file(): problems.append(f'Missing: {relative}')
    return path

package = json.loads(require('package.json').read_text(encoding='utf-8'))
status = json.loads(require('static/spec/infops/0.1/scaffold-state.json').read_text(encoding='utf-8'))
if status.get('normative') is not False: problems.append('Scaffold unexpectedly claims normative status')
if status.get('releaseStatus') != 'PRE_P01_SCAFFOLD': problems.append('Release status has changed without guard update')
for item in ['docusaurus.config.js','sidebars.js','src/pages/index.js','src/css/custom.css',
             'src/pages/INFOPCH-PMDD-guidance/index.md','docs/intro.md',
             'docs/ontology/qualification-boundary.md','docs/infopch/overview.md',
             'docs/pmdd/assessment-guidance.md','static/img/infops-mark.svg']:
    require(item)

docs = {p.relative_to(ROOT/'docs').with_suffix('').as_posix():p for p in (ROOT/'docs').rglob('*.md')}
sidebar = require('sidebars.js').read_text(encoding='utf-8')
for ident in re.findall(r"'([a-z][a-z0-9/\-]+)'",sidebar):
    if '/' in ident or ident=='intro':
        if ident not in docs: problems.append(f'Sidebar doc unresolved: {ident}')

seen = set()
for p in (ROOT/'docs').rglob('*.md'):
    body=p.read_text(encoding='utf-8')
    if not body.startswith('---\n') or '\n---\n' not in body[4:]: problems.append(f'Missing/invalid frontmatter: {p.relative_to(ROOT)}')
    explicit = re.findall(r'^id:\s*(.+)\s*$',body,re.M)
    if explicit:
        if explicit[0] in seen: problems.append(f'Duplicate explicit id: {explicit[0]}')
        seen.add(explicit[0])
    for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',body):
        if link.startswith(('https:', 'http:', '#', 'mailto:','/docs/','/INFOPCH')): continue
        target = p.parent/link.split('#')[0]
        if not target.exists(): problems.append(f'Unresolved relative link in {p.relative_to(ROOT)}: {link}')

config = (ROOT/'docusaurus.config.js').read_text(encoding='utf-8')
for path in re.findall(r"to:\s*'(/[^']+)'", config):
    if path.startswith('/docs/'):
        target = path[len('/docs/'):]
        if target not in docs: problems.append(f'Navbar/footer doc unresolved: {path}')
    elif path == '/INFOPCH-PMDD-guidance':
        if not (ROOT/'src/pages/INFOPCH-PMDD-guidance/index.md').exists(): problems.append(f'Page missing: {path}')

for source in ('docusaurus.config.js','sidebars.js'):
    try:
        proc = subprocess.run(['node','--check',str(ROOT/source)],capture_output=True,text=True)
        if proc.returncode: problems.append(f'Node syntax error {source}: {proc.stderr.strip()}')
    except FileNotFoundError:
        print('NOTE: node executable unavailable; JavaScript syntax check skipped')

print(f'INFOPS pre-P01 scaffold checks: {len(docs)} documentation pages; {len(problems)} issue(s)')
for issue in problems: print('ERROR:',issue)
sys.exit(1 if problems else 0)
