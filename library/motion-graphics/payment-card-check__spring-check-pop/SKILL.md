---
name: payment-card-check-spring-check-pop
description: "A white profile card springs in, a green check circle pops on its right and the line 'Sent by bank transfer' turns from faded to full green. Reach for it for a paid, approved or sent confirmation."
---

# Payment confirmation card

**Code name:** Spring card with check pop.

## What you see
On a white frame a card 700px wide springs in from 75% size, fading in. A round photo, a bold handle and a small grey line ("12 approved items") sit across the top. At the far right of that row there is an empty space. Below a thin grey divider the row reads "Payment" in grey on the left and "Sent by email" in green on the right, faded to 30%. At 20.6s a green circle with a white check springs in in the empty space, growing from 0 with a small overshoot, and at the same time the green status line goes from 30% to full opacity. The confetti skill describes a burst that can follow.

## When to use it
The moment a thing is done and someone gets paid, approved, shipped or confirmed. The two-stage reveal (card, then tick) keeps the moment from being flat. It is wrong when the card needs to carry a long list: it is a one-line receipt.

## How it works
Two springs from two start times:

```js
const q = spring(seg(t, cardStart, cardStart + .55), 7, 11)        // card: scale .75 to 1, opacity clamp(q * 2)
const ck = spring(seg(t, resultsWord - .1, resultsWord + .4), 8, 12)
check.style.transform = `scale(${ck})`; status.style.opacity = .3 + .7 * ck
```
The check circle exists from the start at `scale(0)` and its spring gives it a slight overshoot as it opens. The tick is an inline SVG with round caps: `M5 12.5l4.5 4.5L19 7.5` at stroke 3.4. The card is the shared popup surface: white, radius 30px, shadow `0 50px 110px -30px rgba(0,0,0,.45)`, `overflow: hidden`. All inner sizes are in `em` from the 42px base.

## Numbers that matter
| | |
|---|---|
| Card | 700px wide, padding 32px, font 42px, radius 30px |
| Card entrance | spring k7 f11 over .55s, scale .75 to 1 |
| Check | 1.9em `#1f8f3e` circle, spring k8 f12 over .5s, starts .1s before the voice word |
| Status | `#1f8f3e`, opacity .3 to 1 with the check |
| Avatar | 2.2em circle |

## Sound
A single pop (1700Hz, 0.11s) at the check, 20.7s, then a quick spray of 16 high pops for the confetti.

## Adapt it
- The handle, count, and the row's label and status text.
- Check colour for other states (amber, blue).
- Order of the two reveals: delay the check for a bigger pause.
- Avatar image.

## Files
- `code/demo.html` runs on its own. The avatar is a gradient placeholder.
