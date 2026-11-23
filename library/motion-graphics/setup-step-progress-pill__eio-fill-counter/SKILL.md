---
name: setup-step-progress-pill-eio-fill-counter
description: "A step counter and progress bar that run in sync with a wizard being clicked through. Use it to compress a long setup flow into three seconds."
---

# Setup step progress pill

**Code name:** Eio fill bar with floor-stepped counter.

## What you see
A browser window with a setup wizard rises in from 140px low, tilted back 16 degrees. A frosted pill, 600 by 96, rises under it reading "Step 1 of 7" with an empty bar. Over the next 1.65s the bar fills along an ease-in-out cubic and the number steps 1, 2 ... 7, while the screens in the window cut five times (0s, 0.26s, 0.56s, 0.98s, 1.49s). The window then zooms to 145% on the final button, a cursor clicks it on the word "code", a green "Your site is live" chip pops at the top right, and everything scales up and blurs out.

## When to use it
Compressing a long form, wizard or onboarding into a few seconds, with a voice saying "in minutes". The counter and bar tell the viewer how long the real flow is while the cuts show that it is quick.

## How it works
One progress value drives both the number and the width of the bar.

```js
const prog = eio(seg(t, .15, CODE))
counter.textContent = Math.max(1, Math.min(7, 1 + Math.floor(prog * 6.99)))   // never reaches 8
bar.style.width = (prog * 100) + '%'
```

The window cuts are a list of times, independent of the bar (so they can be tied to the voice). The zoom into the final button (`cam` with a changing focus and zoom) starts 0.26s before the click, so the target is large when the cursor arrives.

## Numbers that matter
- Pill: 600 by 96, radius 48, text 30px heavy, bar 14px high, fill `linear-gradient(90deg,#6d6ef0,#4f46e5)`.
- Counter: `1 + floor(prog * 6.99)`, bar `eio` over 1.65s.
- Cuts: 0, .26, .56, .98, 1.49s.
- Final zoom: 1 to 1.45 with `eio` over 0.36s; click at 1.8s; chip `spring(k=8, f=12)`.

## Sound

## Adapt it
- The step count (7) and the page list; keep cuts and the counter's range equal.
- The cut times, to the voice.
- The final zoom target (the button's point in the capture).
- The chip text and colour.

## Files
- `code/demo.html` runs on its own and loops. The wizard pages are CSS placeholders.
