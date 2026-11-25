---
name: day-in-the-life-one-line-brief-proven-brief-low-poly-3d-cafe-word-timed-captions
description: Part four of the low-poly "day in the life of a UGC creator" reels. A brand's brief is one line ("make it viral"), with no script, hook, examples or onboarding; he stares at a wall for two hours, gets "just be authentic", guesses, and gets 40 views. Then YourBrand's brief fills in block by block: the hook, the script, the shot list, a demo video, videos that already worked. Reach for it when a reel needs the brief story, a document that fills in on the voice, or a "reference next to mine" card.
---

# Day in the life, part four: the one-line brief (low-poly 3D)

**Code name:** three.js cafe and box-built character, a floating page drawn on a canvas that scrolls block by block, hard cuts on voiceover word times, 2D canvas for captions, pills and the match card. **From:** original build, part 4 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-one-line-brief-proven-brief__low-poly-3d-cafe-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.7 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4s.** A brick cafe on a grey afternoon: counter, chalkboard menu, hanging bulbs. He works at a table. "Part four." ✓ NEW CAMPAIGN, arms up.
2. **4 to 7.6s.** He opens the brief. A white page: "Campaign brief", then "make it viral" is typed, then "(end of brief)". THE WHOLE BRIEF: 1 LINE.
3. **7.6 to 11.7s.** His face, flatter with each line: ✕ SCRIPT, ✕ HOOK, ✕ EXAMPLES, ✕ ONBOARDING. The page again, now empty: "Nothing."
4. **11.7 to 14.8s.** From behind him: a blank wall and a clock. The hands spin, the light flickers, coffee cups pile up: 2 HOURS LATER.
5. **14.8 to 17.6s.** The chat: three of his questions, then "just be authentic".
6. **17.6 to 21.9s.** He shrugs under a floating question mark. His post counts up to 40 views, red 40 VIEWS stamp. "I'm cooked": face down on the table, from above.
7. **21.9 to 23.5s.** The laptop glows, the sun comes out, the chrome monogram spins in.
8. **23.5 to 30.9s.** A dark YourBrand page, "Your brief · Video 1". Five blocks land on their words, each with a green tick and a white outline while it is being named, and the page scrolls to keep the current one above the caption: the hook (a quoted line), the script (three numbered lines), the shot list (three timecodes), a demo video (a play tile), videos that already worked (three tiles tagged "worked ✓"). "Down to the detail": the camera pushes into the shot list and its timecodes turn green one by one.
9. **30.9 to 33.1s.** He films with confidence under a card: THE VIDEO THAT WORKED → MINE. Green PROVEN stamp.
10. **33.1 to 35.7s.** He swats away a blank page and the question mark: ✕ BLANK PAGE, ✕ GUESSING. Arms crossed: "No bullshit."
11. **35.7 to 40.7s.** Black end card: chrome monogram, wordmark, "Nothing guessed. Everything proven.", yourbrand.com.

## How it works
Same structure as parts one to three. New here:

- **The page** (`doc`, `drawDoc`): one 3D sheet with a 720x1040 canvas. Mode 0 is the brand's page (white body, one typed line). Mode 1 is YourBrand's (dark body): five blocks pop in at `T.items`; `scroll` moves the blocks up by one block for items four and five and back to zero for the push into the shot list; the header is drawn last over a clip so blocks slide under it.
- **Missing list:** `CONFIG.missing` and `T.no` drive four stacked pills over the face shot, with a head twitch and a shake each.
- **Wall shot:** the character turns to face the right wall (`ry: PI / 2`), the camera sits behind his shoulder; cups appear one by one and the wall clock runs fast.
- **Match card** (`match`): two tiles side by side, the reference and his.
- The words on the YourBrand page are generic placeholders, not from any real campaign brief.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.2x (1.12x ran to 39 s), take 1 of 2. `code/recipe.py` adds typing for "make it viral", a heavier thud for each missing thing, a clock for the two hours, a falling tone for the flop, a rising ding for each brief block, a chord on PROVEN. No music. Nobody has listened to the mix yet.

## Adapt it
New script: generate the voice, run `code/voice/words.py`, replace `WORDS`, regroup `GROUPS`, move `T` and mirror it in `recipe.py`. The product claims here are: the YourBrand brief contains the hook, the script, the shot list, a demo video and real videos that already worked. It shows no view counts or results for YourBrand content. Check any new claim before it goes in.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
