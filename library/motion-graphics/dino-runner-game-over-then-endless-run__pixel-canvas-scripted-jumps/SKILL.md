---
name: dino-runner-game-over-then-endless-run-pixel-canvas-scripted-jumps
description: "A 9:16 video in the look of the offline dino game. The brand is the dino and obstacles are the cacti; it crashes and restarts, then runs at double speed through YourBrand into the chrome monogram and an end card. Reach for it when a problem is a loop people keep restarting."
---

# Dino runner: game over, then the endless run

**Code name:** pixel canvas, scripted jumps on voiceover word times.

## What you see

1. **0 to 6s.** Grey pixel game on black, in a dark UI theme. A white pill names the dino YOUR BRAND, a dark glass pill names the first cactus BAD OBSTACLE.
2. **6.9 and 8.0s.** Two clean jumps, on "dodge one" and "dodge two".
3. **8.9 to 12.1s.** Three cacti arrive with dark glass pills popping on their words: ✕ BLOCKED YOU, ✕ MISSED THE TARGET, ✕ BROKE EVERYTHING. The dino hits them. GAME OVER, a white flash, X eyes.
4. **13 to 18s.** RESTART 1 to 6: the same crash, faster each time, on "new attempts, same cactus". Then the screen dims and EVERY / SINGLE / TIME. slams in at 190px, one word per syllable (16.28, 16.56, 16.96s), SINGLE in pure white with a glow.

Top left for the whole game: the brand's domain. Top right: a small chrome monogram turning like a coin (`cos(t * 2.4)` on its x scale). Both leave when the end card arrives.
5. **18 to 29.7s.** The dino, ground and score turn white. RUNNING THROUGH YOURBRAND in a white pill, 2X SPEED, speed lines, the score racing, a jump every 0.7s with ticks: ✓ CHECKED, ✓ PLAN LANDED, ✓ SHIPPED.
6. **29.75s.** The dino runs into the chrome monogram. White flash into the end card.
7. **30 to 34s.** Black with a grey haze: the chrome monogram and wordmark with a white glow, "Keep going." "Never stop." on their words, the domain in grey, and a white dino still running along the bottom.

## When to use it
A pain that is a loop: retries, churn, rework. Wrong for anything that needs to show a real product.

## How it works
The game is drawn on a 216x150 canvas and scaled 5x with smoothing off, so every pixel is hard. Nothing is simulated: scroll is `speed * t`, and each cactus is placed where the scroll will be at the moment the voice says its word.

```js
const C1 = [[T.j1, 30], [T.j2, 34]].map(([t, h]) => ({ x: s1 * t + DX + 8, h }))
const jumpY = (t, at) => { const p = (t - at) / JUMP + 0.5; return p > 0 && p < 1 ? 46 * 4 * p * (1 - p) : 0 }
```

Captions are three words at a time from the word timings, the current word dark and the hot words (bad, everything, over, YourBrand) in pure white with a glow, the rest silver.

**Colour rule:** the game uses a dark UI theme: black page, `#161619` cards with a 16% white edge, `#a1a1aa` muted text, `#d4d4d8` silver, white ink, chrome logo with a white glow. No blue, pink or green. All type is a system display sans (SF Pro Display on Apple devices): bold from 34px, semibold below.

**Safe zone:** all type stays inside x 70 to 940 and y 250 to 1480 of 1080x1920, clear of the right-hand buttons and bottom caption that vertical short-video apps overlay. `CONFIG.safe` holds the box.

## Numbers that matter
| What | Value |
|---|---|
| Game canvas | 216x150 at 5x, ground at y 118 |
| Speed | 125 px/s, then 270 px/s |
| Jump | 0.56s, 46 px high |
| Voice pace | 2.6 words a second after a 1.18x speed-up |
| Colours | page `#000`, game ink `#8b8b93` then `#fff`, card `#161619`, muted `#a1a1aa`, silver `#d4d4d8` |

## Sound
Voice: a fast, conversational narrator, sped up about 1.18x. Save it as `code/voiceover.wav`. `code/recipe.py` adds square-wave jump blips, a thud per crash, a whoosh into the brand section, a rising tick per cleared cactus and a chord on the monogram.

## Adapt it
`CONFIG` at the top of `code/demo.html`: the tag words, the three fail reasons, the win ticks, the end lines, colours, speeds and the safe box. For a new script, generate the voice, get word times, replace `WORDS` and move the times in `T`.

## Files
`code/demo.html`, `code/recipe.py`, `code/brand-assets.js`, `media/poster.jpg`
