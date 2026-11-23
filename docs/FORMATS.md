# Video formats, recipes and lessons (generic, white-label)

Everything here was learned by making real short-form and long-form motion-graphics videos with an AI coding assistant. Every name, brand, person, handle, domain and path has been replaced with a placeholder: `YOURBRAND`, `yourbrand.com`, `@yourbrand`, "the product", "the reviewer" (whoever approves the video), "the assistant" (the AI that builds).

Conventions used below:

- **Wide** = 1920x1080 (16:9). **Tall** = 1080x1920 (9:16). Both are separate compositions, never a crop of each other.
- Times are seconds from the start of the film. "Word-anchored" means the cut or hit is pinned to the start time of a spoken word taken from a transcript with word timestamps.
- `render(t)` means a page whose whole picture is a pure function of time (see "Common pipeline" in the cross-cutting section).
- Each format ends with two prompts: **short** (what you would type if the kit is already installed) and **detailed** (when starting cold).

## Index of formats

1. Pixel dino-runner reel on black ("game over, then the endless run")
2. Pixel runner on a dithered desert sunset
3. Black-and-white pictogram parable (one white person, capsule tags, dot grid)
4. Black-stage "pawn" explainer engine (one JSON spec per video, voice is the clock)
5. Stamped-word feed-scroll brand film (light stage, modelled on a viral UI-concept reel)
6. Full-platform product film: real feed scroll, red X, flash cut into a dark glass product tour
7. No-voice 3D logo ident (4K 60 fps)
8. Colour-poster "slam" film (one flat colour per beat, type cropped by the frame)
9. Ring-of-phones film (3D ring, screen floods with each layout colour)
10. Dark-stage "cinema" product film (one light beam, orbiting avatars, tilted windows)
11. Product-site film family: five more looks (one-camera board, channel flip, dark chapters, calm glass, light intro)
12. Liquid-glass two-world launch film (16:9, 60 fps)
13. Single-accent-dot keynote-calm launch film (near black, scramble-decode line)
14. Book-opening dark trailer (3D book, four aspect ratios, hook A/B/C)
15. Website launch film: typed URL, morph into the browser, sections, key and click sounds only
16. White-label "how to set up" walkthrough with a follow camera
17. Beat-grid promo (every cut on a beat of a fixed BPM)
18. Retro-console life-sim cutscene reel (AI keyframes + local image-to-video + real UI composite)
19. Screen-recorded app-demo clips for creators (simulator pipeline)
20. Native-UGC-style reels from real recordings (CapCut-style captions, store-search ending): 17-video format family
21. Skeptic-and-answer explainer (two-voice objection loop)
22. Short-form creator formats (talking head, text-hook reaction, split screen, slideshow, POV, AI character)
23. Product listing videos from phone footage (batch ffmpeg)
24. "Day in the life" pain-point-to-solution reel (script template)

Then: cross-cutting lessons and gotchas (pipeline, rendering, ffmpeg, colour, TTS and voices, sound synthesis, captions, safe zones, posting specs, hooks and scripting, review, review patterns).

---

## 1. Pixel dino-runner reel on black ("game over, then the endless run")

**Look in one line:** an offline-browser-dinosaur-game lookalike: grey pixel dino, ground line, pixel cacti, on black; the brand is the dino, bad creators/vendors are cacti; it crashes and restarts, then runs at 2x through the brand and hits a chrome monogram, cut to a black end card.

- **Platform / size:** Reels, TikTok, Shorts, Snapchat, Facebook (tall 1080x1920, 30 fps) plus an X/Twitter cut (wide 1920x1080). 34 s. Voiced, no music (blips and thuds only).
- **Why it works:** one metaphor, one loop (try, crash, restart), a payoff (the loop stops), extremely cheap to produce, and it is a real shared memory for viewers.

### Beat sheet (seconds)

| t | what happens |
|---|---|
| 0-6 | Grey pixel game on black. White pill on the dino ("YOUR BRAND"), dark glass pill on the first cactus ("BAD CREATOR"). Top-left small site text, top-right small chrome monogram turning like a coin the whole game. |
| 6.9, 8.0 | Two clean jumps on the spoken words "dodge one", "dodge two" (jump starts 0.28 s before the word, with a blip). |
| 8.9-12.1 | Three cacti, each with a dark pill popping on its word (`x GHOSTED YOU`, `x MISSED THE BRIEF`, `x POSTED GARBAGE`). Dino hits, "GAME OVER", white flash, X eyes. |
| 13-18 | "RESTART 1 ... 6": same crash, faster each time. Hit times about 14.05, 15.25, 16.3, 16.95, 17.45, 17.85. Frame dims (black at 0.72-0.88 alpha). |
| ~16-17 | One slammed word per syllable ("EVERY / [swear] / TIME.") at 190 px (wide 168 px), stacked on tall, one line on wide; the middle word pure white with glow, the others silver. |
| 18-29.7 | Dino, ground and score turn white. Pill "RUNNING THROUGH YOURBRAND", "2X SPEED", speed lines, score racing, a jump about every 0.74 s (shortening 0.012 s per jump, capped at 8 steps) with rising ticks; check pills (VETTED, BRIEF LANDED, POSTED). |
| 29.75 | Dino runs into the chrome monogram: white flash `exp(-(t-wall)*8)`, circle clip reveal (radius `eo(e)*2400` from the dino) into the end card. |
| 30-34 | Black end card with grey radial haze (`#1a1a1d -> #08080a -> #000`): monogram (360 px tall, white glow shadowBlur 60), wordmark (560 px wide), two 84 px bold lines ("Stop restarting." / "Start running.") appearing on their words, site text in `#a1a1aa` 40 px semibold, a white dino still running along the bottom. The spinning monogram and corner text leave when the end card arrives. |

### Look and numbers

- Palette: page `#000`; game ink `#8b8b93`, then `#fff` in the run; cards `#161619`; muted `#a1a1aa`; silver `#d4d4d8`. No blue, pink or green on the dark theme (see lessons).
- Type: system sans (a geometric neo-grotesque such as SF Pro Display or Inter): Bold 700 from 34 px up, Semibold 600 below.
- Game drawn on a tiny canvas (tall 216x150, wide 384x150) scaled 5x with `imageSmoothingEnabled=false`; ground y=118; dino x offset 26 (wide 70); canvas placed at y=560 (tall) or 150 (wide). Sprites are small ASCII bitmaps (own drawings, never a copy of anyone's sprites). Dino run frame flips 11 times/s (20/s in the 2x phase).
- Nothing is simulated. Scroll = speed x time (125 px/s, then 270 px/s in game pixels). Each cactus is **placed where the scroll will be when the voice says its word**: `cactus.x = speed*t_word + dinoX + 8`. Jump parabola `jumpY(t, at) = 46*4*p*(1-p)`, `p=(t-at)/0.56 + 0.5`.
- Captions: 3 words at a time, chunk breaks at punctuation, current word lit and others dim, "hot" words pure white with glow, 84 px bold, pop with `back()` 0.9 -> 1.
- Hit flash: white overlay `exp(-(t-hit)*9)*0.2` (not in the 2x phase). "GAME OVER" 78 px bold with back-pop.
- Draw order: the spinning monogram is drawn **above** the dim/slam overlay so it stays bright.
- Safe zone (tall): all type inside x 70-940, y 250-1480 so the right-hand buttons and bottom caption/profile area never cover it.

### Sound

- Voice: one take of a young conversational library voice, 2.3 words/s raw, sped up with `atempo=1.18` to about 2.6-3.1 words/s (the pace of the reference narration). Write short declarative lines, one idea each, a full stop where a 0.3-0.5 s breath is wanted.
- Blip (jump): square sweep 520 -> 880 Hz, 0.12 s: `sign(sin(2*pi*cumsum(geomspace(f0,f1,n))/SR)) * exp(-linspace(0,5,n))`.
- Thud (crash): `sin(cumsum(geomspace(140,45,n))) + 0.4*noise`, decay `exp(-linspace(0,7,n))`.
- Whoosh into the run: smoothed noise x `sin(linspace(0,pi,n))^2`, 0.8 s, placed 0.25 s before the new part.
- Rising tick per cleared obstacle (`1320*2^((k%5)/12)` Hz, 0.12 s, gain .035); end chord C4 261.6 / G4 392 / C5 523.3 / G5 784 Hz sine, 3.5 s decay, gain 0.07; `tanh(mix*1.05)` soft clip; normalise to 0.89 peak; 0.5 s fade-out. Mux: `ffmpeg -i silent.mp4 -i sound.m4a -c:v copy -c:a copy -shortest -movflags +faststart`.

### Lessons from review

1. **Brand colours must come from the live site in dark mode, not from an old file.** First build took blue/pink/green from an old film; the reviewer wanted grey plus the chrome mark only: "make that a rule". Open the site in a browser, screenshot dark mode, read the colours.
2. **"Fix the format for X / horizontal"** means a native wide composition (game full width, title top-left, score/logo top-right, captions under the ground line, end card centred), not a crop.
3. **Re-record one line instead of the whole voiceover:** swap a phrase ("every single time" to a punchier line), trim silence, apply the same `atempo`, splice into the same slot so every other timing survives. If the splice jumps in tone, regenerate the full take in one go.
4. Replace a game-score readout with a tiny spinning chrome mark; add the site text top-left.
5. **Verify the delivered file, not the source.** Once, a shell loop (zsh does not word-split unquoted variables) wrote the new render to the wrong filename and the old file was delivered. Always transcribe the delivered file's audio and grab frames from it, and report against each requested change in a table.
6. When restyling logo text (e.g. chrome fill), change only the fill; the first attempt changed the letter shapes and was rejected.

### Prompts that would recreate it

**Short:** "Make a 34 s dino-game reel for YOURBRAND: the brand is the dino, [bad vendors/creators] are cacti, it crashes and restarts six times, then runs at 2x through YOURBRAND into the chrome mark and a black end card. Tall for Reels/TikTok/Shorts and a separate wide cut for X. Use the saved voice, sped 1.18x."

**Detailed:** "Create a pixel-art Chrome-offline-dinosaur-style reel, 1080x1920 at 30 fps plus a native 1920x1080 version, 34 s. Voice-over script (one take, library voice, `atempo=1.18`): 'Every [audience] doing [thing] is playing this game. You're the dino. The cactus is a [bad thing]. You dodge one. You dodge two. Then one [fails three ways]. Game over. So you restart. [Repeat]. Every [swear/emphatic] time. Now watch the same game, running through YOURBRAND. [Three benefits]. The dino doesn't restart anymore. It just doesn't stop. YOURBRAND. Stop restarting. Start running.' Draw the game on a 216x150 canvas scaled 5x with smoothing off. Place each cactus where the scroll will be when its spoken word starts; jump 0.28 s before the word. Pills on the dino and cacti. Crash screen at the first hit, restart counter 1-6 faster each time, one slammed word per syllable on the emphatic line, then white dino at 2x with speed lines and jump ticks, hitting a chrome monogram, white flash, circle reveal into a black end card with monogram, wordmark, two 84 px lines and the site. Palette: black, `#8b8b93`, white, cards `#161619`, silver `#d4d4d8`; no other hues. Keep type in x 70-940, y 250-1480. Synthesise blips, thuds, whoosh and a final chord; mux with `-c:a copy`. Check the delivered file by transcript and frame grabs."

---

## 2. Pixel runner on a dithered desert sunset

Second reel in the same series: same dino, same voice, same ending, new backdrop and a new metaphor (the cactus is a bad warm-up routine for new social accounts, the run is a multi-day automated warm-up).

- **Size:** tall 1080x1920 + native wide 1920x1080, 40 s, 30 fps, voiced.
- **Script structure:** (1) "Every brand doing X is playing this game. You're the dino. The cactus is a [bad routine]." (2) "You get lucky once. You get lucky twice. Then the views die, the reach tanks and the account gets banned. Game over." (3) restart, "New account. Same bad routine. Every [emphatic] time." (4) "Now watch the same game, running through YOURBRAND. One prompt. It creates, warms up and runs the whole process on its own. Three days minimum. No bad accounts. Not one ban." (5) logo line. One take, about 600 characters, 38.5 s raw. Write brand-sensitive words as two words for the TTS ("shadow banned").

### Beat sheet

| t | what happens |
|---|---|
| 0-6 | Sunset in hard pixels (deep purple top, magenta, red, gold horizon), banded half-set sun, two rows of mesas and tiny saguaros drifting, dark desert floor. Dino is a **black silhouette with an orange rim light**. White pill on the dino, dark pill on the first cactus. |
| 6.7, 7.92 | Two clean jumps ("lucky once / twice"). |
| 9.1, 10.1, 11.7 | Pills `x VIEWS DEAD`, `x REACH TANKED`, `x BANNED`; hit at ~12.76; GAME OVER. |
| 13.8-19.3 | "NEW ACCOUNT 1..6": runs `[13.85,14.95] [15.2,16.15] [16.4,17.2] [17.3,17.54] [17.62,17.92] [18.0,18.34]`; the three-word slam lands at 17.54, 17.92, 18.34 with a crash under each; slam window ends 19.25. |
| 19.32-35.5 | **Dusk:** sky cross-fades to the dusk palette in 0.6 s, stars appear, dino and ground turn white. "RUNNING THROUGH YOURBRAND", "2X SPEED", speed lines, jump every `0.74-0.012*i` s with ticks (DAY 1, DAY 2, DAY 3, WARMED UP, NOT BANNED). A bigger pill in the sky follows the voice line by line. |
| 35.5 | Dino hits the chrome monogram, white flash. |
| 35.75-40 | Same black end card as format 1. |

### Look and numbers

- Backdrop canvas is 1/5 frame size (tall 216x384, wide 384x216), scaled 5x with smoothing off; horizon row 230 (tall) / 148 (wide). Game canvas as in format 1.
- **Bayer-dithered sky:** build once per palette. Each row picks between two neighbouring colour stops with a 4x4 Bayer matrix `[[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]`: `f = pow(y/HY, 1.3 [wide 1.05]) * (stops-1); colour = frac(f) > (BAYER[y%4][x%4]+0.5)/16 ? stop[i+1] : stop[i]`. The floor uses `pow 0.55`.
- Sunset stops `#1a0a38 #35104f #641a63 #a3285f #d9414a #f46a33 #ff9a35 #ffc65a`. Dusk stops `#0a0520 #170838 #33104f #641a66 #a52a62 #dd4d48 #f47a36 #ffab45`. Floor `#3a1638 #241028 #150a1c #0a0510`.
- Sun: radius 30 px, three bands `#fff3b0 #ffd670 #ff9d4a`, sinks 22 px over the run; sun x 150 (tall) / 262 (wide). Additive radial glow (`globalCompositeOperation:'lighter'`) at full resolution, radius 60-760, alpha `0.34 - 0.1*dusk`.
- Mesas far `#8e3566 #5a2262` scrolling at 5% of the ground speed, near `#4a1a4f #2c1038` at 12%; cloud streaks `#ff8f7a #d9486b #8c2a73`; stones on the floor pass faster the lower they are (parallax).
- **Readability on a bright sky:** draw dino and cacti twice (offset 1 px in four directions in an edge colour, then the body). Silhouette body `#170b20`, rim `#ffb057`; after dusk, white body with a dark edge. Pills get a soft drop shadow (`rgba(10,4,18,.45)` blur 24, offset 6). Captions sit on the dark floor (y 1400 tall / 968 wide), title y 330 / 56.
- **Colour rule:** type, pills and logo stay in the brand's own theme; only the backdrop changed (that is what was asked). The end card stays black.
- Pills: round rect, width = text + size*1.1, height = size*1.75, font 700 (>=34 px) else 600; non-white pills get a 2 px `rgba(255,255,255,.16)` stroke.
- Voice pace after speed-up: 2.67 words/s.
- Sound additions: seven crash thuds (incl. three under the slam), jump blips gain .10, whoosh at the dusk change gain .5, chord plus thud on the monogram gain .3.
- Posting: tall file to the vertical platforms only, wide file to X only (see posting rules).

### Prompts

**Short:** "Same dino reel, but on a dithered desert sunset instead of black. The cactus is [a bad warm-up routine]. Dusk when the brand arrives. Same voice, same ending, tall and wide."

**Detailed:** "Reuse the dino-runner reel engine. New backdrop: a pixel sunset (stops `#1a0a38 ... #ffc65a`, Bayer 4x4 dithered rows), banded sun, two mesa parallax layers, saguaros, dark floor. Dino = black silhouette with orange rim light. Script about [topic]; one voice take; anchor every cactus, pill and jump to word times from a faster-whisper transcript. At the brand reveal cross-fade to a dusk palette in 0.6 s, add stars, turn the dino white, run at 2x with day-counter ticks and sky pills following the voice. Same end card. Draw dino/cacti with a 1 px edge outline for contrast on the bright sky. 40 s, tall + wide."

---

## 3. Black-and-white pictogram parable (one white person, capsule tags, dot grid)

**Look in one line:** pure black, a faint dot grid, one faceless white pictogram person on a dashed ground line, a soft glow behind whatever matters, small white capsule tags that name each beat in three or four words, and counters and typing that never stop moving. A parable told in long flowing sentences with a twist at the halfway point and a last line that lands as the title.

- **Platform / size:** Reels, TikTok, Shorts. 1080x1920, 30 fps, 68-73 s (about 65-68 s of voice plus a 2.7-5 s end card). 17-20 beats; a new picture every 2-5 s.
- **Built as:** one HTML canvas page, `render(t)`, frames screenshotted and piped to ffmpeg. Rendering a 72 s reel takes about 40 s.

### Structure (general)

1. Hook line that states a paradox ("The best X you've ever heard will never get built. And the reason explains why worse Xs keep winning.") over the person walking in, a glowing icon drawing itself, a counter ticking.
2. Camera slides to the contrasting object; a `?` bubble joins them with dashed lines.
3. Introduce the character ("that one friend who...") at a table of five people with a spotlight from above; a marker over his head makes him recognisable in a crowd.
4. The behaviour: a speech box types itself with a blinking cursor; everyone raises an arm with labels; calendar pages fly (a counter "+1 ... +3" years); a notes card "last edited 3 years ago".
5. "Nobody can explain why": two bystanders with `?`, a checklist card filling line by line (`BUILT X`, `STILL A GREAT IDEA tick`, `STILL TALKS ABOUT IT tick`).
6. The rule flip: split screen with a dashed divider; two cards that flip on the word "other" (`PERFECT IT -> THEN BUILD` flips to `BUILD IT -> THEN FIND OUT`).
7. The cost wall: a price tag swings out on a line and its number spins up, **landing exactly on the spoken number word**; a course card with a progress bar where lesson 4 gets a hand-drawn X.
8. Fog with a `?` and a person at a cliff; each step lights a bridge tile; on "taps" a fingertip touches an icon and the `?` flips to a tick.
9. **Product moment (first mention of the product, ~48 s in):** the cost wall lowers to ground level; a large phone fills the frame, a prompt types itself, the app assembles piece by piece inside (header, list, button, tab bar), `NO CODE` with a `</>` icon crossed out.
10. The rival: someone with a worse idea types it, ships something embarrassing; a patched rocket lifts off, chat bubbles hit it and each one swaps the version badge (`V1`, `V2`, `V3`).
11. The payoff: chart axes draw, the rocket rides a steep curve, a counter climbs, a crowd points up with speech bubbles (`LUCK!`), dice tumble; the last words land as a title (`THEY CALL IT LUCK`).
12. End card (no voice): fade to black; app icon outline draws; one line; then the store listing.

### Look and numbers

- Canvas 1080x1920. Background `#000`; radial wash `rgba(255,255,255,0.06)` centred at 42% height; dot grid `rgba(255,255,255,0.075)`, 2 px dots every 44 px (offset 28/30). Everything else white or grey. **No colour until the end card.**
- Ground: dashed line `[11,10]`, width 3, `rgba(255,255,255,.55)`, at y=1330.
- Person: filled white circle head (r 27*s) on a rounded body (66x96*s), no face; arm = round-capped 17*s stroke; optional marker (small bulb) above the head. Secondary people `#a6a6a6`. A `glow()` radial light (white, alpha .2-.5) sits behind the focus.
- Capsule tag: white fill, black text, weight 700, letter-spacing 0.14 x size, size 26-30, height 1.8 x size, radius full; pop-in with a back ease (scale .82 -> 1) and a soft glow. Never more than two at once plus small labels. Speech bubble: black fill, 3.5 px white stroke, text 22 px.
- Type: a geometric system sans in caps for tags; heavier for counters and the title.
- Motion rules: every beat has at least one thing that changes on its own (counter, typing, draw-on line, clock). Between beats the camera drifts or slides; nothing is still for more than about a second. Easings: `eo=1-(1-x)^3`, `eio` cubic in-out, `back` (c1 1.70158); seeded `rnd(i)=frac(sin(i*127.1+311.7)*43758.5453)`.
- End card: the product's store listing in dark mode drawn to the system layout (icon, name, subtitle, blue Get button, share glyph, ratings strip). Get is tapped at ~1.35 s, the download ring runs, it ends on Open. Read the listing facts from the store the same day and leave out any field where sources disagree (age rating).

### Voice and timing

- Script of 230-240 words for ~66 s; delivery about 5 syllables/s. Voice is a steady adult male (130-165 Hz target), recorded **line by line** (one paragraph per line) and each line re-rolled up to 4 times until its median pitch is inside the target band and the time-stretch stays under 1.3x; then joined with 0.14 s gaps. A single long take drifted from 155 to 184-211 Hz and blurred the last word.
- Beat times come from a `cues.json` of word start times (`C.reason`, `C.friend`, ...); each tag, counter and typing run is pinned to its word. The price counter lands on the word "forty".
- Write the brand name as two words for TTS if it is read wrongly.

### Sound (made from scratch, placed on logged events)

Measured from the reference by subtracting right from left (removes the centred voice): a music bed with one steady hit about every 1.08 s (~55 bpm) and bass entering around 35 s; bright clicks on pop-ins (10-25 ms rise, 15-60 ms fall, centred 8-9.5 kHz); soft swishes on scene changes (80-190 ms rise/fall, 6-8.6 kHz, landing 0.1-0.3 s after the picture changes); low thuds on stamps and landings (4-12 ms attack, 130-320 ms tail); end card: ~0.7 s silence then one deep boom (47 Hz plus 130 Hz, ~1.3 s, the loudest sound in the film).

- 277 sounds in the same four families plus a key tick per typed character, ticks under counters, rising pops as the app assembles, a low rush under the rocket, a tap click and blip on the store button.
- How it stays in sync: a small script plays the page silently and logs the first frame each tag, bubble, tick mark, card and typed character is drawn (`events.json`); the SFX script places sounds on those times plus a hand-timed list per beat. After any change to the picture or voice, re-run: events logger, SFX builder, renderer. A `--level` flag scales all effects together.
- Levels: clicks peak -15 to -18 dB, boom -7 dB. No music bed was copied (only the effects).

### Review lessons

- "Add SFX just like the original video": measure the reference's sound instead of guessing; copy families and levels, not samples.
- The ending must be the **recognisable store UI with the real app icon**, kept simple and clean; no link in bio exists on these accounts, so the call to action must be a clear search instruction.
- Voices that were "childlike" had medians of 254-291 Hz; adult female band is about 170-240 Hz, adult male 95-150 Hz.
- The first cut had a scene that sat empty for two seconds; add a start screen or something moving. Blurred whip-pans in the reference were plain slides in the first build.
- Claims discipline: a final counter such as "100,000 users" or a dollar quote is a claim; label story details as story, leave stats out unless real.

### Prompts

**Short:** "Make a 70 s black-and-white pictogram reel for YOURBRAND in the style of [reference reel]: one white faceless person, dashed ground, dot grid, capsule tags, counters and typing always moving. Story: the friend with the best [idea] never builds it, someone with a worse one wins; the product enters at ~48 s as a phone that builds the app from one sentence; end on a store card. Voice: steady adult male, 5 syllables/s, SFX measured from the reference."

**Detailed:** "Watch the reference reel frame by frame (contact sheets at 2 fps, scene-cut detection, whisper transcript with word times, pitch and loudness). Write a parable that keeps the skeleton (paradox hook, twist at the halfway point, last line as the title) but swaps every tag, counter and prop to fit [topic]. Draw it as an HTML canvas at 1080x1920, `render(t)`, black background with a `rgba(255,255,255,.075)` 44 px dot grid, a dashed ground at y=1330, a white pictogram person, white capsule tags (size 28, weight 700, spacing .14em), counters, typing boxes, checklists, flip cards, a price tag that lands on the spoken number, calendar pages, a cliff and bridge, a desk and clock, a rocket with version badges, a chart, a crowd. Record the voice line by line with a pitch band of 130-165 Hz and a stretch cap of 1.3; pin every beat to word times. Build SFX in four families from the reference's measured envelopes and place them from a logged event list. No colour until the end card, which is the store listing with the real icon. Render frames to ffmpeg (CRF 17), mux with AAC 192k. Give me a contact sheet of every beat before the full render."

---

## 4. Black-stage "pawn" explainer engine (one JSON spec per video, voice is the clock)

**Look:** black stage (`#000`/`#0b0b0b`), faint dot grid, soft blurred bokeh circles, **one** spotlight cone (white 34% to 5% gradient, blur ~22 px) with an elliptical floor pool, a single white pawn figure, heavy counters (Heavy 800 weight), tiny wide-tracked uppercase labels (600 weight, letter-spacing 6 px, alpha .62, 22 px), dashed rings around line icons, and white caption pills (`#f3f3f3` with `#0b0b0b` heavy text, letter-spacing 5, fully rounded, glow, back-ease pop .72 -> 1 with a 24 px rise) that repeat the spoken phrase, one at a time at y 1440-1470. Two accents only: ember orange (money burning, errors) and mint (approved, posted). A light variant: white stage, dark pills, orange and black type.

- **Size:** 1080x1920, 30 fps (60 fps for a 16:9 cut), 28-65 s, voiced. About 1-2 minutes to render 1,500 frames.
- **Engine:** `specs/<name>.json` = `{title, voice, theme?, captions?, handheld?, lines:[{say, scene, p:{...}, pills:[[TEXT, anchorWord | [word,n] | fraction | null]]}]}`. `say` must be exactly what the voice says; consecutive lines with the same `scene` share a segment; the last line is always the end-card scene. Build: `./build.sh specs/x.json voice/take.mp3 [tempo]` glues the drawing kit and a scene library into one page, tempo-adjusts the voice to 48 kHz mono, transcribes word times, renders frames, exports `window.SOUNDS` and `window.VO` cue lists, builds the soundtrack from the cues, muxes.
- **Scene library examples:** counter-burning-money, flakes, treadmill, owners-quitting, versus, title slam, one-camera UI flow following a white ball, strike-through, DMs stacking, hire-flake-fire loop, recruiter stamp, network, brief, side-hustle cards stamped "NEVER PAID", payflow, selfie/actor (clapperboard, front camera), new-page, per-post paid tags, usage rights stamp, subscriptions cancelled, ad-skip, store card, end card.
- **Timing:** word times from faster-whisper (`small.en`, int8, `initial_prompt` with tricky terms). Hazards: repeated anchor words ("your", "a", "and", "it") pin cuts to the wrong occurrence, so anchor to the n-th occurrence or a unique line start (a cut once came 5 s early); Whisper splits "done-for-you" or domain names, so write the `say` line the way it will be heard; it hears "their" twice.
- **Script rules the reviewer set for this family:** order = hook, second hook, emotional line, what you offer, close, end card; one recurring signature word in every script; full sentences in the voice-over (short fragments are fine on screen pills but a run of 3-word punches was rejected); the end card is always the same (wipe to a light glass stage, logo animation, one line, site pill) and never the words "BY YOURBRAND".
- **Daily generator:** a local script on a scheduler (no AI call, no assistant session, free local voice) picks one beat per slot from a beats file (4 hooks x 3 second hooks x 3 emotional lines x 2 offers x 3 closes = 192 combinations), never repeats a combination, skips scripts missing the signature word, drops finished videos plus caption text in a dated folder, never posts. Caveat: all combinations reuse the same dozen scenes and look alike after a week or two.
- **Reviewer corrections:** he rejected a build that explained the business model wrongly (who posts, who gets paid). Lesson: before scripting an explainer, write the business mechanics in one paragraph and get them confirmed; mark scenes built on a wrong model "do not use". Label example numbers "example"; never show real rates you do not know.

### Prompts

**Short:** "Make a 40 s pawn-on-black-stage explainer for YOURBRAND: hook 'Tired of [pain]?', one emotional line, the offer, the close, the standard end card. Use the engine and the saved voice; spec JSON plus build."

**Detailed:** "Write a spec JSON for the pawn engine: lines with `say`, `scene`, and caption pills anchored to spoken words. Look: black stage, dot grid, one spotlight, one white pawn, heavy counters, tracked labels, ember orange for cost and mint for success only. Voice in full sentences, one take, word times from faster-whisper. End on the standard end-card scene (light glass stage, logo animation, 'Your [platform]', site pill). Output 1080x1920 30 fps, loudness -14 LUFS, contact sheet of every scene first."

---

## 5. Stamped-word feed-scroll brand film (light stage, modelled on a viral UI-concept reel)

**Look in one line:** a bright stage where a social post card bursts in with stamped words, a feed scrolls into a blur, a dark "and just like that" beat, a giant slam word, an LED-dot "but what if", a popup with a cursor click, stacked notification cards, bracket-tagged cards, a spotlight joke, and a quiet end card.

- **Platform / size:** brand home page and social, wide 1920x1080 and tall 1080x1920, 30 fps, about 30 s (29 s after revision). H.264 yuv420p, AAC.
- **Origin:** modelled beat for beat on a viral UI-concept reel (a designer account, After Effects, 38.97 s). The reference was measured: narrator median pitch 216 Hz (p10 160, p90 286), about 137 words per minute, speech from 0.0 s.

### Beat structure (final cut, seconds after voice start)

1. 0-3.9 "Film it / Post it / Boost it / Refresh..." post card bursts in (scale 3.4 -> 1, rotate -9 -> 0, spring), stamped words on a blue bar, cursor click, red handwritten annotation with an arrow.
2. ~3.7-6.7 dark beat "And just like that... you lose it", a tiny card dropped.
3. ~6.7 "IN THE" sweep, blurred feed strip (three rows at 2,600 px/s x (1+row*.25), blur 14 px, two arrows), **"ENDLESS FEED" slam** (the word FEED sits under the E, centred, line-height .88).
4. ~7.8 "But what if..." (originally an LED-dot background with a rotating conic glow masked to dots; the reviewer later removed it).
5. ~8-13 a phone drops from the top, "your brand had a thousand creators?", 36-48 creator tiles fly in staggered and spiral into a grid.
6. ~13 popup card with a toggle, three fields, a budget slider, a gradient "Launch" button; cursor click; "And done..!" with a bouncing monogram badge and shadow.
7. ~14 stacked notification cards ("Campaign is live", "24 creators matched", "6 new videos ready").
8. ~15 AI review card (poster, score ring counting to 92, "Approved / Hook 0.8 s" chips, bracket tag `[ review every video ]`).
9. ~17 four platform cards or a row of phones with platform pills (`[ post it everywhere ]`).
10. ~18.5 counter ticking to a huge view count, chart line draws.
11. ~20.7 payout card, confetti burst (26 pieces), `[ pay on results ]`.
12. ~21.3 spotlight joke beat: black radial mask, card "Posting schedule: Every day ( forever )", yellow handwritten "Forever?" rotated -7 degrees with a drawn underline, white "Forever." 
13. 25.6 end card (chrome monogram, "MADE BY CREATORS", site, tagline; later a wordmark with a "Book a call" button, cursor click, site typing).

Scene cuts are word-anchored and land **0.02-0.18 s before** the word (the eye reads the picture first). Anchors in the final cut: dark = "and" minus .16; sweep = "in" minus .02; strip = "endless"; slam = "feed" + .02; phone = "your" minus .02; popup = "pick" minus .06; done = "done" minus .02; notifications = brand name minus .04; review = "review" minus .04; pay = "pay" minus .06; joke = "forever" minus .5.

### Look

- Stage `#f2f2f4`, ink `#0b0b10`, muted `#5f5f6b`, card `#fff`. Brand blue `#2f6bff` (dark edge `#1a46c9`, cyan `#38bdf8`, button gradient `#3b82f6 -> #2563eb`), toggle green `#34c759`, ok chip `#1f8f3e` on `#e8f7ec`, red annotation `#e5262b`, heart `#ff3056`, joke yellow `#ffe600`. Pills: `#0b0b10`, `#e1306c`, `#ff0000`, `#1877f2`. Confetti `#2f6bff #ffd23d #ff2e97 #38bdf8 #1f8f3e`.
- "Lose it" beat: radial gradients of `#ff6a3d` and `#ff2e97` over `linear-gradient(180deg,#0e0a12,#2a0f23)`; hot gradient text `linear-gradient(92deg,#ff7a3d 0%,#ff2e97 55%,#7c3aed 100%)`.
- Type: SF Pro Display (Regular to Heavy loaded as local TTFs); handwritten annotation in a marker-style cursive. Stamp words 800 weight, letter-spacing -.06em, uppercase, white on a blue bar with a `0 .1em 0 #1a46c9` under-shadow. Slam word 800, -.055em, line-height .9, 200-236 px. Sentence words 500-600, -.02em. No emoji anywhere; icons are inline SVG.
- Post card (the UI atom): 9:16 rounded card (28 px), poster `object-fit: cover`, bottom gradient (transparent 45% to `rgba(0,0,0,.72)`), handle bottom-left, right rail of icons with counts, shadow `0 40px 90px -30px rgba(0,0,0,.55)`; font-size = 8.5% of card width so everything inside scales.
- Popup card: radius 26, white, shadow `0 50px 110px -30px rgba(0,0,0,.45)`.
- Tall layout uses a 0.74 type scale and re-laid positions (stacked sentences, 2x2 cards).
- Bracket-tag device: small dark rounded tag `rgba(0,0,0,.72)`, white 600 weight, `[ review every video ]`.

### Motion rules (all pure functions of time)

`eo=1-(1-x)^3`, `eo5`, `ei=x^3`, `eio`, `eio5`, `spring(x,k=7,f=11)=1-e^(-kx)cos(fx)` (k 6-9, f 9-13). Word-in: spring over `dur*2.2` with dur .22, translateY `(1-q)*30`, scale .7 -> 1, opacity `clamp(q*1.6)`. Refresh scroll: `ei` over .9 s, column moves 4.2 card heights, blur peaks 22 px, refresh icon spins 900 deg/s. Cursor click: glide in `eio` over .5 s ending .05 s before the click, press scale `1-.18*sin(pi*...)`, ring 20 -> 140 px fading over .5 s. Slam: spring scale 1.35 -> 1 with a 6 px shake `sin(t*200)/cos(t*170)`. Tile burst: stagger `rnd*.35 s`, spring(6,9), rotation `(1-q)*(rnd-.5)*90`.

### Sound (synthesised)

122 BPM A minor (Am F C G, one chord per bar). Intro: detuned saw plucks (two saws x1.004 through a one-pole low-pass with an envelope-swept cutoff), offbeat hats, rising kick, noise riser (2.2 s) into the slam. Groove from the slam: four-on-the-floor kick (sine 48 Hz + `120*e^(-t/.03)` pitch drop), claps on 2 and 4 (three noise bursts 9 ms apart plus tail), open hat on the offbeat, 16th closed hats, bass (sine + .35 low-passed saw), stabs. Drop-out for the joke (one pluck per bar), soft pad under the end card, impacts at the big moments (sine 38 Hz + `60*e^(-t/.05)` drop + filtered noise), `tanh` soft clip, 1.4 s fade. Ducking: `gain = 1 - .5*clip(voiceEnv/.05)` smoothed 80 ms. SFX: whoosh on every cut (band-passed noise sweep .42 s), pops on word reveals (sine 880 + `700*e^(-t/.018)`), cursor click (high-passed noise 60 ms + 1,600 Hz pop), key ticks under the counter, confetti pops, stamp pops pitched `640 + i*90` Hz. A later engine lets scene code call `cue(t, kind)` and exports a cue list, so audio always follows the picture.

### Voice

A bright, warm, mid-pitched female **library** voice (median ~225 Hz) chosen because its pitch and pace matched the reference narrator; **do not clone a real narrator's voice**. A male candidate at 154 Hz was too low. Processing `atempo=0.93,loudnorm=I=-16:TP=-1.5:LRA=9 -ar 48000` for the early cuts; later cuts used the natural pace ("voice fast and flowy"). Check the transcript for brand-word mispronunciation (a first voice was transcribed back as a different word).

### Revision lessons

- Keep the same voice across sibling films; the second voice sounded more appealing.
- Real screenshots of the **current** product beat flat mock cards.
- Do not centre the film on the reviewer or his accounts: use other creators' posters and faces and invented names.
- Text that reads word-by-word too spaced out: build lines as flex rows (gap only, no doubled margins) so it reads as a sentence; centre, do not left-rag.
- A first poster with a loud caption read as the hook (reviewer note): swap the opening card to something visual.
- The loud LED-dot background was removed; the section became about the actual product behaviour.
- One reviewer note worth keeping: cut a 1.7 s gap between two repeated lines and shorten a 7 s end card.

### Prompts

**Short:** "Rebuild this viral UI-concept reel [link] as a 30 s motion graphic for YOURBRAND: same skeleton (stamped words on a post card, feed blur, dark 'just like that' beat, giant slam word, popup with cursor click, notification cards, bracket tags, spotlight joke, quiet end card), our colours and real product screens, a female library voice matched in pitch and pace to the original narrator (not a clone), synthesised music and effects on the cuts, wide and tall."

**Detailed:** "Download and study the reference (contact sheets at 2 fps, scene cuts with `select='gt(scene,0.25)'`, whisper word times, pitch percentiles with an autocorrelation tracker). Write a 22 s script that keeps its rhythm: [three verbs], 'and just like that, you lose it in the endless feed. But what if [your product did X]? [Three steps]. 'Forever?... Forever.' Build one HTML page with `render(t)` for both layouts. Use the palette and motion constants above. Anchor every cut to word times, 0.02-0.18 s early. Synthesise a 122 BPM bed with ducking. Mux at -16 LUFS. Show me stills of every scene in both layouts before the full render."

---

## 6. Full-platform product film: real feed scroll, red X, flash cut into a dark glass product tour

- **Size:** wide and tall, 76-83 s, one long voice take (about 180 words, numbers spelled out as words).
- **Structure:** opens like format 5 (three verbs, "and just like that, you lose it") then:
  1. "IN THE" sweep; a real phone rises showing a vertical feed (tabs, right rail, captions, bottom bar) snapping video to video like a thumb scroll, speeding 1.75x under the slam with two blurred ghost phones flying past (blur 4 and 7 px, opacity .38, perspective yaw); tag `[ 10,000 videos an hour. Yours was one of them. ]`.
  2. **Red X** draws over the phone (two dashed-draw strokes, .22 s each, `#ff2a4d` with glow); the phone goes grey (grayscale + brightness .65); "But what if the feed worked for you?"
  3. **The flash is the cut:** on "Meet [product]" the phone switches to a flashy clip and zooms until it fills the frame (scale-to-cover, saturate 1 -> 1.8, brightness +.35, shake up to 10 px), a white hit (opacity .85 -> 1 in .11 s), and we land in "our world".
  4. **Our world = dark aurora:** `#07070a` with three blurred blobs (`#7c3aed` .5, `#2f6bff` .4, `#ff2e97` .28; each a radial-gradient circle 95% of the width, blur 30 px, drifting on sin/cos at 0.17-0.27 Hz), a bottom white haze; windows fly in with perspective, depth-of-field blur and a purple glow (`0 0 90px rgba(124,58,237,.22)`); key words get a glowing bracket (`.hl`).
  5. Tour of the product with real recordings: campaign set-up, brief/deliverables/pay terms callouts, agreement signing with a drawn signature, group chat, vetted creators with check marks, connect-account flow, analytics counting up, draft submission, the AI reviewer running for real (scan, stages ticking, callouts), a stats beat, "Good to post? One click" with an Approve click and a timestamped fixes list, a wall of posting phones, tracked views, payout calculations, two dashboards.
  6. Spotlight joke beat, a hard cut to a fast "LAUNCH YOUR [X] / FOR FREE TODAY" slam (each word slamming, glowing bracket on FREE, hit + shake), then wordmark with a light sweep, an orbit of 16 real posts on a tilted ring (radius 760, ry 110) plus 6 face avatars on an inner ring turning the other way, 40 drifting particles, a CTA button (glow `0 0 60px rgba(47,107,255,.55)`) with a cursor click, site typing with a caret, tagline.
- **Reviewer notes that drove v6 -> v8:** more human (more faces); **every number must agree** across scenes (a "live" dashboard at one total and a counter at another broke trust: reshoot everything at one completed state); the ending must look expensive (liquid glass, depth, light); voice fast and flowing (natural pace, `loudnorm` only, no slow-down); use the reviewer's own phone recording of the real feed (Control Center screen record, 41 s, HEVC) with frames extracted at 30 fps to 540 px webp, status bar cropped, black "unavailable" frames skipped (detected with `signalstats` on a 32x32 downscale at 4 fps); never show a page that reveals what creators are paid.
- **Capture harness (reusable):** a tiny dev-server harness (own config) renders the product's public demo views without sign-in. Playwright at viewport 1600x1000, `deviceScaleFactor 2`, dark colour scheme: stills at 3200x2000; clips as `recordVideo` webm then `ffmpeg -vf fps=15 -c:v libwebp -quality 82 f%03d.webp`, with `frame = floor(t*fps)` inside the render page. Jobs are scripted (type with 45-55 ms key delay, draw a signature on a canvas through ~10 mouse points, click Continue every 1.9 s, wait 4.5 s for charts to animate). A MutationObserver plus route interception rewrites the founder's real name, handle and photo so the film never shows the reviewer's account. Media served with `Cross-Origin-Resource-Policy: same-origin` will not load in a localhost harness: route those URLs to local copies (this caused black boxes in the reviewer panel).
- **Delivery detail:** wide master was 31.5 MB, over a 30 MB chat attachment limit: send a smaller web copy as well.

### Prompts

**Short:** "Make the full product film: real feed scroll with a red X, flash cut into a dark liquid-glass tour of both sides of the product, one completed demo state so every number matches, real faces from other creators, end on a CTA slam and an orbit of posts. Wide and tall, 80 s."

**Detailed:** "Record the real vertical feed on my phone (screen record) and the product's demo views with Playwright at 2x. Build one `render(t)` page. Script [183 words, numbers as words]. Cut sequence: verbs, feed scroll in a phone that speeds up under the slam, red X, grey phone, 'what if the feed worked for you', flash zoom, white hit, dark aurora stage (hex above), tilted windows with glow, callout brackets on key words, tour in this order [list], stats beat, approve click, tracked views, payouts, spotlight joke, launch slam, wordmark with sweep, orbit ring of posts, CTA button with click, typed site. Invented names only; label sample data. Voice at natural pace, mux at -16 LUFS."

---

## 7. No-voice 3D logo ident (4K 60 fps)

- **Size:** 40 s, wide and tall, rendered 4K (device scale 2) at 60 fps plus 1080p copies; masters 80-95 MB. No voice; a synthesised cinematic score at -14 LUFS.
- **Origin:** an X launch post of a motion tool: a 44 s dark 3D product ident. The hits of its audio (2.6, 6.1, 9.6, 16.7, 20.2, 30.8, 34.4 s) were copied for the beat structure (the track itself was **not** used; a synthesised score with the same shape was built).
- **Beats:** (1) a point of light; the chrome monogram turns in from dark with blue and violet rim light; first hit: shine sweep + three expanding rings; it rises to the top. (2) A glass prompt bar in perspective slides up, types a request (glowing caret, typing ticks), a cursor hits send, the bar flares and pulls through the camera. (3) The dashboard flies through 3D beside a phone playing the real feed, posts drifting in depth; the next hit swaps to the second dashboard and phone. (4) Reviewer window with the scan, then timeline bars (Hook, Value, Proof, CTA, Fix) growing under a scanning playhead. (5) Extreme close-up of the Approve button with a neon green rim, pulls back, click. (6) Seven phones rise in 3D with a chip. (7) Quiet kinetic type over a drifting light ribbon; the monogram alone; a last shine; fade.
- **Build details that mattered:** monogram as a 14-slice extruded slab with a moving reflection band; blue rim (`#7dd3fc`, blur 7 px, screen blend) and violet rim (`#c084fc`, blur 9 px), blue back-glow (`#2f6bff` blur 55 px), red/blue chromatic split on hits, anamorphic streak plus core flash, wide shockwave. **Rim lights are masked fills with blur applied on a wrapper** (a filter on the masked element itself is clipped by the mask). Mask-image is blocked on `file://`: serve the page over `http` (a local static server) when using masks. Dashboards assembled card by card: every rounded panel photographed as its own transparent layer at 2x (`omitBackground`) and flown in with stagger and spring. Film grain texture, vignette, falling bokeh over everything. A source logo of only 558 px upscaled 2x looks soft: start from a big master.
- **Score recipe:** supersaw pad with chorus and a breathing filter over four chords, sub bass on chord roots, drone bed, half-time 808 groove at 94 BPM with sidechain pump on the pad, snare, hats, pluck motif with ping-pong delay, layered impacts (sub drop + thud + air + reverb tail), pitched risers with a reverse-cymbal swell before cuts, whooshes on 3D moves, **real keypress and click samples** for typing and send, bell shimmers under quiet lines, FFT hall reverb on a send bus, soft clip, loudness -14 LUFS at mux.
- **Render:** `PAGE=ident.html DPR=2 FPS=60 BASE=http://127.0.0.1:PORT node render.cjs video W H out.mp4 layout 1`, then `ffmpeg -i silent -i wav -af "loudnorm=I=-14:TP=-1.0:LRA=9" -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 320k -movflags +faststart -shortest`. About 25 minutes for both shapes.
- **Reviewer feedback:** v1 was rejected bluntly ("much, much better"). Rebuild with layered objects, real depth, a cinematic score, much more fidelity. Use only the logo mark, never the wordmark, in this ident; read the reference post's caption in the browser.

### Prompts

**Short:** "No-voice 40 s dark 3D ident for YOURBRAND using only the chrome monogram: rim-lit logo sting, typed prompt bar in perspective, dashboards and phones flying through 3D, timeline bars, neon button close-up, quiet kinetic text, back to the logo. 4K 60 fps, wide and tall, synthesised score at -14 LUFS."

**Detailed:** "Build a 40 s, no-voice, dark 3D ident for YOURBRAND using only the chrome monogram (never the wordmark), modelled on [reference post] (read its caption in the browser; copy its audio hit points at 2.6, 6.1, 9.6, 16.7, 20.2, 30.8, 34.4 s but not the track). Beats: point of light; monogram turns in with blue `#7dd3fc` and violet `#c084fc` rim lights (masked fills with the blur on a wrapper), shine sweep and three rings on the first hit; a glass prompt bar in perspective types a request and flares through the camera; dashboards assembled from transparent 2x card layers fly through 3D beside phones playing real feed frames; timeline bars grow under a scanning playhead; neon-rim Approve button close-up and click; seven phones rise; quiet kinetic text over a light ribbon; monogram alone, last shine, fade. Add grain, vignette and falling bokeh. Serve the page over http because of masks. Render 4K at 60 fps in four parallel slices plus 1080p copies. Synthesise the score (supersaw pad, sub, half-time 808 at 94 BPM with sidechain pump, pluck motif with ping-pong delay, layered impacts, risers, whooshes, real key and click samples, FFT hall reverb) at -14 LUFS. Give stills of each beat before the long render."

---

## 8. Colour-poster "slam" film (one flat colour per beat, type cropped by the frame)

- **Size:** wide, 27-28 s, 1080p, 140 BPM half-time 808 hits locked to words.
- **Idea:** a poster that changes on every word: full-bleed flat colour per beat, type big enough to crop, hard cuts locked to the voice, real creators' videos playing inside the letters (the word VIDEO cut out of a strip of 14 poster tiles), a stutter-shake on "No. No no no. NO!", a struck-through competitor link, an acid-yellow sheet.
- **Palette:** blue `#1E2BFF`, red `#FF2A12`, acid `#D4FF12`, pink `#FF2A8D`, ink `#0A0A0C`, paper `#F5F1E4`, violet `#7A1FFF`, green `#00D97E`, orange `#FF7A00`, sky `#19C2FF`.
- **Type:** condensed black grotesque (Helvetica Neue Condensed Black, Impact as fallback), uppercase, line-height .84, letter-spacing -.012em; a `fit()` helper auto-sizes words to a width after fonts load.
- **Slam animation:** arrives oversized (1+.42), lands in 0.1 s (`out3`), keeps creeping +2.2%/s so a held word is never still; pop-in with `back` ease .24 s; stutter = `sin(t*190)/cos(t*240)` jitter decaying over .22 s.
- **Script pattern:** accomplishment, then the humiliating default ("you send them... a [cheap template]"), "No. No, no, no. No!", "You're not a [bad thing]. You're a business. So look like one.", short product nouns one per beat, brand, call to action.
- **Bugs to avoid:** scene-show/hide CSS fighting inline display (store the original `display` on show); words cropped (auto-fit); a blank beat before a word (move the boundary to the first word of the new idea); a sheet held at the wrong alpha making the key word unreadable.

**Short prompt:** "A poster film where the whole frame is one flat colour per beat, huge cropped uppercase type, hard cuts on every word, real clips inside the letters, a stutter on 'No', 28 s, 140 BPM hits on words. Product: YOURBRAND."

**Detailed prompt:** "Write a 27 s script in this shape: an accomplishment ('You made the video. You got the views.'), the humiliating default ('then they say send me your link, and you send... a [cheap template]'), 'No. No, no, no. No!', 'You are not a [bad thing]. You are a business. So look like one.', then product nouns one per beat, brand, call to action. Build a `render(t)` page where each beat is a flat full-bleed colour from `#1E2BFF #FF2A12 #D4FF12 #FF2A8D #0A0A0C #F5F1E4 #7A1FFF #00D97E #FF7A00 #19C2FF`, uppercase condensed black type at line-height .84 auto-fitted to width, words arriving at 1.42x and landing in .1 s then creeping +2.2%/s, hard cuts on word starts, a stutter shake (`sin(t*190)/cos(t*240)` decaying over .22 s) on the No beat, the word VIDEO cut out of a strip of 14 poster tiles, a struck-through link. Synthesise 140 BPM half-time 808 hits locked to words, silence plus a limp note for the bad screen, a five-hit climbing stutter on the No beat. Voice at natural pace, -16 LUFS."

---

## 9. Ring-of-phones film (3D ring, screen floods with each layout colour)

- **Size:** wide, 31-32 s, 100 BPM arpeggio climbing one chord per layout.
- **Idea:** a 3D ring of real phones in true perspective (`preserve-3d`); the ring fans open then closes; the screen floods with each layout's colour (a circle grows from the centre on every change); the page on the phone swaps through 10 venetian slats while the buyer's content stays pinned (shows "only the look moves"). A grey "everything looks the same" wall with skeleton cards and a ticking clock for the problem beat; the music drops to a grey drone and clock ticks there. Six accent colours, one per layout (`#FF2E88 #FF6A00 #4A12FF #00C795 #FFC400 #0A3CFF`).
- **Gotcha:** never put a CSS `filter` on a 3D-transformed container; it flattens `preserve-3d` and both faces show. Blur each face or the wrapper instead.
- **Script pattern:** "Every X looks different. So why does every X's [thing] look the same? Here are six ways to look like you... One click and the whole thing changes. Your words stay. Your videos stay. Only the look moves."

**Short prompt:** "A 31 s film with a 3D ring of phones in perspective, a colour flood on each layout change, content pinned while the look swaps via slats, a grey 'everything looks the same' wall for the problem."

**Detailed prompt:** "31 s wide film, bright library female voice, 100 BPM arpeggio climbing one chord per layout. Opening problem: a grey wall of identical skeleton cards with a ticking clock and a grey drone. Then a ring of 6 real phones in `preserve-3d` perspective (no CSS filters on 3D containers) that fans open and closes; each layout change floods the screen with its colour (`#FF2E88 #FF6A00 #4A12FF #00C795 #FFC400 #0A3CFF`) via a circle growing from the centre; the page swaps through 10 venetian slats while the buyer's videos and numbers stay pinned; a browser scene on the buyer's own domain; end card. Script: 'Every X looks different. So why does every X's link look the same? Here are six ways to look like you...'. Invented cast, 'Sample data' tags."

---

## 10. Dark-stage "cinema" product film (one light beam, orbiting avatars, tilted windows)

- **Size:** wide, 42.65 s, 4K master + 1080p + web copy, one female library voice, 104 BPM bed. The film that was kept live.
- **Reference language (7 references studied frame by frame):** one dark stage with ONE wide light beam, glowing avatar circles orbiting in the dark, everyone turning into the same grey silhouette card ("this is you"), screens streaming past the camera with motion blur (the scroll animation), UI windows tilted in 3D with a violet rim and a label beside them, dashboards on dotted lines with a checkmark row, big white words appearing one at a time with ONE outlined word, a TV switch-off only at the very end.
- **Look:** ink `#0B0C14`; stage radial `#120E24 -> #07060C`; accent `#8B7CFF`, second accent `#5B4BE8` (violet is the only colour); violet haze low in frame (radial `rgba(109,90,230,.55)` blurred 40 px); beam = blurred gradient band rotated -4 to -14 degrees, `mix-blend-mode: screen`, thin hot core; dot texture `rgba(255,255,255,.07)` on a 28 px grid; vignette; film grain at opacity .07 (SVG feTurbulence, overlay). Type: SF-style bold, letter-spacing -.035em; outlined pill word = `inset 0 0 0 .05em ACC`, colour ACC, padding `.02em .32em .08em`, radius .3em. Glass chips `rgba(18,15,34,.72)` + inset 1px `rgba(255,255,255,.14)` + a `rgba(139,124,255,.22)` ring + big soft shadow; "Sample data" tags on invented numbers. UI windows: radius 20, `#0E0C1A`, violet rim glow, 46 px title bar with traffic dots and a URL pill; flip between recordings with a diagonal mask wipe (100-degree gradient mask sweeping 130%, .26-.34 s). Phone: black titanium band gradient, bezel, island. Avatar orb 190 px with a coloured 3 px ring and glow.
- **Beat sheet (all times +0.3 s voice offset):**
  1. 0-5: seven glowing portrait orbs (`#8B7CFF #FF8FE0 #7DD3FC #A7F3D0 #FFFFFF #C4B5FD #FDBA74`) orbit an ellipse (r 540x250) and rush in from z -900; "Every creator looks different." (116 px); at ~2-2.9 they go greyscale and slide into a row of identical grey silhouette cards (220x330, `#1a1a22`); "So why does every creator's link look the [same?]" (86 px, outlined pill on the last word).
  2. 4.9-11.75 the scroll: a phone flies in from z -1200 with 30 degree yaw; a feed of 12 clips snaps (each .34 s `out5`) on 12 word-anchored times while 28 more clip cards stream toward the camera in 3D (z speed 520 px/s, loop 4,400, blur by distance); giant niche labels change beside the phone with a thin accent underline growing.
  3. 11.5-15 six sites as six phones on an arc (spacing 360, z `-230*|o|`, yaw `-11*o` degrees), staggered .07 s, "Every one deserves its own site."
  4. 14.6-26 the demo in a floating 1180x784 window tilted -18 degrees with captions beside it each word-by-word ("Type your name / Pick a look / Add your numbers / Drop in your videos / Hit publish / You're live"); the window straightens on "live"; clips lift off the page toward the camera; the full-height page flies past the camera; glass chips with real numbers lift off with settle.
  5. 25.8-28 media-kit phone with side labels.
  6. 27.8-32.2 three dashboard windows (rotateY +-12) on dotted SVG connectors, a checkmark row lights each window (brightness 1.06 vs .55 for the others), inbound inquiry cards fly in.
  7. 32-38 one window swaps among six layouts (14 swaps) with look-name pills on a glass ring; "Your videos stay / Your numbers stay / Only the [look] moves" while the window dims to .45.
  8. 37.7-40.6 end card in the beam: chrome wordmark (dark-background cut) with violet glow from blur(12px), "Pick your [look.]" (104 px), a white pill CTA, domain; then a TV switch-off (about 2 s appended after the end card).
- **TV switch-off close-out (reusable):** a canvas drawn per frame: three colour-tinted copies of the end-card still (R, G, B multiply) drawn with `lighter` blend in 6 px strips with horizontal offsets (RGB split 6 to 50 px growing), per-36px-row tear (random hash per frame), sine wobble `sin(y*.018+s*34)*14`, a moving noise band, vertical roll, snow from four pre-rendered noise canvases (480x270 at frame%4), 4x4 scanline pattern `rgba(0,0,0,.34)`, vignette; at 1.34-1.6 s the picture squashes vertically into a 5 px line while white blooms; 1.62-1.82 s the line collapses to a dot with a blue-white gradient and fades; the whole effect is ~2.05 s. Sound: snow bursts that grow, a 7.8 kHz flyback whine, a falling square zap (`60+2200*e^(-t/.07)` Hz, low-pass 5 kHz), a low thunk (`34+60*e^(-t/.04)`), a final click.
- **Reviewer feedback (the pattern):** stop using the same person as #1 in every scene (rotate the lead); stop the same simple UI; **recognise what the references have in common and reproduce those exact devices**; "stop overcomplicating it". A device the reviewer explicitly pointed out in a reference (the feed-racing scroll) must be in the film or he notices. Use his own real site and one real account's clips under invented names where he says so.
- **Ship rule:** upload under a **new filename** (intro5 -> intro6) so caches update; verify in a real browser at 1440 and 375 px widths.

**Short prompt:** "A 43 s dark-stage product film: one violet accent on near-black, one light beam, orbiting avatars turning into identical grey cards, a phone feed snapping while clip cards fly past the camera, six sites on an arc, a tilted setup demo with word-by-word captions, dashboards on dotted lines, one-click look swaps, end card then a TV switch-off. SF-style bold type, library female voice, 104 BPM bed."

**Detailed prompt:** "Build the 43 s dark-stage film as 8 acts exactly as the beat sheet above (orbiting avatars to grey cards; the feed scroll with 12 snaps and 28 streaming cards; six phones on an arc; the tilted setup demo with word-by-word captions and an outlined pill word; chips lifting off the page; media-kit phone; three dashboards on dotted lines with a checkmark row; six layout swaps with pinned content; end card in the beam; TV switch-off). Colours ink `#0B0C14`, accent `#8B7CFF`, second `#5B4BE8`, stage `#120E24 -> #07060C`, beam as a blurred rotated gradient band in screen blend, grain at .07. All anchors from word timestamps (+0.3 s offset). Invented names only, real numbers or 'Sample data'. 4K master, 1080p, web copy; mux at -16 LUFS; new filename for the web copy."

---

## 11. Product-site film family: five more looks

Each was made to look **different from the last** (the reviewer's standing rule: "each new film must look different").

| Look | Key idea | Notes |
|---|---|---|
| **Light intro film** (25.6 s) | Real screens only: live store, sample creator site in six layouts flash-cut on the beat, wizard filled in, an inquiry landing in the inbox; logo slam with shine and shock ring, 3D window fly-in, address typing, cursor clicks, count-up, circle reveal to dark for the price beat. | Hero video starts muted with a "Sound on" button; no price on screen when it plays on the home page; SF type only; no emoji. |
| **Dark chapters** (54 s, 104 BPM half-time) | Dark grid and beam stage; numbered chapter rail (01 Look / 02 Content / 03 Domain / 04 Dashboard / 05 Price); left-aligned editorial headlines revealed from behind a mask (not blur-in); laptop and phone mockups pushing in like a filmstrip; indigo skewed diagonal wipes between chapters (~2 per chapter); callouts with leader lines pointing at real UI. | Deliberately unlike the first film. |
| **One-camera board** ("The Link", 33 s) | One continuous camera over a bright board driven by a buyer's cursor: an email arrives, the cheap-template link opens (screen narrows like a squint, pinch, tab closes, **the song dies** with a falling 420 Hz droop), then the same creator on a real site; at the end the camera pulls out to reveal the whole film was one board. | Music: thin hopeful plucks, off-key detuned plucks on the bad screen, 808 heartbeat in the dark, full groove when the real site opens. |
| **Channel flip** (35-42 s) | A tunnel of videos, then "Change the channel": each niche (film, study, AI, side hustles, a hobby) is flipped with static and shows a different creator's real site on every channel; then a ring of phones, media kits, dashboards. | The reviewer later disliked **static mid-film**: keep the TV effect for the end only. |
| **Calm glass** (43 s) | Light glass stage (`#F4F3FA`), one indigo accent, scenes "settle into each other with blur and depth instead of cutting"; device frames (phone, browser, laptop) drawn like component-library mockups; six sites on an ellipse; feed snaps through 48 clips in six niches. | 4K recorded at 2x; palette calmed (no flashing yellows/reds), one caption line position and one browser position from demo to dashboards, nothing tilted. |

Cast and data rules for the whole family: every person and site is **invented** (names matching the niche, made-up domains), every inbox sender is made up and tagged "Sample data", views shown are real or omitted, no real handles, and the sample profiles are fully filled in (stats, videos, brands, results, case studies, testimonials, timeline, products, FAQ, media kit) because empty states look broken. One typeface in every scene including the filmed UI (inject the font into the capture), the logo is the only exception.

**Logo trap (hit twice):** the chrome logo PNGs were cut on a white background; on a dark stage they left black holes, and a CSS invert filter produced a negative. Fix: re-cut the dark-background original into a transparent PNG with a solid shape mask (a luminance-alpha cut looked washed out), Lanczos 2x plus an unsharp mask; always use the dark-stage cut on dark stages; verify on white, grey and black with screenshots.

**Prompt (short):** "Give me three fully different versions of the product film (different visual language, different music bed, different pacing), same voice, invented cast. Then I'll pick."

**Detailed prompt:** "Reference the film we already shipped (same voice, same cast rules) and make three fully different variations for the home page: A light, one continuous camera over a board; B poster slam; C 3D ring of phones. Each needs its own script (22-32 s), palette, type treatment and synthesised bed, word-anchored cuts, tall and wide layouts and a poster frame. Invented creators and domains matching each niche, every section filled in, SF-style bold type everywhere (inject the font into captured UI), no price on screen, no emoji. Render stills first and show me a contact sheet of all three."

---

## 12. Liquid-glass two-world launch film (16:9, 60 fps)

- **Size:** 1920x1080, 60 fps, 41 s, AAC. Two visual worlds joined by a circle iris. Renders in ~2 minutes at 60 fps.
- **World 1 (light):** grey stage `#e2e2e3` that **exactly** matches the logo animation's background (otherwise the crop shows as a square; keep the pastel aura out from under it) plus a pastel blue/pink/cyan aura so the glass has something to bend. **World 2 (dark):** near-black with one blue floor glow.
- **Structure:** S1 hook pills (one brand pill; 50 creator pills; 400 account pills flood outward as the camera pulls back; "Nobody posts that by hand." with a gradient on the last words; chip "1 of 400 posted"). S2 the logo animation plays as delivered, wordmark, glass pill "by YOURBRAND". S3 campaign pipeline pan with a stepper 01-07 (contract card with a self-drawing signature and a Signed badge; portrait circles on a wire; handle rows x platform tiles; small phones lighting off a shared wire). S4 AI review (scan line, three ticking checks, score counts to 9.2, Approved) then the video shrinks, arcs and drops behind a folder flap (squash plus "1 new video"), When/Then card with a travelling border beam; the dark world opens **out of the THEN row** with a circle transition. S5 one 3D phone on black: lock screen, app opens, caption types, Post press, Posted check, ring leaves the phone; four step words light in turn. S6 whip turn per platform name with a "Posted on ..." toast and a five-row tick list. S7 eight numbered screenshots fly out into a dark dashboard (border beam, 5/5 ticking, views counting, sparkline). S8 three real clips recorded off the phone held large, pull back into a curved wall of ~100 phones (one canvas, tiles on a cylinder projected by hand, far first, dimmed by facing angle), "100+" lands huge. S9 the light world closes in, logo animation again, wordmark, pill, site.
- **Liquid glass recipe:** CSS `backdrop-filter` blur + saturate, a white gradient film, a bright top rim, a soft lift shadow; inside canvas phones, redraw footage blurred under the panel and film over it with white. Accent gradient (`#2f6bff -> #ff2e97`) on exactly **one** word per line.
- **Motion:** elements arrive on a spring and leave on an accelerating move with a blur ramp ("blur follows speed"); words appear when spoken, rising out of a mask. **Banned in the brief:** stock footage, real creator names or handles, other people's feeds, prices, fake numbers shown as results, crossfades, `Math.random`, CSS transitions, any frame holding still more than 1.2 s except the end card.
- **Footage rules:** real clips recorded off the reviewer's own phone (TikTok, YouTube, X); a clip that showed family and friends' names was dropped, an empty profile was dropped; never film strangers' feeds. Numbers on screen must not run ahead of the product (a "100+ devices" line when only five were connected was flagged in the handoff).
- **References consumed:** a black-stage 3D-phone app shot, liquid-glass shots, a prompt library site (238 prompts scraped; four merged), a component library's glass folder cards, border-beam, halo reel, 3D gallery, device frame.
- **Voice:** a warm bright female library voice (stability 50, similarity 75, speed 100%); TTS spellings: write the brand as two words if it is read wrongly. Music 124 BPM D minor, quiet under the first half, the groove starts when the dark world opens, ducks under voice; whooshes on cuts, ticks under typing, click on Post, impact on the logo; -14 LUFS.

**Short prompt:** "41 s liquid-glass launch film for YOURBRAND: light glass world then a black stage via a circle iris, logo animation open and close, pipeline pan, AI review card, one 3D phone posting, whip turns per platform, dashboard, curved wall of 100 phones, 60 fps, anchor every beat to word times."

**Detailed prompt:** "Two worlds joined by a circle iris: light glass (`#e2e2e3`, pastel aura) and a black stage with one blue floor glow. S1 pills flood outward as the camera pulls back; S2 logo animation then wordmark and a glass pill; S3 pipeline pan with stepper 01-07; S4 AI review (score to 9.2), video drops behind a folder flap, When/Then card with a border beam, dark world opens out of the THEN row; S5 one 3D phone posts; S6 whip turns per platform; S7 screenshots fly into a dark dashboard; S8 three real clips then a curved wall of ~100 phones; S9 close in on the logo. Glass = backdrop blur plus saturate, white film, bright top rim. Gradient on one word per line. No stock footage, no crossfades, no CSS transitions, no `Math.random`, nothing still over 1.2 s. 60 fps, ~2 minute render, 124 BPM D minor bed whose groove starts when the dark world opens, voice at natural pace, -14 LUFS."

---

## 13. Single-accent-dot keynote-calm launch film (near black, scramble decode)

- **Size:** wide, 1920x1080 at 30 fps with 3 sub-samples per frame blended for real motion blur, ~27.4 s, `crf 15-16`, AAC 256k, -14 LUFS (true-peak target -1.5, then a limiter at 0.63 because AAC pushed peaks +0.6 dB).
- **Reference:** a 28 s reel: small italic hook, big glowing payoff, logo reveal, product UI floating in 3D, a scramble line, logo end card. Analysis method: download, `Duration` via ffmpeg, `fps=2,scale=480:-1` frames, `fps=1,scale=360:-1,drawtext` tiled contact sheets, whisper transcript, `volumedetect`.
- **Look:** near-black `#030305` with one soft blue glow pooled at the bottom (breathes slowly); accent `#3b82f6 -> #60a5fa`; "keynote calm". **ONE blue dot is the thread through every scene:** it sits next to the first line, gathers the scattered vendors, becomes the cursor click, marks the user's location, lands as the full stop on the end card. Every shot enters already moving (exponential ease-out) and leaves on an accelerating move or blur ramp; **blur follows speed**. Depth: CSS 3D perspective 1600 px, cards tilted 8-18 degrees, depth blur on far items.
- **Scenes:** S1 hook (small italic medium 56 px, white 86%, words rise from 10 px blur; the key word underlined by a hand-drawn stroke); S2 ~16 small glass vendor tabs pop one per beat at seeded positions and depths with tiny red chips ("!", "pending", "Failed", "14 passwords") while the camera drifts through the chaos; S3 tabs sucked into the dot (spring + overshoot), flash, the payoff line slams in at 150 px bold with a 3-6 px RGB-channel split settling to white plus bloom; S4 the dot opens to a ring of light, wordmark rises from heavy blur with a halo and slow push-in, a glass pill; S5 a product page floating in 3D, a cursor glides, hovers "Add", clicks twice (blue ripples), a cart badge counts, "Place order", a green toast, camera pushes on each click; S6 whip-tilt down to a grid of 50 two-letter state chips lighting in a wave, the dot lands on one, a provider card slides out; S7 three real screens on faces of a slowly turning 3D prism (sharp facing the lens, soft turning away) then fold into one dashboard; S8 hard cut to black, a line **decodes from scrambled glyphs left to right** (seeded swaps, ~2 frames per letter, mono then semibold, key word lit blue); S9 wordmark returns with a wide soft halo and tight glow, zoom-smear copies collapsing in, the URL types in, the blue dot as the full stop; hold.
- **Rules:** keep the hook small; the payoff is the only big hit before the logo; the logo must bloom straight out of the payoff line with no black gap; compliance niches: no prices, doses, claims or product photos, so screens are drawn in the product's style, not captured. A white wordmark is white-on-transparent: never invert, put a glow behind it.
- **Prompt skeleton that worked** (rewrite a collected set of reference prompts into one): `<inputs>` (product, logo file, accent, type, voice settings, script) + `<direction>` (format, palette, motion rules, banned list) + `<structure>` (S1..S9, each with its spoken words) + `<build>` (pure `render(t)`, voice as clock, real UI capture at 2x with Playwright using a demo account only, CSS 3D depth, 1920x1080 30 fps 3 sub-samples crf 15, sound spec) + `<gotchas>`.
- **Sound:** ~118 BPM minor key, quiet under the hook, lifts on the payoff, ducks under voice, whoosh on every cut, soft clicks on presses, key ticks under the decode, a low impact on the logo.

**Short prompt:** "27 s keynote-calm launch film modelled on this reel: tiny italic hook, big glowing payoff line, one blue dot threading every scene, chaos of vendor tabs sucked into the dot, a real product page with cursor clicks, a state map lighting up, a 3D prism of screens, a scramble-decode line, logo end card with typed URL. 30 fps, 3 sub-samples."

**Detailed prompt:** "Use the prompt skeleton `<inputs> <direction> <structure> <build> <gotchas>`. Inputs: product, logo (white-on-transparent, never inverted), accent `#3b82f6 -> #60a5fa`, SF-style type, voice settings, script. Direction: near-black `#030305`, one bottom glow, one blue dot threading all scenes, shots enter already moving and leave on an accelerating move or blur ramp. Structure: S1 hook (small italic with a drawn underline) through S9 wordmark and typed URL as described. Build: pure `render(t)`, voice as clock, demo-account captures at 2x, CSS 3D perspective 1600 px, 1920x1080 at 30 fps with 3 sub-samples, crf 15, -14 LUFS with a 0.63 limiter. Gotchas: no prices or claims in compliance niches, no black gap between payoff and logo."

---

## 14. Book-opening dark trailer (3D book, four aspect ratios, hook A/B/C)

- **Platform / size:** ad and social, rendered at 16:9 (1920x1080), 9:16, 4:5 (1080x1350), 1:1 (1080x1080), 30 fps. Long cut ~103 s (full story), short cut ~56-58 s, plus 30 s cutdowns, posters, hook variants A/B/C and an alternate-narrator cut: 10 deliverables in ~25 minutes of background rendering.
- **Idea:** a dark SaaS-style launch film for a self-published true-story memoir: a real-looking 3D book slides in, a cursor clicks the cover, it opens, the camera pushes into the open page which becomes the stage, then kinetic serif headlines, glass pop-ups with click sounds, a timeline rail, stat tiles, an end card with a store button.
- **Storyboard (short master):** 0-4.5 hook (black; two kinetic lines, the key word in red `#d8463a`; a pop-up card "LAB RESULT"; thuds on each line). 4.5-8.5 truth ("This is NOT fiction." / "This is a true story." in italic gold). 8.5-15.5 the book: CSS 3D (perspective 2600 px), slides in with a back ease, tilts (ry -62 -> -26, rx 10 -> 5), bobs; the cursor glides in and clicks at t0+3.6 (ripple); cover opens `rotateY(-open*168deg)` over 1.7 s with a page-flip SFX; at t0+5.6 the camera pushes into the page (scale x3.6, cubic ease-in); a white flash into the next scene. 15.5-23 setup: a real historic photo with slow zoom 1.0 -> 1.08, eyebrow line, headline, cast chips. 23-33 timeline rail (long cut only): ticks with years, gold fill bar `#e8b43a -> #f7d873` with glow, a red dot on the dark year, a tick sound per mark. 33-45 events: glass cards slam in with click SFX. 45-51.5 value: "She didn't leave." stat tiles. 51.5-58 end card: book + title, a store button, cursor click and ripple, tagline.
- **Look:** stage `#07080b`; grain overlay (SVG feTurbulence .95, opacity .07, overlay); vignette (transparent 55% to `rgba(0,0,0,.6)`); three drifting blurred colour blobs (blur 120 px; mood 0 cold / 1 gold / 2 red). Colours: gold `#e8b43a`, silver `#cfd4dc`, red `#d8463a`, text `#f3f1ea`, muted `#b9bcc6`. Cards `rgba(18,20,26,.82)` with a 1.5 px `rgba(255,255,255,.13)` border, backdrop blur 18, radius 22, a gold tracked uppercase key label with a glowing dot. Fonts: a high-contrast serif (Playfair Display 700/800 with italic gold accent words), SF-style sans for eyebrows (tracking .22em), a slab display font for the cover, a script font, a typewriter font. Photo grade for stock-like images: `contrast(1.08) saturate(.82) brightness(.9) sepia(.12)`; real historic photos used ungraded.
- **Headline motion:** word-by-word slam: each word fades in while scaling 1.3 -> 1 and rising 0.35*fontsize, stagger 0.1 s, 0.45 s ease-out cubic; exit = fade + shrink .96 + 40 px drift. Cards: spring `backS(.,1.9)` over .5 s, scale .78 -> 1, rise 30 px. Plates: `backS 1.4` over .75 s.
- **Book object:** cover width ~540-560 (x scale), height 1.5x, thickness 46; faces back, edges, page block (`#f4efe3`), spine (rotated), front with a moving gloss sweep.
- **Vertical layout:** design scale `S = W/1080`; headlines 100 px vs 128 px; margins 72/110.
- **Scene lengths** auto-fit the chosen narrator's line durations (a duration table regenerated from the voice files).
- **Sound:** free neural TTS (`edge-tts`), a slow low theatrical British-male read (rate -8 to -14%, pitch -5 to -6 Hz); lines written with ellipses for dramatic pauses ("Every October... the blood came back."); retry loop (6 tries, 5 s) because the service flakes; use the Python API rather than the CLI. SFX from a kit: click, key, tick, whoosh, thud, flip; a drone bed (48 Hz sine, tremolo .13 Hz, plus brown noise low-passed at 220 Hz); voice chain `highpass=f=70,acompressor=threshold=-18dB:ratio=3:attack=10:release=120`; final `alimiter=limit=0.95,loudnorm=I=-15:TP=-1.2:LRA=11`. Page flip made with `ffmpeg -f lavfi -i "anoisesrc=d=0.5:c=white:r=48000:a=0.6" -af "highpass=f=1800,lowpass=f=7000,volume=0.6,afade=t=in:st=0:d=0.05,afade=t=out:st=0.1:d=0.4"`.
- **Build:** `./build.sh W H cut name [voice]` renders silent video, builds audio from the page's exported cue list, muxes (`-c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart`), takes a poster frame. Query params `cut=long|short`, `hook=A|B|C`, `voice=...`. Render settings: crf 14, preset slow, jpeg quality 97 for large masters.
- **A/B hooks:** A cold-open detail ("Every October, the blood came back."), B a question ("Would you sleep in that room?"), C a prestige angle with a smaller headline (0.64-0.78x). Test as three ads to the same cold audience, optimising 3-second hold plus link clicks; test narrators as well.
- **Locked rules after the reviewer's corrections (apply to any real-story film):** keep the approved structure ("save the rules; do not veer away from the original video"); exact fact wording (do not upgrade "oldest in the Western region" to "oldest in the country"); **only real photos of the real place**: AI-invented houses were rejected even for one ceremony scene; story beats, names, dates and quotes only from the source text; always render the full set of formats. Lesson: authenticity beats generated art when the subject is a real place; after a cut is approved, change only what was asked.
- **Cover and image-generation lessons:** rebuild an HD cover as HTML (restored photo plate plus vector gold/silver type), screenshot at 1800x2700; extract PDF pages at 300 dpi with a PDF library; an image-generation chat refused "blood splatter" but accepted "aged stains and dark patina"; generated images are not in the DOM (hover and click the download icon); prompt "Using the attached photo as the exact reference... change nothing" for restoration, and compare to the original.

**Short prompt:** "Make a dark SaaS-style trailer for a book: a real-looking 3D book opens on a click, the camera pushes into the page, serif kinetic headlines, glass pop-ups with click sounds, a timeline rail, stat tiles, store-button end card. Render 16:9, 9:16, 4:5 and 1:1, long and short cuts, three hook variants, theatrical narrator."

**Detailed:** "Use the source text as the only source of facts. Build one `render(t)` page with `cut`, `hook` and `voice` query parameters. Storyboard: [beats above]. Stage `#07080b` with grain, vignette and three drifting blobs; gold `#e8b43a`, silver `#cfd4dc`, red `#d8463a`. Book in CSS 3D with perspective 2600, cursor click, `rotateY` open, push-in. Voice with `edge-tts` and pauses written as ellipses. SFX kit plus drone bed. Output all deliverables with posters; list what you could not verify (no one has heard it)."

---

## 15. Website launch film: typed URL, morph into the browser, sections, key and click sounds only

- **Size:** 16:9 1920x1080 and 9:16 1080x1920, 30 fps, 29.5 s, 885 frames each, **no music** (reviewer request), only keyboard and mouse sounds.
- **Palette:** `#f4f5f7` background, ink `#0b0c10`, accent `#5b5ce6`, blobs `#dfe3ff #ffe1ec #dff6ff` (blur 110 px, drifting), cards `rgba(255,255,255,.72)` with a 1.5 px white border and radius 40, browser frame radius 28 with traffic lights `#ff5f57 #febc2e #28c840`, phone body radius 76 (`#0b0c10`, island 126x36). SF-style type, letter-spacing -0.035 to -0.045em, accent colour on the key word.
- **Beats:** 0-3.6 hook (big centred question, word by word); 3.6-5.8 the **search bar zooms in** (push-in .1 wide, .04 tall) and the domain types character by character (16 keypress times with irregular gaps like human typing, e.g. 3.70, 3.83, 3.94, 4.08 ...); return key pill and ENTER at 5.95 with a pulse ring; 6.1-6.95 **morph:** the bar shrinks into the browser's address bar, the window grows around it, a load line runs across, the real homepage fades in; 7-21 sections every ~2.2 s (numbered eyebrow, big title, description, list, with the real page scrolled inside the browser and a phone showing the mobile version, cursor click on nav at 9.9); 21-26 stats on 2x2 glass cards; 26.2 CTA click with a ripple; 26.5-29.5 end card (mark, domain typed per character, name, tagline).
- **Sound:** keypress WAVs (16 variants at ~0.55 volume placed per typed character, a return key at .8), mouse clicks at .7-.8; built with `adelay` and `amix=inputs=N:normalize=0:duration=longest,atrim`. All keystroke and click time constants are duplicated between the render page and the audio script and **must be kept in sync**; a cue-list export removes that risk.
- **Hand-tuned per format:** layout constants (title 92-96 px wide / 30-34 px description, list 32-34 px, stat cards 460x300 etc.) tuned from stills after screenshots showed overlaps; titles auto-shrink to fit the width (measure with a probe element, `scale=min(1,(w-4)/w)`).
- **Capture:** the real site captured with Playwright (videos blocked, a `?preview=1` flag so analytics are not polluted).
- **Output:** `-crf 16 -c:a aac -b:a 192k -movflags +faststart` with the tv-range conversion; poster at 8.0 s.
- **Reviewer's brief (kept as the style guide):** "SF Bold for the domain text, make it zoom in on the link with a clicking sound, aesthetic keyboard sound when typing, then the transition into the website, then motion graphics showing sections; fix the placement for computer and phone so the product placement and positioning is perfect."
- **White-label variant:** seed a blank tenant ("Your Name", placeholder photo, "Your Logo", "Your numbers"), re-capture, retype `yourname.yoursite`, end-card "your logo"; check that no frame contains anything of the real reviewer.

**Short prompt:** "29.5 s launch film for yourbrand.com: hook question, search bar zooms, the domain types with keyboard sounds, morph into the real browser, six sections with a matching phone, stats, CTA click, end card; wide and tall; keyboard and click sounds only, no music; SF-style type."

**Detailed prompt:** "Record yourbrand.com with Playwright (videos blocked, preview flag on) and build a 29.5 s page in 16:9 and 9:16: hook question word by word (0-3.6), search bar zoom (3.6-5.8) with 16 keystrokes at irregular times, ENTER pulse at 5.95, morph into the address bar with a load line (6.1-6.95), six section scenes every ~2.2 s with a cursor click on nav, 2x2 glass stat cards, CTA ripple at 26.2, end card with the domain typed per character. Palette `#f4f5f7`, ink `#0b0c10`, accent `#5b5ce6`, drifting pastel blobs. SF Bold type. Audio: keypress and click samples placed with `adelay`/`amix`, no music; export the cue list from the page so audio follows the picture. Tune layout constants per format from stills and auto-shrink titles."

---

## 16. White-label "how to set up" walkthrough with a follow camera

- 34.5 s, 1920x1080, sound from a cue list. Built by filming the **real** setup wizard and dashboard of a white-label kit with blank values (email you@yourname.com, slug yourname): ten screens (login, about you, colours, contact and socials, numbers, videos, web address, then dashboard overview, design, domain). Before/after shots per field plus click-target coordinates from a capture script; the animation page uses a **follow camera** (a push-in that tracks the field being filled; the first cut read too small), cursor clicks with ripples, typed text, progress. No pricing shown.
- Filming a real product found a real bug (a multi-file upload kept only the last file): fix, reset the database between takes, re-film.
- Placeholder videos in demos = coloured clips made with `ffmpeg -f lavfi -t 1.5 -i "color=c=0x4338ca:s=540x960:r=30"`; **always give a lavfi source `-t`**: forgetting it generated an endless file and filled the disk.

**Short prompt:** "A 35 s walkthrough of the setup wizard with blank placeholder data, a follow camera that zooms to each field as it is filled, cursor clicks, typed text and key sounds, ending on the live site; no prices."

**Detailed prompt:** "Seed a blank tenant (you@yourname.com, slug yourname), script the real wizard with Playwright (before/after screenshots per field plus click-target coordinates) across ten screens, then build a 34.5 s page with a follow camera that pushes in to the active field, cursor ripples, typed text, progress and a final live site. Use coloured placeholder clips for uploads (`lavfi color` with `-t`). No pricing. Export a cue list and build key and click sounds from it. Report any product bug you find while filming, fix it and re-film."

---

## 17. Beat-grid promo (every cut on a beat of a fixed BPM)

- **Size:** 1920x1080, **60 fps**, 32.5 s (the first attempt was 63.5 s and judged too slow), 128 BPM so one beat = 0.469 s; every cut on a beat.
- **Beats:** kinetic "Content [cover] that [cover] sells." (video covers pop in between the words) -> eighth-note niche flash cuts -> logo slam with camera zoom **through** the logo into the dashboard -> real stat cards lift out of the screen -> match cut from a tile to the full posts wall -> whip pans between pages (SVG directional blur) -> giant case numbers -> curtain wipe -> Apply button ripple into the end card.
- **Reference analysis trick:** `ffmpeg -i ref.mp4 -vf "select='gt(scene,0.25)',showinfo" -f null -`; a reference's niche burst had 8 cuts in ~0.6 s (flash cuts every 0.12-0.17 s) then 1-3 s holds.
- **Voice:** 11 short lines fitted to slots; locally generated stock voice, each line rendered at base speed 1.12 and re-rendered faster (`speed*len/slot+.01`, up to 1.35x) if it overran its slot, silence-trimmed (top_db 38), normalised to .9. The reviewer rejected the first voice ("needs to be more upbeat") and picked a male energetic voice then a female voice for the live version.
- **Sound:** music (128 BPM A minor, four-on-the-floor kick, claps on 2 and 4, offbeat open hats, 16th closed hats, offbeat bass sidechained to the kick: gain dips to .25 then recovers over .22 s); impacts on beats 12/40/48/60 (gain .5/.3/.3/.5), risers into the logo slam and the final hit, whoosh peaks on each moving transition, hat ticks on the flash cuts, click on the apply button, final held Am chord plus bass.
- **First attempt's verdict (lessons):** voice too flat, transitions did not match the reference, dashboard tiles were gradient placeholders instead of real covers, pacing too slow. Fixes: real video covers injected into every tile, cut length halved, every cut on a beat.
- **Ship:** an object key on the media bucket is served immutable: upload new cuts under new names and change the player's `src`.

**Short prompt:** "32 s promo at 128 BPM: every cut on a beat, kinetic text with video covers between the words, flash-cut niches, logo zoom-through into the dashboard, whip pans, giant case numbers, curtain wipe, end card; energetic voice slotted into beats; 60 fps."

**Detailed prompt:** "Beat length 0.469 s; put every cut on a beat. Sequence: kinetic text with video covers popping between words, eighth-note flash cuts through niches, logo slam with a camera zoom through the logo into the dashboard, stat cards lifting out of the screen, match cut from a tile to the full wall, whip pans with SVG directional blur, giant case numbers, curtain wipe, button ripple into the end card. Use real covers in every tile (no gradient placeholders). Voice: 11 lines fitted into slots (base speed 1.12, re-render faster up to 1.35x when a line overruns, trim silence). 128 BPM A minor bed with sidechain, impacts on beats 12/40/48/60, whoosh peaks on moves. 60 fps, -16 LUFS."

---

## 18. Retro-console life-sim cutscene reel (AI keyframes + local image-to-video + real UI composite)

**Look:** a "believable clip from a forgotten early-2000s video game": soft low-res textures, baked lighting, static camera, hard cuts every 2-7 s, one short caption at a time in a pixel font in the lower third, dry understated acting, story first, product only at the end. 9:16, 1080x1920, 30 fps, exactly 32.00 s (960 frames).

### Beats

| t | content |
|---|---|
| 0-7 | Couch, side/medium-wide, tiny push-in. A woman scrolls her phone at 2 am; hook caption "POV: IT'S 2AM AND YOU'RE RUNNING FROM IT AGAIN" (0.15-1.45); voice "[mutter]... why am I always trying to escape?" |
| 7-13 | Kitchen: open fridge stare; eating crackers (crunches at 10.3/10.9/11.5/12.1). |
| 13-19 | Bedroom: eyes wide open in moonlight, clock tick every second. |
| 19-23 | Couch again, anxious, messier hair. |
| 22-28 | **Real app recording composited onto the phone in her hand**; the thumb taps the panic button at 22.92, a safety sheet slides up; a readable full-height view 25.5-28. |
| 28-30 | Calm: eyes closed, slow breath in/out (plate slowed to .75x). |
| 30-32 | End card: floating 3D logo on ivory, wordmark, "Coming soon" (**no store badge if the app is not live; never fabricate availability**). |

### Look

- Captions: pixel arcade font (Press Start 2P), 38 px body, line-height 1.45, letter-spacing 1, white with a hard black outline made from stacked text-shadows every px/2, plus a soft 55% black drop; lines at y 1230, hook at y 1395, hook font 27 px `#f4efe6`, margins 70 px, **keep the bottom 420 px clear** of platform UI; one caption at a time, all caps.
- Finishing grade applied identically to every shot: grain (270x480 noise tile at opacity .045, overlay, jittered per frame), scanlines `repeating-linear-gradient(0deg, rgba(0,0,0,.05) 0 1px, transparent 1px 4px)`, vignette `radial-gradient(120% 90% at 50% 45%, transparent 55%, rgba(0,0,0,.38) 100%)`. Keep it light: faces, captions and app UI must stay clear.
- Lighting by room: warm tungsten lamp (living room), cold white fridge light, warm under-cabinet light, cool blue moonlight with a faint warm doorway spill (bedroom).

### How it was built (the version that was used)

1. **Lock the character with one master still** made by a local image model (a 4B image model via an Apple-silicon runner: `generate --model <name> -q 8 --prompt-file master_prompt.txt --width 768 --height 1360 --steps 4 --seed 11 12 13`). Master prompt pattern: "Screenshot from an early-2000s PlayStation-2-era life-simulation game, in-engine 3D render, slightly soft low-resolution textures, baked lighting, subtle polygon edges. Full-body shot of a woman in her mid 20s [outfit/hair/face list]. Background [room props]. Warm tungsten lamp light, muted nostalgic colours, vertical 9:16 frame." Three seeds; the reviewer picked.
2. **Keyframes** for every shot = reference edits of the master with a reusable "SAME" block: "Keep the exact same woman from the reference image: same face, same skin, same outfit... Same early-2000s PS2 life-sim 3D render style... Vertical 9:16 frame." Two seeds per shot, pick the best.
3. **Image-to-video** with a local video model (distilled, MLX, q8) at 704x1280, 24 fps, frame counts of the form 8n+1 (73 = 3 s, 97 = 4 s, 145 = 6 s, 169 = 7 s), prompt prefix "Early 2000s life-simulation video game cutscene, in-engine 3D render, slightly stiff game-character animation, soft low-resolution textures. The camera is static." plus the action and an audio line. Dialogue shots use an audio-to-video mode with the real voice (a brown-noise bed plus lines placed with `adelay`) so lips match. **Run one generation at a time** (the machine chokes); watch disk (weights 28-55 GB).
4. **Phone composite:** have the model generate a hand-held phone whose display is a **flat pure green** rectangle; OpenCV tracks the green quad from its unoccluded edges and the thumb tip; per frame, warp the matching UI recording frame onto the quad and keep everything not-green (thumb, fingers, bezel) on top; crop 9:16 following the phone at 3x working resolution so UI text stays sharp; retime the recording so each UI transition starts when the thumb lands. Make a second tight close-up plate for readability.
5. **Edit and render** in a React video framework (clip slots, a captions component, the grade component, an end-card component); `setVideoImageFormat('jpeg')`, quality 92, `setChromiumOpenGlRenderer('angle')`, concurrency 4. Speed trick: one bundle plus `renderStill` in a node script for many stills (seconds instead of minutes each). Deliverables: MASTER, CLEAN (no captions), PREVIEW (720x1280, `--scale=0.5 --crf=24`), a 2 s end card, a storyboard PNG (12 frames tiled 6x2), and a QA script (duration, resolution, fps, frame count, `blackdetect`, transcript of the final audio).
6. **Sound (all synthesised):** per-room brown-noise tones, scroll ticks (high-passed noise burst plus 2 kHz sine, 8 ms decay), fridge hum (118/236 Hz plus noise, .7 Hz wobble), cracker rustle (high-passed 2.5 kHz noise with slow random amplitude), crunch (7 micro bursts, band 1.2-6 kHz), clock tick alternating 1500/1300 Hz, a tension drone under the anxious scene (48 Hz sine + 96.7 Hz + low-passed brown noise, .13 Hz tremolo, rising over 3.5 s) that **releases** after the panic tap, then a warm pad (F major, then G major through the end card), one soft bell on the logo, inhale/exhale noise bands. Mix: beds duck 50% under voice, curved 0.5 s fade-out, `tanh(1.1x)/tanh(1.1)` soft clip, `alimiter=limit=0.95,loudnorm=I=-15:TP=-1.2:LRA=11`, then trim about -1.3 dB to land at -16 LUFS.
7. Voice: a single custom character voice generated in a hosted TTS web app (the API key was not available locally), two takes per line, silence trimmed both ends with `silenceremove ... areverse ... areverse`, `loudnorm=I=-19:TP=-2`, verified with a local whisper transcript.

### What went wrong (the most valuable part)

- v1 hand-built the character as a 3D model in code (React Three Fiber): **rejected**: "The characters should be just like what I gave you. You didn't need to render anything else." **Never hand-build a character in code; go straight to generated keyframes of the approved look.**
- The final cut was rejected harshly and said not to represent the reference. Earlier warnings: the assistant had only looked at the reference account's grid and never **played the reels end to end**; it stalled instead of running; it spent hours of local-model compute before showing a cheap first look. Lessons: (a) actually play the references fully and extract cuts, captions, audio first; (b) judge an AI look-alike against the reference's **pacing** (2-7 s cuts, dialogue-forward), not a storyboard essay; (c) say what you could not verify (no one watched at speed, the voice was not heard); (d) do not burn credits or hours before a cheap first look is approved; (e) "it needs to fit an iPhone, not horizontal".
- A model sheet carrying a real TV character's name and face was **not** used as a face reference (likeness risk): keep brand characters original.
- Evaluated and not used: a keyframe animation library (nothing to keyframe in static shots), motion capture from video (no source footage), dance generation.

**Short prompt:** "A 32 s vertical Reel styled as a forgotten early-2000s life-sim cutscene: one locked character (ref attached), 2 am scrolling, fridge, crackers, bed, back to the couch messier, then the real app recording taps the panic button, she breathes out, 2 s brand end card. Pixel captions one at a time. First watch the reference reels fully and tell me what you could not verify. Make the master still first and show me before animating."

**Detailed prompt:** "Before building anything: play the reference account's reels end to end and extract cuts, captions, loudness and pacing; report what you could not verify. Make the locked character master still with a local image model (three seeds), wait for my pick, then make two seeded keyframes per shot via reference edits with the SAME block, animate each with the local image-to-video model one at a time (704x1280, 24 fps, frame counts 8n+1), generate a green-screen phone plate, track and composite the real app recording (warp per frame, keep thumb on top, retime to the tap), render in the video framework with pixel captions (Press Start 2P, outline via stacked shadows, y 1230, bottom 420 px clear), grain/scanlines/vignette, a clean end card with no store badge, synthesised foley and a tension drone that releases at the tap, voice from my custom voice with two takes per line. Deliver MASTER, CLEAN, PREVIEW, END CARD, STORYBOARD and a QA report."

---

## 19. Screen-recorded app-demo clips for creators (simulator pipeline)

- **Deliverable:** per creator per day, ONE demo clip (1080x1920, H.264, 30 fps, silent, `+faststart`, 15-20 s) plus component clips (prompt typed, two taps, backup) and cover screenshots at the phone's full resolution. The creators film themselves; the clips are the "app slots" they splice into their own talking-head videos. A brief gives a storyboard such as: 2-6 s the sentence typed (4 s); 6-8 s building, sped up (2 s); 8-14 s two swipes (6 s); cut to the face for 1 s; 15-20 s the third swipe and the match screen (5 s).
- **Naming:** `<Creator>_D<day>_Demo.mp4`, `_A02_Prompt_Typed.mp4`, `_A03_Two_Taps.mp4`; corrected files as `_v2`; shared copies under a general name without the creator (`<AppKind>_<WhatItShows>_<Type>.mp4`).
- **Build and record:** build the app locally (`xcodebuild ... -destination 'platform=iOS Simulator,id=<UDID>' CODE_SIGNING_ALLOWED=NO build`), install with `xcrun simctl install`, launch with arguments to reset demo state (read ints with `UserDefaults.integer(forKey:)`, not `as? Int`), clean status bar (`xcrun simctl status_bar <UDID> override --time "9:41" --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3`), record `xcrun simctl io <UDID> recordVideo --codec=h264 --force raw/take1.mp4 &` and stop with `kill -INT <pid>`. Space taps 1.2 s apart. For the prompt-typed clip, type into the product's web page in the simulator's browser, never press Build, and type long text as one line (a newline submits).
- **Cut with ffmpeg** (from 1206x2622 recordings): app crop `scale=1080:-2:flags=lanczos,crop=1080:1920:0:150` (drops the island); prompt crop `crop=1206:1300:0:150,scale=1080:-2:flags=lanczos,pad=1080:1920:0:(1920-ih)/2:color=0x0B0E0D`; encode `-c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -movflags +faststart -an -r 30`; speed ramp for typed text `setpts=(PTS-STARTPTS)/2.45,fps=30,trim=0:4`; hold frames with `tpad=start_mode=clone:start_duration=0.6:stop_mode=clone:stop_duration=3,trim=0:6`; punch-in on the final tap `trim=3.2:6,setpts=PTS-STARTPTS,scale=1134:2016,crop=1080:1920:27:48`; join with `concat=n=4:v=1:a=0`.
- **Gotchas:** `tpad` placed after `trim` adds nothing (pad before trimming, or hold with `select=eq(n\,0),loop=N:size=1,setpts=N/30/TB`); the simulator recorder writes no frames while the screen is still, so an input `-ss` lands on the next change (use `fps=30,trim=a:b,setpts=PTS-STARTPTS`); with many simulators running, verify that animations really appear in the frames (a coin "spin" was an app bug: the spin started in the same transaction that inserted the coin); leaving a screen can flash a system settings screen for 1.5 s (cut it); template UI can contain another company's name or icon (remove strings, delete test entries in the simulator, grep the built app for leftovers); background workers cannot approve a simulator-control permission prompt, so the main session records shared-simulator clips under a lock file; do not push big files through a tool's truncated output: tar them and PUT to a one-time receiver behind a tunnel with a checksum.
- **QA:** contact sheets (`fps=2,scale=130:-2,tile=15x2`), plus measured checks (duration within +-3 s of the storyboard slot, first and last 3 s). 47 files passed in one day.
- **Rules:** never claim a check passed unless just seen; no other company's brand or famous character on screen; no income, health or medical claims in app text; never publish the app; the reviewer signs in, never type passwords.

**Short prompt:** "For each creator and day, build the demo app from the plan, record it in a clean simulator, cut a 16 s 1080x1920 clip (prompt typed 4 s, two taps 6 s, final tap 6 s) plus component clips, QA with contact sheets, name by the pattern, upload."

**Detailed prompt:** "Read the plan JSON for [creator] day [n]. Build the app locally, install in a clean simulator with the status bar at 9:41, record with `simctl io recordVideo`, drive taps 1.2 s apart, cut with ffmpeg (app crop `scale=1080:-2,crop=1080:1920:0:150`; prompt crop with pad; typed text sped 2.45x into a 4 s slot; hold frames with `tpad` before `trim`; punch-in on the final tap; `concat`), encode crf 18 silent 30 fps, QA with contact sheets and duration checks against the storyboard slots, remove any other brand's text, upload with the naming pattern and a general-named shared copy, and register the clip in the brief page. Never claim a check passed unless you just saw it."

---

## 20. Native-UGC-style reels from real recordings (17-video format family)

A client campaign (an AI app-builder, 16-25 year-old audience, no link in bio) needed organic-feeling vertical videos. Technique: real footage full screen, TikTok/CapCut-style word captions, a slight handheld wobble, and one fixed ending.

- **Spec:** 9:16, 27-43 s each, house voice, every script contains the signature word.
- **Captions style:** white, weight 800, black outline, the spoken word in yellow `#ffe14d`, chunks of up to 4 words or to punctuation, max width 960 px, shrink to fit, pop .86 -> 1. Flags in the engine: `captions:"tiktok"`, `capY`, `nocap`, `handheld`.
- **Ending (every video):** the store search: the product's name types into a store search bar, the real listing pops (icon from the public iTunes lookup, rating), a finger taps GET, "Search '[product]' on the App Store" + "FIRST BUILD FREE" held ~3 s. Later: only the store search and listing pop-up, no extra text on screen (a `clean` option). The voice says it ("search [product] on the App Store"; later "App Store or Google Play").

### Review lessons, in order

1. The CTA must be unmistakable because there is no link: end on the store UI.
2. "Looks a bit like an AI ad": go native (full-screen real footage plus native captions).
3. Do **not** say "it took 18 prompts"; do **not** frame the offer as "templates are free to remix"; keep to the idea that the audience cannot be burdened with complex prompts (screenshots, drawings, a few words).
4. The agent drew game renders of its own: "not ideal, use actual existing games"; then a synthetic video: "I didn't like that because you still generated content." Use **only real screen recordings** with captions, zooms, tap rings, chips, stopwatches and counters on top.
5. The drawing is **inspiration only** for the builder, not the game's art style.
6. After a set of three was praised ("the CTA on those previous ones is perfect"), the reviewer asked for "3 new styles" each time.

### The 17 formats (what each did)

01 replace your subscriptions (labelled example prices stamped CANCELLED); 02 make any game (ads interrupt a tiny game; a notebook sketch stamped NEVER BUILT; the prompt builds a playable game); 03 for 16-25 (pay-to-win and ad simulators; a group-chat idea; templates shown by genre); 04 white stage with real template footage (four phones playing at once, request bubbles each getting "added"); 05 draw it, screenshot it, say it (pen drawing on paper turns into the real game; attach screenshot and photo, type, send); 06 fake ads (a lo-fi fake game ad with a pointing hand, then "nothing like the ad", then the real gameplay); 07 skip-the-ad (an unskippable ad swiped away onto a neon kart race; original drawn karts and a blocky platformer with an "example" tag; phones side by side "no computer needed"); 08 real genres montage (hard cuts each on its word, labelled by genre, original logos cut out); 09 "this paragraph is a whole game" (highlight the real prompt line by line, solid yellow highlight with dark text because the first gradient looked like a strikethrough, then the real demo); 10 POV free arcade; 11 speedrun (20 pages flashed to the voice with a stopwatch and counter frozen at "I give up"); 12 "I can't write prompts, so I sent it screenshots"; 13 "I drew a game and now I can play it" (a drawing filmed stroke by stroke at phone size); 14 "like an app? just screenshot it"; 15 worst-drawing challenge (a deliberately bad sketch, "0/10 ART", zooms on each scribble, before/after split screen, closing "Your drawing can be bad. The game won't be."); 16 "copy any app in 3 steps" (big STEP chips, opens on the finished app as a teaser); 17 "I timed it" (a build-time clock overlay from progress screenshots, turns green at "DONE IN 04:33").

### Recording and compositing techniques

- A recorder drives a mobile-emulated browser (432x768 at device scale 2.5 = 1080x1920) with scripted `scroll`, `jump`, `click` (real click, saves the tap point for a tap ring), `tap`, `type`, `highlight`; selector targets resolve at scroll time because pages grow as their videos load; output is numbered JPEGs plus a taps JSON. A browser user-agent preset may be needed (a store page refused an iPhone UA).
- A `rec` scene draws the recording full-frame and adds zooms (anchor at the left edge x~30 to keep the left of a prompt box in frame), tap rings, chips, stopwatch/counter, build clock, CTA overlay, cues. An assembler stitches stills, recordings and drawing frames into a 30 fps sequence (contain/cover fit, Ken Burns, picture-in-picture, screenshot flash, split screen).
- Real app builds shot from a hosted preview: the preview is a WebRTC `<video>`; record it with `MediaRecorder` on `video.srcObject` while sending taps as pointer events at screen fractions; browsers allow one download per tab, so use one tab per clip. Attach images to a web prompt box by dispatching a synthetic paste (`ClipboardEvent` with a `DataTransfer`); for local files add a temporary hidden `<input type=file>`. Typing long base64 by hand corrupts.
- Footage hygiene: cut before screens that show trademarked titles, label by genre, delete test entries naming other brands, tag clone footage "built in [product] - free template", flag for client sign-off before paid use because clone templates show other companies' names. Never use footage of real third-party games or characters.
- A plan bug to avoid: anchoring a cut to the first occurrence of a common word instead of a unique line start.

**Short prompt:** "Make 3 new organic-style 9:16 videos for [client app]: real screen recordings only, native captions with the spoken word in yellow, handheld wobble, each ends on the store-search CTA. Styles: [A], [B], [C]. Never say it took N prompts; emphasise screenshots and drawings as input."

**Detailed prompt:** "Client facts re-read from the client site today. Audience 16-25; the feeling is 'I have to try this'. Make 3 videos, 28-35 s, 9:16, each a different style from [list], using only real screen recordings (record the live site with the scripted recorder, or real app builds from a hosted preview with MediaRecorder), TikTok-style captions (white 800, black outline, spoken word `#ffe14d`, chunks of up to 4 words), a slight handheld wobble, tap rings and chips only where they serve the story, and the store-search ending (type the name, real listing pops, finger taps GET, no extra text). Voice: house voice, full sentences, the signature word present. Never say how many prompts it took; do not frame the offer as free templates. Label genres, cut before trademarked titles, flag clone footage for client sign-off."

---

## 21. Skeptic-and-answer explainer (two-voice objection loop)

An analysis of a viral faceless explainer (40.9 s, ~30K likes and ~24K comments): a two-person script of **questions and answers** (a skeptic and a "robot"), 18 hard cuts (a cut every ~2.3 s; 10 land within 0.1 s of a word start), pauses 0.3-0.9 s between lines, average 2.5 words/s ("feels fast but not rushed").

- The skeptic voices every objection (price, "what do I get", "where's the catch", "what about credits", "do I share this"); questions are 2-6 words, answers are lists.
- The question sits on the human clip (home base, same set and angle, ~22 s total); the answer sits on an animated explainer card (~18 s); the loop is learned in the first 7 s then repeated five times; cuts land on the first word of each answer.
- Inside lists use motion, not cuts: cards pop on spoken words, counters tick (0 -> 595 -> "600+", credits 930 -> 10 -> "0 needed").
- Hide big topic jumps in a blurred whip (at 21.0 s) or a four-flash burst in 0.3 s (at 26.1 s).
- Captions 1-2 words at a time, payoff word in orange italic; the last 11 s held on one two-character shot with the call to action acted out in UI (a Following button, a comment box typing a keyword, robot eyes becoming hearts). A "comment this word" CTA explains comments roughly equal to likes.
- Tools: yt-dlp (`-f "bv*+ba/b" --merge-output-format mp4 --write-info-json`), ffmpeg `scdet`, `fps=2,scale=480:-1` contact sheets with `drawtext=text='%{pts\:hms}'...tile=4x4`, faster-whisper. If a platform blocks downloads without a login, ask for the original file instead.

**Short prompt:** "Break this reel down (cuts, word-anchored cuts, pauses, wpm, caption style, CTA) and write a skeptic-and-answer script for [topic] with the same rhythm; build the explainer cards with motion inside the lists."

**Detailed prompt:** "Download the reel (or use the original file), list every cut with timestamps and which land within 0.1 s of a word start, the pause lengths, words per second, caption style and the CTA staging. Then write a two-voice question-and-answer script for [topic] where the skeptic voices every objection (price, what do I get, where is the catch, credits, who do I share it with) in 2-6 words and the answer is a list, with the question on a recurring human clip and the answer on an animated card with pops on spoken words and ticking counters. Hide topic jumps in a blur whip or a four-flash burst. Last 10 s held on one shot with the CTA acted out."

---

## 22. Short-form creator formats (the "brain" format library)

Formats that show a person, with conversion ceilings seen in practice (views to installs): talking head plus demo or story (1-2%, the strongest; natural tasks in frame: cutting fruit, coffee, getting ready, brushing teeth, in the car); text hook plus facial reaction then demo (0.5-2%); text over screen plus demo (0.5-1.5%; also the first four warm-up posts); car talk or rant (~1%); reaction, green screen or stitch over a screenshot (0.4-0.8%); problem-to-solution POV (0.5-1%); split-screen face plus screen recording (0.5-1.5%, film landscape, zoom the face); text story into reveal (0.3-0.6%, legible with sound off); slideshow or carousel (0.2-0.4%; 6-10 slides, slide 1 carries everything, the app at slide 6, CTA at slide 7); voice-over over clips (0.3-0.8%, only with confident clean delivery); skit; AI-character UGC (low trust; a fully synthetic presenter without disclosure is a hard fail). Variety in week 1, lock the winning playbook in week 4.

Extra formats: cheat-sheet or list talking head (numbered items pop next to the face, product last), POV with no face on a trending sound (hands, a prop, a punchline, 5-11 s, brand only in the caption), group filming for social apps ("I want to be in that room"), story time or drama recap, before/after side by side, "scan the thing" product moment, outcome showcase with a number, screen recording with a human hook (never a feature tour).

**AI-character and generated-video recipes (use only with rights to the likeness):**
- *Archetype characters:* each = archetype + format + vibe + a reference reel; generate a sheet (close-up front, 3/4 left, 3/4 right, profile, upper body in two outfits, full body) and a voice.
- *Reference-to-video (a video model with element references):* a start frame from an image model at 9:16 (make the placeholder person look **different** from the character so the face swap is not confused), then a face swap, then the video prompt = **motion and action only**, referencing `@Element1` ("@Element1 does X. Then Y. Then Z."), never describing appearance, clothing or environment; state the camera ("Camera stays completely static"); 2-3 beats per 5 s; `generate_audio:false`; poll the request path, not the submit path. 5 s tests, 8-10 s single scenes, 15 s multi-shot. If the video ignores the action, use fewer beats and timing words; if the face drifts, add a clean frontal plus more angles; if it looks too cinematic add "candid phone footage".
- *Talking-head clone reels (a video model that takes a reference video, a clone image and one audio line):* one beat equals one generation; lock one reference video for the whole piece so clips cut together; audio under 8 s (about 20-25 words); prompt: "Using the video as camera and subject reference, the subject is speaking, with little head movements while pointing a finger. Replace the look of subject with the image and speaking the reference audio '[EXACT LINE]'." The exact transcript in quotes is the biggest lip-sync lever; add a spelling hint for brand names; one gesture maximum; camera moves in the hook only; two takes per beat; audition cheap (4 s, standard, 720p), finalise expensive (8 s, pro, 1080p); a likeness flag means only use likenesses you have rights to.
- *Pixel mascot:* master still (1:1, flat off-white background, hard pixel grid, no gradients/outlines/shadows, one or two body colours plus black, recognisable by silhouette); animate with "12 fps stepped animation, hard pixel grid, no motion blur, camera static", one action per clip; reuse the master as the end image for perfect idle loops; transparency with chroma key plus a 2 px mask dilate or erode, audit zero grey opaque pixels, export GIF, APNG and VP9-alpha WebM; never use `colorkey` or AI background removers on pixel art; premultiply alpha before resizing; place as a corner peek at 10-15% of frame width.
- *ASCII carousel covers:* object as a 3D render on pure black, slow loopable spin, a script converts frames to ASCII (threshold .05-.12, gain 1.5-3, font 12-18) at 1080x1350 or 1080x1920, headline in a mono face plus a bold grotesque.
- *Scroll-driven site video:* generate paired start/end frames (assembled and exploded, 16:9, white background), a 7 s start-end transition, four or five versions, keep the one that reads both directions.
- *Ad factory:* write ten distinct angles (pain, proof, curiosity, contrast, objection flip), generate in parallel, review like a picky creative director (spelling, brand colours, framing, claims), sort approved and rejected with reasons, deliver the three to test first.

---

## 23. Product listing videos from phone footage (batch ffmpeg)

- **Goal:** a vertical product video per marketplace listing from raw phone clips (24 GB of `.MOV`). Facts: the platform caps video at 60 s (use <=55 s); a browser upload bridge capped files at 10 MB, so videos were size-targeted below 9 MB (`kbps = budget*8*1024/duration`, capped 6,000k, below 2,300k use 720p instead of 1080p; `-b:v -maxrate 1.3x -bufsize 2x`).
- **HDR to SDR:** iPhone clips are bt2020/HLG and look washed out: `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p` (needs an ffmpeg with `zscale`; check `ffmpeg -filters | grep zscale`).
- **Per-clip filter:** `scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30`, then `concat`; `-an -c:v libx264 -preset medium -pix_fmt yuv420p -movflags +faststart -t 55`.
- **Rotation gotcha (three rebuilds):** phone clips are stored landscape with a -90 display matrix. Reading raw stream dimensions makes portrait content look landscape; a multi-input `filter_complex` does not behave like single-input auto-rotate. After a four-way test on a 3 s sample the variant that came out upright was `-noautorotate -i clip` with **no** transpose in the graph (`transpose=1` on top of autorotate was sideways again). **Never theorise: render a 3 s sample in each variant and look at the frames before batch-processing 24 GB.**
- Upload: the web page's file input needed a manually dispatched `change` event after the file was set; always verify which listing panel is open before each upload.
- Reviewer corrections: all videos vertical, upright, product head-on, good quality; identify items by looking at frames; "ship the listing first, add the video second".

**Short prompt:** "For each folder of phone clips make a single upright 1080x1920 H.264 video under 55 s and under 9 MB, HDR tonemapped to SDR, no audio; test the rotation on a 3 s sample first and show me a contact sheet."

**Detailed prompt:** "For each listing folder, concat the clips in file order into one 1080x1920 H.264 video of at most 55 s with no audio, tonemap HDR to SDR (`zscale ... tonemap=hable ...`), letterbox with `pad`, 30 fps, size-target below 9 MB (`kbps = budget*8*1024/duration`, 720p if below 2,300k). Before processing the batch, render a 3 s sample for each rotation variant (`-noautorotate` without transpose, autorotate, autorotate with transpose) and show a contact sheet; choose the one that is upright. Identify products by looking at frames, not by guessing."

---

## 24. "Day in the life" pain-point-to-solution reel (script template)

A short script structure for a faceless or pictogram reel: **title line; three pain points; discovery of the product; a four-step win; a kicker; the domain read aloud.**

> "Day in the life of a [role]. Wake up. Fifty pitches sent. Zero replies. One [client] finally says yes. But they want [expensive requirement]. So I [do it]. [Weeks of grind]. [Failure]. I film it anyway. Revision one. Revision two. Revision nine. Then they ghost me on the invoice. [Expletive]. Then I found YOURBRAND. I made an account. Joined a campaign. No pitching. No new accounts. No chasing invoices. I read the brief. Make the video. Get approved. Upload the raw video. And I'm done. No [expletive]. That's the whole job now. yourbrand dot com."

Rules: three pains (pitching, setup and warm-up, revisions and unpaid invoice), then relief in four verbs, then one kicker. Spell numbers as words; spell the domain as it should be read ("yourbrand dot com"). Written for a young conversational female library voice; ~2.3 words/s raw, 1.18x speed-up.

**Short prompt:** "Make a 'day in the life of a [role]' reel for YOURBRAND: three pain points, then discovering the product, a four-step win and a kicker, young conversational female voice sped 1.18x, domain read aloud."

**Detailed prompt:** "Write the script in the template above (numbers as words, domain as 'yourbrand dot com'), generate one voice take (stability 50, similarity 75), speed it 1.18x, transcribe word times, then build the reel in whichever look fits (pictogram parable, pawn stage or pixel runner) with a pill per pain point, a counter for the failed attempts ('Fifty pitches. Zero replies.'), a stamped REJECTED or GHOSTED on each failure, a four-step checklist animating on the four verbs, and the standard end card."

---

# Cross-cutting lessons and gotchas

## A. Common pipeline (the "pure-render" method behind almost every film)

1. **One HTML page, `window.render(t)` is a pure function of time.** Also expose `window.DUR` (seconds), `window.READY` (a promise: fonts and images decoded) and optionally `window.SOUNDS = [{t, kind}]` and `window.VO` (line key to start time). No `setTimeout`, no CSS transitions or keyframes, no `Math.random` (use a seeded hash, e.g. `rnd(i)=frac(sin(i*127.1+311.7)*43758.5453)` or an LCG `s*16807 % 2147483647`). A frame is then identical on every render, cuts can be pinned to word times, and a still can be grabbed at any `t` for QA.
2. **Renderer:** Node plus `playwright-core` with the system Chrome (`channel:'chrome'`, headless, args `--force-color-profile=srgb --font-render-hinting=none --disable-lcd-text --allow-file-access-from-files`), viewport = W x H, `deviceScaleFactor 1` (2 for 4K). Loop: `await page.evaluate(t => render(t), i/FPS)`; `page.screenshot({type:'jpeg', quality:94-97})`; pipe to ffmpeg stdin (respect backpressure): `ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i - -c:v libx264 -preset slow -crf 14..20 -pix_fmt yuv420p -movflags +faststart out.mp4`. Modes: `video`, and `still W H t1,t2,...` for contact sheets. Query params select layout and variants (`?w=1080&h=1920&layout=tall&v=2`). `DRAFT=1` = half size, 1 sample per frame for fast checks; the first render after a cold start can be black, so check a lit pixel sum and reload.
3. **Lazy video clips inside the page:** a `<video>` cannot be seeked per frame deterministically, so pre-extract clips to JPEG sequences (`ffmpeg -ss S -t 4 -i src.mp4 -vf "fps=30,scale=576:1024:force_original_aspect_ratio=increase:flags=lanczos,crop=576:1024" -q:v 2 -start_number 0 %04d.jpg`, six in parallel) and draw frame `floor(t*fps) % n` into a canvas (a pending-decode queue flushed before each screenshot; render twice if a frame was pending). Screen recordings are the same: `hold:true` clamps instead of looping.
4. **Real motion blur:** render SUB sub-frames per output frame at slightly different times and average: `-framerate 30*SUB -i ... -vf "tmix=frames=SUB,select='not(mod(n-(SUB-1)\,SUB))',setpts=N/30/TB"` with `-r 30`. 3 samples over a 180 degree shutter ghosted on fast moves; 5 samples over a 0.4 frame shutter (`t=(i+s*0.4/SUB)/30`) was "smooth without ghosts".
5. **4K masters:** `deviceScaleFactor 2`, render four slices of the frame range in parallel (each piped to its own ffmpeg, `-preset medium -crf 12`, bt709 tags), then `-f concat -c copy`; make a 1080p copy with `scale=1920:1080:flags=lanczos`. Keep free disk space (a machine with 3 GB free needed an external drive; external drives may need a privacy permission).
6. **Voice is the clock:** generate the voice, transcribe with word timestamps (faster-whisper `small.en`, int8, `word_timestamps=True`, an `initial_prompt` with brand vocabulary), store `[{w,s,e}]`, and anchor every scene with `at(word, n)` (n-th occurrence; strictly-later search per anchor; a digit alias and prefix fallback for "twenty" to "20"; rejoin split brand names). Add the voice's start offset (0.25-0.5 s). A new voice take then re-times the entire film with one command.
7. **Audio from a cue list:** the page exports cues; a Python script (numpy, soundfile, 48 kHz stereo) synthesises and places them (see section F), mixes with ducking, and the final mux adds loudness normalisation.
8. **QA loop:** render stills at 10-36 timestamps for both layouts, tile into a contact sheet, **look at them**, patch, then render; verify the final MP4 with frame grabs and a whisper transcript of the final mix. Always tell the reviewer what could not be verified ("I cannot hear audio; play it once with sound on").
9. **Background renders:** run long renders in the background and poll a log for a DONE marker; never `sleep N; pkill` in the background (it killed a later recording); use explicit arguments, not shell loops that rely on word splitting in zsh.
10. **Edit safely:** when patching source with a script, `assert s.count(old) == 1` before replacing so edits never silently no-op; keep backups before big edits and keep each released version as a file.
11. **ffprobe may be missing:** read `ffmpeg -i file 2>&1 | grep -E "Duration|Video:|Audio:"`.

## B. Rendering and CSS gotchas

- Never put a CSS `filter` on a 3D-transformed container (it flattens `preserve-3d`); blur each face or a wrapper.
- A masked element with `filter` is clipped by its own mask: apply the blur on a wrapper.
- `mask-image` is blocked on `file://`: serve the page over a local `http` server.
- Many `filter: blur()` or `will-change` elements slow rendering: split the frame range into slices and render in parallel.
- Hidden browser panes pause animation frames (screenshots force frames; offline renders are unaffected).
- Images used in canvas from `file://` taint the canvas: embed small icons as data URIs.
- Pages that reveal sections on scroll give blank gaps in a full-page screenshot: capture a screen at a time and stitch. Wait ~5 s on hero pages whose counters start at zero.
- Mocked product capture: serve the built app locally, route-mock every API call with chosen data, block the real domains, inject the brand font and a visible cursor overlay, hide upsell buttons; make sure the mock returns the mode that stops the SPA redirecting to the live site. Recording at 2x: Chrome's screencast ignores `deviceScaleFactor`: launch with `--force-device-scale-factor=2 --window-size=1600,1200`, context `viewport:null`, set `Emulation.setDeviceMetricsOverride {deviceScaleFactor:0}` per page, screencast size = size x 2, resample to 30 fps.
- Media served with `Cross-Origin-Resource-Policy: same-origin` will not load on a localhost harness: route to local copies.
- Chrome screenshots look soft at 1x: capture at 2x.
- If stills come back all black: check that "hide" CSS and inline display restore are not fighting (store the original display value on show).

## C. ffmpeg recipes and colour

- **Colour range (important):** screenshots are full range, so output becomes `yuvj420p`; always convert and tag: `-vf "scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv`, otherwise players show washed or crushed colours.
- Final mux: `ffmpeg -y -i silent.mp4 -i soundtrack.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 16..20 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart -shortest out.mp4`. Social loudness target -14 LUFS (`loudnorm=I=-14:TP=-1.5:LRA=11`); web hero films -16 LUFS. After AAC the true peak can read +0.6 dB: add a limiter before the encode (`alimiter=limit=0.84` then lower to 0.63 if needed) and re-mux only the audio.
- Web copy: `-crf 25 -maxrate 4M -bufsize 8M -pix_fmt yuv420p -c:a copy -movflags +faststart`; posters: JPG at 1 s then WebP quality 78 method 6 (a 129 KB JPEG became 32-56 KB). Posters must be re-cut each time a film is re-rendered.
- Silence trim and tempo: `silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse`, `atempo=1.18`. A speech tightener: mono 44.1k, RMS (10 ms) below .004 is silence, cap any silence at 0.26 s keeping half each side, then `atempo=1.04,loudnorm=I=-16:TP=-2:LRA=11`.
- Contact sheets: `ffmpeg -i v.mp4 -vf "fps=1,scale=270:-1,tile=8x5" -frames:v 1 sheet.jpg`; timestamped: `fps=1,scale=360:-1,drawtext=text='%{pts\:hms}',tile=...`; key frames `select=eq(n,15)+eq(n,40),scale=640:-1,tile=2x5`.
- Detect cuts `select='gt(scene,0.3)',showinfo | grep pts_time`; black frames `blackdetect=d=0.1:pix_th=0.05`; loudness `volumedetect` or `ebur128=peak=true`; silence `silencedetect=noise=-30dB:d=0.6`; frame count `-map 0:v -c copy -f null -`.
- Solid-colour test clips: `-f lavfi -t 1.5 -i "color=c=0x4338ca:s=540x960:r=30"`; **always set `-t`** on a lavfi source.
- Mix many keystroke/click files: `-filter_complex "...adelay=ms|ms...amix=inputs=N:normalize=0:duration=longest,atrim=0:T"`; page-flip noise: `anoisesrc` with `highpass=f=1800,lowpass=f=7000` and fades.
- Hold a frame: `tpad` must come **before** `trim`; or `select=eq(n\,0),loop=N:size=1,setpts=N/30/TB`. A simulator or phone recorder writes no frames while the screen is still, so use `fps=30,trim=a:b,setpts=PTS-STARTPTS` instead of input `-ss`.
- Letterbox to 9:16: `scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30`.
- **Phone clips and rotation:** test `-noautorotate` vs autorotate on a short sample and look.
- Detect black frames from a source (to skip them): `signalstats` mean Y on a 32x32 downscale at 4 fps.
- Hardware encoders (VideoToolbox) are fine for speed on drafts; use x264 for finals.
- Download references: `yt-dlp -f "bv*+ba/b" --merge-output-format mp4 --write-info-json` (needs the ffmpeg location flag; TikTok needs a pinned yt-dlp plus `curl_cffi`); If a platform blocks the download without a login, ask for the original file instead.

## D. TTS, voices and pace

- **Never clone a real, identifiable person's voice** (an actor or a creator) without their permission. Instead pick a stock or library voice **matched by measurement**, or blend stock voices, or clone the reviewer's own voice with consent. The assistant refused such clones and the reviewer accepted that.
- **Match by measurement, not by ear:** extract the reference narration (16 kHz mono), transcribe with word timestamps, then measure words per minute (or syllables per second), median pitch with p10/p25/p75/p90, pitch range in semitones, speech onset, pause histogram. A simple pitch tracker: frames 40 ms, hop 20 ms, RMS gate .02, autocorrelation lag 60-300 Hz band, accept if the autocorrelation ratio > .5. Reference narrators seen: 188-225 Hz female, ~137-155 wpm, ~2.5-3.1 words/s; a bright female narrator at 254 Hz.
- **Pitch bands that read as adult:** female about 170-240 Hz, male about 95-150 Hz. A voice at 254-291 Hz sounded "like a child" and was rejected, even though it matched the reference numbers. "Voices sounded childlike" -> lower target. Designed voices asked to be "excited" often come out high; any voice can be pitched down in semitones (`asetrate=24000*r,aresample=24000,atempo=1/r`) before pacing.
- **Pace is a setting, not part of the voice.** Matching a reference at 3.93 syllables/s was heard as "very slow"; default became 5.0 syllables/s (4.5 brisk, 5.6 very fast). Library voices render ~2.3 words/s raw and need `atempo=1.15-1.18` for the 2.6-3.1 words/s reels use. Cap time-stretch at about 1.3x or the voice smears.
- **Consistency:** cloned or designed voices drift 2-4 semitones take to take; presets and small stock voices drift less. For long scripts record **line by line**, re-roll any line whose median pitch leaves the target band (up to 4 tries), pace each line, join with 0.14-0.2 s gaps. A single long take drifted from 155 to 184-211 Hz and blurred the last word. Keep one voice across sibling films.
- **Tone words:** "more monotone, better flow" beat "very excited" for long reels. A steady instruction ("calm, confident narrator with a steady level pitch, speaks fast in one smooth continuous flow, words linking naturally, no big rises, no long pauses") plus a lower sampling temperature (~0.6) held 141-178 Hz.
- **Local engines used:** a small fast stock-voice model (Kokoro, ~4 s per voiceover, flatter), an expressive 1.7B model with preset speakers plus an instruction field and a VoiceDesign mode, a cloned-from-reference mode (Base) for identical output each reel, free neural cloud voices via `edge-tts`, OpenVoice for re-colouring toward a consenting speaker. Pronunciation: write brand names as the TTS should say them (a compound brand as two words, a domain as "yourbrand dot com", initialisms as spaced letters "H Q", "shadow banned" as two words, "U G C", "D M"); spell numbers as words; always run whisper on the take and check brand words.
- **Hosted TTS (ElevenLabs-style):** model v4, stability 50, similarity 75, speed 100%; two takes per script, pick the cleaner by word timing; about one credit per character (a 330-character script cost ~330 credits; a 52 s video ~800); prefer the API with your own key over driving the web app; check you downloaded the newest take (an old take is easy to grab by mistake); the "search with audio sample" feature returns a similar library voice, useful for matching a reference.
- **Local model downloads:** a VPN can slow multi-GB downloads to a crawl; download over a direct connection, and keep large downloads off any machine that serves a live site.
- Dubbed lines: splice a re-recorded line into the same slot (trim, same tempo) so no other timing changes; if tone jumps, regenerate in one take.

## E. Captions and on-screen text

- **Platform-native captions:** white 800 weight with a black outline, spoken word in yellow `#ffe14d` or a payoff word in an accent, 1-4 words per chunk (break at punctuation), max width ~960 px on 1080, shrink to fit, pop .86 -> 1.
- **Classic short-form text:** white on a black bar, black on white, or white with a black border; ALL CAPS hook placed above the head (not too far up); never more than two lines; 6-10 words per line; the first caption equals the hook word for word; legible with sound off; no random barely-visible emoji; no punctuation clutter.
- **Safe zones (1080x1920):** text inside x 70-940, y 250-1480 (avoid top ~15%, bottom ~25%, right rail). Pixel-caption reels: keep the bottom 420 px clear. Wide safe box x 70-1850, y 40-1040. Check that a caption does not cover the tapped button at the moment of the tap (moved up twice).
- Caption chunk logic for pills: pop with `back()` scale .72-.9 -> 1 and a 24 px rise; non-white pills get a 2 px translucent stroke; add a soft drop shadow on bright backgrounds.
- One typeface across the film; the **chrome logo is the only exception**.
- A transparent text asset (e.g. a domain in white semibold, no background) is better delivered as a PNG at several widths (600/1200/2400/6000). When restyling a text asset, change only the fill (a chrome version that altered the letter shapes was rejected).
- No emoji in generated films (use inline SVG icons); no em dashes in brief copy.

## F. Sound design recipes (all synthesised, no samples, nothing to license; a few real keypress and click samples from a licensed kit are fine)

- Buses: `mus`, `fx`, `wet` (reverb send), later `tvb`. `put(buf, sig, t, gain, pan)`; all SFX times = word-onset times + voice offset. Sample rate 48 kHz stereo float.
- **Primitives:** kick = sine 45-48 Hz + `110-120*e^(-t/.03-.035)` pitch drop, decay .16, plus a second harmonic; clap = three noise bursts at 0/9/18 ms plus a 90 ms tail; hat closed 50 ms / open 220 ms = high-passed noise; pluck = detuned saws (x1, x1.004) through a low-pass whose cutoff follows a fast decay envelope; stab = three detuned saws per note (1, 1.006, .994) low-passed 500 Hz + bright*env; bass = sine + .35 low-passed saw, decay .35; 808 = `tanh(sine*2.2)` with pitch fall `f+90*e^(-t/.02)`; bell = sine f + .4*sine(2.76f)*e^(-t/.2) + .2*sine(5.4f)*e^(-t/.08); impact = sine 38 Hz + `60*e^(-t/.08)` boom (decay .5) + high-passed noise crash (decay .45); riser = low-pass-filtered noise swelling to the cut; **whoosh** = band-passed noise sweep, placed so its **peak** lands on the cut (`t - d*.45`); typing tick = short noise burst at 1.8-2.4 kHz or a 2.2-2.5 kHz sine 30 ms; mouse click = high-passed noise 60 ms + a 1,600 Hz pop; pop = short sine 500-1,500 Hz; ding = bells at 1568 and 2093 Hz delayed 110 ms; "sad note" = detuned square falling 392 -> 262 Hz with vibrato; droop = 420 Hz falling sine (a song dying when a tab closes).
- **Reference-measured families:** bright clicks on pop-ins (10-25 ms rise, 15-60 ms fall, 8-9.5 kHz), soft swishes on scene changes (80-190 ms rise/fall, 6-8.6 kHz, landing 0.1-0.3 s after the picture changes, sweeping in the direction of the slide, widened with a second unrelated noise take), low thuds on landings (4-12 ms attack, 130-320 ms tail), and a deep boom after a silence on the end card. To measure a reference's effects: subtract right from left channel to remove the centred voice, band-pass and take an envelope.
- **Cue-driven sync:** a script plays the page silently and logs the first frame each pop, tick and typed character draws; the SFX builder places sounds at those times. Re-run after any change to the picture or voice.
- **Ducking:** `lvl = moving average(|voice|, 50 ms)`; `duck = 1 - .5..55*clip(lvl/.04,0,1)`; smooth with an 80 ms box; `mix = (mus + room)*duck*.72..8 + fx*(.6+.4*duck) + voice*1.05..1.1`. Room: five stereo delay taps 113/171/237/331/470 ms at .33/.26/.19/.13/.08 with alternating channels.
- **Master:** fade the last 1.3-1.6 s (`linspace(1,0)^1.5`), soft clip `tanh(mix*1.1)/tanh(1.1)`, normalise, loudnorm as above.
- **Beds:** 104-128 BPM; each film got a **different** bed on purpose. Typical groove arrives on the big payoff (or when the dark world opens), drops out for jokes (one pluck per bar), a soft pad runs under the end card; hopeful then off-key then dead for a "bad" screen; silence then one boom is the strongest end card.
- A "TV off" sound and a "channel change thunk" (see format 10).
- Say plainly: the assistant cannot hear. Ask the reviewer to listen once with sound on, and check the voice stem's transcript for accuracy and the mix for intelligibility only (Whisper hallucinates on a music tail).

## G. Posting and delivery specs

- **Shape rule (enforced by a posting tool):** tall (1080x1920) goes to Instagram Reels, Facebook, TikTok, YouTube Shorts and Snapchat and **never** to X; wide (1920x1080) goes to X **only**. Every video skill ships both layouts and the wide one is a separate composition. Name files by shape (`...-WIDE-x-only.mp4`, `...-TALL-ig-fb-tiktok-shorts-snap.mp4`). Square files are not covered. A posting tool should read the real size with ffmpeg (rotation included) and refuse a wrong-shape file.
- Delivery encodes: H.264 (High profile, level 4.1), yuv420p, AAC 128-256k, `+faststart`, 30 fps (60 fps only for beat-grid or glass films). Upload copy for posting: `crf 23, maxrate 9M`. Hero film on a web page: web copy ~4-11 MB for 30-55 s; starts muted with a "Sound on" button; use `?v=N` or a new filename for every re-render (CDNs cache a file for an hour and may cache an old copy as `application/octet-stream`); iPhones need HTTP range requests (`206` with `content-range`/`accept-ranges`, `416` for out-of-bounds): test with `curl -r 0-262143`; serve video MIME types.
- **Hero player device rule:** upright phones and small tablets get the tall cut (a `matchMedia('(max-width: 900px) and (orientation: portrait)')` check, wrapper `aspect-ratio 9/16`, max-height 78vh); computers and large tablets get the wide cut. Verify at 1440 and 375 px widths.
- Size limits seen: a 30 MB limit on files sent through a chat app (a 31 MB wide master did not play on a phone: send a ~11 MB web copy too); a marketplace caps video at 60 s; a browser upload bridge capped at 10 MB; a free hosting tier allowed a small number of commands per week (pull and push a project in one command each); X captions 280 characters (attach the video before typing the caption, or a bare URL becomes a link card and greys out the media buttons); TikTok description 2,200 characters; Instagram 30-hashtag limit. Verify limits again before relying on them.
- **Clean final file rule (for creator hand-off):** a platform watermark on a **draft** for review is fine, but the approved final must be the original clean file: post privately (set "only me", enable "save to device" without the watermark option), or export from the editor at the highest quality (1080p or higher, 9:16) with the end logo clip deleted; check it once from the camera roll (no logo, no end card, sharp, clean sound); upload the original from the camera roll straight to the shared folder (never a screen recording, never a file passed through a messaging app, never a download of a posted video: all lower quality); name it day number then hook (`01-my-hook.mp4`). Files posted by an automation wall break if they carry marks or are re-compressed.
- **Posting from a real phone (automation notes):** the clip must be in Photos first; the picker is oldest-first; control by fractions of the screen (taps work across devices); never retry inside the create flow, start over instead.
- Hashtags and captions: universal rules: line one sells line two (a specific object: number, tool, place, time); put the cost in the open ("30 questions", "20 minutes, no coding"); deliver, don't announce; ask for the action that matches the strongest signal (saves above ~2% and shares above ~1% are the strongest distribution signals); strip AI tells (no "not X but Y", one-line closers, triads, em dashes, "game-changer", emoji walls; at most one emoji unless the niche norm); draft only, a human approves. Counts: TikTok 4-5 tags after the text; YouTube title hook in the first ~55 characters with one number; Facebook 2-3 tags; X 0-1 tag; avoid copied captions, claims without number plus source plus date, income, weight-loss or health promises, 10+ tags in sensitive niches, "follow for more". Owned accounts: one unique video a day cross-posted the same day; never delete (set private); never use the platform's scheduler; engage a few minutes before and after posting.

## H. Hooks, scripts and structure rules (video-relevant)

- **Theory the reviewer kept repeating:** "The format is not the variable. The first second is: who is on screen, what are they doing, and does the hook read before the thumb moves." "If it looks like an ad, it dies." "A creator reading a script is the fastest way to a 400-view post." "Lead with the problem; speak like you are texting or FaceTiming a friend; the product is the solution, not the whole video." Copy structure and pacing, **never the words**.
- **Principles from a short-form psychology note (apply silently, do not turn into a template):** write for one person, as if sending it to them; a viewer asks two questions (is this valuable, how much time will it cost); open a loop and keep it open (a gap between what the viewer knows and wants to know); line one sells line two; a number, a name or a date beats a summary; value by 5-10 s; disarm "this is an ad" where it lands; cuts refresh attention, loops create it; the 10-year-old test per line; the swap-the-subject test (if the script would still work with the subject swapped, it is formula); name the "drop line" (the first line that does not sell the next).
- **Timing skeleton:** hook 0-2 s; problem 2-6 s; product on screen 6-18 s (by 10-15 s); value 18-35 s; call to action in the last 2-3 s (never in the first 4 s); demo at most 8 s; one feature per video; features translated to outcomes; end on the payoff or loop, no sign-off language after the peak. Something new on screen every 1-2 s; a pattern interrupt about every 2.5 s. Delivery 150-180 wpm for a person on camera (a public creator at 237-296 wpm was not copied: own data showed 140-190 wpm outperforming faster delivery, correlational only). Pictogram or faceless voice-overs run faster (5 syllables/s).
- **Ten hook types:** outcome or specific number; loss-framed problem; curiosity gap or open loop; relatability or identity call-out; contrarian; story cold-open or confession; status or excitement; the question they already ask; authority transfer; visual-only. Text-hook grammar: call-out + condition + promise. Banned openers: "This app is amazing", "Download this app", "You need this app", "This changed my life", "Introducing...".
- **Hard fails for a draft:** app, brand or CTA in the first 4 s (unless feature-first); a generic opener; no hook readable in 1-2 s; non-classic text, more than two lines, bottom of screen, over the mouth, outside the safe zone; dead air (a gap over ~1 s or an unchanging frame over 6-8 s); a third-party watermark, stock footage with an AI voice, an undisclosed synthetic presenter; claims (guarantees, medical, financial, legal promises, fake testimonials); off-niche or off-brief; required product moment missing; trending audio that stopped trending (over 2-4 weeks); not 9:16 or unusable resolution.
- **Editing:** "zero pause or zero gap between lines; gaps and pauses cause drop-off": film with a few seconds of silence after each line so the cut lands a millisecond into the next sentence; film and edit inside the platform's own editor for organic posts (CapCut only for ads or overlay-heavy edits); film in a real environment with the face well lit and not framed too high, subject at least 60% of frame, plain or blurred background, no designer lower-thirds.
- **Series scripting rules the reviewer set for house formats:** one recurring signature word in every script; order = hook, second hook, emotional line, offer, close, end card; full sentences in the voice-over (not runs of 3-word punches); the same end card every time; one metaphor per reel (the dino, the pawn, the parable) so a series is recognisable and cheap to produce; **each new film must look different from the last** (different visual language, bed, pacing) unless it is a deliberate series.
- **Claims and honesty hygiene:** label example numbers "example" and sample data "Sample data"; never invent stats; show only real or reviewer-provided numbers; every number in a film must agree with every other (pick one completed demo state); do not show what creators are paid; do not promise outcomes; do not claim availability that does not exist (a store badge vs "coming soon"); do not let a film show features that run ahead of the product (flag it); re-check client facts on the client's site on the day; if the business mechanics are uncertain, write them down and get them confirmed before scripting (a wrongly explained pay model was rejected); disclosure: when a platform requires a paid-partnership label, the brief may drop an unnecessary label but must never tell creators to deny being paid.
- **IP and likeness:** no real actors' voices cloned; no real TV character faces or names as a reference; no third-party brand characters, game footage, logos or trademarked titles in client videos (label by genre, redraw originals); generated look-alikes of someone's style are fine, reused frames, words or voices are not; use music only that you synthesised or that is licensed (a reference's track belongs to its creator: build a score with the same **shape** instead).

## I. Reviewing a draft (an automatic reviewer, or you)

- **Evidence extraction pipeline (ffmpeg plus a speech model, no cloud):** probe duration, size, fps, audio; frames by exact timestamp (`-ss t -i video -frames:v 1 -vf scale=540:-2 -q:v 4`, one call per frame because select filters drift on variable-frame-rate phone clips) every 0.5 s for the first 6 s then every 1 s (max 140); per-frame features (a rule-based skin-ratio face proxy on a 135x240 downscale, motion = mean absolute gray difference to the previous frame / 255, brightness); scene cuts `gt(scene,0.3)`; audio `silencedetect=noise=-30dB:d=0.6` and `ebur128=peak=true` (music present if audio exists, no transcript, and silence below 50%); transcript with `faster-whisper small, int8, vad_filter, beam 3` (wpm = words / speech seconds * 60; filler regex um, uh, like, you know, basically, literally...; speech onset); OCR for on-screen text (a native OS OCR or RapidOCR); a vision model for labels on at most 20 spread frames; key frames at 0, .5, 1, 2, 3, the first four cuts and the last frame.
- **Verdict shape:** binary "good to post / fix these first", timestamped fixes, reach and conversion scores. Reach dimensions (weights): frame-0 stop power 20, hook type and specificity 15, second hook 3-8 s 12, pacing and payload 13, delivery 10, emotional or identity resonance 12, share or save value 8, ending 5, native-ness 5. Conversion dimensions: product moment timing 25, problem-solution structure 20, features to outcomes 10, trust or proof 15, CTA 15, campaign alignment 15. Conservative post rule: no hard fail and high reach and conversion and alignment. Never inflate ("a 6 is a 6"). Say what is right, what is wrong, a score, and "post it" or "make a new video". Fixes in the reviewer's words: "cut the first two seconds, say the number earlier, keep the app on screen longer".
- **Caveat found:** a reviewer written for face-first creator posts marks motion graphics down (no pain point early, product shown late, a pause before the payoff); decide whether the rule fits the format before obeying it. A local model over-fires hard fails; demote style rules to timestamped must-fixes. Review the whole video against the brief, not a script word for word.
- Typical rejection phrases to detect: "no pain points hit", "0 call to action", "didn't remake the video, only changed the title", "yapped for 25 seconds about nonsense with tons of filler words", "text not classic and sitting at the bottom", "got asked to add a demo, not photos", "random barely visible emoji", "audio hasn't trended since...".
- **Reference breakdown fields** (for every reference): hook text and timing, cut times, caption style, audio loudness, CTA structure, product-reveal timing, view counts **read that day with the date** (never from memory), why it worked.
- **Reading a reference properly:** play the whole thing (reels end to end, not the profile grid); a build based on a grid screenshot was thrown away. Read a brand's content style from the screen that day (screenshots and a scrape), with numbers and the date.

## J. Review patterns (what to do by default)

- **Keep momentum:** pick sensible defaults, state them in one line and build; ask only for what the work cannot proceed without.
- **Show a cheap first look** (a still, a contact sheet, a 3 s sample) before an expensive render or a long local-model run; show the master character still before animating.
- **Study the reference frame by frame and reproduce the exact devices that make it work** (the beam, the scroll-by, the outlined word); when the reviewer names a device, it must be in the film. "Stop overcomplicating it."
- **Deliver variations when asked** (three fully different versions), then iterate on the ones he loves ("I love 2 and 3: combine them").
- **Report against each requested change in a table** and verify the delivered file (frames and transcript), not the source.
- **Quality asks:** "much better quality" means re-record screens at 2x, render 4K, downscale; "more expensive-looking ending" means liquid glass, depth, light, a restrained palette.
- **Colour asks:** calm palettes (no flashing yellows and reds); brand colours read from the live dark-mode site; one accent only; logo cut per background.
- **People asks:** invented names matching the niche; made-up domains; no real handles or counts next to people; rotate the lead face; sample profiles fully filled in; "Sample data" tags.
- **Local and free first:** render on the reviewer's own machine; local TTS and image models where possible; avoid cloud renderers and credits unless the reviewer opts in; save credits (one 52 s video cost ~800 TTS credits; at three videos a day this needs a bigger plan or a local voice); when credits ran out, the reviewer said to use the house voice and keep going.
- **Speed asks:** when the reviewer says "too slow", the usual fix is halving the length, cutting every scene on a beat or a word, and a faster, more upbeat voice; "too fast" means giving a section more time and context.
- **Posting is separate from building:** draft first, publish only when told; keep previous versions in a backup folder; send finished files and keep copies in a named folder; deploy new films under new filenames.
- **Honest limits:** the assistant cannot hear audio or watch at speed; say so each time, and list what remains unverified.

## K. Tool notes (public tools used; swap for your own)

A headless Chromium via Playwright for rendering and capture; ffmpeg (no ffprobe needed); faster-whisper or mlx-whisper for word timestamps; yt-dlp for references; numpy, scipy and soundfile for synthesis; a React video framework for AI-generated-plate reels and templated batches (render stills from one bundle for speed); a free local TTS stack (Kokoro, an expressive 1.7B model, edge-tts, OpenVoice) plus an optional hosted TTS; a component library MCP for 3D book, device-frame, glass and border-beam references (copy the source exactly when told, then re-implement in CSS or canvas); a prompt library site for motion references (read it in a browser); an iOS simulator for clean app recordings; a screen-recording tool for demo clips; a posting server for real phones; a local image model and a local image-to-video model for AI plates; hosted video and image models (Kling-class, Seedance-class, image models) for generated UGC recipes; a gittrend-style repo-trending page for finding existing tools before building one (read the code for safety before running anything).
