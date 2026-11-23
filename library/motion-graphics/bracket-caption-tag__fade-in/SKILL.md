---
name: bracket-caption-tag-fade-in
description: "A small dark translucent label in square brackets that fades in under a scene to say in three words what it shows, such as '[ publish it everywhere ]'. Reach for it as a quiet step label in a sequence of product scenes."
---

# Bracket caption tag

**Code name:** Eased fade of a dark label.

## What you see
A label about 190px wide and 45px high sits under the main object of a scene. It is a rounded rectangle (.4em radius) in 72% black with white semibold text in square brackets with a space inside each: "[ review every item ]", "[ publish it everywhere ]", "[ pay on results ]". It starts invisible 0.2s to 0.3s after each scene cut and eases to full opacity in 0.3s. There is no movement. It can appear in several scenes in a row and always sits in the same place relative to the scene's main object, about 360px below centre on the wide layout.

## When to use it
A tiny label that names what a scene is, in a sequence of related scenes, so the voice and the image do not have to do it alone. It reads as a step marker or a subtitle for a screen recording. It is wrong as a headline; at 26px it is easy to miss and is meant to be.

## How it works
One absolutely positioned `div`, centred with `left: 50%; transform: translateX(-50%)`, with its `top` set per scene and opacity from one eased value:

```js
tag.style.opacity = eo(seg(t, cut + .2, cut + .5))
```
CSS: `padding: .35em .7em; border-radius: .4em; background: rgba(0,0,0,.72); color: #fff; font: 600 1em sans; white-space: nowrap`. Because the box is `em`-based, the font size alone (26px, 19px on tall) sizes it.

The fade is the only thing that makes it a "motion graphic". In the demo it is cut to three different scenes with new text each time; each is a separate scene with its own timing.

## Numbers that matter
| | |
|---|---|
| Fade | `eo` over .3s, .2s after the cut (.3s in two of the three scenes) |
| Text | 26px (`26 * K`), weight 600, white |
| Box | `rgba(0,0,0,.72)`, radius .4em, padding .35em .7em |
| Position | 360px below centre (wide), 560px (tall) in scene A; 400 and 520 in scene B; 230 and 300 in scene C |

## Sound
Silent. It lands in the same beat as a pop from the scene (1250Hz, 0.11s).

## Adapt it
- The text: keep it to three or four words.
- Position and size so it clears the scene's object.
- Fade time and delay.
- Or invert the colours (white label with dark text) on a dark scene.

## Files
- `code/demo.html` runs on its own. The card photo is a gradient placeholder.
