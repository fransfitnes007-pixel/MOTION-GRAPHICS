---
name: black-pill-button-with-travelling-rim-light-sliding-conic-wedge-spin
description: A black pill button with a thin bright arc of light travelling along its edge, on a white page with a large soft shadow underneath. Reach for it as the single primary call to action.
---

# Black pill button with a travelling rim light

**Code name:** Sliding conic wedge with spin.

## What you see
A black pill (304 by 79 in a 1064 by 798 frame, fully rounded, 1px border at 10% white) with 'Shimmer Button' in 26px medium white. An inner glow along the bottom edge (inset 8px, 10px blur, 12% white) makes the lower rim slightly lighter. Under it a soft shadow about 26px blur. The shimmer is a 1 to 2px bright line on the border only, blurred about 1.3px. It brightens along its length like a comet: faint at its tail and brightest at its leading edge, then ends in a hard cut. Over a 6s loop it starts as a short sliver along the bottom middle, slides to the left cap, curls up the left end, then (after a pause) swings round to the top and crosses it, then returns. On hover the bottom glow strengthens to 25% over 0.3s, and on press the button drops 1px. The demo adds a scripted pointer to show hover and press.

## When to use it
One hero or pricing call to action on a light page, where a black button should feel a little charged. Use it once per screen. It reads best at 150px or wider; the light is too thin to notice below about 100px.

## How it works
Three layers. Back: a square the height of the button that slides left and right (`ease-in-out infinite alternate`, 3s each way) and carries an oversized conic gradient `conic-gradient(from 225deg, transparent 0, white 90deg, transparent 90deg)` that spins with its own keyframes (0 to 90 degrees by 15%, hold until 35%, to 270 degrees by 65%, hold until 85%, to 360 by 100%, linear, 6s in all). That layer has a 2px blur. Front: an opaque black pill inset by 0.05em hides everything except a hairline rim, so only the edge glows. The demo draws the same thing with a canvas: it walks 900 points round the pill, for each one works out the angle from the sliding centre, and lights it if it falls inside the spinning 90-degree wedge, with brightness rising across the wedge, within 1.5 button heights of the centre like the original's square. The loop starts 4.2s into the cycle so the first frame matches the preview video.

## Numbers that matter
- Button 304 by 79, radius 39px, fill `#000`, border 1px 10% white, text 26px medium
- Wedge 90 degrees, starts at 225 degrees, spin keyframes 0, 90, 90, 270, 270, 360 degrees at 0, 15, 35, 65, 85, 100%
- Slide 3s ease-in-out alternate; loop 6s
- Rim light 2.4px wide, blur 1.3px, white; inner glow `inset 0 -8px 10px #ffffff1f`, hover `inset 0 -6px 10px #ffffff3f`
- Press: translateY 1px; shadow blur 26px at 22% black

## Sound
Silent.

## Adapt it
- `label`, `fill`, `color` (the shimmer colour; try an accent colour for a coloured rim).
- `speed` for a faster or slower lap (loop is 2 x speed) and `spreadDeg` for a longer or shorter streak.
- `rim` and `blur` for a sharper or softer line.
- `size` and `fontSize` for the button itself.

## Files
- `code/demo.html` runs on its own, loops in 6s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Shimmer Button" by dillionverma on 21st.dev (https://21st.dev/@dillionverma/components/shimmer-button), MIT. This demo is an original recreation written from the public preview.
