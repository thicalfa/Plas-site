#!/usr/bin/env python3
"""Gera, a partir da foto original, (1) a foto recortada sem margem branca e
(2) um "desenho técnico": as arestas do produto em azul sobre fundo transparente.
Uso: blueprint.py ORIGINAL SAIDA_BASE LARGURA [LARGURA...]
Gera SAIDA_BASE-foto-<w>.webp e SAIDA_BASE-desenho-<w>.webp (os originais não são alterados)."""
import sys
import numpy as np
from PIL import Image, ImageChops, ImageFilter

src, base, widths = sys.argv[1], sys.argv[2], [int(w) for w in sys.argv[3:]]
im = Image.open(src).convert("RGB")
diff = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).convert("L").point(lambda x: 255 if x > 18 else 0)
im = im.crop(diff.getbbox())
work = im.copy()
work.thumbnail((1600, 1600))
a = np.asarray(work.filter(ImageFilter.GaussianBlur(1.2))).astype(float)


def sobel(c):
    gx = np.zeros_like(c); gy = np.zeros_like(c)
    gx[1:-1, 1:-1] = (c[:-2, 2:] + 2 * c[1:-1, 2:] + c[2:, 2:]) - (c[:-2, :-2] + 2 * c[1:-1, :-2] + c[2:, :-2])
    gy[1:-1, 1:-1] = (c[2:, :-2] + 2 * c[2:, 1:-1] + c[2:, 2:]) - (c[:-2, :-2] + 2 * c[:-2, 1:-1] + c[:-2, 2:])
    return np.hypot(gx, gy)


m = np.max([sobel(a[..., i]) for i in range(3)], axis=0)
t = np.percentile(m, 86)
v = np.clip((m - t) / (np.percentile(m, 99.5) - t), 0, 1)
v = v ** 1.25
v[v < 0.14] = 0  # remove o "chuvisco" de textura
rgba = np.zeros((*v.shape, 4), np.uint8)
rgba[..., 0], rgba[..., 1], rgba[..., 2], rgba[..., 3] = 31, 95, 168, (v * 255).astype(np.uint8)
draw = Image.fromarray(rgba, "RGBA")
# Fundo transparente na foto: só o branco ligado às bordas (o branco do produto fica).
# Inundação feita com numpy numa versão reduzida (a do Pillow não funcionou aqui).
peq = im.copy(); peq.thumbnail((800, 800))
quase = np.asarray(peq.convert("RGB")).min(axis=2) > 236
fundo = np.zeros_like(quase)
fundo[0, :], fundo[-1, :], fundo[:, 0], fundo[:, -1] = quase[0, :], quase[-1, :], quase[:, 0], quase[:, -1]
while True:
    viz = fundo.copy()
    viz[1:, :] |= fundo[:-1, :]; viz[:-1, :] |= fundo[1:, :]; viz[:, 1:] |= fundo[:, :-1]; viz[:, :-1] |= fundo[:, 1:]
    viz &= quase
    if (viz == fundo).all():
        break
    fundo = viz
alfa = Image.fromarray(np.where(fundo, 0, 255).astype(np.uint8), "L").resize(im.size, Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.2))
foto = im.convert("RGBA")
foto.putalpha(alfa)
for w in widths:
    h = round(work.height * w / work.width)
    foto.resize((w, h), Image.LANCZOS).save(f"{base}-foto-{w}.webp", "WEBP", quality=80, alpha_quality=80, method=6)
    draw.resize((w, h), Image.LANCZOS).save(f"{base}-desenho-{w}.webp", "WEBP", quality=68, alpha_quality=70, method=6)
print(base, work.size)
