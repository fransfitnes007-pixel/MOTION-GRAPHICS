---
name: form-walkthrough-focus-camera-field-click-type-continue
description: "A browser window walks through a multi-step form: for each step the view pushes in on the part being used, a cursor clicks the field, the screen swaps from empty to filled, the page scrolls to the Continue button, the cursor clicks it, and the camera glides to the next step. Reach for it for \"how to set up\" tutorials built from screenshots."
---

# Form walkthrough with a camera that follows the action

**Code name:** Focus-point push-in, before/after screens, scripted cursor.

## What you see
A browser window (1440 x 964 design size) over a pastel ground shows a form step. Each step lasts 2.6s. The view starts wide, then in 0.6s pushes in 1.42x on the middle point between the field and the Continue button. A cursor glides to the field (0.25s to 0.85s), presses at 0.86s with a ripple, and the screen swaps from the empty form to the filled one (cross-fade from 0.95s to 1.3s). The page then scrolls up to bring the Continue button in view (1.3s to 1.75s), the cursor glides to the button (1.5s to 2.05s) and clicks it at 2.16s. The next step's screen fades up 28px from below while the camera glides to its focus point. After the last step the window shrinks to 95% and fades.

## When to use it
A how-to or onboarding video made from screenshots of a flow: sign-up, setup wizard, checkout, settings. It shows exactly where to click and what appears, without recording the screen live. Needs two screenshots per step (before and after). Wrong when the steps are only text.

## How it works
Every screen is a flat image, and everything else is derived from a table of steps. Each step lists the field rectangle and the button rectangle. From those, per step: a focus point (half way between field and button), a scroll offset (enough to bring the button 70px above the view bottom), the cursor's field target (a point 35% along the field, at most 150px in) and the button centre.

```js
s.fo = { x: 650, y: (s.field.y + s.field.h / 2 + s.btn.y) / 2 }
s.sB = s.btn ? Math.max(0, s.btn.y + s.btn.h + 70 - VIEW_H) : 0
const ck = eio(p(q, 0, 0.6))                       // q = time since this step began
const z = 1 + (lerp(pf.z, st.Z, ck) - 1) * g, fx = lerp(pf.x, st.fo.x, ck), fy = lerp(pf.y, st.fo.y - scroll, ck)
tf(cam, clamp(720 - fx * z, 1440 - 1440 * z, 0), clamp(450 - fy * z, 900 - 900 * z, 0), z)
```

The camera is one container transform: scale `z` about the view's top-left and a translate that puts the focus point (fx, fy) at the view's centre (720, 450), clamped so the edges of the page never show. `pf` is the previous step's focus, so the camera glides from step to step; `g` fades the zoom in at the start and out at the end. The cursor and its ripple live inside that container, so they zoom with the page. The cursor's start of each step is where the previous step's button click ended.

In real use the "before" and "after" screens are screenshots, one pair per step, and the sound cues are read out of the page (`window.SOUNDS`): a key tick per character for typing steps and a click for each field and button press. The demo draws three stand-in steps with CSS: a login, a long form that needs scrolling, and a colour pick that changes the preview.

## Numbers that matter
| | |
|---|---|
| Step length | 2.6s |
| Camera zoom | 1.42x (1.24x for the later dashboard steps), push-in 0.6s, ease-in-out-cubic |
| Cursor to field | q 0.25s to 0.85s; press 0.86s to 1.0s (scale .82); ripple 0.9s to 1.35s |
| Before to after | q 0.95s to 1.3s |
| Scroll to Continue | q 1.3s to 1.75s, ease-in-out-cubic |
| Cursor to Continue | q 1.5s to 2.05s; press 2.16s to 2.32s; ripple 2.2s to 2.6s |
| Window | 1440 x 964, shown 1250px wide; radius 22px; pops in .92 to 1 over 0.7s |
| Ripple | 14px to 74px, 4px `#5b5ce6` |

## Sound
Typing steps: five key ticks at q + 0.98s, 1.06, 1.15, 1.23 and 1.32s. Every field click and Continue click: one mouse click (at q + 0.9s and q + 2.2s). The cues are listed in `window.SOUNDS` and mixed from samples afterwards. See the typing and click sound skill.

## Adapt it
- `STEPS`: field and button rectangles and screenshots (`a` empty, `b` filled) for each step.
- Zoom `Z` per step, and the step length `STEP` (2.6s).
- The cursor start point (1040, 660) and ripple colour.
- Window size `G` and the target of the push-in (`fo`).

## Files
- `code/demo.html` runs on its own (9.3s loop, three steps).
