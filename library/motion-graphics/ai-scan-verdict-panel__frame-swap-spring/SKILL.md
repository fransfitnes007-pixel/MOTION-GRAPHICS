---
name: ai-scan-verdict-panel-frame-swap-spring
description: "A post card on the left, a dark scanning panel on the right that plays a short scan, then swaps for a verdict panel with a pop while a purple 'Checked for you' sticker snaps onto its corner. Reach for it to show an AI check or review of a piece of content."
---

# AI scan and verdict panel

**Code name:** Frame sequence swap with spring verdict.

## What you see
A 380px post card pops in on the left (see the post card skill). To its right a dark panel, 860px wide, rises 160px into place while fading in. It shows a purple glowing 3D scan with a floating note, and its frames advance at 24 per second, so the highlight moves through it. At 16.01s a purple pill saying "Checked for you" springs onto the panel's top-right corner, turning 3 degrees. At 16.64s the scan is replaced by a verdict panel that grows from 92% with a spring and fades in: a green box "Yes, good to go", and three scores (84, 77, 81%). A small grey bracketed caption sits below (see the bracket tag skill).

## When to use it
Showing that the product checks the content before it goes out: a review, a score, a risk check. The two-step structure (processing, then result) holds attention. It is wrong where the panel has to be read: the text inside is about 13px at 1x and is atmosphere, not copy.

## How it works
Two panels share one rectangle. The first plays frames, the second replaces it:

```js
const fi = Math.min(30, Math.floor((t - t0) * 24))            // frame index, 24 fps, stops on the last frame
frames.forEach((f, i) => f.style.display = i === fi ? 'block' : 'none')
vis(scanPanel, !showVerdict); vis(verdictPanel, showVerdict)
verdict.transform = `scale(${.92 + .08 * spring(seg(t, tv, tv + .5), 8, 12)})`
```
Use 31 screenshots of a scan (700x403) stacked in the panel; the demo draws a stand-in and moves a bar across it using the same frame index. The sticker uses a spring k8 f12: `scale(sq) rotate(3 * sq deg)`. The panel's purple glow is a third box-shadow: `0 0 90px rgba(124,58,237,.22)`.

## Numbers that matter
| | |
|---|---|
| Panel | 860 by 495px (900 on tall), radius 20px, purple glow `0 0 90px rgba(124,58,237,.22)` |
| Entrance | `eo5` over .6s, rises 160px, fades with it |
| Frames | 31 at 24 per second (1.3s), then holds on the last |
| Verdict swap | spring k8 f12 over .5s, scale .92 to 1; scan hides at the same moment |
| Sticker | `#7c3aed`, 34px bold white, spring k8 f12, rotates to 3 degrees, at panel right - 40px |
| Card | 380px wide, entrance spring k7 f11 over .5s |

## Sound
Mid-level pops (1250Hz, 0.11s) when the sticker snaps on and at the verdict swap, after a whoosh on the cut in.

## Adapt it
- Replace the placeholder panels with screenshots or a video of your own scan.
- The sticker text and colour.
- `T_VERDICT`: set it to the line that announces the result in your voice track.
- Panel size and its position next to the card.

## Files
- `code/demo.html` runs on its own. The two panels are drawn in HTML and the card photo is a gradient.
