#!/usr/bin/env python3
"""Restyle de las páginas internas NOF 2001 al mundo Gusuku.

Okinawa, no Japón-genérico: muros encalados de coral, tejas rojas, mar
Kerama, fénix de Shuri. Una pasada sobre src/html/*.html y src/*.shtml:
decodifica ISO-8859-1, clasifica por arquetipo (hoja de foto / índice de
galería / utilitaria / artículo), extrae el contenido real y reescribe el
archivo in place con la plantilla compartida. Idempotente vía meta
generator. Log: tools/restyle-log.txt
"""
import html as htmllib
import posixpath
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
LOG_PATH = ROOT / 'tools' / 'restyle-log.txt'
MARKER = 'kyudokan-v3-restyle'

# ---------------------------------------------------------------- parser tolerante

VOID = {'img', 'br', 'hr', 'meta', 'link', 'input', 'col', 'area', 'base',
        'param', 'colgroup', 'isindex'}
# tags que cierran un <p> abierto (NOF deja <P> sin cerrar por todos lados)
P_CLOSERS = {'p', 'table', 'tr', 'td', 'th', 'ul', 'ol', 'li', 'div', 'form',
             'h1', 'h2', 'h3', 'h4', 'blockquote', 'layer', 'ilayer'}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent')

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []
        self.parent = parent


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]

    def _close_open_p(self):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == 'p':
                del self.stack[i:]
                return

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in P_CLOSERS:
            self._close_open_p()
        node = Node(tag, {k.lower(): (v or '') for k, v in attrs}, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        tag = tag.lower()
        node = Node(tag, {k.lower(): (v or '') for k, v in attrs}, self.stack[-1])
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        # end tag huérfano: ignorar

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def parse(raw):
    tb = TreeBuilder()
    tb.feed(raw)
    return tb.root


# ---------------------------------------------------------------- helpers árbol

def walk(node):
    for c in node.children:
        yield c
        if isinstance(c, Node):
            yield from walk(c)


def find_all(node, tag):
    return [n for n in walk(node) if isinstance(n, Node) and n.tag == tag]


def collapse(s):
    return re.sub(r'\s+', ' ', s)


def get_text(node):
    parts = []
    for n in walk(node):
        if isinstance(n, str):
            parts.append(n)
        elif n.tag == 'br':
            parts.append(' ')
    return collapse(''.join(parts)).strip()


def depth(node):
    d = 0
    p = node.parent
    while p is not None and p.tag != 'root':
        d += 1
        p = p.parent
    return d


def attr_int(node, name):
    v = node.attrs.get(name, '')
    m = re.match(r'\d+', v.strip())
    return int(m.group()) if m else None


# ---------------------------------------------------------------- imágenes

BOILER_NAMES = ('clearpixel', 'base_negra', 'leon_', 'banner', 'logo_anim',
                'dataicon', 'backround', 'fondoespiral', 'spacer', 'a_blank')


def is_boiler_img(src, w, h):
    s = src.lower()
    if any(k in s for k in BOILER_NAMES):
        return True
    if s.endswith('_np1.gif') or s.endswith('_hp3.gif') or s.endswith('_nbanner_texto.gif'):
        return True
    if re.search(r'/(a_)?rectangle|arrowline', s):
        return True
    if w == 0 or h == 0:
        return True
    return False


def img_src(node):
    return (node.attrs.get('src') or '').strip()


def content_imgs(root):
    out = []
    for img in find_all(root, 'img'):
        src = img_src(img)
        if not src or src.lower().startswith(('http:', 'https:')):
            continue
        if is_boiler_img(src, attr_int(img, 'width'), attr_int(img, 'height')):
            continue
        out.append(img)
    return out


# ---------------------------------------------------------------- arquetipos

INDEXES = {
    'fotos.html', 'fotos_de_torneos.html', 'afiches.html', 'fotos_de_katas.html',
    'fotos_de_exhibiciones.html', 'fotos_de_okinawa.html', 'otras_fotos.html',
    'fotos_con_maestros.html',
}
UTILITIES = {
    'contacto.html', 'horarios.html', 'como_llegar.html', 'presentacion.html',
    'servicios.html', 'promociones.html', 'cupon_de_descuento.html', 'noticias.html',
    'links.html', 'libro_de_visitas.html', 'pensamiento.html',
}
HOJA_NAMES = {
    'fotos_t_karate___kobudo_world.html', 'fotos_t_iii_copa_campana.html',
    'fotos_t_2do__world_champ.html', 'fotos_t_2__metrop__2000.html',
    'fotos_t_1__metrop__river_2000.html', 'fotos_t_pretournament_98.html',
    'fotos_t_2__intern__san_luis.html', 'fotos_t_1__intern__san_luis.html',
    'fotos_t_open_intern_bsas_98.html', 'fotos_t_world_karate_94.html',
    'fotos_t_bermuda_institute.html', 'afiches_yuchoku_higa.html',
    'afiches_3o_camp__campana.html', 'afiches_1__world_tourn___97.html',
    'afiches_2__world_tourn___97.html', 'afiches_campionati_del_mondo.html',
    'afiche_29o_camp__arg__cba_.html',
}


def classify(name, root):
    """-> arquetipo."""
    if name in INDEXES:
        return 'index'
    if name in UTILITIES:
        return 'utilitaria'
    body = find_body(root)
    imgs = content_imgs(body)
    text = total_text(root)
    big = [i for i in imgs if (attr_int(i, 'width') or 0) >= 300 or (attr_int(i, 'border') or 0) >= 2]
    if name in HOJA_NAMES or (len(big) == 1 and len(imgs) <= 2 and text < 400) \
            or (len(imgs) == 1 and text < 400):
        return 'hoja'
    # índice: ≥3 miniaturas pequeñas envueltas en <a> (los grids NOF linkean por JS)
    linky = 0
    for i in imgs:
        w = attr_int(i, 'width')
        p = i.parent
        while p is not None and p.tag != 'root':
            if p.tag == 'a':
                if w is not None and w < 200:
                    linky += 1
                break
            p = p.parent
    if linky >= 3 and text < 800:
        return 'index'
    return 'articulo'


def total_text(root):
    body = find_body(root)
    return len(get_text(body)) if body is not None else 0


def find_body(root):
    bodies = find_all(root, 'body')
    return bodies[0] if bodies else root


class Page:
    def __init__(self, path):
        self.path = path  # Path absoluto
        self.rel = '../' if path.parent.name == 'html' else ''
        self.name = path.name
        raw = path.read_bytes().decode('iso-8859-1', errors='replace')
        self.raw = raw
        self.converted = MARKER in raw
        self.tree = parse(raw) if not self.converted else None
        self.title = ''
        if self.tree:
            t = find_all(self.tree, 'title')
            self.title = orto_fix(titulo_limpio(collapse(get_text(t[0])))) if t else ''
        self.archetype = None
        self.log_notes = []
        self.imgs_ok = 0
        self.imgs_missing = 0
        self.links_out = set()

    def note(self, msg):
        self.log_notes.append(msg)


# ---------------------------------------------------------------- F_OM map (JS de NOF)

FOM_RE = re.compile(
    r"F_OM\(\s*'(\w+)'[^)]*?new Array\([^;]*?F_Parm\([^)]*?'URL','([^']+)'",
    re.S)


def fom_map(raw):
    return {pid: url for pid, url in FOM_RE.findall(raw)}


# ---------------------------------------------------------------- contenido

# Ortografía de títulos: el sitio 2001 perdió ñ/tilde en los <title>.
# Sólo títulos (h1 y <title>); el cuerpo queda verbatim.
TITULO_FIXES = (
    ('Presentacin', 'Presentación'), ('Qu es', 'Qué es'), ('Enseanza', 'Enseñanza'),
    ('Sintesis', 'Síntesis'), ('Histrica', 'Histórica'), ('Fsico', 'Físico'),
    ('Genealgico', 'Genealógico'), ('Arbol', 'Árbol'), ('Nios', 'Niños'), ('Nio', 'Niño'),
    ('Japn', 'Japón'), ('Tipica', 'Típica'), ('Tpica', 'Típica'), ('Dragn', 'Dragón'),
    ('Institucion', 'Institución'), ('Cupon', 'Cupón'), ('Artesania', 'Artesanía'),
    ('Como llegar', 'Cómo llegar'),
)


def titulo_limpio(t):
    for a, b in TITULO_FIXES:
        t = t.replace(a, b)
    return t


# Correccin ortogrfica del cuerpo (pedido del dueño, 2026-09-30): tildes
# perdidas del 2001 y typos puntuales. Claves en minscula; se preserva el
# caso de la palabra original. Solo palabras completas, nunca nombres propios.
ORTO_FIXES = {
    'tambin': 'también', 'travs': 'través', 'travz': 'través', 'aos': 'años',
    'ao': 'año', 'ms': 'más', 'japn': 'japón', 'japon': 'japón', 'japons': 'japonés',
    'nipn': 'nipón', 'fsica': 'física', 'fisica': 'física', 'fsico': 'físico',
    'fsicas': 'físicas', 'nio': 'niño', 'nios': 'niños', 'poca': 'época',
    'est': 'está', 'as': 'así', 'slo': 'solo', 'quizs': 'quizá',
    'prctica': 'práctica', 'prcticas': 'prácticas', 'psiquica': 'psíquica',
    'sinnimo': 'sinónimo', 'prdida': 'pérdida', 'espritu': 'espíritu',
    'tcnicas': 'técnicas', 'tcnica': 'técnica', 'tcnico': 'técnico',
    'tcticas': 'tácticas', 'pgina': 'página', 'generacin': 'generación',
    'caractersticas': 'características', 'bsqueda': 'búsqueda',
    'federacin': 'federación', 'ejecucin': 'ejecución', 'concentracin': 'concentración',
    'concentracn': 'concentración', 'elecccin': 'elección', 'comprensin': 'comprensión',
    'explicacin': 'explicación', 'aplicacin': 'aplicación', 'direccin': 'dirección',
    'institucin': 'institución', 'asociacin': 'asociación', 'organizacin': 'organización',
    'posicin': 'posición', 'discucin': 'discusión', 'informacin': 'información',
    'participacin': 'participación', 'traduccin': 'traducción', 'formacin': 'formación',
    'duracin': 'duración', 'funcin': 'función', 'contraposicin': 'contraposición',
    'obligacin': 'obligación', 'prohibicin': 'prohibición', 'respiracin': 'respiración',
    'confrontacin': 'confrontación', 'seccin': 'sección', 'reduccin': 'reducción',
    'definicin': 'definición', 'exploracin': 'exploración', 'reaccin': 'reacción',
    'sntesis': 'síntesis', 'sintesis': 'síntesis', 'histrica': 'histórica',
    'genealgico': 'genealógico', 'arbol': 'árbol', 'telfono': 'teléfono',
    'repblica': 'república', 'dolar': 'dólar', 'pennsula': 'península',
    'asitico': 'asiático', 'mxima': 'máxima', 'eficz': 'eficaz', 'tena': 'tenía',
    'atrados': 'atraídos', 'higinicas': 'higiénicas', 'trasnportable': 'transportable',
    'corporl': 'corporal', 'trmico': 'térmico', 'trmicas': 'térmicas', 'nica': 'única',
    'nico': 'único', 'unico': 'único', 'convirti': 'convirtió', 'realiz': 'realizó',
    'lleg': 'llegó', 'fund': 'fundó', 'ejerci': 'ejerció', 'decret': 'decretó',
    'finaliz': 'finalizó', 'invadi': 'invadió', 'actu': 'actuó', 'oscureci': 'oscureció',
    'comenz': 'comenzó', 'cay': 'cayó', 'influy': 'influyó', 'dedico': 'dedicó',
    'dirigi': 'dirigió', 'establecio': 'estableció', 'recibiendose': 'recibiéndose',
    'socializarce': 'socializarse', 'fijandose': 'fijándose', 'convirtiendose': 'convirtiéndose',
    'metdicamente': 'metódicamente', 'cacmaradera': 'camaradería', 'camaradera': 'camaradería',
    'respato': 'respeto', 'felz': 'feliz', 'femeneidad': 'feminidad',
    'corrresponde': 'corresponde', 'basicamente': 'básicamente', 'estto': 'esto',
    'kuydo': 'kyudo', 'puetazo': 'puñetazo', 'puntapi': 'puntapié',
    'obvimente': 'obviamente', 'commpleta': 'completa', 'gulpo': 'golpe',
    'tratandose': 'tratándose', 'creadodo': 'creado', 'traido': 'traído',
    'trado': 'traído', 'tamplo': 'templo', 'includo': 'incluido', 'ejemlos': 'ejemplos',
    'vaariedad': 'variedad', 'mosico': 'mosaico', 'isleos': 'isleños',
    'cultra': 'cultura', 'habre': 'abre', 'presentalo': 'preséntalo',
    'enseaza': 'enseñanza', 'shorynryu': 'shorinryu', 'kyodokan': 'kyudokan',
    'sita': 'sitúa', 'lasiones': 'lesiones', 'basdo': 'basado',
    'recaeramos': 'recaeríamos', 'tengos': 'tengo', 'ees': 'es', 'sse': 'se',
    'quere': 'querer', 'tico': 'ético', 'croju': 'goju', 'chiosin': 'choshin',
    'gojushijo': 'gojushiho', 'fukiogata': 'fukyugata', 'an': 'aún', 'ahn': 'aún',
    'inters': 'interés', 'valentia': 'valentía', 'valenta': 'valentía',
    'volvi': 'volvió', 'vivi': 'vivió', 'acta': 'actúa', 'suscríbase': 'suscríbase',
    'presidentede': 'Presidente de', 'xito': 'éxito',
    'enseanza': 'enseñanza', 'pases': 'países', 'creacin': 'creación',
    'invasin': 'invasión', 'repeticin': 'repetición', 'ensean': 'enseñan',
    'enseada': 'enseñada', 'annimo': 'anónimo', 'origenes': 'orígenes',
    'msica': 'música', 'msculos': 'músculos', 'ste': 'éste',
    'yintatsu': 'jintatsu', 'krate': 'karate', 'entren': 'entrenó',
    'extract': 'extrajo', 'discpulo': 'discípulo', 'mbito': 'ámbito',
    'pblico': 'público', 'pblicas': 'públicas', 'fu': 'fue',
}
ORTO_FRASES = [('da a da', 'día a día'), ('el da y la noche', 'el día y la noche'),
               ('se desarrollo', 'se desarrolló'), ('en esas pocas', 'en esas épocas'),
               ('como llegar', 'cómo llegar')]
ORTO_PROTEGE = ('Ping-an', 'Chang-Fu')
_ORTO_RE = re.compile(
    r'(?<![A-Za-zÁÉÍÓÚÑáéíóúñü])(' + '|'.join(
        sorted(ORTO_FIXES, key=len, reverse=True)) + r')(?![A-Za-zÁÉÍÓÚÑáéíóúñü])',
    re.IGNORECASE)
_TAG_RE = re.compile(r'<[^>]+>')


def _orto_case(w, fix):
    if w.isupper():
        return fix.upper()
    if w[0].isupper():
        return fix[0].upper() + fix[1:]
    return fix


def orto_fix(txt):
    """Corrige ortografa en TEXTO PLANO (sin tags ni atributos)."""
    for a, b in ORTO_FRASES:
        txt = re.sub(re.escape(a), b, txt, flags=re.IGNORECASE)
    # nombres con -an real (kata Ping-an) que la clave 'an' corrompera
    marcados = []
    for p in ORTO_PROTEGE:
        if p.lower() in txt.lower():
            marcados.append(p)
            txt = re.sub(re.escape(p), f'\x01{len(marcados) - 1}\x01', txt, flags=re.IGNORECASE)
    txt = _ORTO_RE.sub(lambda m: _orto_case(m.group(0), ORTO_FIXES[m.group(0).lower()]), txt)
    for i, p in enumerate(marcados):
        txt = txt.replace(f'\x01{i}\x01', p)
    return txt


def _parse_fila_nav(txt):
    """Fila nav legacy -> [(label, href|None)] en orden; None = destino inexistente."""
    items = []
    for m in re.finditer(r'<a href="([^"]+)">(.*?)</a>|<a>(.*?)</a>|([^|<]+)', txt, re.S):
        if m.group(1) is not None:
            label = re.sub(r'<[^>]+>', '', htmllib.unescape(m.group(2))).strip()
            items.append((label, m.group(1)))
        elif m.group(3) is not None:
            items.append((htmllib.unescape(m.group(3)).strip(), None))
        else:
            suelto = re.sub(r'<[^>]+>', '', htmllib.unescape(m.group(4))).strip(' |')
            if suelto:
                items.append((suelto, None))
    return [(l, h) for l, h in items if l]


def orto_fix_html(txt):
    """orto_fix preservando tags/atributos (los esconde durante el pase)."""
    tags = []

    def guarda(m):
        tags.append(m.group(0))
        return f'\x00{len(tags) - 1}\x00'

    plano = _TAG_RE.sub(guarda, txt)
    plano = orto_fix(plano)
    return re.sub(r'\x00(\d+)\x00', lambda m: tags[int(m.group(1))], plano)


JUNK_TEXT = re.compile(
    r'(?i)(error occurred while processing|dise.o: matrixway|to english|'
    r'internet explorer|800 x 600|reciba las novedades|cristian lugani\s*-\s*jean\s+jaures|'
    r'cerrar ventana|lugani\s*2001|optimizado p/|pantalla en)')


def esc(s):
    return htmllib.escape(s, quote=True)


# ---------------------------------------------------------------- tablas de datos

def table_rows(t):
    rows = []
    for tr in t.children:
        if not isinstance(tr, Node) or tr.tag != 'tr':
            continue
        cells = [c for c in tr.children if isinstance(c, Node) and c.tag in ('td', 'th')]
        rows.append(cells)
    return rows


def emit_table(t):
    rows = [r for r in table_rows(t) if any(get_text(c) for c in r)]
    if len(rows) < 2 or max(len(r) for r in rows) < 2:
        return None
    if any(len(get_text(c)) > 40 for r in rows for c in r):
        return None  # celdas largas = maquetación, no datos
    out = ['<table class="tabla-notacion"><tbody>']
    for i, r in enumerate(rows):
        tag = 'th' if i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tag}>{esc(orto_fix(get_text(c)))}</{tag}>' for c in r) + '</tr>')
    out.append('</tbody></table>')
    return ''.join(out)


# ---------------------------------------------------------------- figuras

CARTELA = ('<div class="falta"><strong>Falta en el archivo</strong>'
           'Esta fotografía no está en la copia local del sitio 2001; '
           'es recuperable del servidor original.<br><code>{name}</code></div>')


def figure_html(page, img, lazy=True, alt_override=None, caption=None):
    src = img_src(img)
    page.links_out.add(src)
    fname = posixpath.basename(src)
    exists = (page.path.parent / src).exists()
    if not exists:
        page.imgs_missing += 1
        page.note(f'IMG_FALTA {src}')
        return CARTELA.format(name=esc(fname))
    page.imgs_ok += 1
    alt = orto_fix(alt_override if alt_override is not None else collapse(img.attrs.get('alt', '')).strip())
    ldy = ' loading="lazy"' if lazy else ''
    fig = [f'<figure class="lamina"><img src="{esc(src)}"{ldy} alt="{esc(alt)}">']
    cap = caption if caption is not None else alt
    if cap:
        fig.append(f'<figcaption>{esc(orto_fix(cap))}</figcaption>')
    fig.append('</figure>')
    return ''.join(fig)


# ---------------------------------------------------------------- extractor de contenido (artículo / utilitaria)

def extract_content_tds(page):
    """TDs 'topmost' con contenido real, en orden de documento.

    NOF reparte el contenido entre TDs hermanos (texto en uno, una foto o la
    tabla de horarios en otro); califican los TDs con texto (>=40 chars) o con
    alguna imagen de contenido. Se extrae desde el TD calificante MÁS EXTERNO
    (el walker recorre tablas anidadas y figuras flotantes); los TDs contenido
    dentro de otro calificante no se extraen dos veces.
    """
    body = find_body(page.tree)
    tds = [td for td in find_all(body, 'td')
           if len(get_text(td)) >= 40 or content_imgs(td)]
    tdset = {id(td) for td in tds}
    out = []
    for td in tds:
        p = td.parent
        while p is not None:
            if id(p) in tdset:
                break
            p = p.parent
        else:
            out.append(td)
    return out


def content_blocks(page, tds, foms):
    """Párrafos/figuras/tablas de los TDs de contenido, en orden de documento."""
    page.subnav = []
    blocks = []          # str html por bloque
    para = []            # buffer inline
    bare = []            # texto fuera de <a> (para detectar filas de links)
    nlinks = 0
    in_a = False

    def img_cb(img):
        if is_boiler_img(img_src(img), attr_int(img, 'width'), attr_int(img, 'height')):
            return
        _flush_para()
        blocks.append(figure_html(page, img))

    def _flush_para():
        nonlocal para, bare, nlinks, in_a
        txt = orto_fix_html(''.join(para))
        txt = collapse(re.sub(r'&nbsp;?', ' ', txt)).strip()
        # fila de navegación: ≥2 links y casi nada de texto fuera de ellos,
        # o un solo link con texto entre corchetes ([ Presentación ] etc.)
        bare_txt = re.sub(r'[\s|\-–—·\[\]()]', '', ''.join(bare))
        plain = re.sub(r'</?a[^>]*>', '', txt).strip()
        nav_row = (nlinks >= 2 and len(bare_txt) < 3) or \
                  (nlinks == 1 and re.fullmatch(r'\[\s*[^\[\]]*\s*\]', plain))
        para, bare, nlinks, in_a = [], [], 0, False
        leading = not blocks
        fila_subnav = False
        if leading and '<a ' in txt and '<figure' not in txt and '<img' not in txt \
                and not re.search(r'&lt;[a-zA-Z]', txt):
            plano = htmllib.unescape(re.sub(r'<a(?: href="[^"]+")?>[^<]*</a>', '', txt))
            rest = re.sub(r'<[^>]+>', '', plano)
            fila_subnav = len(rest) <= 40
        if txt and len(txt) > 2 and not nav_row and not fila_subnav and not JUNK_TEXT.search(txt):
            blocks.append(f'<p>{txt}</p>')
        elif nav_row or fila_subnav:
            # filas de navegacin del legacy: al inicio se unifican como
            # subsecciones; en el pie se descartan
            if leading:
                for label, href in _parse_fila_nav(txt):
                    if href and link_prohibido(href):
                        continue
                    page.subnav.append((label, href))

    def rec(n):
        nonlocal bare, nlinks, in_a
        if isinstance(n, str):
            para.append(esc(n))
            if not in_a:
                bare.append(n)
            return
        t = n.tag
        if t in ('script', 'style', 'title', 'head'):
            return
        if t == 'form':
            _flush_para()
            blocks.append('<p><em>(Función del sitio 2001 no disponible en esta versión.)</em></p>')
            page.note('FORM_REEMPLAZADO')
            return
        if t == 'table':
            _flush_para()
            tab = emit_table(n)
            if tab:
                blocks.append(tab)
                page.note('TABLA_DATOS')
            else:
                for c in n.children:
                    rec(c)
            return
        if t == 'img':
            img_cb(n)
            return
        if t == 'p':
            _flush_para()
            for c in n.children:
                rec(c)
            _flush_para()
            return
        if t == 'br':
            para.append(' ')
            if not in_a:
                bare.append(' ')
            return
        # a/b/i/span/font/div: render inline salvo <a> con href raro
        if t == 'a':
            href = (n.attrs.get('href') or '').strip()
            if href:
                page.links_out.add(href)
            low = href.lower()
            final_href = href
            if low.startswith(('javascript', '#')) or 'cgi' in low:
                # popup F_OM (miniaturas que abren foto) o enlace real detrás del JS
                target = foms.get(n.attrs.get('id', ''), '')
                if not target:
                    for i in walk(n):
                        if isinstance(i, Node) and i.tag == 'img':
                            target = foms.get(i.attrs.get('id', ''), '')
                            if target:
                                break
                if not (target and not target.lower().startswith(('javascript', '#'))
                        and (page.path.parent / posixpath.normpath(target)).exists()):
                    for c in n.children:  # CGI del 2001: quedará como texto
                        rec(c)
                    return
                page.links_out.add(target)
                final_href = target
            nlinks += 1
            if link_prohibido(final_href):
                # etapa: contenido sin enlace hacia galeras/noticias/etc.
                if any(isinstance(x, Node) and x.tag in ('img', 'p') for x in walk(n)):
                    for c in n.children:
                        rec(c)
                    return
                nlinks += 0  # el enlace sigue contado para el filtro de nav-rows
                in_a = True
                for c in n.children:
                    rec(c)
                in_a = False
                return
            local_ok = final_href.lower().startswith(('http', 'mailto')) or \
                (page.path.parent / posixpath.normpath(final_href)).exists()
            if not local_ok:
                page.note(f'HOJA_FALTA {final_href}')
                for c in n.children:  # destino inexistente: quedará como texto
                    rec(c)
                return
            if any(isinstance(x, Node) and x.tag in ('img', 'p') for x in walk(n)):
                # anchor envolvente NOF (miniatura→hoja): envolver cada bloque
                # emitido con el enlace; un <a> no puede cruzar límites de <p>
                _flush_para()
                marca = len(blocks)
                for c in n.children:
                    rec(c)
                _flush_para()
                for i in range(marca, len(blocks)):
                    blocks[i] = f'<a href="{esc(final_href)}">{blocks[i]}</a>'
                return
            para.append(f'<a href="{esc(final_href)}">')
            in_a = True
            for c in n.children:
                rec(c)
            para.append('</a>')
            in_a = False
            return
        if t in ('b', 'strong', 'i', 'em'):
            tg = 'strong' if t in ('b', 'strong') else 'em'
            para.append(f'<{tg}>')
            for c in n.children:
                rec(c)
            para.append(f'</{tg}>')
            return
        for c in n.children:
            rec(c)

    for td in tds:
        for c in td.children:
            rec(c)
        _flush_para()
    return blocks


# ---------------------------------------------------------------- hojas e índices

BACK_LABEL = 'Volver al inicio'

# Enlaces fuera de esta etapa (pedido del dueño, 2026-09-30): su contenido
# existe pero no se enlaza. El filtro aplica a riel, sitemap, nav de galeras
# y anchors del cuerpo.
NO_LINK_NAMES = {
    'fotos.html', 'otras_fotos.html', 'noticias.html', 'todas_las_notic_.shtml',
    'nacionales.shtml', 'internacionales.shtml', 'institucion.shtml',
    'libro_de_visitas.html', 'links.html', 'promociones.html',
}


def link_prohibido(href):
    n = posixpath.basename(posixpath.normpath(href or '')).lower()
    return n in NO_LINK_NAMES or n.startswith(('fotos', 'foto_', 'afiches', 'afiche_'))


def hoja_emit(page, refs, index_names):
    imgs = content_imgs(find_body(page.tree))
    big = [i for i in imgs if (attr_int(i, 'width') or 0) >= 300
           or (attr_int(i, 'border') or 0) >= 2] or imgs[:1]
    obra = figure_html(page, big[0], lazy=False, alt_override=page.title,
                       caption=page.title) if big else CARTELA.format(name='?')
    # nav anterior/cerrar/siguiente; Cerrar = índice padre
    navs = {}
    parent = parent_of(page, refs, index_names)
    for a in find_all(find_body(page.tree), 'a'):
        txt = get_text(a).lower()
        href = (a.attrs.get('href') or '').strip()
        if 'anterior' in txt and 'anterior' not in navs:
            navs['anterior'] = href
        elif 'cerrar' in txt:
            navs['cerrar'] = parent
        elif 'siguiente' in txt and 'siguiente' not in navs:
            navs['siguiente'] = href
    links = []
    for key in ('anterior', 'cerrar', 'siguiente'):
        href = navs.get(key)
        if not href:
            continue
        if key != 'cerrar' and not (page.path.parent / href).exists():
            page.note(f'NAV_FALTA {key} {href}')
            continue
        if link_prohibido(href):
            continue
        page.links_out.add(href)
        links.append(f'<a href="{esc(href)}">{key.capitalize()}</a>')
    nav = f'<nav aria-label="Galería">{"".join(links)}</nav>' if links else ''
    return f'<main id="contenido" class="hoja-foto">\n{obra}\n{nav}\n</main>'


def index_emit(page, foms, index_names):
    body = find_body(page.tree)
    seen = set()
    items = []
    for a in find_all(body, 'a'):
        imgs = [i for i in walk(a) if isinstance(i, Node) and i.tag == 'img'
                and not is_boiler_img(img_src(i), attr_int(i, 'width'), attr_int(i, 'height'))]
        if not imgs:
            continue
        img = imgs[0]
        src = img_src(img)
        if (attr_int(img, 'width') or 0) >= 220:
            continue  # no es miniatura
        href = (a.attrs.get('href') or '').strip()
        fom = foms.get(img.attrs.get('id', ''), '') or foms.get(a.attrs.get('id', ''), '')
        if fom:
            href = fom  # el popup F_OM manda sobre el href de relleno del NOF
        elif href.lower().startswith(('javascript', '#')):
            href = ''
        key = (src, href)
        if key in seen:
            continue
        seen.add(key)
        target_ok = False
        if href and not href.lower().startswith(('http', 'mailto')):
            target_ok = (page.path.parent / href).exists()
            page.links_out.add(href)
            if not target_ok:
                page.note(f'HOJA_FALTA {href}')
                href = ''
        elif href:
            target_ok = True  # externo: dejar
        caption = collapse(img.attrs.get('alt', '')).strip()
        if not caption and href:
            caption = posixpath.basename(href).rsplit('.', 1)[0].replace('_', ' ')
        if not caption:
            caption = ''
        fig = figure_html(page, img, lazy=True)
        if href and target_ok and not link_prohibido(href):
            items.append(f'<a href="{esc(href)}">{fig}</a>')
        else:
            items.append(fig)
    grid = '<div class="secuencia">\n' + '\n'.join(items) + '\n</div>' if items else ''
    if not items:
        # índice de índices (fotos.html): lista de links a las galerías
        lis, seen_h = [], set()
        for a in find_all(body, 'a'):
            href = (a.attrs.get('href') or '').strip()
            if not href or href in seen_h or href.lower().startswith(('http', 'mailto', 'javascript', '#')):
                continue
            target = (page.path.parent / posixpath.normpath(href))
            if target.name not in index_names or target.name == page.name or not target.exists():
                continue
            seen_h.add(href)
            if link_prohibido(href):
                continue
            label = orto_fix(collapse(get_text(a)) or target.stem)
            lis.append(f'<li><a href="{esc(href)}">{esc(label)}</a></li>')
        if lis:
            page.note('INDICE_DE_INDICES')
            grid = '<ul class="indice">\n' + '\n'.join(lis) + '\n</ul>'
        else:
            page.note('INDEX_VACIO')
    return page_main(page, grid)


def page_main(page, inner, vuelta_href=None, vuelta_label=BACK_LABEL):
    if vuelta_href is None:
        vuelta_href = f'{page.rel}index.html'
    pares = []
    vistos = set()
    for label, href in getattr(page, 'subnav', []):
        clave = (href, label)
        if clave in vistos:
            continue
        vistos.add(clave)
        if href:
            pares.append(f'<a href="{esc(href)}">{esc(label)}</a>')
        else:
            pares.append(f'<span class="sin-destino">{esc(label)}</span>')
    subnav = f'<nav class="subnav" aria-label="Subsecciones">{" · ".join(pares)}</nav>\n' if pares else ''
    return (f'<main id="contenido" class="pagina">\n'
            f'<h2 class="pagina-titulo">{esc(page.title or page.name)}</h2>\n'
            f'{subnav}'
            f'<div class="cuerpo">\n{inner}\n</div>\n'
            f'<p class="vuelta"><a href="{esc(vuelta_href)}">← {esc(vuelta_label)}</a></p>\n</main>')


# ---------------------------------------------------------------- reverse links

def collect_refs(pages):
    refs = {}  # Path absoluto del target -> [nombres de páginas que enlazan]
    for p in pages:
        if p.converted or not p.tree:
            continue
        base = p.path.parent
        for a in find_all(find_body(p.tree), 'a'):
            href = (a.attrs.get('href') or '').strip()
            if not href or href.lower().startswith(('http', 'mailto', 'javascript', '#')):
                continue
            refs.setdefault((base / posixpath.normpath(href)), []).append(p.name)
    return refs


def parent_of(page, refs, index_names):
    for c in refs.get(page.path, []):
        if c in index_names:
            return c
    return 'fotos.html'


# ---------------------------------------------------------------- plantilla

REVEAL_JS = """(function(){
  var laminas=[].slice.call(document.querySelectorAll('.lamina'));
  function mostrar(){laminas.forEach(function(o){o.classList.remove('pre');});}
  if(!('IntersectionObserver'in window))return;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  laminas.forEach(function(o){o.classList.add('pre');});
  setTimeout(mostrar,3000); /* failsafe: nada queda oculto */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){e.target.classList.remove('pre');io.unobserve(e.target);}
    });
  },{threshold:.1});
  laminas.forEach(function(o){io.observe(o);});
})();"""


ESTACIONES = (
    ('inicio', 'Inicio', ''),
    ('presentacion', 'Presentación', 'presentacion.html'),
    ('que_es_karate', 'Qué es Karate', 'que_es_karate.html'),
    ('historia', 'Historia', 'sintesis_historica.html'),
    ('centro_de_ensenanza', 'Centro de Enseñanza', 'centro_de_ensenanza.html'),
    ('horarios', 'Horarios', 'horarios.html'),
    ('como_llegar', 'Cómo llegar', 'como_llegar.html'),
    ('contacto', 'Contacto', 'contacto.html'),
)

BUCKETS_ACTIVOS = (
    ('fotos', ('fotos',)),
    ('noticias', ('noticia', 'naciona', 'internacional', 'novedades')),
    ('que_es_karate', ('que_es', 'nino', 'mujer', 'acond', 'deportivo', 'tradicional', 'credo')),
    ('historia', ('sintesis', 'arbol', 'biografia', 'familia', 'okinawa', 'hombu', 'afiches')),
)


def estacion_activa(page, index_names):
    n = page.name
    if n == 'index.html':
        return 'inicio'
    for key, _label, archivo in ESTACIONES[1:]:
        if n == archivo:
            return key
    for key, prefijos in BUCKETS_ACTIVOS:
        if n.startswith(prefijos):
            return key
    if page.archetype in ('hoja', 'index'):
        return 'fotos'
    return 'presentacion'


def template(page, main_html, html_dir_prefix, activa='inicio'):
    r = page.rel                      # '' en src/ o '../' en html/
    p = html_dir_prefix               # '' en html/ o 'html/' en src/
    title = f'{page.title} — Kyudokan Campana' if page.title else 'Kyudokan Campana'
    lis = []
    for key, label, archivo in ESTACIONES:
        href = f'{r}index.html' if key == 'inicio' else f'{p}{archivo}'
        corriente = ' aria-current="page"' if key == activa else ''
        lis.append(f'    <a href="{href}"{corriente}>{esc(label)}</a>')
    riel = '\n'.join(lis)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="generator" content="{MARKER}">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{r}assets/fonts/shippori-mincho-600.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{r}assets/fonts/zen-kaku-400.woff2">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{r}assets/favicon/favicon-16x16.png">
<link rel="apple-touch-icon" href="{r}assets/favicon/apple-touch-icon.png">
<link rel="stylesheet" href="{r}gusuku.css">
</head>
<body>

<a class="skip" href="#contenido">Saltar al contenido</a>

<header class="masthead">
  <div class="masthead-inner">
    <img class="crest" src="{r}assets/marca/kyudokan-crest.png" alt="Kyudokan">
    <div class="titular">
      <p class="sobre">Karate Dojo Campana - Centro de enseñanza de Karate Do y Kobudo</p>
      <h1>Okinawa Shorin-Ryu Karate-Do Kyudokan Federation Argentina</h1>
      <p class="ficha">Sensei Cristian Lugani (8° Dan Kyoshi) - Campana - Bs. As. - Argentina</p>
    </div>
  </div>
</header>

<nav class="riel" aria-label="Secciones">
  <div class="riel-inner">
{riel}
  </div>
</nav>

{main_html}

<footer>
  <div class="olas" aria-hidden="true"></div>
  <div class="sitemap">
    <nav class="sitemap-col" aria-label="El dojo">
      <h2>El dojo</h2>
      <a href="{r}index.html">Inicio</a>
      <a href="{p}presentacion.html">Presentación</a>
      <a href="{p}centro_de_ensenanza.html">Centro de Enseñanza</a>
      <a href="{p}horarios.html">Horarios</a>
      <a href="{p}como_llegar.html">Como llegar</a>
      <a href="{p}servicios.html">Servicios</a>
      <a href="{p}cupon_de_descuento.html">Cupn de descuento</a>
      <a href="{p}contacto.html">Contacto</a>
    </nav>
    <nav class="sitemap-col" aria-label="Historia y estilo">
      <h2>Historia y estilo</h2>
      <a href="{p}sintesis_historica.html">Síntesis histórica</a>
      <a href="{p}arbol_genealogico.html">Árbol genealógico</a>
      <a href="{p}biograf__jintatsu_higa.html">Jintatsu Higa</a>
      <a href="{p}la_familia_higa.html">La familia Higa</a>
      <a href="{p}okinawa.html">Okinawa</a>
      <a href="{p}escuela_estilo.html">Escuela y estilo</a>
      <a href="{p}katas_esc__kyudokan.html">Katas de la escuela</a>
      <a href="{p}que_es_karate.html">Qu es Karate</a>
      <a href="{p}karate_deportivo.html">Karate deportivo</a>
      <a href="{p}karate_tradicional.html">Karate tradicional</a>
      <a href="{p}acondicionamiento_fisico.html">Acondicionamiento físico</a>
      <a href="{p}el_karate_y_el_nino.html">El karate y el niño</a>
      <a href="{p}el_karate_y_la_mujer.html">El karate y la mujer</a>
      <a href="{p}credo_del_samurai.html">Credo del samurai</a>
      <a href="{p}ventana_bushido.html">Ventana Bushido</a>
      <a href="{p}pensamiento.html">Pensamiento</a>
    </nav>
    <div class="sitemap-col">
      <h2>El dojo en Campana</h2>
      <p>Jean Jaures 983 · Campana · Bs. As.</p>
      <p>Tel: (54) (03489) 431664</p>
      <p><a href="mailto:cristian@karatelugani.com.ar">cristian@karatelugani.com.ar</a></p>
      <a href="https://www.facebook.com/DojoCampana/">Facebook</a>
      <a href="https://www.instagram.com/karatedojocampana/">Instagram</a>
    </div>
  </div>
  <div class="legal">
    <p>© C. Lugani · Centro de Enseñanza de Karate-do Estilo Shorinryu Kyudokan de Okinawa — Filial Campana</p>
    <p class="fuente">Datos e imágenes: sitio 2001 (karatelugani.com.ar) · Diseño: <a href="https://iyaki.ar">iyaki</a> — horarios y grados a confirmar.</p>
  </div>
</footer>

<script>
{REVEAL_JS}
var _riel=document.querySelector('.riel-inner');
if(_riel){{var _rielFin=function(){{_riel.classList.toggle('fin',_riel.scrollLeft+_riel.clientWidth>=_riel.scrollWidth-4);}};_riel.addEventListener('scroll',_rielFin,{{passive:true}});addEventListener('resize',_rielFin);_rielFin();}}
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- main

def main():
    files = sorted(SRC.glob('html/*.html')) + sorted(SRC.glob('*.shtml'))
    pages = [Page(f) for f in files]
    log = []
    counts = {}

    # clasificación en memoria (las fuentes aún no fueron tocadas)
    for p in pages:
        if p.converted:
            continue
        p.archetype = classify(p.name, p.tree)
        counts[p.archetype] = counts.get(p.archetype, 0) + 1

    index_names = {p.name for p in pages if p.archetype == 'index'}
    refs = collect_refs(pages)

    for p in pages:
        if p.converted:
            log.append(f'SKIP {p.name} (ya convertida)')
            continue
        foms = fom_map(p.raw)
        try:
            if p.archetype == 'hoja':
                main_html = hoja_emit(p, refs, index_names)
            elif p.archetype == 'index':
                main_html = index_emit(p, foms, index_names)
            else:  # articulo / utilitaria
                tds = extract_content_tds(p)
                blocks = content_blocks(p, tds, foms) if tds else []
                if not blocks and not getattr(p, 'subnav', []):
                    p.note('NEEDS_REVIEW sin contenido')
                    blocks = [f'<p>Esta página del sitio 2001 no tiene contenido en la copia local. '
                              f'<a href="{p.rel}index.html">Volver al inicio.</a></p>']
                main_html = page_main(p, '\n'.join(blocks))
        except Exception as e:  # nunca dejar una página a medias
            p.note(f'ERROR {type(e).__name__}: {e}')
            main_html = page_main(p, f'<p>Esta página no pudo convertirse ({esc(str(e))}). '
                                     f'<a href="{p.rel}index.html">Volver al inicio.</a></p>')
            p.archetype = 'error'

        html_dir_prefix = '' if p.rel == '../' else 'html/'
        out = template(p, main_html, html_dir_prefix, estacion_activa(p, index_names))
        p.path.write_text(out, encoding='utf-8')
        notes = (' | ' + ' | '.join(p.log_notes)) if p.log_notes else ''
        log.append(f'OK {p.name} arch={p.archetype} imgs={p.imgs_ok} faltan={p.imgs_missing}{notes}')

    resumen = ['---', f'páginas: {len(pages)}', 'arquetipos: ' +
               ', '.join(f'{k}={v}' for k, v in sorted(counts.items())),
               f'NEEDS_REVIEW: {sum(1 for l in log if "NEEDS_REVIEW" in l)}',
               f'errores: {sum(1 for l in log if "arch=error" in l)}']
    LOG_PATH.write_text('\n'.join(log + resumen) + '\n', encoding='utf-8')
    print('\n'.join(resumen))


if __name__ == '__main__':
    main()
