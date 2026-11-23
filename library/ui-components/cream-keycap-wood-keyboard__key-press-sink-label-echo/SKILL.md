---
name: cream-keycap-wood-keyboard-key-press-sink-label-echo
description: "A vintage keyboard: 61 cream keycaps with bevelled edges in a dark wood case on a light page. A key sinks when pressed and its letter appears above the board. Use as a typing hero, a 'press any key' prompt or a retro desk scene."
---

# Cream keycap wood keyboard

**Code name:** Key press sink, label echo.

## What you see
A pale grey page with the text 'Press any key...' in grey 21px centred above a wide wooden keyboard. The case is brown walnut with faint vertical grain, 1160px wide and 405px tall in the demo, with a black well inside. Five rows of 61 cream keycaps: Esc to Backspace, Tab row, CapsLock row, Shift row and the bottom row with a long space bar. Each cap has a soft bevel, a lighter top and a darker bottom edge, a bold dark-grey legend, and small grey shifted symbols (!, @, #) in the top-left of number and punctuation keys. When a key is hit it sinks about 4px, shrinks 2%, darkens 6% and comes back after 0.22s, and the line above changes to that key's letter. The demo types E, R, T, Y, A, S and Space over 5 seconds.

## When to use it
A hero or landing page for something about typing, writing or hardware, a keyboard-shortcut explainer, or an empty state asking the visitor to press a key. It is a showpiece, so it is wasted on a screen that also needs lots of other controls.

## How it works
The rows are plain data with a width in key units (1, 1.5, 1.75, 2.25, 2.75 and a 7.2 unit space bar, all adding up to 15 per row). Each key is an absolutely positioned cell with a `.cap` inside it. The cap's look is all CSS: a cream gradient, an inner highlight on top, an inner shadow at the bottom and an outer drop shadow that reads as the keycap side. The wood is a vertical `repeating-linear-gradient` over a brown gradient. In the real component, key presses come from `keydown` and `keyup` listeners; the demo scripts them.

```js
const down = eo(seg(d, 0, .06))          // 60ms to sink
cap.style.transform = `translateY(${4 * down}px) scale(${1 - .02 * down})`
cap.style.filter = `brightness(${1 - .06 * down})`
```

## Numbers that matter
| | |
|---|---|
| Layout | 5 rows, 15 units wide, unit 75.5px on the 1280 board |
| Keycap | radius 12, 3px gap, gradient `#f1e6d6` to `#d4c0a4` |
| Wood | `#8a5428` to `#5a3217`, 11px visible border, black well `#110c09` |
| Legend | 15px bold `#4a4540`, shifted symbol 10px `#9a9186` |
| Press | 4px sink, scale .98, 0.22s down, 0.12s release |
| Label | 'Press any key...' 21px `#8a8a8a`, then the pressed key 15px |

## Sound
Silent.

## Adapt it
- `strokes`: the keys and times, or wire real key events in your app.
- The cap gradient colours and the wood gradient for a black, white or beige board.
- `ROWS`: change the layout, for example drop the top row for a 40 percent look.
- `travel` and `pressTime`: a deeper or lazier press.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Vintage Keyboard" by ayushmxxn on 21st.dev (https://21st.dev/@ayushmxxn/components/vintage-keyboard), MIT. This demo is an original recreation written from the public preview.
