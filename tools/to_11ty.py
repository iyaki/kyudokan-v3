"""One-shot: rewrites src pages to Eleventy form (front matter + content).

The shared shell (head, masthead, riel, footer, scripts) moves to
src/_includes/base.html; each page keeps only its own <main> content.
URLs and relative asset paths inside content are untouched.
"""
import re, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')

def convert(path):
    src = open(path, encoding='utf-8').read()
    title = re.search(r'<title>(.*?)</title>', src).group(1)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', src)
    body = re.search(r'<body>([\s\S]*?)</body>', src).group(1)
    content = body[body.index('<main'):body.index('<footer>')].rstrip()
    assert '"' not in title, f'title quote in {path}'
    assert not re.search(r'\{\{|\{%', content), f'liquid-like token in {path}'

    fm = ['layout: base.html', f'title: "{title}"']
    if desc_m:
        fm.append(f'description: "{desc_m.group(1)}"')
    open(path, 'w', encoding='utf-8').write('---\n' + '\n'.join(fm) + '\n---\n' + content + '\n')

pages = sorted(glob.glob(f'{SRC}/*.html') + glob.glob(f'{SRC}/html/*.html'))
for p in pages:
    convert(p)
print(f'{len(pages)} pages converted')
