---
name: deal-pipeline-board-stage-columns-drag-drop-cards
description: "A kanban pipeline: five stage columns with colour dots, counts, column totals and weighted values, rich deal cards, and a card that is picked up, carried across and dropped into the next column. Use it for any CRM or workflow-board moment."
---

# Deal pipeline board

**Code name:** Stage columns with drag-and-drop deal cards.

## What you see
Under a "Pipeline" header and a row of filter chips, five columns 280px wide sit side by side, the last one running off the screen edge. Each column header has a coloured dot, the stage name, a count pill and the column's value; stages with a win probability add a small "weighted $1,550 at 25%" line. Cards show a two-letter brand tile, name, deal title, value, a Project or Retainer badge, a terms line and a next-action chip with a date. At 2.3s a card in Replied lifts (border turns violet, big shadow, a 2 degree tilt), travels right over about a second, and drops into Negotiating, whose border and background glow violet while it hovers; counts and totals update when it lands. At 5.2s a second card moves from Contacted to Replied.

## When to use it
Anything that is a pipeline: deals, hiring, content review. The drag moment is the point, so give it time and let the totals change on the drop. If you only need the look, hold the first frame.

## How it works
The board is a flex row of `section`s `w-[280px] rounded-2xl border bg-rv-card/40`; the target column adds `border-rv-purple/60 bg-rv-purple/5` while a card is over it. The card is `rounded-xl border bg-rv-card p-3`, with a 2px left border in amber when stale and red when cold. The kit `KanbanBoard` (dnd-kit) uses the same chrome and settles the drop with a 180ms `cubic-bezier(0.16,1,0.3,1)` animation; the source card stays at 40% opacity during the drag and the overlay carries `border-rv-purple/50` and `shadow-2xl shadow-black/60`.

The demo computes each card's slot from the column lists after the move times, and interpolates the carried card between source and target slots with an ease-in-out:

```js
const k = EASEINOUT(seg(t, m.t0 + .25, m.t1 - .15))        // travel
pos = a + (b - a) * k;  lift = FRAMER(seg(t, m.t0, m.t0 + .25))
```

The column value is the sum of `value_cents`, and the weighted line multiplies it by the stage probability (contacted 10%, replied 25%, negotiating 50%, won 90%).

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Column 280px wide, 12px gap; card 12px padding, 12px radius.
- Lift: 0.25s `[0.16,1,0.3,1]`, 2 degrees tilt, 1.02 scale.
- Stage dots: sourced `#6B7280`, contacted `#3B82F6`, replied `#8B5CF6`, negotiating `#F59E0B`, won `#34D399`.
- Win probabilities: 0, 10, 25, 50, 90 percent.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- Stages and colours in `STAGES`.
- Deals in `DEALS` and the starting lists in `INIT`.
- Moves in `MOVES`: card id, from, to, start and end time.
- Card height `CH`; a taller card needs more lines of terms.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the brands and values are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
