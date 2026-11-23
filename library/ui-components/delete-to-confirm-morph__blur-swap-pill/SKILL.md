---
name: delete-to-confirm-morph-blur-swap-pill
description: "A white sheet with Delete and Edit pills: the first tap blurs the grey Delete pill into a pink Confirm with a check, the second drops the sheet away. Use for two-step destructive actions."
---

# Delete to confirm morph

**Code name:** Blur swap pill.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
A dark stage with a white sheet showing Transaction, rows for Amount $25.00, Date, Category and Note, and two pills: a grey Delete and a pale blue Edit.
- 0.15 to .95s: the sheet rises from below the frame with a small spring overshoot.
- 1.0 to 1.55s: a finger arrives over the Delete pill. 1.6s: it taps (ripple, finger and pill shrink a few percent).
- 1.68 to 2.2s: the grey pill blurs up to 7px while its label fades out; at the midpoint the colour crossfades to pink and Confirm fades in, and the pill sharpens again, now pink with red Confirm and a check that draws. The pill widens with a spring from 352 to 424px and Edit gives up the space.
- 3.1s: a second tap on Confirm. 3.3 to 4.0s: the whole sheet drops down out of view, accelerating. It stays gone until the loop restarts and it rises again.

## When to use it
Two-step confirmation of a destructive action in an app preview or explainer: delete, cancel subscription, remove card. The blur hides the label swap so the button reads as one object changing, not two. Wrong where the second step needs a reason or typed input.

## How it works
One pill element holds two background layers and two label layers. With `p1 = seg(t, 1.68, 2.2)`:
```js
blur  = 7 * sin(PI * p1)                      // peaks mid-swap, zero at both ends
pink  = eo(seg(p1, .3, .7))                    // background crossfade
labelA = 1 - seg(p1, .2, .5); labelB = seg(p1, .5, .8)
width = lerp(352, 424, spring(seg(t, 1.7, 2.4), 7, 10))
```
Edit is positioned from the Delete width, so the row always totals 724px. The sheet's offset is `D * (1 - spring(seg(t, .15, .95)))` on the way in and `D * ei(seg(t, 3.3, 4.0))` on the way out, where `D` is the distance to below the frame; frame 0 and frame DUR both have the sheet below the view, so the loop is clean. The sheet is built at 820 x 800 and scaled 1.1 (1.15 tall).

## Numbers that matter
| | |
|---|---|
| Blur | 0 to 7px to 0, over .52s, sine |
| Width | 352 to 424px, `spring(x, 7, 10)` |
| Tap press | pill scale -5%, finger -17% |
| Sheet in / out | .8s spring / .7s ease-in cubic |
| Colours | grey `#e9e9ee`, pink `#ffdde3`, red `#e5233f` |
| Loop | 5.4s |

## Sound
Silent. A soft click per digit or tap, and a light chime on success, would fit.

## Adapt it
- The row labels and values, and the button text.
- Pink and red for another destructive colour.
- Blur peak and the swap window (`p1`).
- Set the drop to a slide-right dismissal by changing the translate axis.

## Files
- `code/demo.html`
- `media/poster.jpg`
