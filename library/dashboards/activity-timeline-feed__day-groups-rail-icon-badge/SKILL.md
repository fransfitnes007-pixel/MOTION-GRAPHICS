---
name: activity-timeline-feed-day-groups-rail-icon-badge
description: "A recent-activity list: a day label with a hairline, a vertical rail, round icon badges carrying a small tone dot, one-line sentences with bold names and a relative time. In the demo new events slide in at the top."
---

# Activity timeline feed

**Code name:** Day groups on a vertical rail with icon badges.

## What you see
A card with "TODAY" in tracked uppercase and a hairline. Down the left, a thin rail; on it 32px round badges holding an icon (a new member, a payout, a film, a building) with a 10px dot in the tone colour at the bottom right. To the right of each, a sentence in 85% white with the names bold ("Jordan Miles joined as creator") and a time at the far right in tabular grey ("9m ago"). Each new event fades in 12px from the right at the top while the others glide down 48px.

## When to use it
Audit trails, "what happened" panels, live feeds. The app renders the list statically; the arrival motion is for video.

## How it works
Group by `format(d, 'yyyy-MM-dd')`, label Today / Yesterday / `EEE, d MMM`. Each group is a `flex flex-col gap-3` with a label row (`text-[11px] font-semibold uppercase tracking-[0.12em] text-rv-muted` plus `h-px flex-1 bg-rv-border`) and an `ol` with an absolute rail `left-4 top-3 bottom-3 w-px bg-rv-border`. The icon badge is `grid size-8 place-items-center rounded-full border bg-rv-card2` with the tone text colour, and the dot is `absolute -bottom-0.5 -right-0.5 size-2.5 rounded-full border-2 border-rv-bg` in the solid tone. Times use `formatDistanceToNowStrict`.

In the demo each item's slot is the number of later events that have arrived, eased with `EASEOUT` over 0.5s, which keeps the layout a pure function of time.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Badge 32px; dot 10px with 2px page-colour ring.
- Row gap 16px (48px pitch in the demo).
- Text 14px at 85% white; time 12px tabular.
- Slide: 0.5s, 12px from the right.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `EV`: icon, tone, sentence, time, arrival time.
- Add `Yesterday` as a second label and block.
- Tone names: purple, green, amber, blue, red, muted.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
