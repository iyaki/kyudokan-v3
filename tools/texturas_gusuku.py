#!/usr/bin/env python3
"""Texturas del mundo gusuku (kyudokan-v3): encalado de coral.

Genera el revoque calizo de los muros, tileable en ambos ejes:
- encalado.jpg — pared encalada cálida (grano fino + manchas de llana + poros de coral)
- muro.jpg     — el mismo revoque, más oscuro y poroso, para el panel del linaje

Salida: src/assets/texturas/. Determinístico por semilla.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from texturas import ruido_envolvente

OUT = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'texturas'


def revoque(tam, seed, base, amplitud, porosidad, oscuridad):
    """Revoque encalado tileable: grano + manchas de llana + poros con wrap."""
    grano = ruido_envolvente(tam, tam, 7, 7, seed, octavas=4)
    mancha = ruido_envolvente(tam, tam, 2, 2, seed + 1, octavas=3)
    tono = 1.0 + (grano - 0.5) * amplitud + (mancha - 0.5) * amplitud * 2.2
    img = np.zeros((tam, tam, 3))
    for c in range(3):
        img[..., c] = base[c] * tono

    # poros de coral: puntos oscuros dispersos, respetando el wrap para tiling
    rng = np.random.default_rng(seed + 2)
    yy, xx = np.mgrid[0:tam, 0:tam]
    n = int(tam * tam * porosidad)
    for y, x, r, p in zip(rng.integers(0, tam, n), rng.integers(0, tam, n),
                          rng.integers(1, 3, n), rng.uniform(0.05, oscuridad, n)):
        dy = np.minimum(np.abs(yy - y), tam - np.abs(yy - y)) ** 2
        dx = np.minimum(np.abs(xx - x), tam - np.abs(xx - x)) ** 2
        img[dy + dx <= r * r] *= 1 - p
    return np.clip(img, 0, 255)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for nombre, args in {
        'encalado.jpg': ((512, 7, (233, 225, 208), 0.10, 0.0011, 0.14)),
        'muro.jpg': ((512, 17, (219, 209, 190), 0.10, 0.0016, 0.16)),
    }.items():
        Image.fromarray(revoque(*args).astype(np.uint8)).save(OUT / nombre, quality=82)
        print('generado', OUT / nombre)


if __name__ == '__main__':
    main()
