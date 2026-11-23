---
name: admin-overview-dashboard-kpi-tiles-needs-you-activity
description: "A home screen for a team lead: greeting and quick actions, eight KPI tiles that count up, a Needs-you inbox with a filter lamp and approve buttons, and a recent-activity timeline. Use it for the first screen after login."
---

# Admin overview dashboard

**Code name:** Count-up KPI tiles, needs-you inbox, activity rail.

## What you see
The eyebrow, "Good morning" heading and a row of quick-action buttons (one filled violet "New campaign", five glass outlines) are static. Eight tiles in two rows count up from zero in 0.6s, each with a tinted icon square, a small trend pill (+12%) and a sub line. Underneath, the left column is "NEEDS YOU" with a pill control (All / Approvals / Content / Billing / Sign-ups / Campaigns); inbox rows fade in with an avatar, a coloured kind chip and, for approvals, an Approve button and an X. At 3.4s the lamp springs to Approvals and the list filters to approval rows, at 5.4s to Billing, at 7.4s back to All. The right column is Recent activity: round icon badges with a tone dot on a thin vertical rail, one-line sentences and relative times.

## When to use it
The "login and see everything" shot. It reads as an operations product, not a marketing page. Good for the opening of a dashboard walkthrough; too busy to hold under a long voice-over, so cut to a single tile or the inbox for detail.

## How it works
Tiles are `StatTile` (kit): `rounded-2xl border bg-rv-card p-5`, label 12px medium uppercase `tracking-[0.08em]`, icon square `size-8 rounded-lg` at 15% tint, value `text-3xl font-bold` and an optional `TrendPill`. A numeric `value` renders `MotionNumber`, which tweens with framer's `animate(from, to, {duration: 0.6, ease: [0.16,1,0.3,1]})` whenever the number changes. On the live page the figure goes from 0 to the real value as the queries return, which is the count-up you see; the demo starts every tile at 0.

The filter is `SegmentedControl`: a radiogroup whose active button holds a framer `layoutId` pill, so the highlight moves between buttons on a spring (`stiffness 300, damping 30`). Above the pill sits a 32px by 4px violet bar with three soft blurred glows. `springK(t)` in the demo is that spring as a 0 to 1 curve.

```js
const k = springK(t - tPick, 300, 30, 1)      // underdamped: ζ = 30 / (2·√300) ≈ 0.87
left = a.left + (b.left - a.left) * k;  width = a.width + (b.width - a.width) * k
```

`InboxRow` is `rounded-xl border bg-rv-card p-2.5`, with an amber border when `urgent`. The activity list is the kit `ActivityFeed`: day label plus hairline, a rail at `left-4`, `size-8` round icon, a `size-2.5` tone dot with a 2px page-colour border, tabular time at the right.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- KPI tile: 30px value, 12px label, 8px icon radius, 12px between value and sub.
- Count-up: 0.6s, ease `[0.16,1,0.3,1]`.
- Pill lamp: spring stiffness 300, damping 30, mass 1.
- Inbox row 10px padding, 36px avatar, 8px between rows. Kind chips 10px semibold on 10% tints (violet, blue, green, amber, red).
- Activity: 32px icons, 16px between rows.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- The `T` array: label, value, icon, tone, format, sub, trend.
- Inbox rows in `IN`; the filter times in `SEQ`.
- Greeting and date in the header line.
- Tone names map to rgb in the shared `tone()` helper.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the people and numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
