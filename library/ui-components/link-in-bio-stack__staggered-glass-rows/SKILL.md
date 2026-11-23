---
name: link-in-bio-stack-staggered-glass-rows
description: "A phone-width link page: round avatar, name, social icons, two stat tiles, then grouped rows of glass link cards where the first is solid black, each row fading up a few hundredths of a second after the one above. Reach for it as a link-in-bio or a mobile contact card."
---

# Link-in-bio stack

**Code name:** Staggered glass rows.

## What you see
Inside a phone frame on the site's pastel background: two small glass pills at the top (the address and Share), a 112px avatar with a white 4px border, name, handle, a short line and four circular glass social buttons. Two glass stat tiles follow. Then the first group of link rows: the first row is solid black with white text (the highlighted action), the rest are white glass, each with a rounded icon square, a bold label, a grey one-line description and an arrow. The rows appear one after another. After a pause the page scrolls to the shop group (black icon squares, a black price pill) and the contact group, one row lifts 2px on hover, and the page scrolls back.

## When to use it
Anywhere a single phone-width column of links and offers is the whole page: link-in-bio, event pages, a digital business card. The black row says "do this first". Wrong for dense navigation or more than about 12 rows.

## How it works
The header is one `motion.div` with `initial={{ opacity: 0, y: 12 }}`; each `Row` is a `motion.div` with `initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay }}` and `delay = i * 0.04`, with no duration set so framer uses its default (a quick spring on y, a short tween on opacity). The demo approximates that default with a spring of stiffness 500 and damping 25.

```tsx
<TrackedLink className={cn("card-hover flex items-center gap-3 rounded-2xl p-3", l.highlight ? "bg-ink text-white shadow-pill" : "glass")}>
```

`card-hover` is `transition-all duration-300 hover:-translate-y-0.5 hover:shadow-glass-lg`. Rows are grouped with an uppercase 12px label (`tracking-wider text-ink-3`) and `space-y-2.5`. Links can be scheduled or expire (`scheduledAt`, `expiresAt`), and every tap goes through `TrackedLink` for counting.

## Numbers that matter
| | |
|---|---|
| Column | max-w-md (448px), 16px side padding |
| Avatar | 112px, 4px white border, shadow-glass-lg |
| Row | rounded-2xl, 12px padding, gap 12px; icon square 44px rounded-xl; label 14px semibold; description 12px ink-3 |
| Highlight row | bg ink, white text, shadow-pill |
| Stagger | delay i x .04s, y 10 to 0, opacity 0 to 1 |
| Hover | -2px lift and larger shadow, 300ms |
| Group label | 12px semibold uppercase tracking-wider ink-3 |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- Which row is `highlight` (the black one) and the link groups.
- The per-row delay (.04) for a faster or slower cascade.
- Replace the avatar with a logo mark.
- Row radius: `rounded-2xl` to `rounded-full` for pill rows.

## Files
- `code/demo.html` runs on its own and loops. Name, links and numbers are placeholders.
