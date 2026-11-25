---
name: day-in-the-life-job-boards-cover-letter-find-deals-low-poly-3d-post-office-word-timed-captions
description: Part eighteen of the low-poly "day in the life of a UGC creator" reels. In a post office he applies for work every morning on five job boards: a listing with four hundred applicants, one that wants a free sample video, one that wants a cover letter (for a lip balm), one that closed in 2023, one that wants him to pay to apply. Then YourBrand's Find deals: the campaigns open right now, press apply, YourBrand reviews it, and new campaigns are posted there first. He did write the lip balm letter; it was beautiful. Reach for it when a reel needs the job-board story, a run of bad listings, a deal card with an Apply button, or a wax-sealed letter.
---

# Day in the life, part eighteen: a cover letter for a lip balm (low-poly 3D)

**Code name:** three.js post office with a drawn wall of PO boxes, box-built character, five job boards / five listings / Find deals / a parchment letter on a floating sheet, hard cuts on voiceover word times. **From:** original build, part 18 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-job-boards-cover-letter-find-deals__low-poly-3d-post-office-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 37.3 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A post office under strip lights: a wall of numbered brass PO boxes, a blue POST OFFICE sign, a mailbox, parcels, rope posts. He works at the writing counter. "Part eighteen."
2. **3.6 to 5.7s.** He types fast, frowning: EVERY MORNING.
3. **5.7 to 6.9s.** "Job boards": GigBoard, CreatorJobs, UGC Hub, BrandMatch, PitchList, each with a red "new" badge.
4. **6.9 to 9.3s.** Listing 1 of 5: "UGC creator wanted", the applicant count racing to 412, "1 spot".
5. **9.3 to 11s.** Listing 2: "Step 1 of your application: send a custom sample video". UNPAID.
6. **11 to 13.7s.** Listing 3: "Lip balm launch · Required: Cover letter · minimum 500 words", a drawing of the lip balm, then a red FOR A LIP BALM.
7. **13.7 to 15.5s.** Listing 4: "Posted March 2023", a cobweb in the corner, a CLOSED stamp.
8. **15.5 to 17.6s.** Listing 5: "To see this listing: Pay to apply". APPLICATION FEE.
9. **17.6 to 19.3s.** The chrome monogram; the room warms.
10. **19.3 to 20.3s.** His point of view of the laptop: FIND DEALS · Open to apply.
11. **20.3 to 26.4s.** The Find deals page: two campaign cards (Duration, Posts / day, an Apply button); a cursor presses Apply on the first: "Applied ✓", then "In review · YourBrand"; a third card drops in on top with a NEW tag. POSTED HERE FIRST.
12. **26.4 to 29.6s.** He swats away a sealed letter and a big gold coin: ✕ COVER LETTERS, ✕ PAYING TO APPLY. Arms crossed: "No bullshit."
13. **29.6 to 32.3s.** Callback: a parchment in slanted script, "Dear Lip Balm,", six lines of flowing handwriting, "Yours, moisturised,", a tiny lip balm, and a red wax seal with a heart. BEAUTIFUL.
14. **32.3 to 37.3s.** Black end card: chrome monogram, wordmark, "Open campaigns. Press apply.", yourbrand.com.

## How it works
Same structure as parts one to seventeen. New here:

- **`listing(x, i, t)`** draws one of five listings on the same card frame; `state` picks the index from the beat times and re-pops the sheet at each change, so five different pages cost one function. `tag()` inside it draws the red stamp for that listing.
- **The PO box wall** is one canvas (8 rows of 16 numbered doors) on a plane, like the book wall in part thirteen.
- **The letter (`drawDoc` 3):** faux italics come from a canvas shear (`x.transform(1, 0, -0.22, 1, 0, 0)`); the handwriting is six sine-wobbled strokes revealed left to right; the wax seal is a sixteen-point star with a heart.
- **`lipBalm(x, X, Y, s)`** draws the tube; it appears in listing 3 and again on the letter.
- **Props for the finale:** `letP` (a sealed letter) and `coinP` (a coin).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 37.2 s; the rule gave 1.0, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` adds a counter bell at the start, fast typing, a pop per job board, a thud and a buzzer per listing (each slightly worse), a climbing blip for the applicant count, rubber stamps for the lip balm and CLOSED, a click and dings for Apply and "In review", a quill scratching for the letter and a stamp for the wax seal. No music. The mux uses the limiter from part seventeen. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
