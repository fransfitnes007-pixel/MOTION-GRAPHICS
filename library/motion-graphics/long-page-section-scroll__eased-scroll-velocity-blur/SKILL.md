---
name: long-page-section-scroll-eased-scroll-velocity-blur
description: "A tall website screenshot inside a browser window jumps from section to section in 0.85s eased scrolls, blurring while it moves and revealing a sticky nav pill. Reach for it to tour a long page without recording a real scroll."
---

# Long page jump-scroll with motion blur

**Code name:** Eased scroll with velocity blur.

## What you see
A browser window floats on a pastel background showing the top of a long page. At each section start the page scrolls to the next section in 0.85s: it eases in, hits peak speed in the middle and eases out, and while it is moving faster than 20px a frame it is blurred, up to 16px at the fastest. A floating nav pill, hidden on the first screen, fades in as soon as the page has moved 4 to 40px. Each section then holds for about 2s.

## When to use it
A tour of a long web page, an app dashboard or a docs site: any time the true scroll would be too slow or too jerky to record. Pair it with text in the margin naming each section (see the section-title sidebar skill). Wrong for a single screen of content.

## How it works
The page is one tall image (here four CSS panels). The scroll position is a function of time: a list of target offsets, one per section, and the position between two targets is an ease-in-out-cubic of time since that section's start. Blur comes from speed, not from time: compare the scroll position now with one frame ago.

```js
const SCROLL = [0, ...sectionTops.map((v) => v - 100)]
function scrollAt(t) { const i = secIndex(t); if (i === 0) return 0
  return lerp(SCROLL[i - 1], SCROLL[i], eio(p(t, SEC_T[i], SEC_T[i] + 0.85))) }
const sy = scrollAt(t), vel = Math.abs(sy - scrollAt(t - 1 / 30))
strip.style.transform = `translateY(${-sy}px)`
strip.style.filter = vel > 20 ? `blur(${Math.min(16, vel / 34)}px)` : 'none'
nav.style.opacity = p(sy, 4, 40)
```

A fuller build also cross-fades a separate hero image out at the first jump and keeps the sticky nav as a second image clipped to the pill; the demo draws the nav as a plain pill. Section offsets come from measuring the real page , so a new screenshot needs its own list. The demo adds a 0.25s fade in and 0.3s fade out so the loop does not jump back to the top.

## Numbers that matter
| | |
|---|---|
| Scroll time | 0.85s, ease-in-out-cubic |
| Offsets | section top minus 100px (demo: 0, 980, 2060, 3140) |
| Blur | per-frame travel over 20px starts it; blur = travel / 34, max 16px |
| Sticky nav | fades in while scroll goes 4px to 40px |
| Hold between jumps | 2.2s |
| Window | 1920 x 1160 design size, 80px chrome and a 1080px view |

## Sound
Silent apart from a music bed; a short soft whoosh at each jump suits it.

## Adapt it
- Replace `fauxPage` with your own tall screenshot and set `SCROLL` to its section offsets.
- `SEC_T`, the jump start times, to land on your voice.
- Scroll length `0.85` and the blur divisor `34`.
- Window size and position (`G`).

## Files
- `code/demo.html` runs on its own (7s loop, three jumps).
