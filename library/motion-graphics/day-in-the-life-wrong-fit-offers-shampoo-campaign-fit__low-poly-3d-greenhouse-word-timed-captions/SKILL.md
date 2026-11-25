---
name: day-in-the-life-wrong-fit-offers-shampoo-campaign-fit-low-poly-3d-greenhouse-word-timed-captions
description: Part twenty six of the low-poly "day in the life of a UGC creator" reels. In a greenhouse, a bald gardening creator reads today's offers: a shampoo, a stroller (no kids), car wax (he rides a bike). He says yes to the shampoo anyway; they ask him to show the hair. Then YourBrand: he picks his interests once (gardening), every campaign shows whether it fits him, and one that does not fit says so before he applies. So he applies where he fits: seeds, soil, a very nice trowel. The shampoo brand still emails. Still bald. Reach for it when a reel needs the wrong-fit-offers story, offer cards that get stamped, a hat lifted to reveal a shining bald head, interest chips, a "not a fit" warning on a card, or a greenhouse set.
---

# Day in the life, part twenty six: still bald (low-poly 3D)

**Code name:** three.js greenhouse (glass walls on a white frame, potting benches full of pots, hanging baskets, a bike leaning on the glass, hills outside), box-built bald character in a bucket hat, round glasses and an orange apron, offers inbox with stamps / shampoo chat / interests chips / find deals with the fit note / the shampoo brand again on a floating sheet, a seedling, seeds, a soil bag, a trowel, a shampoo bottle and a stroller, hard cuts on voiceover word times. **From:** original build, part 26 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-wrong-fit-offers-shampoo-campaign-fit__low-poly-3d-greenhouse-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.4 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A greenhouse on a grey, rainy morning: potting benches of seedlings, hanging baskets, a bike against the glass. A man in a khaki bucket hat, round glasses and an orange apron works at his potting bench. "Part twenty six."
2. **3.6 to 5.4s.** He holds up a seedling: NICHE: GARDENING.
3. **5.4 to 7.2s.** Today's offers: Silky Shampoo, "for your gorgeous hair".
4. **7.2 to 8.1s.** He lifts his hat: a bald head with a shine on top. HAIR: 0.
5. **8.1 to 12.3s.** Back to the offers, now stamped: BALD. Cozy Stroller, "for your little one": NO KIDS. Mirror Shine Car Wax, "for your ride": BIKE.
6. **12.3 to 16.1s.** The shampoo chat: "Yes! Video attached ▶" · typing… · "Love it!!" · "Can you show the hair?" HAIR: STILL 0.
7. **16.1 to 17.7s.** The chrome monogram; the rain stops and the sky goes blue.
8. **17.7 to 20.2s.** Profile, Interests: ten chips pop in; Gardening turns green with a tick. PICKED ONCE.
9. **20.2 to 24.7s.** Find deals: Green Thumb Seeds (Gardening) and Silky Shampoo (Beauty). Under the shampoo card, in amber: "Not a fit for your profile (interests). You can still apply, but YourBrand may pass." He presses Apply on the seeds card: Applied ✓. CHECKED BEFORE I APPLY.
10. **24.7 to 29.3s.** He holds up a seed packet (FITS: SEEDS), a soil bag lands on the bench (FITS: SOIL), and he raises a trowel that sparkles (FITS: VERY NICE TROWEL).
11. **29.3 to 32.3s.** He swats away a pink shampoo bottle and a stroller: ✕ SHAMPOO, ✕ STROLLERS. Arms crossed: "No bullshit."
12. **32.3 to 35.4s.** Callback: Silky Shampoo again, "Hi again!! :)", "Still loving your hair content.", "New scents dropping!". He lifts the hat once more: STILL BALD.
13. **35.4 to 40.4s.** Black end card: chrome monogram, wordmark, "Deals that fit you. Flagged when they don't.", yourbrand.com.

## How it works
Same structure as parts one to twenty five. New here:

- **The hat** is its own group (`P.hat`) on the head; `hatUp` lifts it up and away and turns on `P.shine`, a small bright box on the crown that flickers. The `head` camera sits high and looks down so the top of the head is in frame.
- **`rstamp(...)`** draws a tilted red outline stamp on an offer card; each card's stamp waits for its own beat, so the BALD stamp (said during the hat shot) is already there when the sheet comes back.
- **The interests page** lays chips out in rows by measuring each label; Gardening pops and fills green on its word.
- **Find deals** shows two campaign cards; the shampoo card gets the amber fit note, the seeds card's Apply turns into "Applied ✓".
- **The greenhouse** is glass panes (low opacity) over a white frame grid, with a sky plane and two low hills outside; the mood flip turns the sky from grey to blue and fades rain into birdsong in the mix.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 40.2 s; the rule gave 1.09, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` lays rain on the glass under the first half and a few birds after the turn, then a pop per offer, a bright shimmer when the bald head is revealed (twice), a rubber stamp per reason, a buzzer on "show the hair", a ripple of pops for the interest chips and a click and ding for Gardening, a two-note "not quite" for the fit note, a ding for Apply, a pop for the seeds, a soft thump for the soil bag, a shimmer for the trowel. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
