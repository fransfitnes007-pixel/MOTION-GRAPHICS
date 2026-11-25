---
name: day-in-the-life-two-minute-script-scissors-script-generator-low-poly-3d-sewing-room-word-timed-captions
description: Part seventeen of the low-poly "day in the life of a UGC creator" reels. In a sewing room the brief says thirty seconds; her script reads at two minutes; she cuts the intro (ninety seconds), the middle and the ending (thirty seconds), and now it makes no sense and never mentions the product. Then YourBrand's script generator: pick thirty seconds; it writes the hook, the beats, the product moment and the call to action, sized to fit, with three more hooks to try. Her first draft is still running. Reach for it when a reel needs the too-long-script story, a stopwatch overrunning its target, blocks being cut out of a stack, or a generated script appearing block by block.
---

# Day in the life, part seventeen: two minutes (low-poly 3D)

**Code name:** three.js sewing room with a pegboard of spools and a dress form, box-built character, a paper script that hangs off the table and gets shorter with each cut, a stopwatch on a floating phone, first draft / cutting stack / generated script on a floating sheet, hard cuts on voiceover word times. **From:** original build, part 17 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-two-minute-script-scissors-script-generator__low-poly-3d-sewing-room-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.3 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4.1s.** A sewing room on a grey afternoon: a pegboard of spools, shelves of fabric, a dress form with a tape measure, a sewing machine. She works at a cutting table; a strip of paper script runs off it and across the floor. "Part seventeen."
2. **4.1 to 6.1s.** A finger in the air: BRIEF: 30 SECONDS.
3. **6.1 to 7.3s.** "SCRIPT · draft 1 · page 1 of 3": twenty-two lines fill the page.
4. **7.3 to 9.6s.** A stopwatch (TARGET 0:30) races past its target, turns red and stops on 2:00.0. 2 MINUTES.
5. **9.6 to 14.6s.** The script as a stack of five blocks with a time chip. Scissors run along INTRO and it drops away: 1:30. MIDDLE · the product goes, then ENDING; the stack closes up.
6. **14.6 to 15.9s.** She holds the scissors up: 30 SECONDS.
7. **15.9 to 17.6s.** What is left: SETUP ("So there I was…") and PAYOFF ("…and that is why."), a green 0:30 and a red "??". MAKES SENSE: NO.
8. **17.6 to 19.6s.** Her face: PRODUCT MENTIONS: 0.
9. **19.6 to 21.5s.** The chrome monogram; the lamp over the table warms the room.
10. **21.5 to 23.2s.** Her point of view of the laptop: UGC Script Generator, Length: 15 / 30 / 60 seconds; 30 turns yellow; Write script.
11. **23.2 to 30.4s.** The result, block by block on the words: HOOK, BODY BEATS, APP / PRODUCT MOMENT, CTA. A meter fills to the 0:30 mark and turns green: "fits ✓" (SIZED TO FIT). Then ALTERNATIVE HOOKS, three lines (+3 HOOKS).
12. **30.4 to 33.5s.** She swats away a stopwatch and a pair of scissors: ✕ STOPWATCH, ✕ SCISSORS. Arms crossed: "No bullshit."
13. **33.5 to 35.3s.** Callback: the stopwatch again, labelled FIRST DRAFT, at 47:12 and counting. STILL RUNNING.
14. **35.3 to 40.3s.** Black end card: chrome monogram, wordmark, "Pick a length. Get a script that fits.", yourbrand.com.

## How it works
Same structure as parts one to sixteen. New here:

- **The cutting stack (`drawDoc` 1):** `BLK` lists the five blocks with a height, a colour and which cut removes them. Each block's y is the running sum of the blocks above it times `(1 - shut)`, so the stack closes up as a cut block slides right, rotates and fades. `scissorsIcon()` sweeps along the top of a block just before its cut. The time chip steps 2:00, 1:30, 0:30.
- **The stopwatch (`drawPhone`):** seconds are a pure function of time; the ring fills once per thirty seconds and goes red past the target. After `T.cb` the same screen is the callback, relabelled FIRST DRAFT.
- **The paper script in 3D:** `pTop`, `pHang` and `pFloor` are the strip on, off and below the table; they shorten at each cut and three `cuts` offcuts appear on the floor and stay there (you can see them in the finale).
- **Props:** `makeScissors()` builds the scissors (held up in one shot, swatted in another); `swP` is the stopwatch.
- **Audio note:** this mix peaked at 0 dB after `loudnorm`, so the mux adds `alimiter=limit=0.8:level=false` (with `level` left on, the limiter pushes the level back up to 0 dB).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.1x (raw 40.4 s; the rule gave 1.09, raised to the 1.1 floor), take 1 of 2. `code/recipe.py` adds a quickening tick as the stopwatch races, a buzzer on two minutes, two scissor snips and a paper rustle per cut, a low whistle on "no sense", a buzzer on the missing product, a ding per script block, a rising tone into "fits", three pops for the extra hooks, a steady tick under the callback. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.
