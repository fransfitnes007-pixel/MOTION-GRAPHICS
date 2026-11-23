---
name: plinko-discount-drop-fixed-step-peg-physics
description: "A dark Plinko board in a white pop-up: a ball with the brand mark falls through five rows of pegs, each peg flashing lilac when hit, into one of six discount pockets, which lights gold with a confetti burst. The result is decided by the server beforehand; the board finds a real physics drop that ends in that pocket. Reach for it for a list-building offer or a reward reveal."
---

# Plinko discount drop

**Code name:** Fixed-step peg physics.

## What you see
A white rounded pop-up on a dimmed page: a yellow "Everyone wins something" pill, a bold headline, two lines of copy. Under it a dark board with 27 grey pegs, six pockets along the bottom (50%, 20%, 10%, 15%, 25%, 75%) and a white ball carrying a small mark, waiting at the top with a pulsing gold glow and a "Your ball" label. A pointer taps the black "Drop to win" button, which dims to "Ball in play...". The ball drops, spinning its mark, bouncing off pegs (each peg swells 35% and flashes lilac for a quarter of a second), settles into the 25% pocket, which glows gold. 34 coloured pieces fan up from it, the headline changes to "You won 25% off. Claim your code." and an indigo claim button replaces the black one.

## When to use it
A reward or reveal where suspense is the point: a discount, a prize, a tier. The outcome is fixed, so it must always be honest about what it is; the source says "Every drop wins at least 10% off". Wrong where the result should be genuinely random or where the board might appear to cheat.

## How it works
A small physics engine, run at a fixed step so the same seed always plays the same way:

```ts
const P = { gravity: 680, pegRestitution: 0.76, wallRestitution: 0.7, tangentRetention: 0.985, pocketRestitution: 0.3, pocketSpring: 150, pocketDamping: 18, fixedStep: 1 / 240, maxPlayTime: 3.5 }
```

Each step adds gravity, moves the 24px ball, bounces it off the walls and off every 5px-radius peg (reflect the normal speed by `pegRestitution`, keep 98.5% of the tangent speed), and records which pegs were hit with a 75ms debounce. After `maxPlayTime` or at the pocket row, the ball is captured: a spring (150, damping 18) pulls it to the pocket centre while gravity and two soft floor bounces settle it.

The trick is `pickSeed`. The server has already decided the pocket, so the board simulates seeds 1 to 700 (`mulberry32(seed)` gives the start jitter and sideways kick) until one naturally lands in that pocket. Only if none does, the capture step steers the ball in. So the viewer sees a genuine bounce that ends where it must.

Pegs flash with a CSS keyframe `gk-peg 260ms cubic-bezier(.22,1,.36,1)`; the landed pocket pulses with `gk-pocket 900ms`; confetti pieces use `rotate(a) translateY(-d) rotate(r)` with durations of 650 to 1010ms. The demo precomputes the whole trajectory from the same code, then plays it by looking up the step for time `t`, so the render is a pure function of time.

## Numbers that matter
| | |
|---|---|
| Board | bg #111216, radius 22, 250px high (220 on phones), width of the pop-up body |
| Pegs | 10px, 5 rows of 5, 6, 5, 6, 5, rows at 10% + 18% steps of the play area |
| Pockets | 6 columns, 44px high: 50, 20, 10, 15, 25, 75 percent |
| Ball | 24px, radial white gradient; mark 14px spins 700ms per turn while dropping |
| Physics | gravity 680, peg restitution .76, wall .7, tangent keep .985, step 1/240s |
| Peg flash | 260ms: scale 1 to 1.35 to 1, #3d3f45 to #cbb8ff, glow rgba(155,130,242,.9) |
| Confetti | 34 pieces 6 x 9px, six colours, fan -150 to 150 degrees, 70 to 160px, 650 to 1010ms |
| Idle | ball glow 1.6s ease-in-out between lilac and gold |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- `POCKETS` and the prizes behind them; keep six columns or change `grid-cols-6` and the slot width.
- The physics numbers: lower `pegRestitution` for a heavier ball, raise gravity for a quicker drop.
- Row layout `ROWS`, `FIVE` and `SIX` for more rows.
- Confetti colours and the pocket glow colour.

## Files
- `code/demo.html` runs on its own and loops. The mark on the ball is a letter; the page behind is a plain dim backdrop. The demo uses a fixed seed that lands in the 25% pocket.
