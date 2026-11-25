# Motion rules: timings, easing, cut rates and a 15-second recipe

Distilled from a frame-by-frame study (eyes and scrapey, `docs/EYES-AND-SCRAPEY.md`) of two public galleries of
AI-made motion videos, revid.ai's ranked launch-week wall and the motionvideo.xyz catalogue, read on 24 Nov 2026, plus
the measurements taken while rebuilding the library pieces named below. Numbers marked "measured by the site" are the
site's own; the rest were read by us. Pair this with the `motion-moves` and `showreel-and-launch-film` skills.

## 1. What the most-liked videos measure (63 videos, measured by the site)

| Measure | Value |
|---|---|
| Length | median 29 s; 52% are 30 s or less; 24 of 63 run 20 s or less |
| Showreels | 16% of videos but 42% of likes; 8 of the top 10 showreels are exactly 15.1 s, 9 of 10 dark, all music, no voice |
| Hard cuts per 10 s | top 10: 2.2, the rest: 1.0; showreels 4 vs 0.9; dark videos 2.0 vs light 0.7 |
| Average shot | top 10: 3.6 s, the rest: 6.0 s |
| Opening | first hard cut at 3.9 s on average; 21% fade in from black; 59% show readable text within 2 s; 59% open on the finished result |
| Aspect | 78% 16:9 |
| Audio | 71% music only, 25% voiceover; median loudness -14.2 LUFS |
| Colour (all frames) | white 43%, black 37%, grey 13%, orange 5%, blue 3%; 25 of 63 are neutrals plus one accent |
| Accent families | blue 16, orange 11, red 10, green 8, mono 8, yellow 5, purple 5 |
| What predicted likes | naming the tool people search for in the post: 3.5x the median likes. No craft measure (length, cuts, colour, motion, loudness) correlated with likes. |

So: distribution beats craft. The hook and the post text matter more than a third pass on easing. Open on the finished
result, not a logo.

### Per style (measured by the site)
| Style | Length | Hard cuts per 10 s | Ground |
|---|---|---|---|
| Showreel | 15 s | 5.3 | dark |
| Startup launch film | 26 s | 0.8 | light |
| Keynote reveal | 20 s | none | light |
| Kinetic type | 157 s | 2 | dark |
| Bauhaus shapes | 15 s | 3.3 | dark |
| 3D logo reveal | 21 s | none | dark |
| Illustrated explainer | 142 s | 5.8 | light |
| UI product demo | 30 s | 0.3 | light |

Rule of thumb: dark if you want faster cuts (about 2 per 10 s), light if calm (about 0.7).

## 2. Easing and timing

| Use | Curve or value |
|---|---|
| Default UI entrance | `cubic-bezier(.22,1,.36,1)` (an ease-out-quint-like curve; the most used curve on both sites' own UI) |
| Symmetric move / morph | `cubic-bezier(.65,0,.35,1)` |
| Morph with the camera on the same curve | 0.8 s `cubic-bezier(.45,0,.15,1)`; content dissolves in the back half of the glide |
| Sheet / drawer | `cubic-bezier(.32,.72,0,1)` |
| Back-out pop | `cubic-bezier(.34,1.56,.64,1)` (pop-in 0.4 s, 20 ms per column or 40 ms per dot stagger) |
| Press | 0.15 s `cubic-bezier(.175,.885,.32,1.275)` |
| Colour change | about 0.35 s `cubic-bezier(.44,0,.56,1)` |
| Letter stagger (logos) | 640 ms bounce, 40 ms per letter |
| Card split / fan | settles in about 0.3 s (images at 0.34 s, fan 0.44 to 0.65 s) |
| App intro loops | 1 to 9 s; springs dominate |
| Carousel glide | about 0.55 s |
| Colour flood | about 0.3 s and it must overscale past the corners |
| Poster-style camera | never stops: a slow 1.03 to 1.07 push per scene; nothing snaps to the beat |
| Beat grid | 120 BPM = 0.5 s per beat; land every entrance on a beat |

Springs are closed-form step responses (no simulation state). A value with many targets is the sum of one spring per
change (`ui-state-morph-chain`). A tab indicator's two edges ride different springs so it stretches. Measured examples
from the library: isometric bars grow on k120 c17 and lift on k200 c22; a critically damped boundary spring at
omega 22 (`dither-donut-chart`); a `linear()` spring string with delay = col x 11 ms + row x 16 ms
(`stacked-cell-kpi-board`); an AI chat reply streams at about 160 characters a second, first token 0.69 s after send.

## 3. Build rules (from the public long-brief prompts, paraphrased)
- One HTML file; every style computed from time inside `render(t)` (`seek(t)`): no CSS transitions, no timers, no
  state between frames.
- Camera: one world, one transform with position and **log-space zoom** (`ball-guided-ui-world-camera`).
- Motion blur: render at 3 to 4 subframes per frame and blend:
  `FPS=180 node engine/tools/render_demo.cjs video in.html sub.mp4 1920 1080` then
  `ffmpeg -i sub.mp4 -vf "tmix=frames=3:weights='1 1 1',select='not(mod(n\,3))',setpts=N/60/TB" -r 60 out.mp4`.
- Render one still per beat first; scan for single-frame pops (frame differences 3x their neighbours).
- Real footage as 30 fps JPEG sequences (or all-intra `-g 1`), and await `seeked` before drawing.
- Sound: one effect per event, placed by its measured peak, not its file start; loudnorm to -14 LUFS.
- No `will-change` on anything the camera scales (blurry text). Never put `opacity` or `filter` on a `preserve-3d`
  element; fade its wrapper. Text swapping inside a morphing container needs its own timing. Match cursor position
  and speed on the loop frame. Last frame = first frame for loops.
- A **banned list** in the brief keeps films clean: crossfades, blur-ins, 3D flips, particles, glows, holds over 1 s,
  bouncy easing, anything that looks like a template.
- The long brief that produced the cleanest films has six blocks: inputs to ask for, direction (look + banned list),
  structure (BPM, scene by scene, "something happens on every beat"), build rules, gotchas, and "show me the beat
  map and 4 stills before the full film".

## 4. The 15-second vertical recipe (1080x1920), from library pieces only
| Time | Beat | Pieces |
|---|---|---|
| 0 to 2 s | Hook | `notification-storm-then-one-card` on light, or a word-by-word question; dark with the accent on the punctuation |
| 2 to 3.5 s | Logo | `habit-tile-grid-diagonal-pop-logo` (a grid built from the product's own idea) or `wordmark-squeeze-into-period-pill` that becomes the main button |
| 3.5 to 11 s | Three feature beats | headline top in two lines + real phone screen below, joined by `ui-state-morph-chain` or `theme-toggle-dark-flood`; `two-phone-cloud-sync-arc` for anything that moves between devices |
| one of them | Proof | `stat-stack-slot-roll-landing-ring`, `unit-dot-grid-fill-count`, `mechanical-odometer` or `dot-matrix-revenue-card` |
| 11 to 15 s | Out | the logo comes apart in reverse, so the last frame is the first and the platform loops it |

Palette: one neutral ground + one accent. Music only or voice; -14 LUFS. Make one 15 s dark cut and one 20 to 30 s
light UI demo cut per product.

## 5. Formats that keep working
- **Showreel** (15 s, dark): near-black + one hot accent + cream; HUD corner marks and mono labels on every scene; an
  easing board (`easing-lanes-comparison-board`), a flood, a Truchet field recoloured by a wave
  (`truchet-arc-tile-field-radial-recolor`), a slam word, an end card.
- **App launch, one continuous take** (about 30 s, square or wide): wordmark folds into its period (.55 to .95 s), dot to
  pill (1.15 to 1.6 s), label (1.8 s), click (2.2 s), iris open (2.5 to 2.85 s, `iris-blade-aperture-photo-open`), circle
  to big rounded square (3.18 s), grid unfold (3.86 to 4.2 s, `photo-tile-grid-paper-map-unfold`).
- **Vertical app update** (15 s, dark navy): two-line headline top with the punctuation in the accent, real phone
  screens below, a segmented pill switching screens, a two-phone sync arc, a logo built from a grid and taken apart.
- **5-second hook**: serif question, accelerating notification storm, blow-out, one card, the answer line.
- **Light pastel app promo** (about 18 s): mascot icon, headline left + phone right, marker highlight on accent words,
  floating notification chips, a theme toggle that floods the scene dark.
- **One-shape film** (about 11 s): one shape on light grey becomes icon, button, toast, menu, tab bar, widget, tick.
- **Keynote reveal** (about 20 s, white): one word at a time, slow pushes, no hard cuts.

## 6. Faceless explainers: what nine measured reels share
From a frame-by-frame study of nine high-performing faceless motion reels in nine niches, 24 to 25 Nov 2026. Full
numbers, the nine looks and seven caption variants: [`FACELESS-EXPLAINER-STYLES.md`](FACELESS-EXPLAINER-STYLES.md).

| Measure | Value |
|---|---|
| Hard cuts | 0 to 1 per reel in 7 of 9 (ffmpeg scene threshold 0.3); the others 2 to 7, or one every 8.2 s |
| New idea / set | every 2 to 4 s (diagram redraws every 4 to 8 s at the slowest) |
| New small element | every 0.4 to 2 s; nothing still longer than ~3.5 s |
| Voice | 155 to 205 wpm (2.4 to 3.4 words/s), from frame 0, gaps 0.3 to 0.6 s at most |
| Music | none audible by level in most: the level drops to silence between phrases; effects on the hits |
| Loudness | mean -16.9 to -17.7 dB on the references; master -14 to -16 LUFS |
| Spring pop | scale 0.8 or 0.85 to 1.05 to 1, 6 to 9 frames, 4 to 8 % overshoot |
| Stamp slam | 1.6x to 1x with 2 to 6 deg tilt, then hold |
| Slide-in | 0.3 to 0.4 s ease-out (fast slides get motion blur) |
| Caption word in | fade + 6 px rise + blur-in over ~0.15 s, or a colour sweep on the word's start time |
| Calm diagram style | ease-in-out 0.3 to 0.8 s, no overshoot |
| Stagger | 70 to 100 ms between list rows |
| Counter | ease-out over 1 to 3 s; exponential for "racing" money-style counters |
| Bottom of frame | the lowest 30 to 35 % stays empty for the platform UI |

Rules: the hook is complete on frame 0 (no logo, no fade); change the picture, not the shot (springs, morphs,
redraws, circle wipes, colour floods); one accent colour and emphasis by dimming the rest; a number that moves from
start to end; the ending loops into the first frame or lands on one line. A new account changes the story device,
narrator and camera, not only the palette (FORMATS.md format 26).

## 7. Low-poly 3D series numbers (50 parts)
39 to 41.5 s (35 s of voice + a 5 s end card), 1080x1920 at 30 fps, hard cuts on word times,
captions at 64 % of the height with a 0.2 x size black stroke, punch words at 1.5 to 1.6x, stamps at y 960 to 975
or above 650, sheet content out of y 660 to 900, mean -19.5 to -20.5 dB and max about -2 dB after
`loudnorm=I=-16:TP=-2` plus `alimiter=limit=0.8:level=false`. Details: [`../pipelines/day-in-the-life/`](../pipelines/day-in-the-life/).
