---
name: faq-accordion-glass-height-auto-fade
description: "A frosted-glass list of questions where one answer is open at a time; the open answer grows to its natural height while it fades in, the previous one closes at the same time, and the chevron turns over. Reach for it for FAQs and any single-open list."
---

# Glass FAQ accordion

**Code name:** Height auto fade.

## What you see
Left, a glass card titled "Questions" holding a second, lighter glass card with four rows. The first answer is open. A pointer clicks the second question: the first answer collapses and fades while the second grows open and fades in, both over a quarter of a second, and the chevrons swap. A third click opens the fourth question; clicking it again closes everything. On the right, a larger glass card holds the closing pitch, a checklist and two buttons.

## When to use it
FAQ blocks, settings groups, spec lists: anywhere only one answer should be open so the page does not jump. Wrong for content people compare side by side (use tabs or show all).

## How it works
State is just `open: string | null`, initially the first item. Clicking the open item sets it to null, otherwise to the new id. Each answer is an `AnimatePresence` child that animates `height` between 0 and `"auto"`, which framer measures, together with opacity:

```tsx
<AnimatePresence initial={false}>
  {isOpen && (
    <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }}
      exit={{ height: 0, opacity: 0 }} transition={{ duration: 0.25 }} className="overflow-hidden">
```

`initial={false}` keeps the first item from animating on page load. The chevron is not framer: it is `transition-transform` with a `rotate-180` class when open. Rows are separated by `divide-y divide-ink/5`. `aria-expanded` is set on each button. The demo measures each answer's natural height once and then sets it as a pixel value over time.

## Numbers that matter
| | |
|---|---|
| Container | `glass` (white/55, blur 24px), rounded-3xl, dividers ink/5 |
| Row | px-5 py-4, question 16px semibold, chevron 16px ink-3 |
| Answer | px-5 pb-5, 14px, ink-2, leading-relaxed |
| Motion | height 0 to auto and opacity 0 to 1, .25s tween, no spring |
| Chevron | rotate 180deg, Tailwind transition-transform (150ms) |
| Mode | one open at a time; tap the open one to close it |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The items; they are `{ id, q, a }`.
- Duration (.25) for snappier or softer.
- Start closed by initialising `open` to null.
- Allow several open by holding a set of ids instead of a single one.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.
