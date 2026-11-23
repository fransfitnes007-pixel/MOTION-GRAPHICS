---
name: dropdown-select-with-avatar-rows-and-avatar-value-custom-value-render
description: "A \"User\" select: a 256 by 36 px pill trigger that opens a popover of five people (32 px gradient avatar, name, email, check mark on the chosen one), and shows a 16 px avatar plus the name in the closed trigger. Reach for it for assignee, owner and account pickers."
---

# Dropdown select with avatar rows and an avatar in the trigger

**Code name:** Custom value render in the trigger.

## What you see
White page, label "User", and a pill trigger with the grey placeholder "Select a user" and a chevron. A click opens a white popover with 27 px corners that fades and scales in over about 0.2s. It lists Bob, Fred, Martha, John and Jane, each on a 52 px row: a 32 px round avatar painted as a soft two-tone sphere (blue-violet, green, magenta, red, orange), the name in 14.5 px medium above the email in 12.5 px grey. The row under the pointer fills light grey.

Clicking Bob closes the popover in 0.16s and the trigger now shows a 16 px copy of his avatar and "Bob" in black. Opening it again shows a check mark at the right of Bob's row. The preview video (2s) shows the same sequence compressed; the demo stretches it to 4.6s and ends with a click-away close.

## When to use it
Choosing a person: assign an owner, pick a teammate, switch an account. The rich row helps tell similar names apart; the small avatar in the trigger keeps the choice recognisable after it closes. With many people add search.

## How it works
The usage example is the interesting part: `Select.Value` accepts a render function with `{ defaultChildren, isPlaceholder, state }`. When nothing is chosen it returns `defaultChildren` (the placeholder); when several are chosen it returns "N users selected"; when one is chosen it looks the user up by key and returns a flex row with a `size-4` `Avatar` and the name:

```tsx
<Select.Value>{({ defaultChildren, isPlaceholder, state }) => { ... <div className="flex items-center gap-2"><Avatar className="size-4" size="sm">...</Avatar><span>{name}</span></div> }}</Select.Value>
```

Each option is a `ListBox.Item` holding an `Avatar`, a column with a `Label` and a `Description`, and a `ListBox.ItemIndicator` (the check). The demo does the same with plain boxes: avatars are radial gradients, and the trigger text is swapped when the pick click happens.

```js
open = eo(seg(t, clickOpen, clickOpen + .22)) * (1 - eo(seg(t, clickPick, clickPick + .16)))
```

The plain-text version of this select is the sibling `dropdown-select-with-check-mark__rounded-popover-fade-scale-row-hover`. Emails in the demo use example.com.

## Numbers that matter
| | |
|---|---|
| Trigger | 256 by 36, 18px radius, `#f6f6f7`, chosen value with a 16px avatar and 8px gap |
| Popover | 256 wide, 27px radius, 9px padding, 9px under the trigger |
| Rows | 52px tall, 32px avatar at x 14, text at x 58, hover fill `#f1f1f3` |
| Text | name 14.5px medium, email 12.5px `#6f6f75` |
| Avatars | radial gradient from a light tint at 30% 25% to the full colour at 85% |
| Open and close | 0.22s and 0.16s, scale .96 to 1 |

## Sound
Silent.

## Adapt it
- `items`: name, email and the two avatar colours for each person (or remove `avatar` and `email` for plain rows).
- `label`, `placeholder`, `width`, `rowH`.
- `pick` for which person is chosen; the `click...` times for the script.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "HeroUI Select" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-select/custom-value), MIT. This demo is an original recreation written from the public preview.
