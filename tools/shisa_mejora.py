#!/usr/bin/env python3
"""Mejora de los shisa GIF 2001 (kyudokan-v3).

Toma los GIFs de 43x68, los escala 6x con Lanczos, cuantiza la paleta
(aplana el ruido del escalado en regiones de color limpias: look
ilustrado), realza color/contraste y recorta el fondo gris con flood
fill desde los bordes. Salida: PNG 6x con transparencia.
"""
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

OUT = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'marca'
ESCALA = 6


def recortar_fondo(im):
    """Flood fill desde los bordes: fondo conectado -> transparente."""
    a = np.array(im.convert('RGBA'))
    h, w = a.shape[:2]
    fondo = a[0, 0, :3].astype(int)
    cand = np.abs(a[..., :3].astype(int) - fondo).sum(axis=2) < 60
    fuera = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if cand[y, x] and not fuera[y, x]:
                fuera[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if cand[y, x] and not fuera[y, x]:
                fuera[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and cand[ny, nx] and not fuera[ny, nx]:
                fuera[ny, nx] = True
                q.append((ny, nx))
    a[fuera, 3] = 0
    return Image.fromarray(a)


def mejorar(src, dst):
    im = Image.open(src).convert('RGB')
    im = im.resize((im.width * ESCALA, im.height * ESCALA), Image.LANCZOS)
    # cuantizar a paleta plana: aplana el ruido del escalado (look ilustrado)
    im = im.quantize(colors=10, method=Image.MEDIANCUT).convert('RGB')
    im = ImageEnhance.Color(im).enhance(1.18)
    im = ImageEnhance.Contrast(im).enhance(1.10)
    im = im.filter(ImageFilter.MedianFilter(5))
    rgba = recortar_fondo(im)
    rgba.save(dst)
    print(dst, rgba.size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    leg = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'images'
    mejorar(leg / 'leon_izquierda.gif', OUT / 'shisa-izq.png')
    mejorar(leg / 'leon_derecha.gif', OUT / 'shisa-der.png')


if __name__ == '__main__':
    main()
