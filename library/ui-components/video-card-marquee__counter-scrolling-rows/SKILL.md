---
name: video-card-marquee-counter-scrolling-rows
description: "Two rows of 9:16 glass-framed video cards drifting in opposite directions with a niche chip on each, a lift and play dot on hover, and a click that springs a glass sheet up with the full player. Reach for it as a work reel under a hero."
---

# Video card marquee

**Code name:** Counter-scrolling rows.

## What you see
A centred headline, then two rows of tall cards on glass frames, 230px wide with 16px between them. The top row slides left, the bottom row slides right, about 27px a second, with the page edges fading out. Each card shows a muted loop, a frosted niche chip at top left and a gradient at the foot. A pointer rests on one card: it lifts 4px and a round play dot fades in at its top right. The pointer clicks; the background blurs and darkens (ink/70) and a glass sheet rises 40px with a spring, holding a chip, a close button and the vertical player.

## When to use it
A portfolio or agency page with many vertical clips where range matters more than any single clip. The clips should be short and loop. Wrong for a handful of videos (they would repeat visibly), or for landscape video.

## How it works
Rows come from `mixNiches`, a round-robin over niches so no run of one niche appears, then split into even and odd halves. Each row is an `InfiniteSlider` with `duration = row.length * 9` and `durationOnHover = row.length * 30`; the second row has `reverse`. Two details keep a wall of 60 videos cheap: a card only sets its `src` when an `IntersectionObserver` says it is 20% visible, and removes it again when it is more than 600px away.

The modal uses `AnimatePresence`:

```tsx
<motion.div initial={{ y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: 40, opacity: 0 }}
  transition={{ type: "spring", damping: 26, stiffness: 260 }} className="glass-strong w-full max-w-md rounded-t-4xl p-3 sm:rounded-4xl">
```

The demo reproduces that spring analytically. Hover uses Tailwind `group-hover:-translate-y-1` over 300ms. Because the placeholder cards are all different, the loop fades at the wrap rather than joining seamlessly.

## Numbers that matter
| | |
|---|---|
| Card | 230px wide (190 on phones), 9:16, glass-strong rounded-3xl, 6px padding, inner radius 18.4px |
| Row speed | half width in (cards x 9)s; hover slows to (cards x 30)s |
| Row gap | 16px between cards and between rows |
| Chip | text 11px semibold white, border white/30, fill white/25, blur md |
| Hover | translate -4px over 300ms, play dot opacity 0 to 1 |
| Sheet | spring damping 26, stiffness 260, y 40 to 0, max-w-md, overlay ink/70 with blur md |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- Card width and the row count (one row below 14 videos).
- Chip text: niche, result, or platform.
- Row duration multiplier (9) for faster or slower drift.
- Sheet spring: lower damping for a bouncier arrival.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.
