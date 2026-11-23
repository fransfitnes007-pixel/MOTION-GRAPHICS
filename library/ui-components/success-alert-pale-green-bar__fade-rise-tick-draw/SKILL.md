---
name: success-alert-pale-green-bar-fade-rise-tick-draw
description: "A success banner: rounded, pale mint fill with a green-tinted border, a green circle-check icon, 'Success!' in medium black and a grey confirmation line beneath. Use after a save, a payment or a completed task."
---

# Success alert, pale green bar

**Code name:** Fade rise, tick draw.

## What you see
A near-white page with one alert, about 576 x 74 in life (shown 1.7x): radius 14, 1px border `#a9e6cf`, fill `#f4faf8`. A 17px green `#3fb487` outlined circle with a tick sits top left. 'Success!' in 15.5px weight 500 black, and 'Everything is working as expected. You can continue with your task.' in 14.5px `#707074` beneath. The page gives only a still, so the motion is added: at 0.3s the bar fades in over 0.45s while rising 10px, the icon pops in from 60 percent size with a small overshoot, and the tick draws itself over 0.45s with a stroke dash, then the text fades in, and at 3.4s the bar fades out so the loop closes.

## When to use it
Confirming something finished: a saved form, a sent invite, a passed check. Use it inline where the user is already looking; for confirmations that should vanish on their own, a toast is better.

## How it works
Same structure as the error alert: a bordered, tinted box, a coloured icon and a title plus description stack. The tick path has `pathLength=100` and a dash array of 100, so setting `stroke-dashoffset` from 100 to 0 draws it from start to end.

```js
tick.setAttribute('stroke-dashoffset', 100 * (1 - eo(seg(t, showAt + .3, showAt + .75))))
icon.style.transform = `scale(${.6 + .4 * spring(seg(t, showAt + .1, showAt + .65), 7, 11)})`
```

The real component is static and its source is locked, so everything that moves is an addition for the demo.

## Numbers that matter
| | |
|---|---|
| Box | 576 x 74, radius 14, border `#a9e6cf`, fill `#f4faf8` |
| Icon | 17px, stroke 2, `#3fb487`, at left 17 top 17 |
| Title | 15.5px, 500, left 46 top 14 |
| Text | 14.5px `#707074`, left 46 top 38 |
| Tick draw (demo) | 0.45s ease-out cubic, starts 0.6s |
| Entry (demo) | 10px rise, icon spring k 7 f 11 |
| Loop | 4.4s, in at 0.3s, out at 3.4s |

## Sound
Silent.

## Adapt it
- `title` and `text`: the message.
- `bg`, `border`, `icon`: any success green, or a brand colour.
- `w` and `h`: size.
- `showAt` and `hideAt`: timing, or drop the motion for a static alert.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Success Alert" by cnippet-dev on 21st.dev (https://21st.dev/@cnippet-dev/components/v-alert-5), MIT. This demo is an original recreation written from the public preview.
