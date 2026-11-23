---
name: rotating-word-swap-flip-up-staggered
description: "One word in a sentence keeps changing: the old word flips up out of view letter by letter while the new one flips in from below, and the highlight pill resizes between them. Reach for it for taglines that list benefits, audiences or use cases."
---

# Rotating word swap

**Code name:** Flip up, staggered. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
"Built to feel" in white, followed by a glowing indigo pill holding the word "simple" at 150px weight 800. Each word holds for about 0.8s. Then the letters of the old word rotate up and away one after another (0.045s apart, rotating to -90 degrees on the X axis while sliding up 0.45em, each over 0.42s), and 0.12s later the letters of the next word rotate in from +90 degrees below. While this happens the pill width and the sentence position ease to the new word's width over 0.4s, so the phrase stays centred. Four words cycle (simple, fast, bold, calm) and the sentence returns to the first word exactly at 4.8s. Four dots under the phrase mark the current word. On tall layouts the lead sits above and the pill and word below, centred.

## When to use it
Taglines that say one thing about many things: "Built for teams / founders / agencies", feature or benefit lists, a hook where the last word changes. One word at a time keeps the message short. It is wrong for more than about five words (the cycle gets long) and for long words (the pill grows past the frame).

## How it works
Every letter is a span, so letters can have their own timing. A parent with `perspective: 900px` makes the X-axis rotation look like a flipping drum rather than a squash. Word widths are measured once with a hidden clone so the pill and the centring can interpolate between old and new width.

```js
const k = Math.floor(t / 1.2), ph = t - k * 1.2           // which word, time inside its slot
out:  p = eio(pr(ph, .78 + j*.045, .42));  rotateX(-90*p)  translateY(-.45em*p)  opacity 1-p*p
in:   p = eo (pr(ph, .90 + j*.045, .50));  rotateX( 90*(1-p)) translateY(.45em*(1-p)) opacity p
boxW = lerp(wCur, wNxt, eio(seg(ph, .88, 1.28))) + 2*pad  // pill and layout follow
```
Because the swap lives inside each 1.2s slot and the last slot ends on word 0, the loop has no seam.

## Numbers that matter
| | |
|---|---|
| Slot | 1.2s per word, swap starts at 0.78s |
| Letter stagger | 0.045s, out 0.42s `eio`, in 0.5s `eo`, new word 0.12s late |
| Flip | rotateX 90 degrees, 0.45em slide, perspective 900px |
| Pill | pad 0.22em, radius 0.3em, `#828cff` to `#5b5ce6` at low alpha, ring 45% `#a5b4fc` |
| Type | 150px (190px tall), lead weight 700, words weight 800, tracking -0.04em |

## Sound
A short soft tick per word change (one tick, not one per letter) and a very light flip noise. Optionally pitch the tick up a semitone each word.

## Adapt it
- `WORDS`, the lead text and `FS`.
- `STG` (stagger) and `T` (hold): slower holds for longer words.
- Flip direction: use `-90` on entry and `+90` on exit to roll downward.
- The pill colours, or remove the pill for plain text; the measuring logic still centres the phrase.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`
