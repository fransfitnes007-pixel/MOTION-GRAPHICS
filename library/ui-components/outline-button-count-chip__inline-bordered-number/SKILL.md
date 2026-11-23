---
name: outline-button-count-chip-inline-bordered-number
description: A white outline button with a label and a small bordered number chip inside at the right end, like Messages 18. Reach for it for inbox, tab and filter buttons that need a count without a notification dot.
---

# Outline button with count chip

**Code name:** Inline bordered number.

## What you see
A pill-cornered white button about 116 by 32 on a white page, a 1px light-grey border and a faint shadow. The word Messages sits in 14px medium black text. At the right end, after a 12px gap, is a 20px-high chip with its own 1px border, rounded 4px, holding the number 18 in 10px medium grey. Nothing moves in the original. The demo scripts a cursor so you can see hover (fill goes light grey), press (scale .985) and the focus ring (3px soft grey).

## When to use it
Navigation tabs, inbox and notification buttons, filter buttons that show how many results match. The chip is quiet, so it suits a count that is information, not an alert. For something that must be noticed, use the dark badge button, `bell-button-count-badge__click-clears-badge`.

## How it works
A normal outline button with a child span. The span has its own border, 4px radius, `h-5 px-1`, 10px text, `text-muted-foreground`. Negative end margin (`-me-1`) pulls the chip closer to the button edge so the visual padding looks even, and `ms-3` pushes it off the label.

```tsx
<Button variant="outline">
  Messages
  <span className="-me-1 ms-3 inline-flex h-5 items-center rounded border border-border px-1 text-[0.625rem] font-medium text-muted-foreground">18</span>
</Button>
```

## Numbers that matter
| | |
|---|---|
| Button | height 36px real (shown at 2.2x), padding 0 16px, radius 8px, border 1px `#e2e2e2` |
| Label | 14px, weight 500 |
| Chip | height 20px, padding 0 4px, radius 4px, 10px text, grey `#737373`, margin-left 12px, margin-right -4px |
| Hover | fill `#f4f4f5` |
| Focus | 3px ring `rgba(120,120,130,.35)` |

## Sound
Silent.

## Adapt it
- `CONFIG.label` and `CONFIG.count`: the text.
- `CONFIG.zoom`: scale of the hero button.
- `CONFIG.border`, `CONFIG.hover`, `CONFIG.ring`: the three greys.
- `CONFIG.others`: the smaller example buttons.

## Files
- `code/demo.html` runs on its own and loops. A scripted cursor shows hover, press and focus.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Button" by originui on 21st.dev (https://21st.dev/@originui/components/button/button-with-number), MIT. This demo is an original recreation written from the public preview.
