---
name: stat-card-icon-tile-fade-up-stagger
description: "Dark stat cards with a tinted icon tile, a bold value, a muted label and an optional up/down percent, each with a soft coloured shadow. They rise 16px and fade in one after another."
---

# Stat cards

**Code name:** Fade-up stagger with tinted icon tile.

## What you see
Cards appear in reading order, each moving up 16px and fading in over 0.5s, 0.05s after the one before. Each has a 38px rounded icon tile at the top left tinted at 15% of its colour (violet, blue, amber, green), an optional trend chip at the top right ("12%" green with an up arrow, "3%" red with a down arrow), the value in 24px bold below, then the label in 12px grey. A coloured shadow glows under each card.

## When to use it
Any row of headline numbers. It is the app's plain stat card; use the shine-border tile when one number should draw the eye.

## How it works
```tsx
<motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, delay, ease: [0.16, 1, 0.3, 1] }}
  className={`bg-rv-card border border-rv-border rounded-2xl p-5 shadow-lg ${c.glow}`}>
```
The ease `[0.16, 1, 0.3, 1]` is a fast start and a long soft stop; `FRAMER` in the demo is that curve. Pages pass `delay` as `index * 0.05`. Colours come from a map: purple `bg-rv-purple/15 text-rv-purplel`, blue `bg-rv-blue/15 text-rv-bluel`, green `bg-emerald-500/15 text-emerald-400`, amber `bg-amber-500/15 text-amber-400`, with `shadow-lg` tinted at 20% of the same colour.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Card padding 20px, radius 16px, shadow `0 10px 15px -3px` at 20% tint.
- Icon tile: 10px padding around an 18px icon, 12px radius.
- Value 24px bold with `tracking-tight`; label 12px; value to label gap 4px, tile to value 16px.
- Motion 0.5s, delay 0.05s per card, ease `[0.16,1,0.3,1]`, rise 16px.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `S1` rows: label, value, icon, tone, change.
- The `.05` stagger and the `.15` start time.
- Tone map in `tone()`.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
