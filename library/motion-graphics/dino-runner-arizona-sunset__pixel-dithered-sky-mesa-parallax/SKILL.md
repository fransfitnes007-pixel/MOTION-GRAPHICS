---
name: dino-runner-arizona-sunset-pixel-dithered-sky-mesa-parallax
description: "A pixel dino-game video on a desert sunset instead of black. A dithered purple-to-orange pixel sky, a setting sun, mesas and saguaros in parallax, the dino as a silhouette that turns white when the brand takes over. Reach for it when a video needs the dino format with a warmer, more scenic look."
---

# Dino runner, Arizona sunset

**Code name:** pixel canvas, Bayer-dithered sky, mesa parallax, scripted jumps on voiceover word times. A sibling of `dino-runner-game-over-then-endless-run__pixel-canvas-scripted-jumps`. The idea is the offline dinosaur game; every pixel here is drawn new.

## What you see
Open `code/demo.html` in a browser; it loops (40 seconds, 1080x1920 or 1920x1080 with `?w=1920&h=1080`).

Top left for the whole game: the brand's domain. Top right: a small chrome monogram turning like a coin. Both leave when the end card arrives.

1. **0 to 6s.** A desert sunset in hard pixels: deep purple at the top, through magenta and red to gold at the horizon, a banded sun half set, two rows of mesas and tiny saguaros drifting behind, a dark desert floor below. The dino is a black silhouette with the sun on its edge. A white pill names it YOUR PRODUCT, a dark pill names the first cactus BAD LAUNCH.
2. **6.7 and 7.9s.** Two clean jumps, on "lucky once" and "lucky twice".
3. **9.1 to 12.8s.** Three cacti with pills on their words: ✕ SIGNUPS STALL, ✕ BUDGET BURNS, ✕ SHELVED. The dino hits them. GAME OVER.
4. **13.8 to 19.3s.** NEW IDEA 1 to 6: the same crash, faster each time. Then the frame dims and EVERY / SINGLE / TIME. slams in, one word per syllable (17.54, 17.92, 18.34s), each with a crash under it.
5. **19.3 to 35.5s.** Dusk: the sky cools, stars come out, the dino and ground line turn white. RUNNING THROUGH YOURBRAND, 2X SPEED, speed lines, a jump every 0.7s with ticks (✓ DAY 1, ✓ DAY 2, ✓ DAY 3, ✓ LAUNCHED, ✓ GROWING). A larger pill in the sky follows the voice through `CONFIG.steps`.
6. **35.5s.** The dino runs into the chrome monogram. White flash.
7. **35.75 to 40s.** Black end card: chrome monogram and wordmark, "Keep going." "Never stop.", the domain, a white dino still running.

## When to use it
The dino format when black feels flat, or any pixel scene that wants a desert sunset behind it. The backdrop alone (`skyCanvas`, `backdrop`) lifts out cleanly. Use the tall version for vertical short-video feeds, the wide one for landscape players.

## How it works
Two small canvases, both scaled 5x with smoothing off. The game (216x150, or 384x150 wide) scrolls at `speed * t`; each cactus is placed where the scroll will be when the voice says its word, so nothing is simulated. The backdrop is a full-frame canvas at one fifth size (216x384 or 384x216).

**The sky** is built once: each row picks between two neighbouring colour stops with a 4x4 Bayer matrix, so the gradient is real pixel dithering, not a blur.

```js
const f = Math.pow(y / HY, 1.3) * (list.length - 1), i = Math.floor(f), fr = f - i
const c = fr > (BAYER[y % 4][px % 4] + 0.5) / 16 ? list[i + 1] : list[i]
```

A second sky (`CONFIG.dusk`) is cross-faded over it in 0.6s when the brand takes over. Per frame, on top: stars, the sun as stacked rows in three bands sinking 22 pixels over the run, cloud streaks, far mesas at 5% of the scroll, near mesas and saguaros at 12%, and stones on the floor that pass faster the lower they are. A soft additive glow is added at full resolution around the sun.

**Reading on a bright sky.** The dino and cacti are drawn twice: once shifted a pixel in each direction in an edge colour, then the body. Before the brand that is a dark body with an orange rim; after, a white body with a dark edge. Pills carry a soft drop shadow, captions sit on the dark floor.

**Colour rule.** Type, pills and logo stay in a dark UI theme: `#161619` cards, white and silver text, chrome logo. Only the backdrop is the sunset. The end card is plain black.

**Safe zone:** all type inside x 70 to 940, y 250 to 1480 of 1080x1920.

## Numbers that matter
| What | Value |
|---|---|
| Backdrop canvas | 216x384 (tall), 384x216 (wide), at 5x; horizon at row 230 / 148 |
| Sky stops, sunset | `#1a0a38 #35104f #641a63 #a3285f #d9414a #f46a33 #ff9a35 #ffc65a` |
| Sky stops, dusk | `#0a0520 #170838 #33104f #641a66 #a52a62 #dd4d48 #f47a36 #ffab45` |
| Floor | `#3a1638 #241028 #150a1c #0a0510` |
| Sun | radius 30 px, bands `#fff3b0 #ffd670 #ff9d4a` |
| Silhouette / rim | `#170b20` / `#ffb057` |
| Speed | 125 px/s, then 270 px/s |
| Voice pace | about 2.7 words a second |

## Sound
`code/recipe.py` mixes a voiceover with square-wave jump blips, a thud per crash (the last three under EVERY, SINGLE, TIME), a whoosh into dusk, a rising tick per cleared cactus and a chord on the monogram. Record your own voiceover first, save it as `code/voiceover.wav`, then run the recipe. A fast, conversational narrator suits it; sped up about 1.18x.

## Adapt it
`CONFIG` at the top of `code/demo.html`: tags, the three fail reasons, the restart word, the win ticks, `steps` (the timed sky pills), end lines, both skies, floor, sun, mesa and rim colours, speeds, the safe box. For a new script: generate the voice, get word times from any transcription tool, replace `WORDS`, move the times in `T` and in `steps`, and mirror `PART2`, `WALL` and the hit times in `recipe.py`. The monogram and wordmark come from `brand-assets.js`, a generated file of embedded placeholder logos.

## Files
`code/demo.html`, `code/recipe.py`, `code/brand-assets.js`, `media/poster.jpg`
