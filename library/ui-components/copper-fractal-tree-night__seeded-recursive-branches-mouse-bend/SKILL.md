---
name: copper-fractal-tree-night-seeded-recursive-branches-mouse-bend
description: A near-black page with a single copper tree drawn from recursive splitting branches, a dim glowing crown and floating dust. Branches lean away from the cursor. Use for a quiet hero background, a 404 or an AI/nature section.
---

# Copper fractal tree at night

**Code name:** Seeded recursive branches, mouse bend.

## What you see
Black background with a faint brown glow behind the crown. A straight copper trunk, about 6px wide at the bottom, rises from the bottom centre of the screen and splits into two. Each branch splits again and again, about 12 levels, with each level shorter and thinner, until the tips are hairs a pixel wide drawn in dim olive-grey with low opacity, which together look like a foggy crown wider than it is tall. The crown covers roughly the top 60% of the frame. A few dust specks sit in the dark. A small white cursor drifts through the crown and the branches near it lean away; the whole tree also sways very slightly. In the original clip the shape barely changes, so the movement is subtle by design.

## When to use it
A calm, dark hero or empty-state background where one organic object carries the page, or a section about growth, an agent, or nature. Too busy to sit behind long body text, and it needs a dark page.

## How it works
One recursive function draws a line, then calls itself two or three times with a shorter length, a thinner width and an angle offset. A seeded random generator is reset at the start of every frame, so the same branch always gets the same lean and length, which keeps each frame a pure function of time. Wind is a sine added to each branch angle, stronger on thin tips. Cursor bend adds an angle away from the pointer for branches within 150px. Colour fades from copper to olive grey with depth and the strokes use additive blending, so overlapping twigs glow into a cloud.

```js
const sway = Math.sin(t / DUR * 6.283 + phase + d * .6) * .02 * (.3 + tip * 1.4)
if (dist < 150) a += Math.sign(dx) * .34 * (1 - dist / 150) ** 2 * (.3 + tip)
branch(x2, y2, a + side * lean, len * shrink, d + 1, w * .74)
```

The original code is locked, so the exact branching rules are guessed from the picture. The overall shape and colours match; the individual branch layout does not.

## Numbers that matter
| | |
|---|---|
| Depth | 12 levels, about 2 children per branch, 12% chance of 3 |
| Trunk | 160px long, 6px wide, width x .74 per level |
| Length | x .66 to .8 per level |
| Lean | 15 to 44 degrees per child |
| Colours | copper `rgb(150,82,34)`, tips `rgb(120,112,80)`, background `#08070a` |
| Sway | .02 rad at the tips, one cycle per 5s loop |
| Cursor | 150px reach, .34 rad lean |

## Sound
Silent.

## Adapt it
- `seed`: gives a different tree each time you change it.
- `depth`: 10 is lighter and more skeletal, 13 is denser (it doubles the line count).
- `copper` and `leaf`: the wood and the foliage colours, such as green for spring or white for frost.
- `spread` and `shrink`: wide and flat like an acacia, or narrow like a poplar.
- `mouseBend` and `mouseRadius`: set `mouseBend` to 0 to switch off the cursor reaction.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Generative Tree" by mengto on 21st.dev (https://21st.dev/@mengto/components/generative-tree), MIT. This demo is an original recreation written from the public preview.
