#!/usr/bin/env python3
"""Tile every t-*.png still from `render_demo.cjs still` into one labelled sheet.jpg, so one image shows the whole video.
Usage: sheet.py <stills dir> <columns>      then look at <stills dir>/sheet.jpg"""
import glob, os, sys
from PIL import Image, ImageDraw

d, cols = sys.argv[1], int(sys.argv[2])
fs = sorted(glob.glob(d + '/t-*.png'), key=lambda f: float(os.path.basename(f)[2:-4]))
if not fs:
    sys.exit('no t-*.png in ' + d)
first = Image.open(fs[0]); w = 270; h = round(first.height * w / first.width)
rows = (len(fs) + cols - 1) // cols
S = Image.new('RGB', (cols * w, rows * (h + 24)), 'black'); dr = ImageDraw.Draw(S)
for i, f in enumerate(fs):
    x, y = (i % cols) * w, (i // cols) * (h + 24)
    S.paste(Image.open(f).convert('RGB').resize((w, h)), (x, y + 24))
    dr.text((x + 6, y + 4), os.path.basename(f), fill='yellow')
S.save(d + '/sheet.jpg', quality=85); print(d + '/sheet.jpg')
