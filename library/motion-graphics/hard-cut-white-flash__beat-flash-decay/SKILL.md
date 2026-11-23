---
name: hard-cut-white-flash-beat-flash-decay
description: "A full-frame white layer jumps to 55 percent opacity on the first frame of each cut and drains linearly to zero in 0.12 seconds, so a straight cut between flat colour fields reads as a hit. On the beat of a video cut to music, especially on cuts without a transition."
---

# White flash on a hard cut

**Code name:** Beat flash decay.

## What you see
Straight cuts between flat colour fields. On the first frame of each cut a white layer covers the frame at 55 percent opacity and drains to nothing linearly in 0.12s (about 7 frames at 60fps), so the cut has a kick.

## When to use it
On the beat of a video cut to music, especially on cuts without a transition. It stops a hard cut feeling like a mistake. Do not use it on every cut; three or four per video.

## How it works
A full-frame white div above all scenes. Its opacity is computed from the distance to each cut time and the largest wins.

```js
for (const h of hits) { const k = seg(t, h, h + .12); if (k > 0 && k < 1) flash.style.opacity = Math.max(+flash.style.opacity, (1 - k) * .55) }
// alternative: k = seg(t, a - .08, a + .18); opacity max(prev, (1 - Math.abs(k * 2 - 1)) * .22)   (a triangle around the cut)
```

## Numbers that matter
| | |
|---|---|
| Peak | .55 (alternative .22) |
| Decay | 0.12s linear (alternative: symmetric, 0.26s) |
| Colour | #fff, z-index above scenes |

## Sound
A suitable soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. Each flash sits on a hit.

## Adapt it
- Peak and length.
- Colour (white, or a brand tint).
- The cut list.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.
