---
name: stepper-timeline-done-active-pulse
description: "A progress stepper, vertical and horizontal: done steps filled violet with a check, the active step outlined with a pulsing ring, a blocked step in amber with a lock, and to-do steps greyed. Use it for onboarding or a project checklist."
---

# Stepper timeline

**Code name:** Four-state steps with a pulsing active marker.

## What you see
Two cards, the same five steps. Squares 36px with a 12px radius: done is solid violet with a check, active is a violet outline with a filled dot and a faint ring that grows and fades (scale 1 to 1.25, opacity 0.6 to 0) every 2 seconds, blocked is amber with a lock, to-do is dark grey. A rail joins the markers, violet at 60% once the step before it is done. In the clip the third step is active and the fourth blocked; at 2.8s the third is done and the fourth becomes active; at 5.2s the fourth is done and "Go live" is active.

## When to use it
Onboarding, set-up, contract flows: any ordered list where one step can be stuck. The blocked state is the useful one; do not use the pulse on more than one marker.

## How it works
Marker classes by state: `done: border-rv-purple bg-rv-purple text-white`, `active: border-rv-purple bg-rv-purple/15 text-rv-purplel`, `blocked: border-amber-500/40 bg-amber-500/10 text-amber-400`, `todo: border-rv-border bg-rv-card2 text-rv-muted`. The active pulse is a second absolutely positioned bordered box animated with framer:

```tsx
animate={{ opacity: [0.6, 0, 0.6], scale: [1, 1.25, 1] }}
transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
```
Keyframe arrays split the duration evenly, so each half takes 1s with an easeInOut curve; the demo applies `EASEINOUT` to a triangle wave of `t % 2`. In vertical mode the rail is `w-px flex-1 min-h-6`; in horizontal mode it is `h-px mx-2 mt-[18px]`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Marker 36px square, 12px radius, 1px border.
- Pulse: 2s, easeInOut, infinite, scale to 1.25.
- Rail 1px; violet `rgba(139,92,246,0.6)` after a done step, otherwise `#1A1A2E`.
- Text: label 14px semibold, hint 12px muted.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `STEPS`: label, hint, icon.
- `SEQ`: the state of each step over time.
- Orientation: both are in the file; keep the one you need.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
