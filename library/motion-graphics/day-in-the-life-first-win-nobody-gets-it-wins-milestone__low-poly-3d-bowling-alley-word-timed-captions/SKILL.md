---
name: day-in-the-life-first-win-nobody-gets-it-wins-milestone-low-poly-3d-bowling-alley-word-timed-captions
description: Part twenty two of the low-poly "day in the life of a UGC creator" reels. In a bowling alley, his video hit a hundred thousand views, his first one. He told the group chat (they said "nice", then talked about parking), his roommate ("of what?") and his plant (the plant gets it), then threw a party: attendance, him. Then YourBrand: when a post hits a milestone it lands in #wins with his handle, and the whole network sees it, people who actually get it. He still tells the plant first; the plant was there from day one. Reach for it when a reel needs the nobody-to-celebrate-with story, a view counter rolling to a round number with confetti, chat threads that change the subject, a chat-style channel card with reactions, a party for one, or a bowling alley set.
---

# Day in the life, part twenty two: the plant gets it (low-poly 3D)

**Code name:** three.js bowling alley (ten lanes with pins, neon back wall, score screens, balls rolling down other lanes), box-built character with a potted plant in the next seat, video stats / group chat / roommate chat / #wins on a floating sheet, party hats, a party horn, a balloon and confetti, hard cuts on voiceover word times. **From:** original build, part 22 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-first-win-nobody-gets-it-wins-milestone__low-poly-3d-bowling-alley-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 38.7 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A bowling alley under grey house lights: lanes, pins, a neon wall, a score screen that reads LANE 22 · NICO · PLANT. A man in a mint bowling shirt works at a booth table; a potted plant sits in the seat beside him. "Part twenty two."
2. **3.6 to 7.1s.** Video stats: the view count rolls 99,361 … 99,999 … **100,000**, turns green, confetti, a "100K views" badge. Both arms up: FIRST ONE EVER.
3. **7.1 to 11.4s.** Group chat "the boys": MY VIDEO HIT 100K!!! · "nice" · "anyway who parked in my spot" · "it was dave" · "it's always dave". NEW TOPIC: PARKING.
4. **11.4 to 13.9s.** Roommate: "bro. my video hit 100K views" · typing dots · "of" · "of what?" · "also we're out of milk".
5. **13.9 to 16.1s.** He turns and shows his phone to the plant. Its leaves nod. THE PLANT GETS IT.
6. **16.1 to 18.7s.** Party hats pop onto him and the plant, a balloon rises, confetti falls, he blows a party horn (PARTY). Then the face drops and the horn droops: ATTENDANCE: 1.
7. **18.7 to 20.2s.** The chrome monogram; the room turns purple and the lanes warm up.
8. **20.2 to 27.4s.** A chat-style channel, "# wins · YourBrand server". Flubby (APP) posts a card: trophy, MILESTONE, **@nico.bowls**, "passed a view milestone on video app". "# wins" and the handle each flash yellow on their words. Five reactions pop in, then two replies: "what was the hook??" and "saving this format". THEY GET IT.
9. **27.4 to 30.4s.** He swats away a speech bubble that says "of what?" and a party hat: ✕ EXPLAINING, ✕ PARTY FOR ONE. Arms crossed: "No bullshit."
10. **30.4 to 33.7s.** Callback: he shows the phone to the plant again (TOLD FIRST: THE PLANT). Close on the plant, still in its party hat, nodding: FAN SINCE DAY ONE.
11. **33.7 to 38.7s.** Black end card: chrome monogram, wordmark, "Your wins. In front of people who get it.", yourbrand.com.

## How it works
Same structure as parts one to twenty one. New here:

- **The set has depth behind him.** Ten lanes run from `z = -4` to `-32` with ten pins each, a masking unit and a drawn neon strip on the back wall (`neonMat`, tinted by the mood). Two balls loop down other lanes (`balls`, `z = -5 - d`). Score screens hang at `z = -4.7`; only his lane's has text.
- **The plant** is `plantG` (pot) with `plantTop` (stem and five flattened icosahedra) so the leaves can nod by setting `plantTop.rotation.x = nod`. `hatPl` is its party hat, shown from `T.partyHit` to the end.
- **His party hat** lives in `P.fnote` (a group the rig already has on the head) and is scaled in by `hat`.
- **`CAM.duo`** frames him and the plant together; **`CAM.plantC`** is the close-up for the last line.
- **`bubble(...)`** draws one chat bubble with a pop scale; the two chats are one page with a `mode` switch.
- **The counter** is `Math.floor(lerp(99361, 99999, ...))` until `T.kHit`, then exactly 100,000; confetti is 26 rectangles flying out from the number.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 38.3 s; the rule gave 1.04, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` lays a low room tone with a ball rolling and pins falling far away every few seconds, then ticks as the counter climbs and three dings at 100,000, message pops for the chats (a low one for "nice"), a buzzer for "of what?", leaves rustling, two party-horn toots and one that sags on "me", dings as the #wins card, the channel name and the handle land, five rising pops for the reactions, and three dings on "day one". No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
