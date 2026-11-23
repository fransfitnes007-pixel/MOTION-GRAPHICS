---
name: ai-prompt-box-mode-pills-icon-grows-to-coloured-pill
description: A big dark AI chat input with a toolbar of toggle buttons that expand into cyan, purple and orange labelled pills. Reach for it as the main input on an AI chat or search screen.
---

# AI prompt box with mode pills

**Code name:** Icon grows to coloured pill.

## What you see
A near-black page with one wide rounded input box, 1160px across and 148px tall, in dark grey with a thin border. The top line is grey placeholder text. Along the bottom: a paperclip, a globe, a thin violet divider, a gear, another divider, a folder icon with code brackets. On the right a white round button with a microphone. Clicking the globe turns it into a cyan pill, "Search", and the placeholder reads "Search the web...". Clicking the gear swaps that to a purple "Think" pill and "Think deeply...". Clicking the folder adds an orange "Canvas" pill next to it; clicking it again fades it out. Each pill grows from the icon's width to about 100px over about 0.3s while the icon cross-fades into icon plus label, and its neighbours slide along.

## When to use it
The main entry point of an AI assistant, a search page with modes, any composer where a few features can be switched on per message. Wrong for a single-purpose input; the toolbar is the point.

## How it works
Each toolbar slot has an icon state and a pill state, and a progress `p` from 0 to 1. The slot width is `lerp(40, pillWidth, p)`, the icon opacity is `1-p`, and the pill (icon plus label, coloured) opacity is `p`. Slots are laid out left to right from their current widths, so neighbours slide as one grows. The pill tint is the colour at about 15% for the background and 50% for the border.

```js
w = lerp(40, mode.pill, eo(seg(t, t0, t0+.28)))
slot.x = previous.x + previous.w + gap
```

Search and Think are exclusive, Canvas is independent. In the demo the clicks are scripted with a drawn cursor. The send, voice and file-upload actions are not animated.

## Numbers that matter
| | |
|---|---|
| Box | 1160x148, 30px radius, `#1f2023`, border `#34353a` |
| Placeholder | 22px, `#8d8d95` |
| Pills | 38px tall, widths 104 / 98 / 112, morph .28s ease-out |
| Colours | Search `#38bdf8`, Think `#a78bfa`, Canvas `#fb923c`, backgrounds at 14 to 16% |
| Clicks | Search .9s, Think 2.4s, Canvas on 3.6s, off 4.8s, Think off 5.4s |

## Sound
Silent.

## Adapt it
- `placeholders` and the `modes` labels, colours and widths.
- `events`: the click order and timing.
- `growSec` for a snappier or softer morph.
- Add a fourth mode by adding an icon to `I` and an entry in `modes` and `icons`.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "AI Prompt Box" by johuniq on 21st.dev (https://21st.dev/@johuniq/components/ai-prompt-box), MIT. This demo is an original recreation written from the public preview.
