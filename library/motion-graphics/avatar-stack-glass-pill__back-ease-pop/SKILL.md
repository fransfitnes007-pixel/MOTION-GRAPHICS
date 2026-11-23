---
name: avatar-stack-glass-pill-back-ease-pop
description: "A frosted-glass pill rises in carrying a row of six overlapping round avatars that pop one after another with a small overshoot, next to a two-line label."
---

# Avatar stack glass pill

**Code name:** Back-ease pop.

## What you see
A 700x118 white-glass pill (72% white with a 24px backdrop blur and a soft shadow) lifts 60px into place and scales from 90% to 100% with a springy ease at 6.54s. The six 74px avatars, each with a 4px white ring and overlapping the previous by 16px, scale from 0 to 1 with an overshoot to about 1.1 and settle, 0.05s apart. The label reads "Creator team" with a small grey line under it.

## When to use it
To show "people" behind a service: a team, a roster, backers, a waitlist. Use real faces if you have consent; the stack at this size reads as human at a glance. It supports a headline, it should not carry one.

## How it works
The container spring and each avatar's `back()` ease are separate so the pill arrives first and faces follow.

```js
const tp = spring(seg(t, at - .02, at + .55), 7, 12)
S(team, { opacity: clamp(tp * 1.4) * (1 - out), transform: `translateY(${(1 - tp) * 60}px) scale(${.9 + .1 * tp})` })
faces.forEach((f, i) => { const p = back(seg(t, at + i * .05, at + .35 + i * .05)); f.style.transform = `scale(${clamp(p, 0, 1.3)})` })
// back(x, s=1.9) = 1 + (s+1)(x-1)^3 + s(x-1)^2
```
`flex` with a negative `margin-left` on all but the first face makes the overlap; the white ring (`box-shadow: 0 0 0 4px #fff`) separates them.

## Numbers that matter
| | |
|---|---|
| Pill | 700x118, radius 30px, padding 0 26px, `rgba(255,255,255,.72)`, blur(24px) |
| Faces | 74px circles, -16px overlap, 4px white ring |
| Pill spring | k=7, f=12, 0.57s; rise 60px, scale .9 |
| Face pop | `back(s=1.9)`, 0.35s each, 0.05s apart, scale clamped at 1.3 |
| Label | 30px bold + 20px regular grey |

## Sound
Silent by default; a very short pop per face would suit it.

## Adapt it
- The faces (`background` URL per avatar) and the label.
- Number of faces and the overlap.
- `CREATOR`: the start time.
- The pill's `bottom-left` position (default (120,900)).

## Files
- `code/demo.html` (avatars are gradient placeholders).
