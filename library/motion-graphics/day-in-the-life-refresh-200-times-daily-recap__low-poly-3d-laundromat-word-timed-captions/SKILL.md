---
name: day-in-the-life-refresh-200-times-daily-recap-low-poly-3d-laundromat-word-timed-captions
description: Part ten of the low-poly "day in the life of a UGC creator" reels. A beginner in a laundromat posted a video an hour ago and has refreshed it two hundred times. 300 views: is that good? His mom is proud. Last week one video did great, the copy flopped, and he does not know why either time; the shrug gets bigger. Then YourBrand: his views are tracked, and every morning the campaign chat posts a recap with the top videos and why number one worked. His laundry has been done for three hours. Reach for it when a reel needs the "is this good, and why" story, a refresh gag, a chat with mom, or an analytics and recap payoff with no numbers shown.
---

# Day in the life, part ten: refreshed two hundred times (low-poly 3D)

**Code name:** three.js laundromat with a row of spinning washers, box-built character with glasses and a three-size shrug, post / chat / "my videos" / chat recap pages on a floating phone and sheet, hard cuts on voiceover word times. **From:** original build, part 10 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-refresh-200-times-daily-recap__low-poly-3d-laundromat-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 39.9 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.4s.** A laundromat under cold tube light: WASH · DRY · WAIT sign, checkered floor, washers turning along the back wall. He works at a folding table next to his basket. "Part ten."
2. **3.4 to 8.9s.** His post, "Posted 1 hour ago". A pull-to-refresh spinner; a red REFRESHED × counter races to 200. Then "300 views".
3. **8.9 to 10.7s.** His face, head tilted: GOOD? Shrug number one: NO IDEA.
4. **10.7 to 13.1s.** A chat with Mom: "is 300 views good" · "SO proud of you!!" · "What is a view".
5. **13.1 to 16s.** "My videos": last week's tile with a full green bar, DID GREAT. Shrug number two: WHY? NO IDEA.
6. **16 to 19.9s.** The tile duplicates itself (COPY), the copy turns red with an empty bar: FLOPPED. Shrug number three lifts him off the chair: STILL NO IDEA.
7. **19.9 to 21.5s.** The chrome monogram on the laptop; the light turns warm.
8. **21.5 to 22.9s.** His point of view of the laptop: Analytics (Followers, Avg views, Engagement as lines; Views over time as bars). TRACKED.
9. **22.9 to 28s.** The campaign chat's #wins channel: a YourBrand card, "Day 6 · Your campaign", the top three videos slide in as bars, then a yellow "Why #1 works" box.
10. **28 to 29.7s.** A light bulb pops up beside his head, arm in the air: NEXT VIDEO: SORTED.
11. **29.7 to 32.8s.** He swats away a blue refresh arrow and a crystal ball: ✕ REFRESHING, ✕ GUESSING. Arms crossed: "No bullshit."
12. **32.8 to 34.9s.** Callback: his washer, the only one not turning. The panel reads DONE +3:00:12 and keeps counting. STILL IN THERE.
13. **34.9 to 39.9s.** Black end card: chrome monogram, wordmark, "See what worked. Make that next.", yourbrand.com.

## How it works
Same structure as parts one to nine. New here:

- **Elbows bend sideways too:** poses gained `alez` / `arez` (the elbow's z rotation), which is what makes a palms-up shrug possible. `SHRUG[0..2]` are the three sizes; `shrug(n, t0, hit)` in `state` plays one with a wobble.
- **`washer(x, hero)`** builds one machine; the others' clothes groups are in `drums` and turn every frame, the hero's stay still and its panel is a canvas (`drawPanel`) that counts seconds past three hours. The `washer` camera frames it.
- **`pov` camera** needs an upright pose (no forward lean) or the head and glasses poke into the lens; fov 80 shows the whole laptop screen.
- **Pages:** `drawPhone` 'post' (spinner, then the count) and 'mom' (`bubble()` draws a chat bubble); `drawDoc` 0 "My videos" (the copy slides out of the original), 1 the chat recap. `thumb()` draws a video thumbnail of him, `spark()` a small line chart, `spinner()` a refresh arc.
- **Props:** `ringP` (refresh arrow: a torus arc and a cone), `ball` (crystal ball), `bulb`.
- **No YourBrand numbers:** the Analytics page and the recap show lines and bars only. 300 views and 200 refreshes are his own made-up numbers in the pain half. The recap wording follows the app: a "Day N" card in #wins each morning, top videos, "Why #1 works".
- The laptop lid's G is hidden in the light-bulb shot because the caption sits on it.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 39.8 s; the rule gave 1.076, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` adds a low washer slosh under the first half, sixteen quickening refresh chirps, message pops for the chat, a falling whistle on each shrug (longer each time), a rise and ding for the hit, a buzzer for the flop, a ding per row of the recap, a bulb ping, the washer's finished beep. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
