---
name: floating-phone-hero-with-credential-marquee-float-rotate-translate
description: "A warm cream hero with an oversized sans headline carrying one italic serif accent word, a dark-bezel phone showing a mini dashboard that drifts up and tilts a degree each way, and a white strip of credentials sliding under it. Reach for it for a programme or app landing page that should feel friendly and premium."
---

# Floating phone hero with credential marquee

**Code name:** Float rotate translate.

## What you see
A cream page (`#FAF7F1`) with two soft colour pools, teal top right and gold bottom left. A floating white pill nav. On the left: a small pale-blue caps eyebrow, a 68px 800-weight headline where one word ("career") is set in Georgia italic in blue, a grey lead paragraph, a solid blue pill button and an outlined navy one. On the right a 300x610 phone, near-black bezel with a thin inner ring, a notch pill, and a screen showing a mini dashboard: greeting, a navy "next session" card with a teal join pill, three percentage tiles over a gradient progress bar, and a row of avatar circles. A white strip with hairline borders runs across the bottom, carrying credential phrases with the key words in bold navy.

- 0 to 0.9s: the text block and then the phone rise 28px and fade in (`.reveal`, 0.7s, `cubic-bezier(.2,.7,.2,1)`, the phone 0.16s later).
- Every 7s: the phone floats up 16px while rotating from -1.2 to +1.2 degrees, then back. Each half is ease-in-out.
- Continuous: the strip slides left, linear.

## When to use it
A first screen for a coaching, course, health or app product aimed at people who respond to warmth. The italic accent word is what stops a big sans headline feeling corporate. Skip it when the product screen is not worth showing: the phone only works if its content reads at 300px wide.

## How it works
```css
.phone { width:300px; height:610px; border-radius:48px; background:#0B1216; padding:12px;
  box-shadow: 0 24px 70px rgba(10,58,82,.14), inset 0 0 0 2px #2A3942 }
.phone::before { /* notch */ top:22px; width:110px; height:26px; border-radius:20px }
.phone-screen { border-radius:38px; overflow:hidden }
.phone-float { animation: phoneFloat 7s ease-in-out infinite }
@keyframes phoneFloat { 0%,100% { transform: translateY(0) rotate(-1.2deg) } 50% { transform: translateY(-16px) rotate(1.2deg) } }
.marquee-track { display:inline-block; animation: marquee 30s linear infinite }
@keyframes marquee { from { transform: translateX(0) } to { transform: translateX(-50%) } }
```

Changes in the demo, so it loops cleanly:
- The marquee runs one 14s cycle here, not 30s, so the 14s clip closes. The source track holds one copy of the items, so `-50%` would jump; the demo doubles the list so `-50%` is exactly one copy and the join is invisible. Do the same in production.
- The two blurred 420px circles are radial gradients, to avoid a large blur filter.
- Placeholder copy replaces the real programme and credentials.

## Numbers that matter
| | |
|---|---|
| Palette | blue `#1290CB`, navy `#0A3A52`, teal `#68CCD1`, aqua `#74FFF6`, gold `#C9A24B`, cream `#FAF7F1` |
| Phone | 300x610, radius 48px, bezel 12px, screen radius 38px |
| Float | 7s ease-in-out, -16px, +-1.2 degrees |
| Marquee | 30s linear in the source, items 15px 700-weight with 34px side margins |
| Headline | 68px, weight 800, tracking -0.03em, accent in Georgia italic 400 |

## Sound
Silent.

## Adapt it
- The headline and which word gets the italic accent.
- The phone's screen contents: any app view that reads at that width.
- Brand blue and navy; the marquee text.
- Float distance and tilt for a calmer or livelier phone.

## Files
- `code/demo.html`: runs on its own.
