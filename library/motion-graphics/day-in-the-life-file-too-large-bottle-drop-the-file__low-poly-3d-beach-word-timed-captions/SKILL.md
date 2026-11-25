---
name: day-in-the-life-file-too-large-bottle-drop-the-file-low-poly-3d-beach-word-timed-captions
description: Part twenty of the low-poly "day in the life of a UGC creator" reels. On a beach the video is done and now he has to send it: the email says file too large, so he compresses it (now he is a mosaic), the free app adds a watermark (on his face), he sends a link the brand cannot open ("can you fax it?"), so he puts it on a USB stick, in a bottle. Then YourBrand: he drops the file right in the app, YourBrand posts it exactly as he uploads it (the original, no watermark), and changes happen in one thread with Resubmit. The bottle came back, with their notes, on a floppy disk. Reach for it when a reel needs the file-delivery story, a video pixelating as it is compressed, a watermark growing over a face, a drop zone taking a file, a revision thread, or a thrown object landing in the sea.
---

# Day in the life, part twenty: in a bottle (low-poly 3D)

**Code name:** three.js beach (sea with moving waves and foam, palm, striped umbrella, sailboat, crab), box-built character, email / compressor / free-app export / chat / drop zone / approved card / revision thread on a floating sheet, a bottle thrown toward the camera and washed back, a floppy disk, hard cuts on voiceover word times. **From:** original build, part 20 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-file-too-large-bottle-drop-the-file__low-poly-3d-beach-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.5 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.4s.** A grey, overcast beach: flat sea, a palm, a coral and white umbrella, a folding table with a laptop, a drink with a tiny umbrella. A man in a straw hat types. "Part twenty."
2. **3.4 to 6.1s.** Both arms up: VIDEO: DONE ✓. Then the smile goes: NOW: SEND IT.
3. **6.1 to 8.4s.** New message. The attachment slides in (beach_day.mp4 · 1.8 GB), turns red and shakes: "File too large · Attachment limit: 25 MB".
4. **8.4 to 10.7s.** Compress video: the size counts down from 1.8 GB to 24 MB while his video frame breaks into bigger and bigger squares. 35 PIXELS. "Small enough to email."
5. **10.7 to 13.8s.** Export on the FREE PLAN: a small "made with FREE APP" tag appears in the corner of the frame, then grows and tilts until it covers his face. ON MY FACE.
6. **13.8 to 16s.** Chat with the brand: he sends the link; "can't open it"; "can you fax it?"
7. **16 to 17.9s.** Deadpan, he holds up a red USB stick. PLAN B.
8. **17.9 to 18.9s.** Seen from the water: he throws a green bottle, with the stick inside, straight at the camera. It splashes. SENT. PROBABLY.
9. **18.9 to 20.4s.** The chrome monogram; the clouds turn white, the sea turns turquoise.
10. **20.4 to 22.3s.** Content, "Submit a draft for review": a dashed box ("Drop the video file, or paste a link to the draft"); the file falls in and the box turns purple (DROPPED IN); "Upload and review" is pressed and a bar fills.
11. **22.3 to 26.6s.** "Approved. YourBrand posts it exactly as you upload it." His frame, sharp, and three ticks: The original, No watermark, Highest quality.
12. **26.6 to 29.1s.** Revision thread: "Open on the product, then the beach." He types what changed and presses Resubmit; the chip flips from "v1 · Changes asked" to "v2 · In review". ONE THREAD.
13. **29.1 to 32.1s.** He swats away a nine-pixel mosaic of himself and the bottle: ✕ COMPRESSING, ✕ BOTTLES. Arms crossed: "No bullshit."
14. **32.1 to 35.5s.** Callback: the bottle rides the foam back onto the sand (RETURN TO SENDER); he holds it up and looks inside (THEIR NOTES); a blue floppy disk fills the frame, label "NOTES · disk 1 of 6".
15. **35.5 to 40.5s.** Black end card: chrome monogram, wordmark, "Drop the file. Posted as you made it.", yourbrand.com.

## How it works
Same structure as parts one to nineteen. New here:

- **The set is outdoors with a horizon.** A sand box, a wet-sand strip, a sea box, a foam strip whose `z` follows `foamZ` (a sine, overridden in the wash-ashore shot so the foam carries the bottle in), five wave strips that loop toward the shore, a sailboat, a sun and clouds near the far plane (`z` about -100). Dunes and bushes at `z = 22` exist only for the one camera that looks back at the beach.
- **Mood flip:** overcast grey to postcard blue by lerping `scene.background`, `seaMat`, `cloudMat`, `sunDisc`, `sandMat` and the lights with `good`.
- **`frame(x, X, Y, w, h, cols)`** draws his video frame (`pv`, a 360x480 canvas drawn once) at any number of pixel columns: it is scaled down to `cols` wide on a scratch canvas, then back up with smoothing off. `cols = 0` means sharp. The compressor runs `cols` from 64 to 5.
- **The watermark** is one rounded tag whose position, scale (1 to 3.3) and tilt lerp on "on my face".
- **`CAM.shore`** sits over the water and looks back at him, so the throw comes at the camera. Positions `A` (cocked hand), `B` (release) and `L` (landing) drive the bottle; the arm swings overhand by taking `alx` from 2.6 up through pi to 4.1.
- **The bottle** (`botP`) is translucent glass with two inner models, `usbIn` and `flopIn`; `flopIn` shows from `T.back`. The hero floppy is `flop`, with a drawn label.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 40.5 s; the rule gave 1.095, raised to the 1.1 floor), take 2 of 2. "U G C" and "U S B" are spaced so they are spelled out. `code/recipe.py` lays a very quiet bed of surf under the whole story, then a thud and buzzer for "file too large", a buzz that steps lower as the video is crushed, a tacky jingle and a rising slide as the watermark grows, a mail swoosh for the link, two seconds of fax tones, a throw whoosh and a splash, a thud and a ding as the file lands in the drop zone, a rising tone for the upload, a ding per tick, typing and a ding for Resubmit, a wave washing in, glass on sand, and a disk drive grinding under the floppy. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
