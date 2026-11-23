---
name: timeline-accordion-glass-cards-dot-rail-height-auto
description: "A vertical hairline with a dot per item and a frosted glass card beside each. The cards rise in one after another, and clicking one opens its detail with a height and fade animation while its dot turns blue and its chevron flips. Use for a services list or a process on a light marketing page."
---

# Timeline accordion of glass cards

**Code name:** Dot rail, height auto.

## What you see
A narrow column, 768px at most, with a 1px grey line running down the left. Beside the line sit rounded glass cards (28px radius, 55% white, a bright inner top edge, a soft grey drop shadow), 12px apart. Each has a dot on the line at its top: black when closed, blue and 14px with a white ring when open. A card's row holds a 40px rounded blue-tinted icon tile, a small blue number such as "03", the title and a chevron. Open one and its text and a row of white pill tags grow out underneath in 0.3 seconds while the chevron turns over and the card's shadow deepens; the previously open card closes at the same time. On first view the cards rise 24px and fade in, .03s apart.

## When to use it
A services list, a how-it-works sequence or a feature breakdown with up to nine short items, on a page where the process matters more than any one item. The rail makes the list read as a sequence even when it is not. Wrong for long answers (use a FAQ) and for items users need to compare side by side.

## How it works
State is one index, `open`, so only one card is open at a time and the first starts open. Each panel is an `AnimatePresence` child animating `height` from 0 to `auto`, which framer-motion measures for you:

```tsx
<motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }}
  transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }} className="overflow-hidden">
```
The entrance is `FadeUp`: `initial {opacity 0, y 24}`, `whileInView {1, 0}`, `viewport {once: true, margin: '-60px'}`, `duration .7`, `delay .03 * i`, ease `[0.16, 1, 0.3, 1]`. The chevron uses a CSS `transition-transform duration-300` with `rotate-180`, and the dot a CSS colour transition. `aria-expanded` and `aria-controls` tie button and panel together. The glass is `background: rgb(var(--g-bg))` with a 24px `backdrop-filter` blur; the demo leaves the blur out because the page behind is a flat wash.

Content is indented under the title: `pl-[4.5rem]` so the text lines up with the title, not the icon.

## Numbers that matter
| | |
|---|---|
| Column | `max-w-3xl`, rail at `left-[19px]`, `top-3 bottom-3`, `w-px bg-ink/10` |
| Dot | 14px, `left-3 top-[22px]`, 2px ring in the page colour, `bg-ink` closed, `bg-rv-purple` open |
| Card | radius 28px (`rounded-[1.75rem]`), fill `rgb(255 255 255 / .55)`, edge `rgb(255 255 255 / .7)`, shadow `0 8px 32px -12px rgba(15,17,26,.18)`, open `0 24px 64px -24px rgba(15,17,26,.28)` |
| Row | `px-4 sm:px-5 py-3.5`, icon tile 40px radius 16px, number 12px semibold blue |
| Open | height 0 to auto and opacity .3s `[0.16, 1, 0.3, 1]` |
| Tags | `gk-fill` 70% white, 12px medium, `px-2.5 py-1`, gap 6px |
| Reveal | y 24, .7s, delay `.03 * i` |

## Sound
Silent.

## Adapt it
- The items: icon, title, text and tags.
- Which card starts open, or none (`useState<number | null>(null)`).
- Allow several open: use a set instead of one index.
- Dot and tile colour via `--rv-purple`.

## Files
- `code/demo.html` runs on its own and loops in 10s.
