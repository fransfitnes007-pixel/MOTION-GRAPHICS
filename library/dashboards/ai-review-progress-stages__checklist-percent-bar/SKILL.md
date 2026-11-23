---
name: ai-review-progress-stages-checklist-percent-bar
description: "A violet-tinted 'Reviewing your draft' panel: a spinner, a percentage and a thin progress bar, with a two-column checklist of twelve stages that tick from clock to spinner to check. Use it for any multi-step background job."
---

# AI review progress

**Code name:** Stage checklist with percent bar.

## What you see
A rounded panel with a 5% violet fill and a 20% violet border. At the top a spinning loader icon and "Reviewing your draft" at the left, "66%" in tabular grey at the right. A 6px bar fills in violet. Under it twelve stages in two columns, each starting as a faded clock, becoming a white label with a spinning loader when active and a green check with green text when finished (Uploading your draft, Opening the file ... Writing your fixes). A line of reassurance sits below. At 8.3s the panel fades and a green "Yes, good to post" banner takes its place.

## When to use it
Uploads, renders, AI jobs, imports: anything where the system can report a named stage. The compact list is the part to reuse; the full app view adds an animated brain scan and message bubbles.

## How it works
`REVIEW_STAGES` is an ordered list of `{key, label}`. The worker writes `review_jobs.stage` and `progress` over realtime; the panel finds `current = stageIndex(job.stage)` and shows `pct = max(15, job.progress)` (or 15% of the upload percentage while uploading).

```tsx
<div className="h-1.5 rounded-full bg-white/5 overflow-hidden mt-2"><div className="h-full rounded-full bg-rv-purple transition-all duration-500" style={{ width: `${pct}%` }} /></div>
```
List items: `done ? text-emerald-400 : active ? text-white : text-rv-muted` with `Check`, `Loader2 animate-spin text-rv-purplel` or `Clock opacity-50` icons, 12px text. The demo steps one stage every 0.62s and turns progress into a function of time.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Panel: `rgba(139,92,246,0.05)` fill, `rgba(139,92,246,0.2)` border, 12px radius, 16px padding.
- Bar 6px; width transition 0.5s.
- Minimum shown progress 15%.
- Stage rows 20px high, 2 columns, 16px column gap.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `STAGES` labels.
- `STEP` seconds per stage.
- The end state (verdict) or loop back.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
