---
name: product-ui-depth-camera-dof-rack-focus-pan
description: "A mock app window made of three depth layers (a background list, a floating card, a toast) where the camera pans between them and racks focus with blur as depth of field, ending on a tight push into the card's primary button and a click. Reach for it as the feature beat of a product demo or launch film."
---

# Product UI depth camera

**Code name:** DOF rack focus pan. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
A dark app window (sidebar, nine list rows) fades in sharp at 0 to 0.6 s. At 1.2 s a card springs up in front of it ("Publish your changes?" with Cancel and Continue) and focus racks from the list to the card by 2.0 s, the list falling into soft blur. At 2.6 s a toast ("Changes saved") drops in from the top right, blurred because it is nearer than the focus plane. From 3.2 s to 4.0 s focus racks to the toast while the camera pans up and to the right at 130 % zoom; it holds until 4.8 s. The camera then swings back and the focus returns to the card by 5.5 s. A cursor glides in from 5.2 s, the camera pushes to 215 % zoom on the Continue button (6.4 s), the button hovers brighter and at 6.2 s is clicked: it dips 7 % and a ring spreads from it. The scene fades out from 6.65 s so the loop restarts clean.

## When to use it
Showing a product doing one thing: a confirmation, a save, a purchase. Depth of field makes a flat screen look filmed, and the rack focus tells the viewer where to look. It is wrong for dense UI that must be read in full (the out-of-focus layers are unreadable on purpose) and for fast, loud edits.

## How it works
Three absolutely positioned layers sit at the frame centre, each with a depth `z` of 0 (window), 1 (card) or 2 (toast). One camera, defined by tracks of centre `(cx, cy)`, `zoom` and `focus` (each a list of `[time, value]` keys eased with `eio`), drives all three:

```js
scale_z = zoom * (1 + 0.09 * z)             // nearer layers are bigger
transform = translate(-cx * scale_z, -cy * scale_z) scale(scale_z)
blur_px = |focus - z| * 11                  // depth of field: distance from the focus plane
```
Because nearer layers have a larger scale, the same pan moves them further, which is the parallax. `focus` is just another animated number: 0 on the list, 1 on the card, 2 on the toast, back to 1. The button centre is computed from the card layout, so the camera target and the click ring always land on it. Everything inside (card spring, toast drop, cursor path, hover, press, ring) is a closed-form function of `t`.

## Numbers that matter
| | |
|---|---|
| Layers | window 1400x860, card 580x430, toast 500x100 (tall: 940x1360, 700x560) |
| Parallax | scale gain 9 % per depth step |
| Depth of field | 11 px of blur per unit of focus distance |
| Rack focus | 0 to 1 over 1.2 s to 2.0 s; 1 to 2 over 3.2 s to 3.9 s; 2 to 1 over 4.8 s to 5.5 s |
| Push in | 5.6 s to 6.4 s, zoom 1.08 to 2.15 (1.75 tall), `eio` |
| Click | 6.2 s, press -7 %, ring 240 px wider over 0.5 s |
| Colours | ink `#0b0b10`, paper `#f2f2f4`, accent `#6aa8ff` |

## Sound
Silent in the demo. A soft thud as the card lands, a bright ping as the toast arrives, a shallow breath-like whoosh on each rack focus, and a click (40 ms) on the press.

## Adapt it
- The three layer contents (`list`, `card`, `toast` HTML) for your own UI.
- The camera tracks `CX_`, `CY_`, `ZM_`, `FC_`: add or retime keys to point at other regions.
- `BLUR` (11) and `PAR` (0.09) for more or less depth.
- Accent colour in the CSS (`#6aa8ff`) and the button label.

## Files
- `code/demo.html` runs on its own, loops every 7 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`
