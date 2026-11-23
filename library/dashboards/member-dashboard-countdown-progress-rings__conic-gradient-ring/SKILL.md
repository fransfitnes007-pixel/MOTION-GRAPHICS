---
name: member-dashboard-countdown-progress-rings-conic-gradient-ring
description: "A soft cream dashboard for a cohort programme. A navy gradient strip carries a live countdown to the next session, module tiles show conic-gradient progress rings, and white pill-cornered panels reveal in a staggered rise. Reach for it for a friendly member area or course portal."
---

# Member dashboard with countdown and progress rings

**Code name:** Conic gradient ring.

## What you see
Warm cream page with a floating white nav pill. A greeting with one blue word. A navy to blue gradient card holds an aqua eyebrow, the session title, four frosted countdown boxes (days, hours, minutes, seconds) and a teal pill button. Below, a two-thirds and one-third grid. Left: a "90-day map" panel of six module tiles, each with a small ring, and a checklist with a struck-through completed item. Right: a pod of five avatar circles and a wins wall of quote cards with a teal left edge. Panels have 28px corners and a soft blue shadow.

- 0 to 1.0s: panels reveal one after another. Each rises 28px and fades in over 0.7s with `cubic-bezier(.2,.7,.2,1)`. The delays are 0, .08, .16, .24 and .32s, the same as the site's `.d1` to `.d4` classes.
- Every second: the countdown seconds tick down, as the site's `setInterval(tick, 1000)` does.
- 0.6 to 1.8s: the rings fill to their value. The site sets them statically, so this sweep is an addition for the demo.

## When to use it
A member portal, student area or onboarding dashboard that should feel warm and reassuring rather than technical. The countdown strip works as the one loud element of the screen. Do not use it for dense data, since the tiles are big and low density.

## How it works
The ring is one element and one custom property.

```css
.ring { --p: 0; width: 46px; height: 46px; border-radius: 50%;
  background: conic-gradient(var(--bw-teal) calc(var(--p) * 1%), var(--bg-tint) 0); }
.ring::after { content: attr(data-label); background: #fff; width: 34px; height: 34px; border-radius: 50%; }
.ring.full { background: conic-gradient(var(--bw-blue) 100%, var(--bw-blue) 0); }
```

The white `::after` disc cuts the centre out, leaving a ring. In the demo the `--p` value is written each frame so the sweep is a pure function of time.

Countdown: `diff = target - Date.now()`, then days from `diff / 86400000`, and hours, minutes and seconds with modulo and a two-digit pad. The demo counts down from a fixed remaining time using `Math.floor(t)`, so it repeats.

Locked modules use `opacity: .55` and a small padlock.

## Numbers that matter
| | |
|---|---|
| Palette | blue `#1290CB`, navy `#0A3A52`, teal `#68CCD1`, aqua `#74FFF6`, gold `#C9A24B`, cream `#FAF7F1` |
| Radius | panels 28px, tiles 16px, pills 999px |
| Shadow | `0 10px 40px rgba(10,58,82,.08)` |
| Reveal | 0.7s, `cubic-bezier(.2,.7,.2,1)`, 28px rise, stagger 0.08s |
| Ring | 46px outer, 34px inner disc |

## Sound
Silent.

## Adapt it
- The two brand colours (blue and teal) and the navy strip.
- Module list and percentages.
- The countdown target.
- Drop the `.reveal` rise if the page should simply be there.

## Files
- `code/demo.html`: runs on its own, with placeholder names and copy.
