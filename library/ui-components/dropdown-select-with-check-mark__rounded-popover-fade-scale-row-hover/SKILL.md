---
name: dropdown-select-with-check-mark-rounded-popover-fade-scale-row-hover
description: "A light select field: label \"State\", a 256 by 36 px pill trigger with a chevron, and a rounded popover listing six options with a grey hover row and a check mark on the chosen one. Reach for it for address forms and checkout fields."
---

# Dropdown select with a check mark

**Code name:** Rounded popover, fade and scale open, row hover.

## What you see
White page. The label "State" (14 px medium) sits above a 256 by 36 px trigger with fully rounded ends, very light grey fill and a soft hairline shadow; the grey placeholder "Select one" is on the left and a small chevron on the right.

When the pointer clicks it, a white popover (27 px radius, wide soft shadow) fades and scales in from 96% in about 0.2s, directly under the trigger and as wide as it, with a 9 px gap. It lists Florida, Delaware, California, Texas, New York and Washington on 40 px rows in 14.5 px medium text. The row under the pointer gets a light grey (`#f1f1f3`) rounded fill. Clicking an option closes the popover in about 0.15s and puts the choice in the trigger in black text, with the chevron flipped back. Opening it again shows a check mark at the right of the chosen row. The preview video (2s) shows exactly this open, hover, pick, close, reopen sequence; the demo spreads it over 4.6s and adds a click-away close.

## When to use it
Any single-choice field with more than three options and no search need: state, country, plan, sort order. For long lists with search use a combobox. The check mark makes it a good fit for forms where a returning user needs to see what is already set.

## How it works
HeroUI v3's Select is built on React Aria and has a compound API, as the usage example shows: `Select`, `Select.Trigger`, `Select.Value`, `Select.Indicator`, `Select.Popover`, `ListBox`, `ListBox.Item` and `ListBox.ItemIndicator`. The description lists single and multiple selection, groups with headers, disabled items, a controlled value, keyboard support and type-ahead; none of that shows in the preview video.

The demo rebuilds the look with absolute boxes and times each state from the clicks you script in `CONFIG`:

```js
open = eo(seg(t, clickOpen, clickOpen + .22)) * (1 - eo(seg(t, clickPick, clickPick + .16)))
popover.style = { opacity: open, transform: `scale(${.96 + .04*open}) translateY(${(open-1)*6}px)` }
```

The sibling `dropdown-select-with-avatar-rows-and-avatar-value__custom-value-render` is the same select with avatar and email rows and a custom value in the trigger.

## Numbers that matter
| | |
|---|---|
| Trigger | 256 by 36, 18px radius, `#f6f6f7`, 14px text, placeholder `#6b6b70` |
| Popover | 256 wide, 27px radius, 9px gap under the trigger, 9px inner padding |
| Rows | 40px tall, 18px radius hover fill `#f1f1f3`, 14.5px medium |
| Check | 14px, 2.6 stroke, right edge 14px in |
| Open | 0.22s, scale .96 to 1, 6px slide; close 0.16s |
| Demo clicks | open 0.5s, pick 1.6s, reopen 2.6s, click away 3.9s |

## Sound
Silent.

## Adapt it
- `label`, `placeholder` and `items` (name per option; add `email` and `avatar` for a richer row).
- `width` and `rowH` for the size, `pick` for which option is clicked.
- `hoverFill` and `accent` for colours.
- `clickOpen`, `clickPick`, `clickOpen2`, `clickAway` to retime the script.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "HeroUI Select" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-select), MIT. This demo is an original recreation written from the public preview.
