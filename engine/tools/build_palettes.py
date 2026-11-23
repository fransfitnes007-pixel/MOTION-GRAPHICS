#!/usr/bin/env python3
"""Rebuild palettes/palettes.json (by_piece), palettes/index.html and the swatch list in PALETTES.md from the library demos.
The hand-named signature palettes in palettes.json are kept.  Usage: python3 engine/tools/build_palettes.py"""
import collections, glob, html, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PJ = os.path.join(ROOT, "palettes", "palettes.json")
P = json.load(open(PJ)) if os.path.exists(PJ) else {"signature": []}
out = []
for f in sorted(glob.glob(os.path.join(ROOT, "library", "*", "*", "code", "demo.html"))):
    d = os.path.relpath(f, os.path.join(ROOT, "library")).split("/code/")[0]; m = json.load(open(os.path.join(ROOT, "library", d, "meta.json")))
    t = re.sub(r"data:[^'\"]+", "", open(f, errors="ignore").read())
    hx = [h.upper() if len(h) == 7 else ("#" + "".join(c * 2 for c in h[1:])).upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b(?![0-9a-fA-F])", t)]
    rgb = ["#%02X%02X%02X" % tuple(map(int, x)) for x in re.findall(r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})", t) if all(int(v) < 256 for v in x)]
    c = collections.Counter(hx + rgb)
    if c: out.append({"piece": d, "name": m["visual_name"], "tags": m.get("tags", []), "colors": [k for k, _ in c.most_common(10)]})
P["by_piece"] = out; json.dump(P, open(PJ, "w"), indent=1)
sw = lambda cs: "".join(f'<span class="s" style="background:{c}" title="{c}"></span>' for c in cs)
def flat(s):
    if isinstance(s.get("colors"), list): return s["colors"]
    o = [c for k in ("sky", "dusk", "floor", "sun") for c in s.get(k, [])]
    for v in (s.get("colors") or {}).values(): o += v if isinstance(v, list) else [v]
    return [c for c in o if c.startswith("#")]
rows = "".join(f'<section><h2>{html.escape(s["name"])} <code>{s["id"]}</code></h2><p>{html.escape(s["use"])}</p><div>{sw(flat(s))}</div><p class="h">{" ".join(flat(s))}</p></section>' for s in P["signature"])
pieces = "".join(f'<div class="p"><div>{sw(p["colors"][:8])}</div><a href="../library/{p["piece"]}/code/demo.html">{html.escape(p["name"])}</a></div>' for p in out)
open(os.path.join(ROOT, "palettes", "index.html"), "w").write(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Palettes</title>
<style>body{{margin:0;padding:24px;background:#0d0d10;color:#f2f2f5;font:15px/1.5 system-ui,-apple-system,sans-serif}}h1{{margin:0 0 6px}}h2{{font-size:18px;margin:28px 0 4px}}code{{color:#9a9aa6;font-size:13px}}p{{color:#c9c9d1;margin:4px 0 8px;max-width:70ch}}.h{{font:12px ui-monospace,monospace;color:#8e8e98}}
.s{{display:inline-block;width:44px;height:44px;border-radius:8px;margin:0 6px 6px 0;border:1px solid #2a2a32}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:12px}}.p .s{{width:28px;height:28px;border-radius:6px;margin-right:4px}}.p a{{color:#9db8ff;text-decoration:none;font-size:13px}}</style></head>
<body><h1>Palettes</h1><p>Signature looks first, then the colours each library piece uses, most used first. Hover a swatch for its hex. Data: <code>palettes.json</code>.</p>{rows}<h2>Every piece</h2><div class="grid">{pieces}</div></body></html>""")
md = os.path.join(ROOT, "palettes", "PALETTES.md"); t = open(md).read()
t = re.sub(r"plus the colours of all \d+ library pieces", f"plus the colours of all {len(out)} library pieces", t); open(md, "w").write(t)
print(len(out), "pieces,", len(P["signature"]), "signature palettes")
