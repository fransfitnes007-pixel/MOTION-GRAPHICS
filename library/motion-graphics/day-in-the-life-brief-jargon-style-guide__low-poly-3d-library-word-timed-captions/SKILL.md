---
name: day-in-the-life-brief-jargon-style-guide-low-poly-3d-library-word-timed-captions
description: Part thirteen of the low-poly "day in the life of a UGC creator" reels. A first-week creator in a library gets her first brief: do a POV, green screen, talking head, with B-roll. She nodded and understood none of it; every site says something different; the brand says "you know, UGC style"; she thought B-roll was a type of bread. Then YourBrand's Content Style Guide: ten styles, what each one is and when to use it; talking head is the best default for a new creator. She still thinks B-roll sounds like bread. Reach for it when a reel needs the jargon story, highlighted terms with question marks, contradicting search results, or a guide page that opens one entry.
---

# Day in the life, part thirteen: I nodded (low-poly 3D)

**Code name:** three.js library with a drawn wall of books, box-built character, a standing BREAD book whose cover is a live canvas, brief / search / style-guide grid / one style opened on a floating sheet, a chat with the brand on a floating phone, hard cuts on voiceover word times. **From:** original build, part 13 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-brief-jargon-style-guide__low-poly-3d-library-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.5 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A library on a grey afternoon: a wall of books, a ladder, a QUIET PLEASE sign, a green reading lamp. She works at an oak table; a book called BREAD stands next to the laptop. "Part thirteen."
2. **3.6 to 5.3s.** Arms up: FIRST BRIEF.
3. **5.3 to 10.6s.** The brief: "Do a" then four yellow highlights land one per line, POV, GREEN SCREEN, TALKING HEAD, with B-ROLL, each followed by a red question mark.
4. **10.6 to 13s.** Her face, nodding with a fixed smile: NODDING. Then wide eyes: UNDERSTOOD: 0%.
5. **13 to 15.8s.** A search for "what is a pov with b-roll": about 4,000,000 results, three that disagree ("Actually…", "No. THIS is a POV.", "Stop saying POV wrong").
6. **15.8 to 19.3s.** A chat with the brand: "what is a POV?" · "and B-roll??" · "you know" · "UGC style :)".
7. **19.3 to 21.6s.** The BREAD book: a red circle draws round the roll on the cover and "B-roll ?" is written under it. B-ROLL = BREAD?
8. **21.6 to 23.2s.** The chrome monogram; the reading lamp warms the room.
9. **23.2 to 25.6s.** Content Style Guide: ten cards pop in, numbered 01 to 10, with the real style names. 10 STYLES.
10. **25.6 to 30.2s.** One card opened: Talking head. WHAT IT IS fades in, then WHEN TO USE IT; the title turns yellow on "Talking head" and a highlight runs across "Best default for a new creator."
11. **30.2 to 31.1s.** Both hands point at herself: NEW CREATOR: ME.
12. **31.1 to 33.7s.** She swats away a JARGON A–Z dictionary and a nodding bobblehead: ✕ JARGON, ✕ NODDING. Arms crossed: "No bullshit."
13. **33.7 to 35.5s.** Callback: the BREAD book again; the note now reads "B-roll !". B-ROLL = BREAD. STILL.
14. **35.5 to 40.5s.** Black end card: chrome monogram, wordmark, "Ten styles. When to use each one.", yourbrand.com.

## How it works
Same structure as parts one to twelve. New here:

- **The wall of books** is one canvas texture on a plane (six shelves of random spines from a seeded generator), tinted cooler before YourBrand and left untinted after. Cheap, and it fills every background.
- **`drawBread(t)`** redraws the standing book's cover each frame: the red circle is an ellipse arc revealed by `k`, the note under it switches from "?" to "!" at `T.still`. The `book` camera frames it so the whole cover sits above the caption.
- **Pages:** `drawDoc` 0 the brief (highlights and question marks), 1 the search, 2 the ten-style grid, 3 the opened Talking head card; `drawPhone` the chat. `bubble()` draws a chat bubble.
- **`CAM.face`** aims lower here (y 2.62) so the mouth stays above a large caption.
- **Props for the finale:** `dict` (a book with a JARGON A–Z cover) and `bob` (a bobblehead whose head rocks on `bobHead.rotation.x`).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.29x (raw 47.7 s, aimed at 37 s), take 1 of 2. Write "P O V" with spaces so it is spelled out. `code/recipe.py` adds a page turn, a falling note and a small rising "?" for each term in the brief, five soft nod ticks, typing for the search, a buzzer on the three results, message pops for the chat, a pencil scratch for the red circle, a low note on "bread", ten pops for the style cards, dings for the two sections and the highlight, a bobblehead boing. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
