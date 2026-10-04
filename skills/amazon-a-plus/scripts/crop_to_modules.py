#!/usr/bin/env python3
"""Resize + centre-crop an image to exact Amazon A+ module sizes.

  python crop_to_modules.py in.png --module header            # 970x600
  python crop_to_modules.py in.png --size 1464x600 --out premium.jpg
"""
import argparse, os
from PIL import Image, ImageOps

MODULES = {
    "header": (970, 600), "overlay": (970, 300), "logo": (600, 180),
    "tile300": (300, 300), "tile220": (220, 220), "sidebar-main": (300, 400),
    "sidebar": (350, 175), "comparison": (150, 300), "brand-story": (1464, 625),
    "premium": (1464, 600), "premium-mobile": (600, 450),
}

ap = argparse.ArgumentParser()
ap.add_argument("image")
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--module", choices=MODULES)
g.add_argument("--size", help="WxH")
ap.add_argument("--out")
a = ap.parse_args()
w, h = MODULES[a.module] if a.module else map(int, a.size.lower().split("x"))
out = a.out or f"{os.path.splitext(a.image)[0]}-{w}x{h}.jpg"
ImageOps.fit(Image.open(a.image).convert("RGB"), (w, h), Image.LANCZOS).save(out, quality=90, optimize=True)
print(out, f"{os.path.getsize(out)/1024:.0f} KB (A+ limit 2 MB)")
