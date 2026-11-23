---
name: handwritten-annotation-clip-wipe-arrow-draw
description: "A red felt-tip note wipes in left to right next to an object while a curved arrow draws itself toward it. Reach for it to point at a button or a detail, the way someone marks up a screen recording."
---

# Handwritten annotation with arrow

**Code name:** Clip-path wipe and arrow draw.

## What you see
Right after a blue button springs in at the bottom of a post card, a short note in red marker handwriting appears to the right of the card, tilted 8 degrees up to the right. It is revealed from its left edge to its right like a pen writing it, in 0.35s. A hand-drawn curved arrow starts at the note and travels down and left toward the button, drawn stroke first, then the arrowhead, finishing 0.35s later. Both vanish at the next cut. The demo runs the wipe and the draw at half speed.

## When to use it
To point at one specific control or detail inside a screen or card, with a human, marked-up feel against a clean interface. It reads best next to a quiet area of the frame. A second use: a yellow note with a wavy underline on black (see the spotlight skill). It is wrong when the note needs to be legible for more than a second; it is a flash.

## How it works
No stroke animation library. The text reveal is a `clip-path: inset()` whose right inset shrinks from 100% to 0, so the words uncover left to right while the element stays still:

```js
clipPath = `inset(-20% ${(1 - eo(hq)) * 100}% -20% -5%)`      // top/bottom -20% so the marker's ascenders are not cut
```
The arrow is an SVG with two `<path>`s. Each gets `stroke-dasharray: 400` and a `stroke-dashoffset` that runs from 400 to 0 on the same eased value, so both strokes draw together:

```js
p.style.strokeDasharray = 400; p.style.strokeDashoffset = 400 * (1 - eo(aq))
```
The handwriting is whatever marker font the machine has: `'Marker Felt', 'Noteworthy', 'Bradley Hand', cursive`. On a machine without those it falls back to the generic cursive family.

## Numbers that matter
| | |
|---|---|
| Note | 84px (70px tall layout), `#e5262b`, rotate -8 degrees, transform origin left centre |
| Wipe | `eo` over .35s |
| Arrow | 220x120 svg, stroke 7, round caps, dash length 400, `eo` over .35s, starts .1s after the note |
| Placement | note at card centre + (.5 width, .12 height); arrow at (.36 width, .22 height) |

## Sound
Silent on its own. It sits well right under a button click.

## Adapt it
- The note text and colour (use a contrasting colour to the background).
- The two arrow paths: any SVG path works, set `stroke-dasharray` to its length (`getTotalLength()`).
- Position relative to the target.
- Speed: the defaults are .35s for each.

## Files
- `code/demo.html` runs on its own.
