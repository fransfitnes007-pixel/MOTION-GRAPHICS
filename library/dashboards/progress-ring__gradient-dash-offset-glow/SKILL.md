---
name: progress-ring-gradient-dash-offset-glow
description: "Rings with a faint track, a gradient stroke that fills to a percentage with round caps and a soft glow, and the number in the middle. Use them for completion, quota or goal progress."
---

# Progress rings

**Code name:** Gradient stroke with animated dash offset.

## What you see
Four 150px rings start empty. Each stroke sweeps clockwise from 12 o'clock to its value (72%, 45%, 88%, 30%) over 1.2s, the rings starting 0.12s apart. The stroke is a diagonal gradient from the tone colour to the same colour at 55%, with round ends and a 6px glow. The percentage (30px bold) counts in the centre with a small uppercase caption. At 3.6s three of the rings move on to 90%, 60%, 88% and 55% (the same 1.2s easing).

## When to use it
A single "how far along" figure, or a handful side by side. For a long list of steps use the stepper; for money amounts use the stacked bar.

## How it works
An SVG rotated -90 degrees so progress starts at the top: a track circle `stroke-white/[0.06]` and a `motion.circle` with `strokeDasharray = circumference` and an animated `strokeDashoffset = circumference * (1 - value)`:

```tsx
animate={{ strokeDashoffset: offset }} transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
style={{ filter: `drop-shadow(0 0 6px rgba(${t.rgb},0.45))` }}
```
The gradient is `x1 0% y1 0% x2 100% y2 100%` from `rgb(tone)` to `rgba(tone, 0.55)`. The label sits in an absolutely positioned centre flex: `text-lg font-bold tabular-nums` (the demo scales it up) and a 10px uppercase sub label. Default size 96 and stroke 10; the demo uses 150 and 14 so it reads on video.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- App default: size 96, stroke 10; demo: 150 / 14.
- Track `rgba(255,255,255,0.06)`; glow 6px at 45%.
- Fill 1.2s ease `[0.16,1,0.3,1]`.
- Gradient end alpha 0.55.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `RINGS`: tone, values (`a` then `b`), caption, title.
- `SZ` and `ST` for ring size and thickness.
- Change `-90deg` rotation for a different start angle.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
