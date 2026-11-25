---
name: day-in-the-life-lost-count-tally-delivered-counted-low-poly-3d-bakery-word-timed-captions
description: Part twenty three of the low-poly "day in the life of a UGC creator" reels. In a bakery before dawn, the contract says twelve videos. She counts what she has sent (eleven), counts again (thirteen), and the brand counts nine: three different numbers for one job. Some did not count and nobody says which, so she keeps a tally on the wall. Then YourBrand: her campaign page keeps count (Delivered 7 / 12, Days left 9) and every post says Counted or Not counted. It was thirteen, by the way: a baker's dozen, force of habit. Reach for it when a reel needs the lost-count story, items being counted one by one with a moving ring, tally marks chalked on a board, a segmented progress row filling in, status badges landing on a list, or a bakery set.
---

# Day in the life, part twenty three: a baker's dozen (low-poly 3D)

**Code name:** three.js bakery (checker floor, shelves of bread, oven, window, a chalkboard that takes a live tally), box-built character, contract / sent folder counted twice / the brand's email / "which ones?" / campaign page / post list on a floating sheet, a tray of rolls, hard cuts on voiceover word times. **From:** original build, part 23 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-lost-count-tally-delivered-counted__low-poly-3d-bakery-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.7 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A bakery before dawn: blue window, cold oven, bread on the shelves, a chalkboard (TODAY: sourdough, baguettes, rolls ×12). A woman in a yellow headwrap and a striped apron works at a butcher-block table beside a tray of rolls. "Part twenty three."
2. **3.6 to 5.8s.** The agreement: "3. Deliverables. The creator will deliver **12 videos**". THE DEAL: 12.
3. **5.8 to 9.9s.** Her Sent folder. A red ring steps from thumbnail to thumbnail, numbering them: **11**. Again, faster, and two grey extras appear ("a copy?", "the redo?"): **13**.
4. **9.9 to 12s.** Re: where are we at? "Hi! By our count you have delivered **9** videos. :)"
5. **12 to 14.7s.** Deadpan, with three tags stacked over her head: ME: 11 · ME AGAIN: 13 · THE BRAND: 9. Her head tilts on "for one job".
6. **14.7 to 17.1s.** "What I sent": six rows, each tagged "counted?", then a red WHICH ONES? across the list.
7. **17.1 to 19.6s.** At the chalkboard, arm up: thirteen tally marks appear under VIDEOS SENT, then "= 13 ??". TALLY: ON THE WALL.
8. **19.6 to 21.2s.** The chrome monogram; morning light, the oven glows, the board now reads FRESH TODAY.
9. **21.2 to 26.5s.** My Campaigns, Sunny Soda (Active): two tiles, Days left and Delivered (IT COUNTS FOR ME). A Deliverables row of twelve squares ticks up to seven; Delivered lights up **7 / 12**; Days left lights up **9**.
10. **26.5 to 29.4s.** Your posts: Video 7, 6 and 5 get green "Counted"; Video 4 gets amber "Not counted". IT SAYS WHICH.
11. **29.4 to 32.4s.** She swats away a slate of tally marks and an abacus: ✕ TALLY, ✕ RECOUNT. Arms crossed: "No bullshit."
12. **32.4 to 35.7s.** Callback: close on the tray of twelve rolls; a thirteenth drops on top (THIRTEEN). She shrugs: A BAKER'S DOZEN · FORCE OF HABIT.
13. **35.7 to 40.7s.** Black end card: chrome monogram, wordmark, "Your campaign page keeps count.", yourbrand.com.

## How it works
Same structure as parts one to twenty two. New here:

- **`drawBoard(marks, open)`** repaints the chalkboard texture only when its inputs change: a menu on the left, and on the right either `marks` tally strokes (every fifth is the diagonal) with "= 13 ??" at thirteen, or FRESH TODAY once the mood flips. `marks` runs 0 to 13 during the wall shot and she sidesteps a little with each one.
- **The count** on the Sent page is two passes of the same loop: `cur` is how many thumbnails are numbered and which one has the ring; on the second pass `N` grows from 11 to 13 with two dashed extras.
- **Three stacked pills** (rows 0 to 2) carry "three different numbers".
- **The Deliverables row** is twelve squares; `n` of them are green with a tick, and the newest one pops.
- **`roll13`** is the thirteenth roll: it falls onto the tray at `T.itHit` and bounces twice.
- **`CAM.board`** looks up at the wall from behind her; **`CAM.tray`** is the close-up on the rolls.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.259x (raw 46.6 s, aimed at 37 s), take 2 of 2. `code/recipe.py` lays a faint oven hum under the story, then a tick per video counted (eleven, then thirteen), a buzzer on thirteen and on the brand's nine, three falling pops for the three numbers, a pop per "counted?", thirteen chalk strokes, seven rising notes as the squares fill, a ding each for 7 / 12 and for 9, three dings for Counted and a duller tone for Not counted, a soft thump as the thirteenth roll lands. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
