---
name: day-in-the-life-media-kit-font-salad-profile-low-poly-3d-train-word-timed-captions
description: Part twenty one of the low-poly "day in the life of a UGC creator" reels. On a train, a brand wants her media kit and she does not have one, so she makes one: three hours on the font (she picks the first one), page one is her laughing at a salad, page two is screenshots of stats that are already out of date, and fourteen pages later they reply "just send your three best videos". Then YourBrand: her profile is what brands see (one line about her, her top three videos, her views, tracked), she switches on "Discoverable to brands" and brands can invite her. For the record: that salad was not funny. Reach for it when a reel needs the media-kit story, a font picker cycling through typefaces, a stock-photo laugh with a camera flash, screenshots going stale, a profile card filling in, a toggle switching on, or scenery scrolling past train windows.
---

# Day in the life, part twenty one: the salad (low-poly 3D)

**Code name:** three.js train car (windows with a scrolling strip of countryside, luggage rack, swinging straps, "COACH 21" display), box-built character, inbox / font picker / stats page / page grid / reply / profile / discoverable-and-invite on a floating sheet, a salad bowl and fork, hard cuts on voiceover word times. **From:** original build, part 21 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-media-kit-font-salad-profile__low-poly-3d-train-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.8 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.5s.** A train on a grey day: countryside sliding past the windows, straps swinging, a suitcase on the rack. A woman in a red beret and a striped top works at the table. "Part twenty one."
2. **3.5 to 5.2s.** Inbox: "Hi! We love your videos. Could you send over your **media kit?** Thanks!! :)"
3. **5.2 to 7.7s.** A fixed grin, eyes darting: MEDIA KIT: NONE. Then fists up: HOW HARD CAN IT BE.
4. **7.7 to 9.7s.** media_kit.pdf: the words MEDIA KIT flick through a dozen typefaces while "fonts tried" runs to 214 (3 HOURS). She lands on Plain Sans: "✓ the first one".
5. **9.7 to 12.2s.** PAGE 1: COVER PHOTO. She lifts a salad bowl and a fork, throws her head back and laughs; a flash freezes it. LAUGHING AT: A SALAD.
6. **12.2 to 16.3s.** Page 2, "My stats": three phone screenshots land (Views, Followers, Likes); each number is struck through and tagged OLD, OLDER, OLDEST. ALREADY OUT OF DATE.
7. **16.3 to 17.3s.** media_kit_v9.pdf: fourteen page thumbnails fill the sheet. "14 pages · 38 MB".
8. **17.3 to 20s.** Re: media kit. The attachment says "not opened". "Thanks!! Could you just send your **3 best videos?**" PAGES READ: 0.
9. **20 to 21.6s.** The chrome monogram; sun through the windows, the countryside in full colour.
10. **21.6 to 27.4s.** Profile, "What brands see when they look for creators.": her card (Nia, Creator), a headline that types itself ("Food creator making honest reviews"), "My top 3 videos" (three numbered tiles), then Total views and Views growth draw themselves. NO SCREENSHOTS.
11. **27.4 to 30.6s.** "Discoverable to brands": the switch slides to green (DISCOVERABLE: ON) and the app's line appears; a card rises, "NEW INVITE · A brand invited you to a campaign", and "View invite" is pressed. INVITED.
12. **30.6 to 33.2s.** She swats away a black "Aa" block and the salad: ✕ FONTS, ✕ SALAD. Arms crossed: "No bullshit."
13. **33.2 to 35.8s.** Callback: back at the table she gives the salad a long sideways look. Close on the bowl; SALAD: NOT FUNNY; the fork tips over.
14. **35.8 to 40.8s.** Black end card: chrome monogram, wordmark, "One profile. Brands can invite you.", yourbrand.com.

## How it works
Same structure as parts one to twenty. New here:

- **The windows** are four planes that share one drawn 1024x256 strip of countryside (`sc`), each with its own cloned texture (`repeat.x = 0.3`) whose `offset.x` advances with `t`. Hills are sums of sines with whole periods so the strip loops with no seam. The mood flip is a tint on the window materials (grey to white) plus the usual light and wall lerps.
- **`FONTS`** is a list of made-up font names, each with a real system font family to draw it in. The font page redraws MEDIA KIT in `FONTS[fi]` twelve times a second, and the list underneath scrolls in step; from `T.fontHit` it is pinned to entry 0.
- **The laugh:** `HOLD` raises both hands (bowl in one, fork in the other); `lk` blends to head back, eyes shut, mouth wide, with a 24 Hz bob that stops when the flash fires (`v.flash` at `T.saladHit`), so the pose reads as a photo.
- **Screenshot cards** on the stats page take a strike-through and a tag in turn from `T.stale`.
- **`rattle`** adds a few millimetres of carriage shake to her hips; `straps` swing out of phase.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.244x (raw 46.0 s, aimed at 37 s), take 1 of 2. `code/recipe.py` lays a low carriage rumble and a da-dum of rail joints under the story, then a tick per font, a buzzer for "the first one", five rising pops for the laugh and a camera shutter, a shutter per screenshot, a clunk per OLD tag, fourteen pages landing, a buzzer on "3 best videos?", typing for the headline, a ding per top video, a click and two dings for the switch, a ding for the invite, and a fork clinking over at the end. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
