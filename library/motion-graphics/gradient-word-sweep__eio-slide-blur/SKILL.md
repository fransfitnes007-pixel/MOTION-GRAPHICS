---
name: gradient-word-sweep-eio-slide-blur
description: "A giant two-colour gradient word sweeps from the right edge across the whole frame to the left, blurred at its fastest point. Reach for it as a transition word between two scenes."
---

# Gradient word sweep

**Code name:** Eased slide with peak blur.

## What you see
The frame has just cut from the dark scene to plain white. A huge two-word title in a gradient from orange through pink to violet is already sitting at the right edge, cut off by the frame. In 0.4s it slides to the left across the full width and out of the frame, slow at the start, quickest in the middle and slow again at the end, while a blur builds to 10px at the midpoint and clears. It is a word used as a wipe. The next scene starts behind it. The demo runs it at half speed.

## When to use it
A very short bridge word between two beats, or as a transition when you want a word to carry the cut instead of a plain whoosh. It works best when the next scene begins at the moment the word clears the frame. Too long and it becomes a title card; hold it under half a second.

## How it works
One absolutely positioned element, centred with `translate(-50%,-50%)`, moved on x only:

```js
const q = seg(t, t0, t0 + .4)
left = CX + lerp(900, -1500, eio(q))        // starts 900px right of centre, ends 1500px left
filter = `blur(${Math.sin(Math.PI * q) * 10}px)`
```
The start and end distances are bigger than the word width (about 1100px at 330px type) so it begins partly in frame and ends fully out. The fill is `linear-gradient(92deg, #ff7a3d, #ff2e97 55%, #7c3aed)` clipped to the text with `background-clip: text`. Type is weight 800 with -.055em tracking and line height .9.

## Numbers that matter
| | |
|---|---|
| Duration | .4s typical (.8s in the demo) |
| Travel | from `CX + 900` to `CX - 1500` |
| Ease | `eio` cubic in-out |
| Blur | `sin(pi * q) * 10` px |
| Type | 330px wide layout, 250px tall layout, weight 800 |
| Gradient | `#ff7a3d` to `#ff2e97` at 55% to `#7c3aed`, 92 degrees |

## Sound
A falling noise whoosh (6kHz down to 800Hz, 0.35s) that starts about 0.04s after the cut. It is a downward whoosh; pair it with rising ones elsewhere.

## Adapt it
- The word, its size and gradient stops.
- The start and end x so the word fully clears at your size.
- Peak blur and duration.
- Direction: swap the two numbers to sweep left to right.

## Files
- `code/demo.html` runs on its own.
