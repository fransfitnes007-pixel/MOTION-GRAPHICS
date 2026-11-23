---
name: mono-loader-grid-fourteen-spinner-morph-metaballs-newton-scramble
description: "Fourteen 40px loaders in black on white with grey labels: spinner, dots, bars, dot matrix, dither, morph, comet, metaballs, newton, helix, scramble, percent, ASCII and ASCII braille. Use as a menu of loading indicators for buttons, panels and AI waits."
---

# Black and white loader grid, fourteen styles

**Code name:** Spinner, morph, metaballs, newton, scramble.

## What you see
A white page with a grid of fourteen loaders, each 40px in the original (shown 1.5x), a grey 12.5px label under each, five to a row, 134px apart, with the last row holding four. Spinner: a light grey ring with a black quarter arc with round caps, one turn a second. Dots: three dots in a wave that rise and fall in turn, going darker at the top. Bars: four rounded bars of changing height like an equalizer. Dot matrix: a 3 x 3 grid where a dark pulse travels diagonally, dots growing as they darken. Dither: a 4 x 4 grid of squares changing grey at hashed offsets. Morph: one solid black shape turning between square, circle and triangle. Comet: a dot orbiting with a blurred trail. Metaballs: two black circles that pull together and apart with a gooey bridge. Newton: five dots where the end ones swing out in turn. Helix: two columns of dots twisting, with near dots larger and darker. Scramble: 'LOADING' where random characters lock in from the left. Percent: a number with a thin bar counting 0 to 99. ASCII: a braille-style spinner of 2 x 3 dots in ten frames. ASCII braille: a 2 x 3 dot cell with three dots lit chasing round the edge.

## When to use it
Pick one as the waiting state for a button, a card, a chat reply or a full panel. The grid is a catalogue: use the single loader you want and drop the rest. The text ones (scramble, percent, ASCII) suit developer tools and AI interfaces; the rounded ones suit consumer apps.

## How it works
Each loader is a function of time that returns SVG markup for a 56-unit box, redrawn every frame. A phase helper `ph(t, period)` gives 0 to 1 and each loader maps that to its geometry. Metaballs uses an SVG filter (a Gaussian blur followed by a high-contrast alpha matrix) so two circles fuse. Morph keeps all three shapes as 8 points and blends between them, then rotates. Dither and scramble use a deterministic hash of the cell index and time step instead of random numbers. All periods divide the 6s loop evenly, so the loop closes.

```js
const ph = (t, p, o = 0) => (((t / p + o) % 1) + 1) % 1
// metaballs: two circles, gap d, merged by the goo filter
<filter id="goo"><feGaussianBlur stdDeviation="2.2"/><feColorMatrix values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9"/></filter>
```

The real component has 17 variants, reduced-motion support and a `size` prop. The usage example lists 14 of them and the demo shows those 14, matched by eye from the clip, so shapes and timings are close and not identical. The 'ASCII' frame order is the standard 10-frame braille spinner.

## Numbers that matter
| | |
|---|---|
| Size | 40px box, `size` scales everything |
| Ink | `#111`, track `#d6d6d6`, mid `#8c8c8c` |
| Periods | spinner 1s, dots and bars 1.2s, matrix, comet, newton 1 to 1.5s, morph and percent 3s |
| Grid | 5 columns, 134 x 116px, labels 12.5px `#737373` |
| Spinner | ring 3px, arc 25 percent of the circle |
| Metaballs | blur 2.2, alpha matrix 20 / -9, gap 3.5 to 12.5 |
| Loop | 6s |

## Sound
Silent.

## Adapt it
- `size` and `speed`: scale and pace. `speed` should stay 1, 2 or 3 so loops stay whole.
- `ink`, `soft`, `mid`: the colours; use one brand colour for all three tones.
- `LOADERS`: delete the ones you do not need, or change a loader's period.
- Scramble's `word` and Percent's range for your own copy.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Loader" by starc007 on 21st.dev (https://21st.dev/@starc007/components/loader), MIT. This demo is an original recreation written from the public preview.
