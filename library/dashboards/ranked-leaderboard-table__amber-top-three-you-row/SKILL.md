---
name: ranked-leaderboard-table-amber-top-three-you-row
description: "A leaderboard table: square rank chips (amber for the first three), avatars, views in white semibold, posts, earned in green, and a violet-tinted row with a YOU tag for the viewer. Use it for any ranked list."
---

# Ranked leaderboard table

**Code name:** Rank chips with amber top three and highlighted self row.

## What you see
A header with a small amber trophy, "LEADERBOARD" in uppercase and "Ranked by counted views" at the right, then a bordered table. Rows slide up 8px and fade in 0.12s apart. Rank chips are 28px rounded squares: amber (15% fill, amber-300 text, amber border) for 1 to 3, grey for the rest. The fourth row, the viewer, has a 10% violet background and a "YOU" tag. From 3s the view counts tick up as new posts are counted.

## When to use it
Competitive or social proof: creator rankings, sales leaderboards. The self row shows the viewer where they stand without a separate widget.

## How it works
```tsx
<span className={`inline-flex items-center justify-center w-7 h-7 rounded-lg text-xs font-bold ${top
  ? 'bg-amber-500/15 text-amber-300 border border-amber-500/30' : 'bg-white/5 text-white/70'}`}>{r.rank}</span>
<tr className={`border-b border-rv-border/60 last:border-0 ${me ? 'bg-rv-purple/10' : 'hover:bg-white/[0.02]'}`}>
```
Header cells are 11px uppercase `tracking-wider` muted; numbers are right-aligned; Earned is `text-emerald-300 font-semibold`. A loading state is three `h-12` shimmer rows. The row arrival and the ticking counts are demo additions.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Rank chip 28px, 8px radius; amber `245,158,11` at 15% fill, 30% border.
- Row padding 10px 12px; avatar 28px.
- Self row `rgba(139,92,246,0.10)`.
- Earned colour `#6EE7B7`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `ROWS`: name, views, posts, earned, self flag.
- Drop the Earned column with the app's `hideEarned` prop.
- Top-N highlight count: change `i < 3`.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
