---
name: day-in-the-life-mirror-daisy-coin-draft-review-low-poly-3d-hair-salon-word-timed-captions
description: Part twenty five of the low-poly "day in the life of a UGC creator" reels. In a hair salon, hair in rollers, she wants to know if her video is any good: she asks the mirror (you look tired), pulls petals off a daisy (post it, don't, post it), flips a coin (heads) and posts: two hundred views, everyone gone at second two. Then YourBrand: she uploads the draft before she posts and gets a verdict, "No, minor changes first", with the fixes on a timeline (the hook comes too late, dead air at second four); she fixes both and gets "Yes, good to post". The mirror still says she looks tired; the mirror is right. Reach for it when a reel needs the guessing-before-posting story, a talking vanity mirror, petals pulled one by one, a coin flip, a retention curve falling off a cliff, a review verdict that flips from amber to green, or a timeline with markers.
---

# Day in the life, part twenty five: the mirror is right (low-poly 3D)

**Code name:** three.js hair salon (terrazzo floor, three styling stations with bulb-framed mirrors, hood dryers, a neon "salon" sign, a towel cart), box-built character in rollers and a mint cape, mirror / post stats with a retention curve / submit draft / review verdict with hook card and timeline on a floating sheet, a daisy that loses petals, a coin, hard cuts on voiceover word times. **From:** original build, part 25 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-mirror-daisy-coin-draft-review__low-poly-3d-hair-salon-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.6 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.7s.** A salon under flat grey light: styling stations with bulb mirrors, hood dryers, a terrazzo floor. A woman in pink, blue and yellow rollers and a mint salon cape works at the counter in a red salon chair. "Part twenty five."
2. **3.7 to 5.2s.** Hand on her chin, head tilted: "Is my video any good?"
3. **5.2 to 8.7s.** The mirror: a bulb-framed vanity with her face in it. A black bubble: "you look…" then "you look tired." The reflection's eyes droop and get bags. MIRROR SAYS: TIRED.
4. **8.7 to 12.9s.** She holds up a daisy (PETALS: 8) and pulls one petal per beat; each flutters down. POST IT · DON'T · POST IT.
5. **12.9 to 14.6s.** She flicks a gold coin into the air; it spins, lands in her hand. HEADS.
6. **14.6 to 18.3s.** Your post: Views 200. "Still watching": a red line that falls off a cliff at 0:02, with "everyone left". GONE AT 0:02.
7. **18.3 to 19.7s.** The chrome monogram; the bulbs come on and the room turns pink.
8. **19.7 to 21.9s.** Content, "Instant feedback before you post": "Submit a draft for review"; my_video_v2.mp4 (draft · not posted) drops in; "Upload and review" is pressed and a bar fills. NOT POSTED YET.
9. **21.9 to 27.4s.** The verdict, in amber: "No, minor changes first". THE HOOK, FIRST 3 SECONDS: "The hook comes at 0:03. Move it to the first second." TIMELINE ("Click a marker to jump there"): an amber marker at 0:03, then a red "Dead air" block at 0:04.
10. **27.4 to 29.6s.** Both markers turn into green ticks ("2 fixes done", "Fixed in v2."); the banner flips to green: "Yes, good to post". KNOWN BEFORE POSTING.
11. **29.6 to 32.5s.** She swats away a giant daisy and a giant coin: ✕ DAISIES, ✕ COIN FLIPS. Arms crossed: "No bullshit."
12. **32.5 to 35.6s.** Callback: the mirror again, her reflection still tired: "still tired." THE MIRROR IS RIGHT.
13. **35.6 to 40.6s.** Black end card: chrome monogram, wordmark, "Know before you post.", yourbrand.com.

## How it works
Same structure as parts one to twenty four. New here:

- **`face(x, cx, cy, s, tired)`** draws her blocky face on a canvas (hair, rollers, eyes, blush); `tired` shortens the eyes, angles the brows and adds purple bags. The mirror page draws a bulb-framed vanity around it.
- **The daisy** is a stem, a yellow centre and eight petal groups rotated around it; `gone` hides one petal per beat (`T.p1`, `T.dont`, `T.p2`) and a separate `loose` petal tumbles down from each.
- **The coin** (`coinP`, named so it does not clash with the shared overlay's `coin()` function) flies on a sine arc from her hand while spinning on x, and stops flat on `T.heads`.
- **The retention curve** is drawn point by point (flat to 0:02, then an exponential drop) and revealed left to right.
- **The review page** keeps one layout: the verdict banner, the hook card and the timeline. Before `T.bothHit` the timeline shows the amber hook marker and the red dead-air block; after it, two green ticks. The banner switches text and colour at `T.yesHit`.
- **Lighting:** before the turn the wall, mirror glass, bulbs and sign are grey; after it the bulbs light up and the walls go pink.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.251x (raw 46.3 s, aimed at 37 s), take 2 of 2. `code/recipe.py` lays a faint hood-dryer hum under the story, then a shimmer when the mirror speaks and a sag on "tired", a pluck per petal with a ding for "post it" and a buzz for "don't", a metallic ping and a spin for the coin, a falling tone as the viewers leave and a buzzer at 0:02, the drop and upload sounds, a two-note "not yet" for the amber verdict, a pop per marker, two rising dings for the fixes, three dings for "Yes, good to post", and the shimmer again for the last mirror line. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
