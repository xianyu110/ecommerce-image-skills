#!/usr/bin/env python3
"""Combine images into a grid.  python make_grid.py a.png b.png ... --cols 3 --cell 800 --gap 16 --out grid.png"""
import argparse, math
from PIL import Image, ImageOps

ap = argparse.ArgumentParser()
ap.add_argument("images", nargs="+")
ap.add_argument("--cols", type=int, default=3)
ap.add_argument("--cell", type=int, default=800)
ap.add_argument("--gap", type=int, default=16)
ap.add_argument("--bg", default="#FFFFFF")
ap.add_argument("--out", default="grid.png")
a = ap.parse_args()
rows = math.ceil(len(a.images) / a.cols)
W = a.cols * a.cell + (a.cols + 1) * a.gap
H = rows * a.cell + (rows + 1) * a.gap
canvas = Image.new("RGB", (W, H), a.bg)
for i, p in enumerate(a.images):
    im = ImageOps.fit(Image.open(p).convert("RGB"), (a.cell, a.cell), Image.LANCZOS)
    r, c = divmod(i, a.cols)
    canvas.paste(im, (a.gap + c * (a.cell + a.gap), a.gap + r * (a.cell + a.gap)))
canvas.save(a.out)
print(a.out)
