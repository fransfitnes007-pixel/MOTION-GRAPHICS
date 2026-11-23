---
name: brand-setup
description: "White-label the whole kit for a brand in one pass: name, domain, handle, colours, logo, app icon, App Store card and voice, then apply a palette to a piece. Use first on a fresh clone, or when the user says \"make this ours\", \"rebrand\", \"use our colours\" or \"use the sunset palette\"."
---

# Brand setup

`KIT` = the repository root.

## 1. Fill in the brand
Edit `KIT/brand.config.json`: `name`, `name_upper`, `slug`, `domain`, `handle`, `tagline`, `colors`, and under `app_store` the listing details and a path to the real app icon (a square PNG in `KIT/assets/`). Take facts like ratings from the live store page that day, and write the date in the hand-off notes. Never invent ratings or reviews.

## 2. Apply it
```bash
pip install pillow numpy scipy   # once
python3 KIT/engine/tools/apply_brand.py --dry-run   # see what will change
python3 KIT/engine/tools/apply_brand.py
python3 KIT/engine/tools/build_index.py
```
It swaps the brand words in every library piece and pipeline (it remembers the last values, so it can be run again after a rename), renders a liquid-chrome monogram and wordmark into each `brand-assets.js`, and writes the pictogram reel's `assets/brand.js` (name, handle, App Store card, icon). For a different chrome logo font set `fonts.logo_ttf`. To make a chrome logo on its own:
```bash
python3 KIT/engine/tools/chrome_text.py <font.ttf> out/ "yourbrand.com"
```

## 3. Palettes
`KIT/palettes/PALETTES.md` names the signature looks (`arizona-sunset`, `pictogram-mono`, `dark-ember`, `gold-book`, `violet-ai`, `chrome-cobalt`, `rainbow-led`, `light-studio`, `cursor-yellow`). `palettes.json` also has the colours of every library piece. To apply one: open the piece's `code/demo.html`, find its `CONFIG` or colour constants, and swap them for the palette's values, keeping light/dark contrast the same (text on the darkest colour, accents used once per frame). Render a still to check.

## 4. Voice
Set `voice.male`, `voice.female` and `voice.syllables_per_second` in the config, matching keys in `KIT/pipelines/voice/voices/voices.json`.

## 5. Check
`grep -ri "yourbrand" KIT/library KIT/pipelines` shows anything still on the placeholder. Render one still of a branded piece and look at it.
