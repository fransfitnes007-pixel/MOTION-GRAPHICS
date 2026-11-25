---
name: day-in-the-life-handbook-webinar-quiz-getting-started-low-poly-3d-classroom-word-timed-captions
description: Part sixteen of the low-poly "day in the life of a UGC creator" reels. A beginner in a classroom signs up to a creator platform and gets a welcome pack: a ninety page handbook that lands on his desk, a two hour webinar whose replay only works on Tuesdays, then a quiz on the handbook (four out of twenty). Then YourBrand's Getting started: three levels, each a five minute read, finish one and the next unlocks, every step linking to the page it is talking about. He fails their quiz again, on purpose. Reach for it when a reel needs the onboarding-overload story, an object dropping onto a desk, a webinar player, a marked quiz paper, or level cards that unlock.
---

# Day in the life, part sixteen: the welcome pack (low-poly 3D)

**Code name:** three.js classroom with a chalkboard that is rewritten when the day turns, box-built character, a handbook that falls onto the desk, welcome email / webinar player / quiz paper / Getting started levels / level one opened on a floating sheet, hard cuts on voiceover word times. **From:** original build, part 16 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-handbook-webinar-quiz-getting-started__low-poly-3d-classroom-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 37.9 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.4s.** A classroom on a grey day: a chalkboard reading "ONBOARDING · Module 1 of 37 · (bring the handbook)", a strip of coloured cards, rows of desks, a globe. He works at a school desk. "Part sixteen."
2. **3.4 to 5.4s.** Arms up: SIGNED UP.
3. **5.4 to 6.6s.** An email, "Your welcome pack!": Handbook.pdf (90 pages), Onboarding webinar (2 hours), Quiz (on the handbook).
4. **6.6 to 8.4s.** He looks up. A blue HANDBOOK the size of a breeze block falls out of the air onto his desk; the laptop jumps. 90 PAGES.
5. **8.4 to 12s.** A webinar player: "Onboarding · Part 1 of 9 · Slide 3 of 214", a presenter saying "can everyone see my screen?", 0:03 of 2:00:00. Then a red banner: "Replay available on Tuesdays only · Today: Wednesday".
6. **12 to 15.7s.** A quiz paper; "The Handbook, ch. 1–12" is highlighted; red crosses down the side and a circled 4/20.
7. **15.7 to 17.6s.** His face, looking left and right: WHERE IS ANYTHING.
8. **17.6 to 19.2s.** The chrome monogram; sun through the windows; the board now reads "LEVEL 1 ✓".
9. **19.2 to 24.8s.** Getting started, "Learn the platform in three levels": three cards (Dashboard & deals, Tracking & analytics, Time management & editing). The "5 min read" chips turn yellow one after another; "Mark complete" becomes "Completed ✓"; the padlock on level two opens: "In progress".
10. **24.8 to 27.4s.** Level 1 opened: six link chips pop in (Open Home, Manage handles, Browse deals, My campaigns, Link chat, Payout details); a cursor lands on Open Home and it turns yellow.
11. **27.4 to 30.2s.** He swats away a handbook and a webinar screen: ✕ HANDBOOK, ✕ WEBINAR. Arms crossed: "No bullshit."
12. **30.2 to 32.9s.** Callback: the quiz again, every answer C, a circled 0/20, and in blue pen "on purpose :)". ON PURPOSE.
13. **32.9 to 37.9s.** Black end card: chrome monogram, wordmark, "Three levels. Five minutes each.", yourbrand.com.

## How it works
Same structure as parts one to fifteen. New here:

- **The handbook drop:** `tome` (built by `makeTome`, with the label on its front and top) starts above the frame and falls with a squared ease to the desk at `T.bookHit`, bounces, and stays. `laptop.position.y` hops on the same hit. The beat uses its own `desk` camera because the stock `front` camera cuts the left of the table off.
- **`drawBoard(state)`** redraws the chalkboard only when the state flips (onboarding module, then "LEVEL 1 ✓").
- **Pages:** `drawDoc` 0 the email, 1 the webinar player (the timecode ticks), 2 the quiz paper (after `T.cb` it becomes the second attempt), 3 the three level cards, 4 level one with its link chips. `padlock()` draws a closed or open lock.
- **Props for the finale:** `tome2` and `webP` (a small screen with a play triangle).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 37.6 s; the rule gave 1.02, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` adds a faint school bell at the start, a falling whistle and a heavy slam for the handbook, a buzzer on the Tuesdays banner, red-pen scratches and a buzzer for the score, a ding per level card, a lock click when level two opens, pops for the link chips, pen scratches for the second quiz. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
