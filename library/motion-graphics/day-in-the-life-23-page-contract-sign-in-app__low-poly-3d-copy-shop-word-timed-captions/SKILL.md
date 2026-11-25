---
name: day-in-the-life-23-page-contract-sign-in-app-low-poly-3d-copy-shop-word-timed-captions
description: Part eight of the low-poly "day in the life of a UGC creator" reels. A veteran creator gets a 23-page contract by email: print it, sign it, scan it, send it back. Nobody owns a printer, the copy shop's copier jams, every page needs initials, his thumb is in every scan, then "small change, version two, do it again". Then YourBrand: the agreement is on the campaign page; read it, sign it there, it is countersigned, the brief unlocks, the signed PDF is his. Reach for it when a reel needs the contract or paperwork story, a copier gag, or a signature that draws itself.
---

# Day in the life, part eight: twenty three pages (low-poly 3D)

**Code name:** three.js copy shop and box-built character, a copier that spits and jams sheets, contract / initials / scan / agreement pages on a floating phone and sheet, hard cuts on voiceover word times. **From:** original build, part 8 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-23-page-contract-sign-in-app__low-poly-3d-copy-shop-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.8 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4s.** A copy shop: red COPY · PRINT sign, shelves of paper reams, blue carpet tiles. He works at a white table. "Part eight. New deal": NEW DEAL, arms up.
2. **4 to 6.8s.** The email with Contract.pdf. The contract itself: CONTENT CREATOR AGREEMENT, Page 1 of 23. 23 PAGES.
3. **6.8 to 9.7s.** His face, flatter with each line, under a card of four red chores: Print it, Sign it, Scan it, Send it back.
4. **9.7 to 10.9s.** "Nobody owns a printer": PRINTERS OWNED: 0.
5. **10.9 to 13.9s.** At the copier: sheets fly out in arcs, then the status light blinks red, a crumpled ball sticks in the tray, the machine shudders. PAPER JAM stamp, hand over his face.
6. **13.9 to 16.6s.** The same page with an "initial" box on every clause; scribbles fill them while the header races to Page 23 of 23. INITIALS 23 / 23.
7. **16.6 to 19.8s.** The phone as a scanner: flash, then a thumb slides over the page. Three thumbnails, a thumb in each. THUMB: IN ALL 23.
8. **19.8 to 22.5s.** "Small change!" Contract_v2.pdf, 23 pages, "one comma moved :)". DO IT AGAIN stamp.
9. **22.5 to 24s.** The chrome monogram; warm light through the shop window.
10. **24 to 31.4s.** A dark My campaign page. The Agreement card: a highlight runs down the text (read), a white signature draws itself in the box (sign), the button turns to Signed ✓. Three rows land: Countersigned (by YourBrand and the brand), Brief unlocked, Signed PDF.
11. **31.4 to 33.9s.** He swats away a small printer and a flatbed scanner: ✕ PRINTER, ✕ SCANNING. Arms crossed: "No bullshit."
12. **33.9 to 35.8s.** Callback: his mug lands on the stack of 23 pages. COASTER.
13. **35.8 to 40.8s.** Black end card: chrome monogram, wordmark, "Read it. Sign it. Right there.", yourbrand.com.

## How it works
Same structure as parts one to seven. New here:

- **The copier** sits where the tripod stood in earlier parts and is only visible in the `film` camera. Eight sheet meshes follow an arc from the tray and land flat on the floor; at `T.jam` they freeze, `crumple` appears, the status light alternates red, and the body jitters.
- **`scribble(x, X, Y, s, k)`** draws a signature as a polyline revealed by `k`; it is used for the initials, the scanned page and the signature on the agreement.
- **`legal()`** fills a block with grey rules of uneven length, for contract text nobody reads.
- **Pages:** `drawDoc` 0 the contract, 1 the initials page (header counts 1 to 23), 2 YourBrand's campaign page; `drawPhone` 'scan' (viewfinder, thumb, thumbnails) and 'v2' (the brand's chat).
- **Callback props:** `stack` (visible from "small change" on) and `mug`, which drops onto it in the `coaster` close-up.
- Claims follow the app's own wording: read it and sign, YourBrand and the brand countersign, then the brief unlocks, and the signed PDF can be opened. Nothing is said about what the agreement contains.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.173x (raw 43.4 s, aimed at 37 s), take 1 of 2. `code/recipe.py` adds a copier motor and paper whooshes, a crunch and buzzer on the jam, pen scratches for the initials and the signature, shutter clicks for the scan, a ding per row on the campaign page, a small knock when the mug lands. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
