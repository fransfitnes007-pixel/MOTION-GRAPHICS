---
name: upvote-downvote-card-green-red-digit-roll-colour-fade
description: A white vote card with a count and two black round buttons (up, down). Voting up turns the card mint green with a green up button, voting down turns it pink-red with a red down button, and only the digit that changed rolls to its new value. Use for votes, likes or ratings.
---

# Upvote downvote card, green and red

**Code name:** Digit roll, colour fade.

## What you see
A white page with one small card, about 132 x 114px in real size (the demo shows it 2.9x): off-white `#fafafa`, 14px radius, soft shadow, with '14 Upvotes' in 15.5px semibold on top and two 40px black circles below, an up arrow and a down arrow in white. At 1.0s the cursor clicks up: over 0.25s the card fills with mint `#86efac` and a green border, the text goes white, the up button turns green `#00c055`, and the units digit rolls from 4 up to 5, the old digit leaving upward with a little blur while the new one rises from below over 0.38s. At 2.5s a second click on up gives 16. At 4.0s a click on down makes the card pink `#fca5a5` with a red border, the down button turns red `#f0293f`, and the digit rolls downward to 15. At 6.0s the demo resets to neutral so the loop closes; the original clip does not show a reset, so that part is invented.

## When to use it
Voting, helpful-or-not, thumbs on comments, or any small count a person can nudge up or down where you want instant colour feedback. The card is the whole control, so it suits a list of items better than a dense table cell.

## How it works
The number is split into digits and each digit is its own animated cell, so a change from 14 to 15 only moves the last digit. The motion library used by the original is `motion-number`, a number-roll component. The colour state is a single value: neutral, up or down, and every colour on the card is a pure function of that value, so a transition is just a blend between the old set and the new set.

```js
const k = eo(seg(t - tChange, 0, .25))
colour = mix(prevSet[i], nextSet[i], k)          // card, border, text, both buttons
old.y = -dir * 14 * p;  new.y = dir * 14 * (1 - p) // digit roll, p over .38s
```

The click sequence in the demo (up, up, down) was read from the clip. Behaviour on a repeat click of the same button is not shown there.

## Numbers that matter
| | |
|---|---|
| Card | 132 x 114, radius 14, shadow `0 8px 22px rgba(0,0,0,.09)` |
| Neutral | fill `#fafafa`, border `#ececec`, text `#111`, buttons black |
| Up | fill `#86efac`, border `#22c55e`, text white, up button `#00c055` |
| Down | fill `#fca5a5`, border `#ef4444`, text white, down button `#f0293f` |
| Buttons | 40px circles, 20px arrows, 2.2 stroke |
| Colour fade | 0.25s ease-out |
| Digit roll | 0.38s, 14px travel, 1.5px blur |

## Sound
Silent.

## Adapt it
- `start` and `label`: the count and the word after it.
- `colors`: the three state palettes; swap green and red for brand colours.
- `clicks`: scripted sequence, replaced by real handlers in your app.
- `roll`: the speed of the digit roll.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Upvote Downvote Counter" by uilayout.contact on 21st.dev (https://21st.dev/@uilayout.contact/components/motion-number-upvotes), MIT. This demo is an original recreation written from the public preview.
