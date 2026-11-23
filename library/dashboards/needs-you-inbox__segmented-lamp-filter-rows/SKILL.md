---
name: needs-you-inbox-segmented-lamp-filter-rows
description: "A filter pill bar where a violet highlight with a glowing top bar springs from option to option, over a list of inbox rows with kind chips and approve buttons. Use it for a triage list with filters."
---

# Needs-you inbox

**Code name:** Spring lamp segmented filter over action rows.

## What you see
A "NEEDS YOU" title with a pill-shaped control (All 9, Approvals 3, Content 2, Billing 2, Sign-ups 1, Campaigns 1), each option with a small count. A violet 15% pill sits behind the active option with a 32px glowing bar on top. At 2.1s the lamp springs to Approvals, with a small overshoot, and the list shows only approval rows; at 3.9s Billing; 5.7s Content; 7.5s All again. Rows show an avatar, a title, a coloured kind chip, a sub line and, for approvals, a green Approve button with an X. Urgent rows have an amber border.

## When to use it
Triage and filtered lists. The lamp makes the change of filter feel physical. For a pure tab bar without a list, the control alone is the skill.

## How it works
Each option renders its own `motion.span layoutId="${uid}-lamp"` only when active; framer measures the old and new boxes and animates between them on `{ type: 'spring', stiffness: 300, damping: 30 }`. Above the pill sits:

```tsx
<span className="absolute -top-1 left-1/2 h-1 w-8 -translate-x-1/2 rounded-t-full bg-rv-purple">
  <span className="absolute -left-2 -top-2 h-6 w-12 rounded-full bg-rv-purple/25 blur-md" /> ...
```
A spring with mass 1, stiffness 300 and damping 30 has a damping ratio of about 0.87, so it overshoots slightly; `springK(t)` in the demo is the closed-form curve, applied to the left and width of the pill together. Container `rounded-full border bg-rv-card p-1 gap-1`; options `h-9 px-4 text-sm` (`h-7 px-3 text-xs` in `sm`). The row: `rounded-xl border bg-rv-card p-2.5`; kind chips `text-[10px] px-1.5 py-0.5 rounded-md` on 10% tints.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Spring: stiffness 300, damping 30, mass 1.
- Control height 36px (md), count chip 10px.
- Row: 36px avatar, 10px padding, 8px gap; urgent border `rgba(245,158,11,0.3)`.
- Kind chips: Approval violet, Content blue, Billing green, Sign-up amber, Deadline red.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `OPT` and `ALL`: options, counts, rows.
- `SEQ`: which option is picked when.
- Use size `sm` (28px) for in-card controls.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
