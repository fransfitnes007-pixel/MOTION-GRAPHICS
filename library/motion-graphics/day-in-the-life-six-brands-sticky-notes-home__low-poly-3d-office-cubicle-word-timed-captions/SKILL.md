---
name: day-in-the-life-six-brands-sticky-notes-home-low-poly-3d-office-cubicle-word-timed-captions
description: Part fourteen of the low-poly "day in the life of a UGC creator" reels. A veteran in an office cubicle works with six brands; each wants something today, he thinks; it is on a sticky note, somewhere. Two posts a day, three a week, one change in an email he never opened, a missed deadline for a brand he forgot he had. Then YourBrand's Home: his next step, his live campaigns, posts per day right on the card. The notes fall off the wall. He finds the sticky note; it says "check sticky notes". Reach for it when a reel needs the too-many-brands story, sticky notes that multiply then fall, a lock-screen deadline, or a home dashboard with a checklist.
---

# Day in the life, part fourteen: it's on a sticky note (low-poly 3D)

**Code name:** three.js office cubicle whose back panel fills with sticky notes that later all fall, box-built character with a note on his forehead, today list / cork board / Home page / one big note on a floating sheet, a lock screen on a floating phone, hard cuts on voiceover word times. **From:** original build, part 14 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-six-brands-sticky-notes-home__low-poly-3d-office-cubicle-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 39.1 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** An open-plan office under cold tube light: grey cubicle panels, a water cooler, a wall clock that runs. He works at the desk; a few sticky notes are on the panel behind him. "Part fourteen."
2. **3.6 to 5.2s.** Arms out: 6 BRANDS.
3. **5.2 to 7s.** A TODAY list: Brand A to Brand F, each tagged "something?".
4. **7 to 8s.** His face, squinting: I THINK.
5. **8 to 10.3s.** He looks left and right while notes multiply on the panel. On "Somewhere" one lands on his forehead: SOMEWHERE.
6. **10.3 to 15.9s.** A cork board: a yellow note "Brand A · 2 posts a day", a pink note "Brand B · 3 posts a week", a blue note "Brand C · changed it" with an envelope stamped UNOPENED.
7. **15.9 to 17.2s.** A lock screen at 23:58: "Brand F · Your post was due YESTERDAY." then "Hello? Are you still on this campaign?" MISSED.
8. **17.2 to 19.2s.** His face, the note still on his forehead: WHO IS BRAND F.
9. **19.2 to 20.7s.** The forehead note drops off; the chrome monogram; the light warms.
10. **20.7 to 21.8s.** His point of view of the laptop: Home, four stat tiles (bars, no numbers) and a Next step strip.
11. **21.8 to 26.3s.** The Home page: a NEXT STEP card with a four-line checklist (two ticked, "Sign the agreement · YOUR TURN" highlighted), then Live campaigns with two cards, then the POSTS PER DAY row on each card lights up and the cards get a yellow outline.
12. **26.3 to 27.7s.** He leans back, hands behind his head, and every note falls off the panel. TODAY: KNOWN.
13. **27.7 to 31s.** He swats away a pad of sticky notes and a purple "?" box: ✕ STICKY NOTES, ✕ MYSTERY BRANDS. Arms crossed: "No bullshit."
14. **31 to 34.1s.** Callback: one big yellow note. FOUND IT. The words land one at a time: check · sticky · notes, underlined.
15. **34.1 to 39.1s.** Black end card: chrome monogram, wordmark, "Open Home. See what today is.", yourbrand.com.

## How it works
Same structure as parts one to thirteen. New here:

- **`NOTES` and `notesAt(t)`**: 46 small planes on the panel behind him with seeded positions, colours and tilts. `notesAt` shows the first `n` (the count rises beat by beat) and, from `T.today`, drops each one on a staggered timer with a squared fall and a spin. One shot of them all letting go is the payoff picture.
- **`P.fnote`** is a note parented to his head: it pops on at "Somewhere" and falls off when he finds YourBrand.
- **Pages:** `drawDoc` 0 the TODAY list, 1 the cork board (three rotated notes, an envelope, a stamp), 2 YourBrand's Home (Next step checklist, Live campaigns, Posts per day), 3 the found note; `drawPhone` the lock screen; the laptop shows the Home tiles in the point-of-view shot.
- **`drawClock(t)`** turns the minute hand on the far wall.
- **Props for the finale:** `pad` (a block of notes with a curled top sheet) and `mbox` (a purple box with "?" faces).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 38.9 s; the rule gave 1.05, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` adds a low office hum under the first half, fifteen paper slaps as the notes multiply and a harder one for his forehead, a slap and a note per cork-board note, a buzzer on UNOPENED, two double beeps for the lock screen, ticks for the checklist, a long paper flutter when the notes fall, three thuds for "check / sticky / notes". No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
