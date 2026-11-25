# Faceless explainer styles: house rules and nine looks, measured

Nine high-performing faceless motion-graphic reels, one per niche (side hustles, study, gaming, phone widgets, sports,
health, money, ADHD, relationships), were watched frame by frame (10 fps frames, 0.5 to 2 s contact sheets), cut-detected
with ffmpeg (`select='gt(scene,0.3)'`), transcribed with faster-whisper and level-measured (`volumedetect`,
`silencedetect`). This file keeps what was measured. It is a style reference only: copy the look, flow, pace, motion,
type and sound, never anyone's script, topic, character or footage. How to read a reference yourself:
[`EYES-AND-SCRAPEY.md`](EYES-AND-SCRAPEY.md). Pipeline that builds these: [`../pipelines/multi-account-content/`](../pipelines/multi-account-content/).

Honest limit: each look was measured on a handful of reels. On one account the clean flat-vector reel did about 67x the
account's median while two other looks on the same account did not; the topic may explain that as much as the look.
Nobody listened to the reference audio by ear: music and effects below are read from levels, not heard.

---

## 1. The ten house rules (true of all nine)

1. **No hard cuts.** One continuous stage that keeps transforming: 0 to 1 scene cuts per reel in 7 of 9 (ffmpeg scene
   threshold 0.3). Change the picture, not the shot: elements spring in, morph, redraw, wipe.
2. **A new idea every 2 to 4 s, a new small element every 0.4 to 2 s.** Nothing sits still longer than about 3.5 s.
3. **The hook is complete on frame 0.** The first frame already shows the claim, the contrast or a moving counter. No
   logo intro, no fade from black, no greeting. Motion starts by 0.1 to 0.3 s.
4. **Word-timed captions** where the spoken word lights up and the rest is dim, plus ONE accent word per phrase in the
   single accent colour (box, chip or colour). Captions live in a fixed band (top third, mid 55 to 58 %, or 67 to 75 %).
5. **Dark stage, one accent colour.** Near-black, navy or plum backgrounds, white line art, one accent (teal, cyan, gold,
   green, purple). Emphasis = dimming everything else, not adding colour.
6. **Flat 2D line art; characters are symbols** (stick figure, glowing silhouette, wireframe skeleton). No real faces,
   no stock footage. Props are thin outline icons that spring in.
7. **Numbers move.** Counters, tickers and odometers carry the tension. Count the problem, never money earned.
8. **A fast, calm voice carries everything:** 155 to 205 words per minute, starting on frame 0, gaps of 0.3 to 0.6 s at
   most. Most have no music bed (the level drops to silence between phrases), only effects on the hits. Loudness
   -14 to -16 LUFS.
9. **The ending loops or lands softly:** a callback to the first image, a one-line card, or a question. The ask lives
   in the post caption, not on screen.
10. **9:16, 1080x1920, 30 fps** for everything you post (normalise 4:3 or 60 fps references).

Plus one rule from building several accounts at once: **a new account must change the format, not only the skin.**
Nine accounts that share narrator + centred karaoke caption + corner counter + phone mock-up + the same outro read as
one creator on a feed, whatever the palette. Change who tells the story, where the camera is, and the story device
(see FORMATS.md, format 26).

---

## 2. The nine looks

| # | Look | Stage and accent | Motion | Captions | Pace | Length |
|---|---|---|---|---|---|---|
| 1 | Stick-figure money stories | navy `#050a12` to `#0d1726`, gold `#d8a838`, green `#38d888`, red `#ff4d5e` | flat 2D, locked camera, props spring in (4 to 8 % overshoot, 6 to 9 frames), red X stamps slam 1.6x to 1x with 2 to 3 deg rotation, counters ease out over 1 to 3 s | heavy grotesque caps 70 to 78 px at 67 %, spoken word on a gold plate (radius 14, tilted -1.5 deg), 1 to 3 word chunks | new thing every 0.4 to 0.7 s, new set every 3 to 5 s, ~2.5 words/s | 95 to 105 s |
| 2 | Glowing stick figure, outline props | black, white glow, teal `#22b4a1` | no cuts, one teal outline prop drawn every ~2.4 s | whole phrase laid out at once at the top, 56 px; unsaid words `#3a4545`, said white, key word teal | 190 wpm, no half-second gap in 80 s | 36 to 81 s |
| 3 | Dark stage, flat cards, selection-box caption | `#0b0b0d` with a green glow in the middle, cards `#131518` border `#2a2d31` radius 10 to 14 | no camera; slide-ins 0.3 to 0.4 s ease-out, spring stamps tilted 3 to 6 deg, blur crossfades, tick-draw, strike-through, gliding cursor | 40 px, weight 600 to 700, 2-line block at 55 to 58 %; said white, unsaid 35 %, ONE key word in a green 1 px selection box with 4 corner handles | new picture every 2.4 s, 205 wpm | 31 s |
| 4 | Dark/light UI explainer joined by circle wipes | alternating dark and light scenes, pale blue accent, orange halo behind the hero | 5 scenes, 4 iris circle wipes, zero cuts, scene 2 to 8 s; springs, rolling digit drums, slot-machine blur on lists | one line near the top (y 300 to 340), word by word, newest bold, older grey; key nouns in a pale-blue selection rectangle, set in a serif italic | 2.4 words/s, one word every 0.4 s | 27 to 30 s |
| 5 | Navy glass UI cards with a slow-motion replay | navy glass cards, faint grid, cyan `#35BBF4` | locked 2D; every interaction plays at 1x, then dims and replays at 1/4 speed with its easing curve drawn live; ghost-finger tap ring; stagger 70 to 100 ms | kicker `01 · NAME` 26 px grey caps, 2 to 4 word headline 76 px with the last word in cyan ("Drop, then bounce."), spec pill with numbers (ms, px, %) | one real cut every 8.2 s, a change every 0.3 to 0.5 s | 32 s |
| 6 | X-ray wireframe skeleton world | black void, teal floor grid at 75 %, white skeleton = you, pink = the other person, gold = ideas | 3D, constant slow push / orbit, whip-through into the next set piece, a literal 3D picture for every phrase | ONE word at a time, dead centre, bold display serif, 9 to 12 % of frame height, one letter tinted, word blended into the scene | 2.4 words/s, a set piece every 1.5 to 3 s, 2 to 7 cuts | 60 to 65 s |
| 7 | Mono glowing silhouette | black, white, grey only; spotlight cone, bloom, vignette, dot grid | camera pulls back on every reveal; props slide in and wipe the stage; exponential counters | no karaoke; tiny caps labels under props (36 to 48 px), outline pill labels above, big tabular counters 90 to 110 px | new idea every 3 to 5 s, a change every 0.5 to 1 s | 65 to 71 s |
| 8 | Lilac UI world with a metro line | dark plum for tension, light lilac for the how; purple `#7a5af8` | colour-flood wipes between dark and light every 2 to 6 s, card shrinks into the next header, motion blur on fast slides, a glowing "metro line" route as a running motif, split-flap board in the hook | top third, 2 lines, words fade + rise 6 px + blur-in (0.15 s), older words grey, one huge display word per scene | 21 scenes in 43 s, a move every 0.3 to 0.5 s | 36 to 43 s |
| 9 | Line-art diagram on black | pure black, white and grey only | zero cuts; a diagram that redraws every 4 to 8 s, an icon or label every 1 to 2 s, cross-out lines, emphasis by dimming the rest; smooth ease-in-out 0.3 to 0.8 s, no overshoot | a bold title that never leaves (10 % from top) with a bracketed serif sub-line; a condensed serif karaoke line at 75 %, sentence case, unsaid `#4a4a4a`, said white | 205 wpm, nearly no pauses | 41 s |

### What each one teaches
1. **One number the eye can track from frame 0 to the end**, plus a persistent HUD strip of small pills that tick as the
   story advances. Mid-video re-hook at ~50 % ("But here's where most people mess up"). Ends on a red engagement question.
2. **A contradiction hook** (a bad behaviour with a good result). Every phrase is drawn, so sound-off still works; the
   teal key word gives a second rhythm over the voice. A turn at ~2/3, then a loop.
3. **A before/after label flip** reads silently on frame 0 ("1 PLAYER" struck, "2 PLAYERS" in green). Dim future words set
   the reading pace; the selection box says which word matters. Proof objects (counter, bar, ticked list, stamp)
   instead of talk. Bottom 35 % empty for the platform UI.
4. **Dark/light alternation plus the same circle wipe** resets attention every ~5 s without a cut. One idea and one object
   per scene. Soft tactile UI (rounded white cards, shadows, glow) reads calm and polished.
5. **One repeatable template** so each reel is cheap and followers learn it. Real numbers on every item make it saveable.
   The slow-motion replay with its curve is a satisfying loop: the same second watched three times.
6. **A strict colour code for who is who**, a literal picture for every abstract idea, one readable word at a time. No CTA
   card: it loops; replays and shares are the CTA.
7. **A "YOU" label on a faceless figure** lets the viewer step in. Strict two-tone world, cheap to make with code. Ends on a
   two-line imperative card.
8. **Never the same layout twice in a row.** Open loop early ("the last one almost nobody uses" at 8 s pays off at 33 s).
   One running example the viewer learns once. A self-roast in the first 5 s buys trust for the facts.
9. **One diagram per sentence**, so the eye never chooses between caption and picture. The title makes it understandable
   muted; the serif karaoke line makes it followable muted. The last diagram is the first one again.

---

## 3. Caption variants (build one engine, switch by CONFIG)

| Variant | Said word | Unsaid words | Accent | Band |
|---|---|---|---|---|
| Plate karaoke | black on a tilted coloured plate | white | the plate | 67 % |
| Dim-future phrase | white | 20 to 35 % grey | one key word in the accent colour | top third or 55 to 58 % |
| Selection box | white | 35 % | 1 px box with 4 corner handles around one word, word turns accent | 55 to 58 % |
| Serif-italic accent | bold near-white | grey | key noun in a serif italic inside a pale selection rectangle | top (y ~300) |
| One word centred | the word itself, 9 to 12 % of height, display serif | none | one tinted letter | centre |
| Serif karaoke line | white | dark grey | none (title carries the topic) | 75 % |
| Stroke caps (the low-poly series) | yellow | white once said | punch words at 1.5 to 1.6x size | 64 % |

All of them pop or sweep on the word's start time from a word-timestamp file (faster-whisper with the script as the
prompt, or the TTS provider's character alignment).

## 4. Hooks that were measured (first 1 to 2 s)
- A surprising claim with a number in the first sentence, while a counter is already running.
- A contradiction ("the one who does the wrong thing ends up ahead").
- A before/after label flip readable with no sound.
- A status claim typed word by word with a badge ("the most ... out"), then a number rising.
- A bold two-line claim over a mosaic that previews the payoff.
- A conflict between two symbol characters, first word at 0.3 s.
- A faceless figure labelled YOU, or a counter racing to six figures.
- A promise spoken and spelled by a split-flap board, then proof (notifications land) inside the first second.
- A contrarian instruction as a persistent title with a bracketed twist under it.

## 5. Endings that were measured
- A red question to the viewer, then a 3 to 4 s follow card (comments driver).
- A one-line imperative card ("CHOOSE YOUR ROOM.").
- A callback to the first image with one reversal line, ending 0.4 s after the last word so it loops.
- A one-sentence reframe, then large animated Like / Follow buttons (1.9 s).
- No card at all: hold the last end state and let it loop.
- For a product: the store-native CTA (FORMATS.md section L), never a bare logo.

## 6. Pieces these looks need (build once, reuse)
Caption engine with the variants above; a neutral prompt box + chat step rows + an app appearing on a phone; a
stick-figure rig (6 poses: idle, point, shrug, hands-up, tap-phone, celebrate) and a prop-card kit with a red-X overlay;
a glowing silhouette rig with a spotlight; a wireframe skeleton rig with a 3D camera on a grid; a line-art diagram kit
that redraws with a persistent title; a home-screen widget kit with circle wipes; a card + live curve + 1/4-speed
replay template; a split-flap board + metro line; a near-black stage + card kit with a label flip; counters and
odometers (in the library already: `mechanical-odometer__drum-carry-spring`, `odometer-number-roll__digit-column-translate`).
Track who builds what in a shared list (`pipelines/multi-account-content/templates/SHARED-PIECES.md`). Every piece:
`render(t)`, a `CONFIG` block for words, colours and timings, no brand baked in, 1080x1920 at 30 fps.
