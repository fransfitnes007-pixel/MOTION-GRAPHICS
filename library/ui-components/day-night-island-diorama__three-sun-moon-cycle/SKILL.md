---
name: day-night-island-diorama-three-sun-moon-cycle
description: "A low-poly three.js island scene whose sky runs a full day to night cycle: a yellow sun with glow, a moon, stars, cloud and bird layers, sunset orange, torches and coloured spotlights at night, with small box-bodied agents walking about and showing chat bubbles. Reach for it as a living 3D backdrop or a hero for an \"AI agents at work\" story."
---

# Day-night island diorama

**Code name:** Three sun-moon cycle.

## What you see
An aerial view over a sandy island ringed with turquoise water. A straw-roofed tiki hut on a wooden deck, a grey lab building with a green lit sign, a floor of coloured dance tiles with two speakers, fifteen palm trees. Six small characters (a coloured box body and a skin-tone box head) walk between waypoints with a little hop, and speech bubbles ("Deploy is live", "Numbers up 12%") rise over them. A mono clock in the corner reads the time of day.

The demo plays one whole day in 16 seconds, starting at 05:46:
- 0 to 2s: dawn. The sun is a low orange disc with a glow, the sky is light blue to orange.
- 2 to 8s: day. The sun climbs and crosses, clouds drift, birds circle, the water glitters.
- 8 to 10s: dusk. The sky lerps to sunset orange, then to deep navy.
- 10 to 16s: night. Stars fade in, the sun and glow hide, a moon rises, fireflies pulse, the torches and dance spotlights are the only light and three coloured beams sweep the dance floor.

## When to use it
A 3D ambient background for an agent or automation product, a "while you sleep, it works" beat, a loading or empty state with personality. It reads as a toy world, so it suits friendly or playful positioning. It is wrong for a serious enterprise look, and the sand is bright, so on a white page it can feel washed out.

## How it works
Everything is driven by one number, `dayNightT`, 0 to 1 over a day. The app runs it for 30 real minutes, the demo for 16 seconds.

```js
const sunAngle = dayNightT * Math.PI * 2 - Math.PI / 2
const sunY = Math.sin(sunAngle), sunX = Math.cos(sunAngle) * 80
sunLight.position.set(sunX, Math.max(5, sunY * 80), 40)
sunLight.intensity = Math.max(0, sunY) * 2.5
moonLight.intensity = Math.max(0, -sunY) * 0.4
sunSphere.position.set(sunX * 3, Math.max(-50, sunY * 200), -100)   // moon is the mirror
starMat.opacity = sunY < 0 ? Math.min(1, -sunY * 3) : 0
ambLight.intensity = 0.15 + Math.max(0, sunY) * 0.5
renderer.toneMappingExposure = 0.6 + Math.max(0, sunY) * 1.0
// sky: day #87CEEB -> sunset #ff6633 (sunY .2 to -.05) -> night #0a0a2a (-.05 to -.2)
```

Sky and fog take the same colour, so the horizon dissolves into the haze. The sun glow is a canvas radial-gradient sprite with additive blending. Chat bubbles are canvas textures on sprites that fade in over 0.3s and live 4.5s.

Changes that make the loop repeatable and let it run standalone:
- `Math.random` is replaced by a seeded generator, so stars, palms and clouds are fixed.
- Every drifting thing (waves, clouds, birds, fireflies, spotlight sweep) repeats once per loop, so the last frame joins the first. The wave formula is the app's, `sin(x*.08 + e*1.5)*.4 + cos(y*.06 + e*1.2)*.3 + sin((x+y)*.05 + e*.8)*.2`, with the three speeds snapped to 4, 3 and 2 cycles per loop. The spotlight sweep is the app's `baseAngle + elapsed * 1.5`, snapped to 4 turns per loop.
- Characters follow waypoint loops instead of the random Wanderer state machine. They keep its hop, `abs(sin(t * 8)) * 0.07`.
- The app's glTF characters and the environment cube map are replaced by the app's own box fallback character and plain lights. Water uses opacity, not transmission.
- Camera sways around the island instead of OrbitControls. Exposure is a little lower than the app's, to stop the sand clipping.
- The sign text is a placeholder: "NORTHSTAR LABS".

## Numbers that matter
| | |
|---|---|
| Day length | 16s here (1800s in the app) |
| Sun | 8-radius sphere `#ffdd44`, turns `#ff6622` below sunY 0.15; glow sprite 30 + sunY * 15 |
| Lights | ambient .5, hemisphere sky `#87CEEB` ground `#f4a460`, sun 2.5, fill `#8899cc` .4, rim .3, moon `#4466aa` |
| Fog | exp2 0.003 |
| Island | sand cylinder r80, lagoon r120, hut roof cone r22 h10, 15 palms |
| Camera | fov 50 (68 in tall), 150 units out, sways 0.45 rad |
| Tone mapping | ACES filmic |

## Sound
Silent. Waves, a low synth pad that darkens at night and a few soft chat blips would suit it.

## Adapt it
- `DUR` for day length, and the start offset `0.24` for the time you want at frame 0.
- The sky colours `skyDay`, `skySunset`, `skyNight`.
- The sign text, building colours and the `AGENT` table (colour and waypoints).
- Remove the dance floor and spotlights for a calmer island.

## Files
- `code/demo.html`: runs on its own, including from a double-click. `code/three.global.js` is three.js (MIT) bundled as a plain script, so no server is needed.
