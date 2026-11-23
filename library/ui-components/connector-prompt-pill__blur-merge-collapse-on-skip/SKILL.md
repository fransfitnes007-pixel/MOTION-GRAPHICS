---
name: connector-prompt-pill-blur-merge-collapse-on-skip
description: "A prompt box with a connector offer pill stacked on top of it: provider mark and name, a Skip text button and an outlined Connect button. Skipping blurs the pill into the composer, which re-centres and takes focus. Reach for it in AI chat inputs that offer to connect an app."
---

# Connector prompt pill

**Code name:** Blur-merge collapse on Skip.

## What you see
A white page with two stacked pieces, both 560 wide in the poster. On top, a pill 86 high with a 2px light grey outline: a small boxed logo mark, "MCP Connector" in 15px grey over the provider name in 23px semibold, "Skip" in grey semibold and a 124 by 44 "Connect" pill with a pale lavender outline and blue text. 14px below it, a composer 170 high with a 40px radius, off-white fill, "Ask anything..." in 24px grey at the top left and a 44px light grey send button with an up arrow at the bottom right.

In the 2.3s clip the cursor sits on Connect, and both outlines turn lavender blue (`#8f95d9`) while it is hovered. The cursor then moves to Skip and clicks at about 1.97s. Within about 0.15s the pill blurs, loses opacity and sinks into the composer, which slides up about 50px so the single box is centred, and a blue focus rectangle appears around the text area. The clip loops back to the full stack.

The demo runs 6.6s and slows the collapse to 0.55s so it can be read; the pill returns at 5.2s so it loops.

## When to use it
An AI chat or search input that wants to offer one optional step (connect an account, enable a tool) without a modal. The offer is attached to the box it affects and goes away in one click. Not for required steps; a skippable pill reads as optional.

## How it works
Two siblings in a column. Collapse is one value `out` from 0 to 1:

```js
composer.transform = translateY(-(pillH + gap) / 2 * out)
pill.transform = translateY((pillH + gap) / 2 * out) scale(1 - .08 * out)
pill.opacity = 1 - clamp(out * 1.25);  pill.filter = blur(out * 7px)
```

The component is named Liquid Connector and, from the name, likely uses an SVG gooey filter to join the two shapes. The clip shows a blur and fade rather than a visible metaball, so the demo uses a CSS blur. The usage props are `open gap={10} provider eyebrow placeholder connectLabel skipLabel promptLabel sendLabel stageLabel`; `gap` and `open` control the stack spacing and whether the pill shows.

## Numbers that matter
| | |
|---|---|
| Pill | 560 x 86, fully rounded, 2px `#dedede`, gap 14px to composer |
| Composer | 560 x 170, 40px radius, `#fbfbfb`, 2px `#dedede` |
| Hover outline | `#8f95d9` on both pieces |
| Connect | 124 x 44, border `#dfe1f8`, text `#1f4fc4` 20px / 600 |
| Send | 44px, `#dcdcdc`, white arrow |
| Collapse | clip about 0.15s; demo 0.55s, blur 7px, scale .92 |
| Focus ring | 2px `#4c5fd1` around the text area after collapse |

## Sound
Silent.

## Adapt it
- `CONFIG.provider`, `eyebrow`, `placeholder`, `connectLabel`, `skipLabel`.
- `hoverBorder` and `restBorder` for brand outlines.
- `collapseSec` back to about 0.15 for the original snap.
- `skipClickAt` to time the click against a voiceover.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Liquid Connector" by zanwei on 21st.dev (https://21st.dev/@zanwei/components/liquid-connector), MIT. This demo is an original recreation written from the public preview.
