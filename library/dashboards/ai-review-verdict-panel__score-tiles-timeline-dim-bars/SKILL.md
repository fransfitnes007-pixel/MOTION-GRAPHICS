---
name: ai-review-verdict-panel-score-tiles-timeline-dim-bars
description: "A scored AI review of a video: a green verdict banner, composite score tiles with bars, a fix list with timestamps, a coloured structure timeline with markers, and a two-column score sheet with per-dimension bars coloured by score."
---

# AI review verdict panel

**Code name:** Verdict banner, score tiles, timeline and dimension bars.

## What you see
A green banner reads "Yes, good to post" with a one-line reason. Four tiles below: Reach 82/100 and Conversion 74/100 each with a coloured bar that fills, a Reach probability 68% tile and an Account baseline tile. An amber block lists two timestamped fixes ("0:05" and "0:15" chips). A timeline strip shows the video as coloured sections (hook violet, problem blue, product green, value and proof sky, CTA amber), a green outline where the product is on screen, a red block for dead air, and two dots for fixes that pop in. The page scrolls to the score sheet: nine reach and six conversion dimensions, each with a score in its tone colour, a bar and an evidence line.

## When to use it
Any "AI grades your work" screen: a verdict first, evidence after. The tone scale (green, blue, amber, red) is the part to copy.

## How it works
Tone by score: `scoreTone(v, max)` returns green `52,211,153` at 80% or more, blue `96,165,250` at 65%, amber `251,191,36` at 45%, red `248,113,113` below. The banner uses the verdict tone as `bg-emerald-500/15 border-emerald-500/30 text-emerald-400` (amber, red and grey variants exist). `Composite` is `rounded-xl border bg-rv-bg/60 px-3 py-2.5 text-center` with a `h-1.5 rounded-full bg-white/5` track and a fill of `width: value%` that carries `transition-all duration-500` in the app. The timeline positions every element with `left: t / duration * 100%`.

In the app the widths render at their final value with the transition class; the demo animates them from zero so the bars read on video:

```js
bar.style.width = v * 10 * EASE(seg(t, tStart, tStart + .5)) + '%'      // .5s CSS 'ease'
```
Dimension rows show the code, label and weight (`x20`), the score, the bar and the evidence in 11px muted.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Tone scale: `52,211,153` / `96,165,250` / `251,191,36` / `248,113,113` at 80 / 65 / 45 percent.
- Bars 6px high, 0.5s `ease` fill.
- Timeline strip 12px high; fix dots 8px; legend 10px.
- Section colours: hook `139,92,246`, problem `59,130,246`, product `16,185,129`, value/proof `96,165,250`, CTA `245,158,11`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `REACH`, `CONV` rows: key, label, weight, score, evidence.
- `SEC` timeline sections and the 32s duration.
- Verdict text and tone for a 'reshoot' variant (`248,113,113`).
- Scroll distance at the end (`330`).

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the verdict, scores and evidence text are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
