---
name: day-in-the-life-series
description: "Make the next part of the low-poly 3D \"Day in the Life of a UGC Creator\" reel series end to end: a new creator and pain point, the product with one real feature at the midpoint, a callback ending, about 40 s at 1080x1920 with word-timed captions and synthesised sound. Use when the user says \"go\" for the series, asks for the next part, or wants a day-in-the-life reel for a creator product."
---

# Day in the Life series

`KIT` is the repository root, two folders up from this skill. `P` is `KIT/pipelines/day-in-the-life`.

1. Read `P/PLAYBOOK.md` (rules and build steps) once per session and `P/SCENE-KIT.md` before writing code.
2. Read `P/EPISODE-LOG.md` before choosing: creator, setting, pain point, gags and payoff must not repeat the
   "already used" lists. Odd parts use voice A (a woman), even parts voice B (a man).
3. Check the feature exists in the product before scripting it. No prices, results or view counts for the product;
   views as bars; no real brands, platforms or people. If `KIT/brand.config.json` still says `YourBrand`, run the
   `brand-setup` skill first.
4. Build from the last part: copy its shared files, write `middle.js` and `spec.json`, assemble with `P/tools/fill.py`,
   check stills with `P/tools/sheet.py`, then `P/tools/mux.sh` and look at both frame sheets.
5. Log the part in `P/EPISODE-LOG.md`, write its `SKILL.md` and `meta.json`, rebuild the index once.
6. Report what happens in it, what the owner may want changed, whether anyone has listened to the mix, and end with
   `Say "go" for Part N+1.`

The 50 finished parts are runnable examples: `python3 KIT/engine/tools/find_skill.py day in the life` or
`library/motion-graphics/day-in-the-life-*`.
