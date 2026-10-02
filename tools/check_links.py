#!/usr/bin/env python3
"""Verifica que todo href/src local en src/ resuelva a un archivo existente."""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / 'src'
ATTR = re.compile(r'(?:href|src)="([^"]+)"', re.I)

broken = []
checked = 0

def resuelve(base, u):
    """Un ref local resuelve a archivo, a directorio con index.html, o a foo.html (URL /foo/)."""
    u = re.sub(r'[?#].*$', '', u).rstrip('/')
    t = (SRC / u.lstrip('/')) if u.startswith('/') else (base / u)
    if t.is_file():
        return True
    if t.is_dir() and (t / 'index.html').is_file():
        return True
    return t.suffix == '' and t.with_suffix('.html').is_file()

for f in sorted(SRC.glob('*.html')):
    base = f.parent
    for m in ATTR.finditer(f.read_text(encoding='utf-8')):
        u = m.group(1).strip()
        if not u or u.startswith(('http://', 'https://', 'mailto:', '#', 'javascript:')):
            continue
        checked += 1
        if not resuelve(base, u):
            broken.append(f'{f.relative_to(SRC)}: {u}')

print(f'links/verificados: {checked}  rotos: {len(broken)}')
for b in broken:
    print('ROTO', b)
sys.exit(1 if broken else 0)
