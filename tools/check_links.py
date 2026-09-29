#!/usr/bin/env python3
"""Verifica que todo href/src local en src/ resuelva a un archivo existente."""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / 'src'
ATTR = re.compile(r'(?:href|src)="([^"]+)"', re.I)

broken = []
checked = 0
for f in sorted(SRC.glob('html/*.html')) + sorted(SRC.glob('*.shtml')) + [SRC / 'index.html']:
    base = f.parent
    for m in ATTR.finditer(f.read_text(encoding='utf-8')):
        u = m.group(1).strip()
        if not u or u.startswith(('http://', 'https://', 'mailto:', '#', 'javascript:')):
            continue
        checked += 1
        target = base / re.sub(r'[?#].*$', '', u)
        if not target.exists():
            broken.append(f'{f.relative_to(SRC)}: {u}')

print(f'links/verificados: {checked}  rotos: {len(broken)}')
for b in broken:
    print('ROTO', b)
sys.exit(1 if broken else 0)
