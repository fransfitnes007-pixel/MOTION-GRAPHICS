---
name: spotlight-vignette-joke-radial-gradient-mask
description: "A black frame with a single profile card lit in a soft oval spotlight that sways slightly, a yellow handwritten word that wipes on with a wavy underline that draws itself, and a white word that pops beside it. Reach for it for a deadpan punchline before the end card."
---

# Spotlight vignette joke beat

**Code name:** Radial-gradient vignette with a hand-drawn note.

## What you see
The scene cuts from white to pure black, and the drums drop out. A wide white profile card (1100px, radius 30px) springs in at the centre: a round photo, a handle, a grey line "Update schedule: Every day ( forever )" and a "Following" button. Dark falls toward the edges of the frame: an oval spotlight, 34% by 30% of the frame, is clear in the middle and black at 93% around it, so the card's outer edges are dimmed. The oval's centre sways left and right by 1.5% of the frame width at about 0.5 Hz. At 21.82s a yellow handwritten "Forever?" with a soft glow wipes on under the card from left to right, and 0.3s later a wavy yellow underline draws itself under it. At 22.82s a bold white "Forever." pops up to its right. Everything fades to black from 24.95s to 25.35s.

## When to use it
A deadpan joke or a sharp aside as the last content beat, just before the end card. The dark break, the single lit object and the handwritten note give it a different mood from the bright scenes around it. It is wrong when the joke needs more than one short line; there is no room for it.

## How it works
Four layers stacked in this order: black stage, the card, a full-frame vignette `div` that is drawn over the card, and the handwritten and white words on top.

```js
spot.style.background = `radial-gradient(ellipse 34% 30% at ${50 + 1.5 * Math.sin(t * 3)}% 44%,
  rgba(0,0,0,0) 0%, rgba(0,0,0,0) 55%, rgba(0,0,0,.93) 100%)`        // clear to 55% of the radius, then dark
```
The sway is the only motion in the spotlight. The handwritten word is revealed with a right-hand `clip-path: inset()` wipe (as in the annotation skill), and the underline is an SVG path with `stroke-dasharray: 460` and `stroke-dashoffset: 460 * (1 - eo(l))`. The white word reuses the LED skill's pop-in (`wordIn`). The whole scene fades by one `fade` value multiplied into every opacity.

On the tall layout the oval is taller (48% by 22%) because the card is narrower.

## Numbers that matter
| | |
|---|---|
| Card | 1100px wide (900 on tall), radius 30px, entrance spring k7 f11 over .5s |
| Vignette | `ellipse 34% 30%` (`48% 22%` tall), clear to 55%, `rgba(0,0,0,.93)` edge, centre at 44% height |
| Sway | `1.5 * sin(3t)` percent, horizontal |
| Yellow note | 150px (120 tall), `#ffe600`, rotate -7 degrees, glow `0 0 24px rgba(255,230,0,.45)`, wipe .5s |
| Underline | 420 by 60 svg, 8px stroke, .4s draw, starts .3s after the note |
| White word | 110px weight 800, pops at 22.82s |
| Fade out | .4s, ending .05s before the end card cut |

## Sound
The drum groove drops out; only a soft plucked note per bar remains under the voice. A low pop (500Hz) lands on "Forever?" and a lower one (420Hz) on "Forever.". No whoosh: the cut is hard.

## Adapt it
- Card content: any single object (a quote, a review, a receipt).
- The two words and the pause between them (a full second works).
- Vignette size and sway amount.
- Note colour: yellow reads on black; use white on a dark red.

## Files
- `code/demo.html` runs on its own. The avatar is a gradient placeholder.
