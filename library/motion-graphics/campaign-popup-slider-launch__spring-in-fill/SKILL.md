---
name: campaign-popup-slider-launch-spring-in-fill
description: "A white settings popup springs in beside a round badge, a budget slider fills on the spoken words, and a cursor clicks the blue launch button as the card fades. Reach for it for a set-up or configure-and-launch step in a product film."
---

# Project popup with slider and launch

**Code name:** Spring-in card with eased slider fill.

## What you see
On the white stage a round chrome badge springs in on the left. At 10.92s a white popup card, 640px wide with 26px corners and a deep soft shadow, springs in beside it from 70% size. It is a small setup form: a title "New project" with a green toggle switched on, three equal fields (Niche, Members, Items / day), a budget row with a slider, and a blue "Launch project" button. At 11.92s the slider fills from empty to 68% over about a second, its blue bar growing under a white knob. At 12.82s a cursor appears over the launch button, squeezes, and a ring bursts out; the button dips to 94%. At 12.93s the popup shrinks to 91% and fades out in 0.2s, and the badge is replaced by the next beat.

## When to use it
The "set it up" step: choosing a category, setting a budget, pressing launch. It tells the viewer the product is simple enough to fill out in a few seconds. It is a small card, so keep the fields to three words each. It is wrong for a real product tour, where the audience needs to read every control.

## How it works
Pure HTML and CSS, one spring on the card, one eased value on the slider, and the click function from the cursor skill:

```js
const pq = spring(seg(t, WT.pick, WT.pick + .55), 7, 11)
popup.transform = `scale(${(.7 + .3 * pq) * (1 - hide * .3)})`; popup.opacity = clamp(pq * 2) * (1 - hide)
const sv = eo(seg(t, WT.set, WT.budget + .3)) * .68
fill.width = sv * 100 + '%'; knob.left = sv * 100 + '%'          // fill and knob share one value
```
`hide = ei(seg(t, done - .05, done + .15))` removes the card as the cursor finishes. Everything inside the card is sized in `em` from the card's `fontSize` (40px), so the form scales as one piece. The transform origin is the top centre (`50% 0`), so the card seems to unfold downward.

## Numbers that matter
| | |
|---|---|
| Card | 640px wide, padding 34px, font 40px, radius 26px, transform origin `50% 0` |
| Entrance | spring k7 f11 over .55s, scale .7 to 1 |
| Slider | `eo` from 11.92s to 12.58s, ends at 68% |
| Toggle | 2.3em by 1.3em, on colour `#34c759` |
| Launch button | `#3b82f6` to `#2563eb`, height 2.3em, dips to 94% for .2s |
| Exit | `ei` over .2s, scale to 91% |
| Cursor | arrives .5s before the click, click at 12.88s |

## Sound
One click on the button (60ms of high-passed noise with a 1600Hz blip) at 12.88s, with a rising noise swell underneath that peaks at the next scene's impact. Pops of 700, 900 and 1100Hz follow on the "done" beat.

## Adapt it
- The form's fields, title and button text.
- Slider fill value (`.68`) and its two timings.
- Card position: wide has it right of centre, with the badge on its left.
- The click time `WT.done - .12`.

## Files
- `code/demo.html` runs on its own. The badge is a chrome-gradient placeholder.
