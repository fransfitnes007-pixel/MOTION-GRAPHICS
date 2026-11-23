---
name: shattered-glass-headline-svg-shard-parallax-cursor-glow
description: A dark hero of seven cracked glass shards with glinting white edges, a blue-grey headline showing through and slightly displaced inside each shard, and a soft light that follows the cursor. Use for an edgy landing hero or title card.
---

# Shattered glass headline

**Code name:** SVG shard parallax, cursor glow.

## What you see
A near-black page with a faint blue vignette. Seven irregular glass shards sit in a jigsaw with thin dark gaps, together about 720px wide and 560px tall. Each is almost black with a diagonal sheen, a bright white rim about 2px wide with a soft glow, and a few hairline cracks across it. The headline 'broken by design.' (bold, 80px, blue-grey `#9aa0b8`) runs across the middle. Inside each shard its copy is shifted a few pixels, so letters appear cut and slipped at the cracks, which is why the 'n' and 'g' look split. A soft white bloom about 60px across follows the cursor and only shows on the glass. The shards drift 4px toward the cursor at different rates and rock about a third of a degree. A small speaker button sits bottom right in the original, an author credit bottom left (left out of the demo).

## When to use it
A single-screen hero for a bold, technical or edgy brand, a title card for a launch, or a 404. It is one headline only, so it needs a short phrase, and the cursor glow needs a pointer.

## How it works
One SVG. Each shard is a `polygon`. Its group holds the dark gradient fill, a `clip-path` group with a displaced copy of the headline, the crack lines and the cursor glow circle, and then two strokes for the rim (a blurred bright one under a thin one). The base headline is drawn once behind everything. The shard groups are transformed with `translate` and `rotate` computed from the cursor, so clip and contents move together. The glow is a radial-gradient circle inside every shard's clip, so it only lights glass.

```js
s.g.setAttribute('transform', `translate(${tx} ${ty}) rotate(${rot} ${cx} ${cy})`)
glow.setAttribute('cx', cursor.x - tx)   // cursor light, drawn inside the shard's clip
```

The original may be a canvas or WebGL piece with real refraction; this is an SVG imitation of that look, matched by eye. The shard outlines were traced from one frame.

## Numbers that matter
| | |
|---|---|
| Shards | 7 polygons, 4 to 9 points each |
| Rim | 2.2px `rgba(235,240,255,.75)` blurred 1.2px, plus 1px `rgba(255,255,255,.35)` |
| Fill | gradient from white .1 to black .7 |
| Headline | 80px bold, letter-spacing -3px, `#9aa0b8`, copy opacity .42 in shards |
| Refraction | each shard copy shifted up to 5px |
| Drift | 4px toward the cursor, 1.2px ambient, 0.35 degree rock |
| Glow | 60px radius, white .55 to 0 |

## Sound
Silent.

## Adapt it
- `text`, `fontSize`, `textColor`: the headline.
- `SHARDS`: the polygon points and crack lines; trace a new set for a different break pattern.
- `refract`: 0 for a clean read, 10 for heavy slip.
- `glowSize` and `rim`: cooler or warmer light, or a tinted glass.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Broken By Design — Shattered Glass Hero" by gughigug on 21st.dev (https://21st.dev/@gughigug/components/broken-by-design), MIT. This demo is an original recreation written from the public preview.
