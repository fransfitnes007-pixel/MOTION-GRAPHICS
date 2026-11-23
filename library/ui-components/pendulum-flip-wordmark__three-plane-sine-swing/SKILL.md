---
name: pendulum-flip-wordmark-three-plane-sine-swing
description: "A white logo wordmark on a flat three.js plane that swings left and right through a full half turn on a 7 second sine, turning edge-on and coming back readable, over a faint radial glow on black. Reach for it as a hero logo that needs life without a video."
---

# Pendulum flip wordmark

**Code name:** Three plane sine swing.

## What you see
A black page with a very faint white round glow in the middle. The wordmark, white and flat, hangs at the centre. It turns about its vertical axis: slowly out of rest, narrowing to a thin edge, then reappearing from the other side, and it keeps turning until it has made a half turn (180 degrees) in each direction before slowing and returning. Because the plane is flipped at the moment its back faces the camera, the letters are never mirrored. Perspective makes the near edge larger as it passes.

One swing period is 7 seconds. The demo's corner caption shows the current angle.

## When to use it
A hero logo on a dark landing page, a loading idle, a logo sting that has to run forever. The motion is slow and symmetrical, so it feels calm. Use a one-colour, flat wordmark; a detailed or shaded logo will look wrong when it turns edge-on. If WebGL is unavailable the source falls back to a static image with a glow, which is worth copying.

## How it works
A `planeGeometry` carrying the wordmark as a `meshBasicMaterial` texture (transparent, `toneMapped: false`, double-sided), updated every frame.

```tsx
useFrame((state) => {
  const t = state.clock.getElapsedTime();
  const swing = Math.sin((t * Math.PI * 2) / 7);
  mesh.rotation.y = swing * Math.PI;                    // +-180 degrees
  const facing = Math.cos(mesh.rotation.y);
  mesh.scale.x = facing < 0 ? -1 : 1;                   // un-mirror when the back is showing
});
```

The mirror flip is the key line. A double-sided plane seen from behind is a mirror image, so scaling X by -1 once `cos(rotation.y)` goes negative makes it read correctly again. Camera: `position [0, 0, 4.4]`, `fov 45`. Plane width 5, height from the texture aspect.

The source loads a white PNG with a hand-made `Image` (so a redirect to a CDN does not break the texture loader). The demo draws a placeholder wordmark on a canvas at the same 2.6 aspect. The glow is `radial-gradient(closest-side, hsl(0 0% 100% / .10), transparent 70%)` behind the canvas.

## Numbers that matter
| | |
|---|---|
| Period | 7s (`2π / 7`) |
| Amplitude | rotation.y = +-π |
| Camera | z 4.4, fov 45 |
| Plane | 5 units wide, aspect 2.6 |
| Glow | white 10% to transparent at 70%, `closest-side` |
| Siblings | `pendulum-flip-chrome-wordmark__two-faced-rotatey` is the same idea in CSS with dwells and a second face; `logo-y-spin-and-swing__css-preserve-3d-keyframes` has the plain CSS spin and swing |

## Sound
Silent. A slow low pad or a soft pendulum tick on each pass through centre would suit it.

## Adapt it
- The wordmark: replace the canvas texture with your own PNG through `THREE.TextureLoader` (loading image files into WebGL needs a local server).
- The 7 in `sin(t * 2π / 7)` for speed, and the `Math.PI` factor for how far it turns (use `Math.PI / 2` for a gentle sway with no flip).
- Background colour and glow strength.

## Files
- `code/demo.html`: runs on its own, including from a double-click. `code/three.global.js` is three.js (MIT) bundled as a plain script, so no server is needed.
