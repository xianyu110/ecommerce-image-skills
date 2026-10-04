#!/usr/bin/env python3
"""Stitch detail-page screens into one long image at a fixed width (Taobao/Tmall/PDD: 750 px) and export upload slices.

  python stitch_long_image.py screen-1.png screen-2.png ... --width 750 --out detail-750.jpg [--slice 1546]
"""
import argparse, os
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("images", nargs="+")
ap.add_argument("--width", type=int, default=750)
ap.add_argument("--slice", type=int, default=1546, help="max slice height for upload (0 = no slices)")
ap.add_argument("--out", default="detail-750.jpg")
a = ap.parse_args()
ims = []
for p in sorted(a.images):
    im = Image.open(p).convert("RGB")
    ims.append(im.resize((a.width, round(im.height * a.width / im.width)), Image.LANCZOS))
H = sum(i.height for i in ims)
long_img = Image.new("RGB", (a.width, H), "white")
y = 0
for im in ims:
    long_img.paste(im, (0, y)); y += im.height
long_img.save(a.out, quality=88, optimize=True)
print(a.out, f"{a.width}x{H}")
if a.slice:
    d = os.path.splitext(a.out)[0] + "-slices"
    os.makedirs(d, exist_ok=True)
    for n, top in enumerate(range(0, H, a.slice), 1):
        p = os.path.join(d, f"{n:02d}.jpg")
        long_img.crop((0, top, a.width, min(top + a.slice, H))).save(p, quality=88, optimize=True)
        print(p)
