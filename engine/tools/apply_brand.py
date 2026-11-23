#!/usr/bin/env python3
"""Rebrand the whole kit from brand.config.json in one go.
  python3 engine/tools/apply_brand.py            apply the config
  python3 engine/tools/apply_brand.py --dry-run  list what would change
What it does:
 1. Swaps the brand words (name, NAME, slug, domain, handle) in every library piece and pipeline, from whatever was applied
    last time (engine/.brand-applied.json; the first time, the YourBrand placeholders) to the new values.
 2. Writes library brand-assets.js files: a chrome monogram and a chrome wordmark (BRAND_ASSETS.MARK_*, WORD_*).
 3. Writes pipelines/pictogram-reel/build/assets/brand.js: BRAND (name, handle, App Store card) and ICON (your app icon,
    or a generated gradient icon with your first letter).
Needs Python 3.9+, Pillow, numpy, scipy."""
import base64, io, json, os, re, sys, glob
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); from chrome_text import chrome
CFG = json.load(open(os.path.join(ROOT, "brand.config.json"))); DRY = "--dry-run" in sys.argv
STATE = os.path.join(ROOT, "engine", ".brand-applied.json")
DEFAULT = {"name": "YourBrand", "name_upper": "YOURBRAND", "slug": "yourbrand", "domain": "yourbrand.com", "handle": "@yourbrand"}
old = json.load(open(STATE)) if os.path.exists(STATE) else DEFAULT
new = {k: CFG.get(k) or DEFAULT[k] for k in DEFAULT}
TEXT = (".html", ".js", ".py", ".md", ".css", ".json", ".txt")
# 1. words. Longest first so the domain is replaced before the slug inside it.
pairs = sorted(((old[k], new[k]) for k in DEFAULT if old[k] != new[k]), key=lambda p: -len(p[0]))
changed = 0
if pairs:
    for base in ("library", "pipelines", "prompts", "docs"):
        for f in glob.glob(os.path.join(ROOT, base, "**", "*"), recursive=True):
            if not f.endswith(TEXT) or os.path.isdir(f) or f.endswith(("catalog.json", "three.global.js")): continue
            t = open(f, encoding="utf-8", errors="ignore").read(); u = t
            for a, b in pairs: u = re.sub(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])", b, u)
            if u != t:
                changed += 1
                if not DRY: open(f, "w", encoding="utf-8").write(u)
# brand initial used by monogram pieces, marked in code as 'Y'/*brand-initial*/
ini = new["name"][0].upper(); ichanged = 0
for f in glob.glob(os.path.join(ROOT, "library", "*", "*", "code", "demo.html")):
    s = open(f, encoding="utf-8").read(); u = re.sub(r"'[^']'/\*brand-initial\*/", "'" + ini + "'/*brand-initial*/", s)
    if u != s:
        ichanged += 1
        if not DRY: open(f, "w", encoding="utf-8").write(u)
print(("would change" if DRY else "changed"), changed, "files", pairs, "| monogram pieces:", ichanged)
if DRY: sys.exit()
# 2. fonts and logo images
def find_font():
    if CFG.get("fonts", {}).get("logo_ttf"): return os.path.join(ROOT, CFG["fonts"]["logo_ttf"])
    for p in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Helvetica.ttc", "/Library/Fonts/Arial Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"]:
        if os.path.exists(p): return p
    sys.exit("no bold font found: set fonts.logo_ttf in brand.config.json")
font = find_font()
def uri(img, fmt="PNG", maxw=1200):
    if img.size[0] > maxw: img = img.resize((maxw, round(img.size[1] * maxw / img.size[0])), Image.LANCZOS)
    b = io.BytesIO(); img.save(b, fmt, optimize=True); return f"data:image/{fmt.lower()};base64," + base64.b64encode(b.getvalue()).decode()
mark_plain, mark_glow = chrome(font, new["name"][0].upper(), SIZE=600)
word_plain, word_glow = chrome(font, new["domain"], SIZE=500)
assets = {"MARK_DARK": uri(mark_glow, maxw=700), "MARK_LIGHT": uri(mark_plain, maxw=700), "WORD_DARK": uri(word_glow), "WORD_LIGHT": uri(word_plain)}
js = "// Generated from brand.config.json by engine/tools/apply_brand.py. Logos embedded so canvas/WebGL can use them from file://.\nwindow.BRAND_ASSETS=" + json.dumps(assets) + ";\n"
n = 0
for f in glob.glob(os.path.join(ROOT, "library", "*", "*", "code", "brand-assets.js")):
    open(f, "w").write(js); n += 1
print("wrote", n, "brand-assets.js")
# 3. pictogram reel brand.js
st = CFG.get("app_store", {})
icon_path = st.get("icon") and os.path.join(ROOT, st["icon"])
if icon_path and os.path.exists(icon_path): icon = Image.open(icon_path).convert("RGB").resize((640, 640), Image.LANCZOS)
else:
    a, b = [tuple(int(c.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) for c in CFG["colors"].get("icon_gradient", ["#7C5CFF", "#3A7BFF"])]
    icon = Image.new("RGB", (640, 640)); d = ImageDraw.Draw(icon)
    for y in range(640):
        k = y / 639; d.line([(0, y), (640, y)], fill=tuple(round(a[i] + (b[i] - a[i]) * k) for i in range(3)))
    f = ImageFont.truetype(font, 360); ch = new["name"][0].upper(); x0, y0, x1, y1 = f.getbbox(ch)
    d.text((320 - (x0 + x1) / 2, 320 - (y0 + y1) / 2), ch, font=f, fill=(255, 255, 255))
brand = {"name": new["name"], "handle": new["handle"], "domain": new["domain"], "tagline": CFG.get("tagline", ""),
         "store": {"name": st.get("name", [new["name"]]), "sub": st.get("subtitle", ""), "rating": st.get("rating", 5),
                   "cells": [[st.get("ratings_label", "RATINGS"), str(st.get("rating", "")), "stars"], ["CATEGORY", st.get("category_icon", "cap"), st.get("category", "")],
                             ["DEVELOPER", "person", st.get("developer", new["name"])]]}}
out = os.path.join(ROOT, "pipelines", "pictogram-reel", "build", "assets", "brand.js"); os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w").write("// Generated from brand.config.json by engine/tools/apply_brand.py\nconst BRAND=" + json.dumps(brand) + ";\nconst ICON=new Image(); ICON.src='" + uri(icon, "PNG", 640) + "';\n")
print("wrote", os.path.relpath(out, ROOT))
json.dump(new, open(STATE, "w"), indent=1)
