---
name: form-label-above-pill-input-click-label-focuses-field
description: "A label and a text field, stacked with a 4 px gap: \"Name\" in 14 px medium over a 256 px wide, fully rounded white input with a soft shadow and grey placeholder \"Enter your name\". The label is linked to the input by `htmlFor`, so clicking it focuses the field. Reach for it as the basic building block of any form."
---

# Form label above a pill input

**Code name:** Label tied to the field with htmlFor.

## What you see
White page. The caption "Name" is in medium weight, near black, sitting right above a pill input about 2 times the CSS size in the preview image (513 by 73 px there). The input is white with a very faint border, a two-layer soft shadow (`0 1px 2px` plus `0 4px 10px`) and the grey placeholder "Enter your name" at 24 px in from the left.

The 21st.dev page has no video, only this still, so the motion is the demo's. A pointer clicks the "Name" label at 1.1s; a blue (`#0485f7`) 3 px ring fades in on the field and a caret blinks, which is the whole point of linking the label to its input. "Alex Morgan" types in at 0.09s per character from 1.7s. At 4.3s the pointer clicks elsewhere, the ring fades out and the text stays; the text clears just before the loop restarts.

## When to use it
Every form field. Use it when you want a visible caption that also gives the control its accessible name and a bigger click target. It is wrong for placeholder-only fields, where the name disappears as soon as someone types.

## How it works
The usage example is two parts. The `Label` from this component takes `htmlFor`, and HeroUI's `Input` takes the matching `id`:

```tsx
<div className="flex flex-col gap-1">
  <Label htmlFor="name">Name</Label>
  <Input className="w-64" id="name" placeholder="Enter your name" type="text" />
</div>
```

Association is native: a `<label for>` forwards a click to its control, which focuses it, and screen readers read the label with the input. The demo shows that by scripting the click on the label. The focus ring colour and shape in the demo are chosen for it; the preview image only shows the resting state. Caret position is the measured width of the typed text.

```js
caret.left = 24 + widthOf(typed)           // px, blinks at 1Hz while focused
ring.opacity = eo(seg(t, click + .04, click + .2)) * (1 - eo(seg(t, away + .04, away + .2)))
```

## Numbers that matter
| | |
|---|---|
| Box | 850 by 650 (the preview image at 2x of CSS pixels) |
| Label | 27px medium at x 208, 4 CSS px above the field |
| Input | 513 by 73, fully rounded, white, border `#f1f1f2` |
| Shadow | `0 1px 2px rgba(0,0,0,.06), 0 4px 10px rgba(0,0,0,.08)` |
| Text | 27px, placeholder `#707076` |
| Focus (demo choice) | 3px ring `#0485f7`, 0.16s |
| Typing | 0.09s per character from 1.7s |

## Sound
Silent.

## Adapt it
- `label`, `placeholder`, `typed` for the words.
- `accent` for the focus ring; `inputW`, `inputH` for the size.
- `clickLabel`, `typeFrom`, `typeStep`, `clickAway` to retime the story.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "HeroUI Label" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-label), MIT. This demo is an original recreation written from the public preview.
