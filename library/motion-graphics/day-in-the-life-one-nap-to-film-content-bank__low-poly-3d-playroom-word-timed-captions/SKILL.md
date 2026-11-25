---
name: day-in-the-life-one-nap-to-film-content-bank-low-poly-3d-playroom-word-timed-captions
description: Part thirty one of the low-poly "day in the life of a UGC creator" reels. A mom of two gets one nap, twenty minutes, to film. Take one, the doorbell; take two, the dog; take three, her son walks in holding the product. The brand wants B-roll and a screen recording, the nap is over, and she ends up sitting in the playpen. Then YourBrand: her brief comes with a content bank, the clips and screen recordings ready, so she only films her part: one take, one nap. The brand loved it; they asked if her son is available. Reach for it when a reel needs a parent creator, a playroom or nursery, a crib, a playpen, a clapperboard per take with CUT stamps, a barking dog, a toddler walking into shot, a nap timer, or phone sheets for a brief with a content bank link and a grid of ready clips.
---

# Day in the life, part thirty one: is your son available (low-poly 3D)

**Code name:** three.js playroom (mint walls, a window, a flag garland, a striped round rug, a crib with a baby, a playpen, a toy box, blocks, a teddy, stacking rings), a white desk with a laptop showing a nap timer, a phone on a tiny tripod with a blinking REC dot, a baby monitor, a clapperboard, a box-built dog and a box-built toddler, box-built mum with a bun and a pink cardigan, floating phone sheets, hard cuts on voiceover word times. **From:** original build, part 31 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-one-nap-to-film-content-bank__low-poly-3d-playroom-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.6 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 5.2s.** A playroom on a grey afternoon; a woman at a desk with a phone on a tripod. "Part thirty one." The crib: MOM OF 2.
2. **5.2 to 8.2s.** The laptop's nap timer counting down: 1 NAP, 20 MINUTES.
3. **8.2 to 14.8s.** TAKE 1 on the clapperboard; the doorbell (DING DONG), CUT. TAKE 2; the dog barks into shot (WOOF), CUT. TAKE 3; her toddler walks in and holds up the product (GUEST STAR), CUT.
4. **14.8 to 17.9s.** The brand: "Love the vibe! Can you add B-roll?" and "And a screen recording of the app?" (+ B-ROLL, + SCREEN RECORDING).
5. **17.9 to 19.7s.** The baby sits up crying in the crib; she sits in the playpen hugging her knees: NAP: OVER.
6. **19.7 to 21.6s.** She looks up; the chrome monogram on the laptop; warm sun in the window.
7. **21.6 to 26.1s.** The campaign brief and its link, "Your content bank: the clips and screen recordings for your videos" (CONTENT BANK). The bank: six clips (product close-up, app screen recording, B-roll), Ready to use ✓ (B-ROLL: READY, SCREEN REC: READY).
8. **26.1 to 29.4s.** TAKE 1, she films her part: MY PART ONLY, 1 TAKE, 1 NAP, THAT'S A WRAP.
9. **29.4 to 32.4s.** She swats away a brass doorbell (✕ DOORBELL) and a film strip (✕ B-ROLL), then crosses her arms: "No bullshit."
10. **32.4 to 35.6s.** The brand: "Loved it!!", "Is your son available?" Her toddler in sunglasses with the product: NEW TALENT.
11. **35.6 to 40.6s.** Black end card: chrome monogram, wordmark, "The clips are ready. You film your part.", yourbrand.com.

## How it works
Same structure as parts one to thirty. New here:

- **The clapperboard** (`clap`, hinged `clapTop`) is redrawn only when the take number changes (`drawClap`), snaps on each take beat and pops out; `cut()` puts the CUT stamp and a shake on each interruption.
- **The toddler** (`kid`) is a separate small rig: a body, a head with its own mouth and sunglasses, two arm groups; the product bottle rides on the right arm, which swings up on "product". The **dog** bounces and its jaw opens and shuts.
- **The baby** in the crib lies down until the nap is over, then sits up with the mouth opening and closing; the baby monitor's light blinks red.
- **The playpen low point:** the `PEN` pose sits her on the floor inside the pen, knees up, arms round them.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), take 1 of 2 (raw 41.8 s), sped 1.13x. `code/recipe.py` ticks the nap timer twice a second until the nap is over, snaps the clapperboard on each take, rings a two-note doorbell, barks three times, stamps each CUT, pops the brand's messages, cries for the baby, then the reveal chord, a ding for the content bank, pops as the clips land, dings for ready, one take and one nap, swats, pops for the replies and a ding for new talent. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
