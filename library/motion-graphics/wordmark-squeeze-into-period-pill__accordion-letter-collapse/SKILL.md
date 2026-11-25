---
name: wordmark-squeeze-into-period-pill-accordion-letter-collapse
description: A heavy lowercase wordmark folds letter by letter into its own full stop, the dot stretches into a black pill and a label rises inside it; then it all plays back out. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Wordmark squeeze into period pill

**Code name:** Accordion letter collapse into the dot. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
A black lowercase wordmark with a full stop ("yourbrand.") sits on warm off-white (#ecede8) with a small grey tagline. At 0.55s the letters start to slide right into the full stop and get narrower as they go, accelerating (ease-in) so by 0.95s only the dot is left, sitting where the period was. At 1.15s the dot springs out sideways into a black pill and travels to the centre (a short horizontal smear while it moves fast). At 1.75s the label rises into the pill from below its own edge. A cursor drifts in and presses it at 2.45s. From 3.05s it plays backwards: label drops, the pill springs back into a dot at the period's spot, and the letters spring back out to the full word by about 4.5s. The last frame is the first frame.

## When to use it
Opening or closing a launch film or app promo whose name is one word: the logo turns into the main button, which says "this is what you tap". It is the open and the close of the same film, so it suits loops. Wrong for long names (over about 9 letters the squeeze looks like a smear) or names without a final mark; use a dot you add, as the source did.

## How it works
Every letter moves toward the dot by the same factor `f` and its drawn width follows (scaleX from its left edge), so neighbours keep touching all the way in. The source did this with a variable font's width axis; this demo uses scaleX on each glyph, which reads the same at speed.
```js
const x = dotX - (dotX - left[i]) * f              // f: 1 = word, 0 = folded
span.style.transform = `scaleX(${f})`              // transform-origin: left
f = 1 - ei(seg(t, .55, .95))                         // in: ease-in, letters accelerate into the dot
```
The dot is the same element all the way: its size and position are two closed-form springs (`1 - e^(-zwt)(cos wd t + zw/wd sin wd t)`), with the reverse written as a second spring subtracted, so every frame is a pure function of t. The pill's label lives in its own `overflow:hidden` box and rises from 90% of the pill height (mask-line reveal).

## Numbers that matter
| | |
|---|---|
| Squeeze | .55s to .95s, ease-in cubic, letters scaleX with their x |
| Dot to pill | spring f 1.9 Hz, zeta .74 (size); f 1.6, zeta .8 (position), position starts .04s later |
| Pill | 300 x 92 at 1920 wide, fully round, ink #0c0c0d |
| Label | rises .35s eo5 at 1.75s, 33% of pill height |
| Unsqueeze | spring f 1.6, zeta .62 (a visible bounce as the word reopens) |
| Type | heavy sans 800, 210px at 1920; tagline grey #8d8c87 |

## Sound
Source film: a soft whoosh into the squeeze and a click on the cursor press, each placed on its measured peak. Pair with `whoosh-on-cut__lowpassed-noise-sweep` and `cursor-click__noise-burst-plus-sine-pop` from the motion-reel-kit sound set. The demo is silent.

## Adapt it
- `CONFIG.word` and `CONFIG.label` (the button text).
- Colours `bg` and `ink`.
- `CONFIG.t` to sit the squeeze on the beat before a drop.
- `pill.w` to fit a longer label.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #8: Develop: a photo print app launch" by @twoclipping (https://x.com/twoclipping/status/2103835273813496100), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
