---
name: dark-feature-bento-grid-five-cards-mini-visuals
description: "A dark features section laid out as a bento: three equal cards on top and two wide cards underneath, each with a small line-art visual (scribbled ellipse, fingerprint scan, speed wave, mini chart, avatar line) over a title and a short paragraph. Reach for it as the features block of a dark product landing page."
---

# Dark feature bento grid

**Code name:** Five cards, each with a small drawn visual.

## What you see
A near-black page with five cards separated by 10px gaps: three on the first row (274 by 267 at the poster's scale) and two wide ones on the second (415 by 221). Each has a 1px `#232326` border, 17px corners and a `#0b0b0d` fill.

Top left: "100%" in 58px semibold inside a hand-drawn white ellipse with a second grey stroke above it, with "Customizable" under it. Top middle: a fingerprint inside two faint concentric rings with a white horizontal line across it, then "Secure by default" and three lines of grey-white text. Top right: a small download icon with "Download" at the left and "14,34 mbps" at the right, a jagged white wave with a soft fill below it, then "Faster than light" and a paragraph. Bottom left: a shield in two rings, "Faster than light" and a paragraph on the left, and on the right a browser frame with three dots holding a rising jagged white chart with a fill. Bottom right: a people icon in two rings, "Keep your loved ones safe" and a paragraph, and on the right a thin vertical line with three round avatars and name tags (Likeur, M. Irung, B. Ng) on alternating sides.

The 21st.dev page is a still image with no video, so the motion is added in the demo (8s): cards rise in 0.12s apart, the ellipse draws itself and "100%" counts up, the fingerprint scan line sweeps over 3s, the speed wave moves and the mbps figure drifts, the chart draws on, and the avatars bob with their tags fading in. Everything fades at 7.4s so it loops.

## When to use it
The "what you get" section of a dark SaaS or developer-tool landing page, where five short points each get a picture. The mix of two row sizes keeps it from looking like a flat list. Keep copy to one paragraph per card.

## How it works
A CSS grid of five bordered cards. The visuals are small inline SVG, not images: concentric rings plus a fingerprint path, a polyline whose points come from a sum of sines, and a jagged chart from sines at different frequencies.

```js
y = 98 - (sin(x*.09 + t*3)*.5 + sin(x*.23 - t*5)*.35 + sin(x*.51 + t*2.1)*.25) * 16 * envelope(x)
```

The ellipse and chart use `pathLength="1"` with a dash offset so they draw on. The page usage is just `<Features />` imported from a blocks folder, so all copy and shapes come from the poster; the paragraphs are the lorem text shown there.

## Numbers that matter
| | |
|---|---|
| Grid | 3 cards of 274 x 267 over 2 cards of 415 x 221, gap 10px |
| Card | `#0b0b0d`, border `#232326`, 17px radius |
| Titles | 18px/500 (cards 2 to 5), 25px/600 ("Customizable") |
| Body | 14.5px, line 21px, `#dedee0` (centred) or `#cfcfd3` (left) |
| Rings | 1.5px `#202024`, radii 62 and 46 (top), 33 and 22 (bottom) |
| Lines | `#e8e8ea` 2px; ellipse 3px |
| Avatars | 26px, 2px `#0b0b0d` ring; tags 28px high, border `#3a3a3e` |
| Demo loop | 8s, fade-out 7.4s |

## Sound
Silent.

## Adapt it
- `CONFIG.secure`, `speed`, `chart`, `team`: title and paragraph for each card.
- `people`: names, side of the line and avatar colour.
- `stroke`, `speedBase`, `scanSec`: line colour, the mbps figure, scan speed.
- Swap the SVG in any card for your own picture.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Features 8" by meschacirung on 21st.dev (https://21st.dev/@meschacirung/components/features-8), MIT. This demo is an original recreation written from the public preview.
