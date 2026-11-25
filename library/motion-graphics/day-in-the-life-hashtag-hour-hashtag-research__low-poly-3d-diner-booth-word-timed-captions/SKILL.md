---
name: day-in-the-life-hashtag-hour-hashtag-research-low-poly-3d-diner-booth-word-timed-captions
description: Part twelve of the low-poly "day in the life of a UGC creator" reels. In a late-night diner booth the video took ten minutes and the hashtags took an hour: one guru says thirty, one says three, one says hashtags are dead; he typed FYP four ways and one is banned; his pancakes went cold. Then YourBrand's Hashtag Research: type the niche, fifteen tags in broad, niche and micro buckets, each with a reason, the campaign's tags on top, Copy all. This time he ate the pancakes. Reach for it when a reel needs the hashtag story, contradicting guru cards, a wall of tag chips, or a food prop that freezes and gets eaten.
---

# Day in the life, part twelve: the hashtag hour (low-poly 3D)

**Code name:** three.js diner at night with a flickering neon sign, box-built character, a pancake stack that frosts over and is later an empty plate, guru cards / Hashtag Research results on a floating sheet, a caption box full of tag chips on a floating phone, hard cuts on voiceover word times. **From:** original build, part 12 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-hashtag-hour-hashtag-research__low-poly-3d-diner-booth-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 39 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.5s.** A diner at night: checkered floor, red booth, pink DINER neon that flickers, stars in the window. He works at the booth table next to a stack of pancakes. "Part twelve."
2. **3.5 to 5.3s.** Arm in the air: VIDEO: 10 MIN.
3. **5.3 to 7.2s.** The caption box of a new post (a 0:09 video): tag chips fill it while an "editing" clock runs to 1:00:00. HASHTAGS: 1 HOUR.
4. **7.2 to 11.8s.** Three guru cards, one per line: "USE 30 HASHTAGS.", "ONLY USE 3.", "HASHTAGS ARE DEAD." All three shake.
5. **11.8 to 16.3s.** Back in the caption box: #fyp, #FYP, #foryou, #foryoupage light up yellow one by one; the fourth turns red and is struck through. 1 OF 4: BANNED.
6. **16.3 to 18.1s.** The pancakes, close: a cap of frost and icicles forms. PANCAKES: COLD.
7. **18.1 to 19.8s.** The chrome monogram; the pendant lamp warms the room.
8. **19.8 to 20.9s.** His point of view of the laptop: Hashtag Research, Niche: "home coffee", Research.
9. **20.9 to 27.7s.** The results page: fifteen grey chips pop in (15 TAGS); BROAD turns blue, NICHE purple, MICRO green on their words; a WHY line appears ("Community tags your target viewers actually browse."); a yellow REQUIRED BY THE CAMPAIGN row drops in on top.
10. **27.7 to 29.1s.** He presses a key: COPIED · 15 TAGS.
11. **29.1 to 32.2s.** He swats away a megaphone and a big blue "#": ✕ GURUS, ✕ HASHTAG HOUR. Arms crossed: "No bullshit."
12. **32.2 to 34s.** Callback: the plate, empty, a fork, crumbs and a smear of syrup. PANCAKES: EATEN.
13. **34 to 39s.** Black end card: chrome monogram, wordmark, "Type your niche. Copy all fifteen.", yourbrand.com.

## How it works
Same structure as parts one to eleven. New here:

- **`chips(x, list, X, Y, maxW, font, hgt, gap, fn)`** lays out pill-shaped tags left to right with wrapping; `fn(i, s)` returns `[background, text colour, alpha, scale, struck]` per chip. It draws the caption wall, the four FYPs, the banned tag and all three result buckets.
- **The pancakes** are a `plate` group on the table: `stack` (three discs, butter, syrup), `frost` (an ice cap and icicle cones, scaled in at `T.coldHit`), and `crumbs` with a `fork`, shown from `T.ate`. The `plate` camera looks down at it.
- **`drawSign(t)`** redraws the neon each frame; it flickers until YourBrand and is steady after.
- **Pages:** `drawPhone` the caption box; `drawDoc` 0 the three guru cards, 1 the Hashtag Research results; the laptop shows the tool's form in the point-of-view shot.
- **Props for the finale:** `mega` (megaphone) and `hashP` (a "#" from four bars).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 38.8 s; the rule gave 1.05, raised to the 1.1 floor), take 1 of 2. Write "F Y P" with spaces so it is read as letters. `code/recipe.py` adds a low diner hum under the first half, typing clicks for the tag wall, a pop and a note per guru (the third one low, with a buzzer), four pops for the FYPs, a buzzer on the ban, frost crackle, fifteen quick pops for the results, a ding per bucket, a key click and two dings for the copy, a fork on a plate. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
