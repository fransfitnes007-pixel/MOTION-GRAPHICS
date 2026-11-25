---
name: product-tour-card-with-live-pictures__ghost-pointer-step-through
description: A first-run welcome card that steps through four features, each shown as a small live picture (a prompt box, a project's files, a running command, a keyboard shortcut), with a ghost pointer that clicks the primary button to move on. Reach for it for "here is how the app works" tours in app promos.
---

# Product tour card with live pictures

**Code name:** Ghost pointer step-through.

## What you see
A white 448x372 card with a hairline ring on a white page. Top: a grey picture panel (432x176). Under it a bold title, a two-line grey explanation, a segmented progress bar (four short bars, filled ones near-black) with "1 of 4", and a footer: "Skip tour" in grey at the left, "Back" (from step 2) and a black primary button at the right. Step 1 (fades in over 0.35s): a prompt box with "Why does the checkout test pass locally but fail on CI?" and a round up-arrow send button. A small black pointer fades in at 0.5s, glides onto the primary button "Show me projects" (0.62s) and presses it at 3.0s; the step changes at once: step 2 shows a file card for a project (Instructions, schema.prisma 14 KB, runbook.md 6 KB); step 3 a run log (Read src/lib/checkout.ts, Edited tests/checkout.test.ts, a spinner on Running pnpm test --filter checkout); step 4 two keycaps ⌘ K above a search pill. Each step lasts 3.13s, the pointer moves to the next button label and clicks. 12.5s loop.

## When to use it
Screen-recorded "how it works" beats for an app: four short ideas, one picture each. At 9:16 the card fills 90% of the width. The pictures are the point: replace them with your own mini-UIs. Wrong when a step needs more than one sentence.

## How it works
Timeline per step (read from the page's Web Animations): the pointer layer animates `opacity 0 -> 1` (220ms ease-out) on first show and `transform translate(...)` for 620ms with `cubic-bezier(0.4, 0, 0.2, 1)`; the pointer svg presses with `scale 1 -> 0.86` for 120ms ease-out and back; the step text swaps 134ms after the press and it is a hard cut (no slide, no fade, except the first mount). A pointer glide starts 0.834s before the swap, ends 0.214s before it, the press starts 0.134s before it. The segments tint with `transition: background-color 0.15s`. The spinner is a `chatcn-spin` keyframe, 800ms linear per turn. The pointer lands at 50% of the button's width and 60% of its height. In the demo the whole timeline is a pure function of time; the pointer is placed from the measured width of each step's button label.

## Numbers that matter
| | |
|---|---|
| Card | 448x372, radius 16, ring `0 0 0 1px` at 6% black |
| Picture panel | 432x176 at 8px inset, radius 8, bg oklch(0.975 0 0) |
| Title / body | 18px 600 / 14px 400 colour oklch(0.44 0 0) |
| Progress | 4 bars 16x4, 4px gap, filled oklch(0.145 0 0), empty oklch(0.93 0 0) |
| Buttons | 32px high, radius 8, 14px 500; primary bg oklch(0.145 0 0) |
| Step time | 3.133s; glide 0.62s; press 0.12s |

## Sound
Silent. A click per press and a soft tick on each step.

## Adapt it
- `CONFIG.steps`: title, body, button text and which picture (`prompt`, `files`, `run`, `keys`).
- `CONFIG.stepSec` for pacing; the loop length follows.
- Pictures are HTML strings in `PICS`; swap them for your own product screens.

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Onboarding" by aadixc0de (https://21st.dev/@aadixc0de/components/onboarding), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
