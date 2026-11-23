---
name: error-alert-pale-red-bar-fade-rise-icon-pop
description: "A single-line-and-title error banner: rounded, pale pink fill with a pink border, red circle-exclamation icon on the left, 'Error!' in medium black and 'Please try again...' in grey beneath. Use for failed saves, failed requests and destructive states."
---

# Error alert, pale red bar

**Code name:** Fade rise, icon pop.

## What you see
A near-white page with one alert, about 512 x 74 in life (shown 1.85x): radius 14, 1px border `#f0aaaa`, fill `#faf4f3`. A 17px red `#dc2626` outlined circle with an exclamation mark sits top left, 17px in from the edges. 'Error!' in 15.5px weight 500 black starts 46px from the left, and 'Please try again. If the problem persists, contact support.' in 14.5px `#707074` sits beneath. The page gives only a still, so the motion is added: at 0.3s the bar fades in over 0.45s while rising 10px, the icon pops in from half size with a small overshoot and the exclamation mark gives one short shake, the text fades in just after, and at 3.4s it fades out so the loop closes.

## When to use it
An inline error under a form, above a table or at the top of a page after a failed request. For a message that stays on screen and needs no button, this is enough. If the user must act, add a retry button on the right, or use a modal for something destructive.

## How it works
Three parts: a bordered, tinted rounded box, an icon with the status colour, and a title plus description stack. The tint is a very pale version of the border colour, so the same layout becomes a warning or info alert by swapping `bg`, `border` and `icon`. The icon and its transform are separate from the box so it can overshoot on its own.

```js
const p = eo(seg(t, showAt, showAt + .45))
box.style.transform = `translateY(${(1 - p) * 10}px)`; box.style.opacity = p * out
icon.style.transform = `scale(${.5 + .5 * spring(seg(t, showAt + .1, showAt + .65), 7, 11)})`
```

The real component is static and its source is locked, so everything that moves is an addition for the demo.

## Numbers that matter
| | |
|---|---|
| Box | 512 x 74, radius 14, border `#f0aaaa`, fill `#faf4f3` |
| Icon | 17px, stroke 2, `#dc2626`, at left 17 top 17 |
| Title | 15.5px, 500, left 46 top 14 |
| Text | 14.5px `#707074`, left 46 top 38 |
| Entry (demo) | 0.45s ease-out cubic, 10px rise, icon spring k 7 f 11 |
| Loop | 4.4s, in at 0.3s, out at 3.4s |

## Sound
Silent.

## Adapt it
- `title` and `text`: the message.
- `bg`, `border`, `icon`: red for errors, amber for warnings, blue for info.
- `w` and `h`: size; the box grows with its text in real use.
- `showAt` and `hideAt`: when it appears and leaves, or remove the motion entirely for a static alert.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Error Alert" by cnippet-dev on 21st.dev (https://21st.dev/@cnippet-dev/components/v-alert-7), MIT. This demo is an original recreation written from the public preview.
