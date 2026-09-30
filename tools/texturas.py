#!/usr/bin/env python3
"""Texturas de madera para el mundo shomen (kyudokan-v3).

Genera maderas sin costuras a partir de ruido de valor con lattice envolvente:
- pared.jpg  — tablones de nogal oscuro para el fondo general
- nicho.jpg  — fondo del tokonoma (más profundo, veta más larga)
- noble.jpg  — tokobashira (postes, veta densa vertical)
- piso.jpg   — piso elevado del tokonoma (veta horizontal, más contraste)

Salida: src/assets/texturas/. Determinístico por semilla.
"""
import numpy as np
from PIL import Image
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'src' / 'assets' / 'texturas'


def ruido_envolvente(w, h, freq_x, freq_y, seed, octavas=4):
    """Ruido de valor con lattice que envuelve: tileable en ambos ejes."""
    rng = np.random.default_rng(seed)
    acc = np.zeros((h, w))
    amp_total = 0.0
    amp = 1.0
    for o in range(octavas):
        f = 2 ** o
        gx, gy = freq_x * f, freq_y * f
        lat = rng.random((gy, gx))
        # muestreo envolvente: índices módulo el tamaño del lattice
        yi = (np.arange(h) * gy / h).astype(int)
        xi = (np.arange(w) * gx / w).astype(int)
        fy = (np.arange(h) * gy / h) % 1
        fx = (np.arange(w) * gx / w) % 1
        fy = fy[:, None]
        fx = fx[None, :]
        v00 = lat[yi][:, xi]
        v01 = lat[yi][:, (xi + 1) % gx]
        v10 = lat[(yi + 1) % gy][:, xi]
        v11 = lat[(yi + 1) % gy][:, (xi + 1) % gx]
        # suavizado (smoothstep)
        sx = fx * fx * (3 - 2 * fx)
        sy = fy * fy * (3 - 2 * fy)
        acc += amp * (v00 * (1 - sx) * (1 - sy) + v01 * sx * (1 - sy)
                      + v10 * (1 - sx) * sy + v11 * sx * sy)
        amp_total += amp
        amp *= 0.55
    return acc / amp_total


def madera(freq_x, freq_y, tam, semilla, base, luz, bandas=None, ancho_banda=176, contraste=1.0):
    """Devuelve array float HxW en tono de madera."""
    fibra = ruido_envolvente(tam, tam, freq_x, freq_y, semilla)
    fibra = 0.5 + (fibra - 0.5) * contraste  # afila la veta
    mancha = ruido_envolvente(tam, tam, 2, 2, semilla + 1, octavas=3)
    tono = 0.72 + 0.28 * fibra
    tono *= 0.92 + 0.16 * mancha
    if bandas:
        # tono por tablón con jitter + juntas biseladas
        rng = np.random.default_rng(semilla + 2)
        x = np.arange(tam)
        idx_banda = (x // ancho_banda) % len(bandas)
        factor = np.array(bandas)[idx_banda]
        factor *= 1.0 + 0.03 * ruido_envolvente(1, tam, 1, 6, semilla + 3)[0]
        junta = np.ones(tam)
        for k in range(ancho_banda, tam, ancho_banda):
            junta[k - 1:k + 1] = 0.72   # sombra de la junta
            junta[k + 1:k + 2] = 1.14   # línea de luz del bisel
        tono = tono * factor[None, :] * junta[None, :]
    img = np.zeros((tam, tam, 3))
    for c in range(3):
        img[..., c] = base[c] * tono * luz[c]
    return np.clip(img, 0, 255)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tam = 1024

    # pared: nogal oscuro, veta VERTICAL (freq_x alta), tablones suaves
    pared = madera(96, 4, tam, 11, (72, 52, 33), (1.0, 0.98, 0.94),
                   bandas=[1.0, 0.96, 1.04, 0.98], contraste=1.35)
    Image.fromarray(pared.astype(np.uint8)).save(OUT / 'pared.jpg', quality=86)

    # nicho: fondo del tokonoma — más profundo, veta larga vertical
    nicho = madera(64, 3, tam, 23, (58, 42, 26), (1.02, 0.99, 0.94), contraste=1.25)
    Image.fromarray(nicho.astype(np.uint8)).save(OUT / 'nicho.jpg', quality=86)

    # noble: tokobashira — veta vertical densa con chatoyance
    noble = madera(130, 5, tam, 37, (82, 60, 38), (1.04, 1.0, 0.93), contraste=1.5)
    Image.fromarray(noble.astype(np.uint8)).save(OUT / 'noble.jpg', quality=88)

    # piso: veta HORIZONTAL (freq_y alta), más contraste, tablón pulido
    piso = madera(5, 110, tam, 51, (108, 78, 46), (1.05, 1.0, 0.92), contraste=1.45)
    Image.fromarray(piso.astype(np.uint8)).save(OUT / 'piso.jpg', quality=88)

    print('texturas generadas en', OUT)


if __name__ == '__main__':
    main()
