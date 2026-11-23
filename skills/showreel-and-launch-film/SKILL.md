---
name: showreel-and-launch-film
description: "Plan and build a 15 to 60 second showreel, launch film or product demo with the kit: beat structures that recur in popular AI-made reels, timing tokens per genre, camera and transition vocabulary, a three-colour palette rule, a one-family type ladder, sound rules, and a fill-in storyboard template. Use when the user asks for a showreel, a launch video, a product demo or an 'apple-keynote style' film."
---

# Showreel and launch film

`KIT` is the repository root, two folders up from this skill. This skill is the planning layer: it decides the beats, the clock, the palette and the sound. The pieces themselves come from `library/` (find them with `motion-library`), the order of work from `reel-maker`, the voice from `voiceover-local` or `voiceover-elevenlabs`.

## What the popular ones have in common

Studied from the public catalogue at motionvideo.xyz (639 videos, with prompts, tags and palettes) and the ranked launch-week wall at revid.ai (64 videos, with lengths and categories). Six preview clips were read as contact sheets for beat structure. Numbers below are counted from that data, not remembered.

- **Length.** On the ranked wall 17 of 64 are exactly 15 s, the most common length by far; 47 of 64 are 40 s or shorter; the median is 29 s. The three most-shared are 15 s, 2:22 and 32 s. Plan 15 s for a showreel, 30 s for a launch film or demo, 45 to 60 s only when there is a story to tell.
- **Canvas.** 63 % of the catalogue is 1920x1080; vertical 1080x1920 is only 7 %, square 6 %. Make wide first, then re-compose tall rather than cropping.
- **Content.** Kinetic type appears in 45 % of the videos, product UI in 33 %, music in 24 %, particles in 16 %. A reel is mostly type moving, then a screen being used.
- **Palette.** Every video has 1 to 5 extracted colours; 61 % lead with a near-black (`#000000` is the single most common value, 113 times), 31 % lead with a near-white. Of videos with a saturated colour, the accent hue is red-orange (0 to 60 degrees) about half the time, blue (180 to 270 degrees) over a quarter, pink most of the rest. Almost none use more than one accent at a time.
- **Stacks named in prompts.** Plain HTML/CSS/canvas is the default (HTML 87 prompts, canvas 52, CSS 41, SVG 31); three.js and WebGL 39, Remotion 20, GSAP 8. This kit's `render(t)` canvas and DOM approach is the common case, not the odd one.
- **Common prompt shape.** Two kinds win. The one-liner: "a 15-second motion graphics video that shows what an incredible motion designer you are, like a showreel for a résumé" (131 prompts mention a showreel). And the long brief with three blocks: inputs to ask for, a direction paragraph (look, type, banned list) and a structure paragraph (a BPM and "something happens on every beat"). The long brief produces the cleaner films; copy its three blocks.
- **Recurring rules inside the long briefs.** 120 BPM (28 prompts); a banned list (no crossfades, no particles, no holds over 1 s); "one continuous take" where every scene is made out of the last (14 prompts); one font family (Inter 46 mentions, Geist 26); a cursor that really clicks (32).

## Beat structures

All times are for a 30 s film and scale with length. A beat is one idea on screen, one sentence long.

### A. Showreel (15 s, 6 to 9 beats)
| Beat | Time | What |
|---|---|---|
| Hook | 0.0 to 1.2 | One object or one word, centred, already moving. No logo. |
| Slam | 1.2 to 3.0 | The name or claim, huge, on a hit. |
| Range | 3.0 to 12.0 | 4 to 6 quick demonstrations of skill: type, shape, UI, depth, light. 1.5 to 2.0 s each. Each is a different medium but the same palette. |
| Climax | 12.0 to 13.5 | The densest frame: everything at once or a hard flash. |
| End card | 13.5 to 15.0 | Name, one line, handle. Holds 1.2 s of stillness. |

### B. Launch film (30 s, 8 to 12 beats)
| Beat | Time | What |
|---|---|---|
| Hook | 0.0 to 2.0 | The problem as a single line of type or a single broken UI state. |
| Reveal | 2.0 to 5.0 | Product name or app icon arrives on a hit; the palette locks. |
| Feature 1 to 4 | 5.0 to 24.0 | 3 to 5 beats of 3.5 to 5 s, each a real interaction (cursor click, drag, type, toggle) that visibly changes the UI. One feature per beat. |
| Proof | 24.0 to 27.0 | One number, one quote or one before/after. |
| End card | 27.0 to 30.0 | Wordmark, one line, call to action, URL. Holds 2 s. |

### C. Product demo (30 to 60 s, 5 to 7 beats)
Open on the finished result (2 s), cut to the empty state, then show the 3 to 5 steps that get there, each as a tight camera move into the UI region being used. Close on the result again, now with the call to action. The camera, not cuts, links the steps: push in, hold, pan to the next region, rack focus.

### D. Loop (10 to 20 s)
One shape that becomes the next scene, ends where it began. No end card; the last frame is the first frame. Use for social autoplay.

## Timing tokens

Use these as constants; change them per genre, not per beat.

| Token | Showreel | Launch film | Product demo |
|---|---|---|---|
| Beat length (BPM 120 = 0.5 s) | 0.5 s | 0.5 s | 0.5 s |
| Cut cadence | every 1.0 to 1.5 s (2 to 3 beats) | every 2.0 to 3.0 s | every 4 to 6 s |
| Longest allowed hold | 1.0 s | 1.5 s (end card 2.0 s) | 2.5 s |
| Entry ease | 0.30 to 0.45 s, `eo5` | 0.45 to 0.6 s, `eo5` or spring | 0.6 to 0.9 s, `eio` |
| Spring (`spring(x, k, f)`) | k 7, f 11 (punchy) | k 6, f 9 | k 5, f 7 (calm) |
| Overlap between scenes | 0.10 s (cut on the hit) | 0.20 to 0.30 s | 0.35 to 0.50 s |
| Stagger between siblings | 0.06 s | 0.08 to 0.10 s | 0.12 s |
| Flash frame on a hard cut | 2 frames white at 30 fps (0.067 s) | none or 1 frame | none |
| Typing speed | not used | 14 to 18 chars/s | 12 to 16 chars/s |

Rules that held across the most-shared videos:
- Something moves on every beat. A beat with nothing moving is a dead beat; cut it or fill it.
- Nothing enters at rest and nothing leaves at rest: it arrives with speed and leaves with acceleration (`ei`).
- The final element of each beat lands on the downbeat, not before it. Build the clock from the music grid, then place picture to it.
- Cut on motion: end scene A mid-move and start scene B already moving the same direction.

## Camera and transition vocabulary

| Move | Numbers | Use |
|---|---|---|
| Push in | scale 1.0 to 1.18 over a beat, `eio` | Focus on one control. |
| Tight push | scale 1.0 to 2.4 onto a button, last 0.6 s | Land on the click. |
| Pan | translate 20 to 35 % of the frame over 0.8 s | Move to the next UI region. |
| Rack focus | blur 0 to 14 px on the layer leaving, 14 px to 0 on the one arriving, 0.5 s | Depth between layers of a screen. |
| Fly-through | camera z moves 1 panel spacing per 0.6 s, panels fade as they pass | Reveal a stack of screens. |
| Shake | 8 to 14 px, decays in 0.35 s, only on impacts | Slam of a headline. |
| Slam | scale 1.35 to 1.0 in 0.18 s with 3 % overshoot | Title on a hit. |
| Hard cut | 0 frames, optional white flash | On a drum hit. |
| Match cut | shape of A becomes shape of B (circle to dot, bar to line) | The continuous-take style. |
| Iris / mask wipe | circle or bar mask grows over 0.4 s, `eo5` | A scene change without a crossfade. |
| Whip | 600 px of horizontal motion blur, 0.2 s | Between two flat posters. |

Avoid: crossfades longer than 0.15 s, 3D page flips, spinning logos, bouncing ease on UI. They appear in the banned lists of the better briefs.

## Palette: ink, paper, one accent

Three colours, always, and they are named by role, not by hue.

- **Ink** is the darkest: `#0b0b10` to `#0e0e12` (never pure black on a UI, pure `#000` only for full-bleed type).
- **Paper** is the lightest: `#f2f2f4` or warm `#ede6d5`. Text on ink is paper at 100 %; secondary text is paper at 55 %.
- **Accent** is one saturated colour with luminance between 35 and 60 %, for example `#ed4938` (orange-red), `#2f6bff` (blue) or `#ff2e97` (pink).

Where the accent is allowed: the one word you want read, the primary button, the progress or cursor, the flash on the final beat. Where it is not: backgrounds of more than one beat, body text, borders, every icon. Budget: the accent covers at most 12 % of the pixels in a beat, except in one full-bleed poster beat per film, where it covers 100 % (flat accent, ink type).

Light and dark are two modes, not a gradient between them: pick one for the hook and flip once for the reveal. Flat colour beats gradients on type; gradients are for metal, glass and light only.

## Type: one family, two weights

- One family: the system stack (`-apple-system, 'SF Pro Display', system-ui`) or Inter or Geist if bundled. A serif italic is allowed only as a second voice for one word per film (serif is named in only 10 of 639 prompts).
- Two weights: 800 to 900 for display, 500 for labels and captions. No third weight.
- Size ladder in 1920x1080 (multiply by `K` for tall): 300 to 420 px giant word, 150 to 200 px headline, 72 px sub-headline, 36 px body, 22 px caption with 0.14 to 0.3 em tracking in capitals.
- Display words may be cropped by the frame edge on a poster beat; nothing else may be.
- Letter-spacing: display `-0.03 em`, caption `+0.2 em`. Line height 0.9 for display, 1.3 for body.
- A reading rule: three words or fewer per beat at display size, eight words at body size, and each held for at least `0.25 s + 0.06 s per word`.

## Sound

- **Hits on cuts.** One short transient (a 60 to 120 ms low thump or snap, see `sound-design`) on every hard cut and every slam, placed 20 to 40 ms before the picture change so it feels locked.
- **Whoosh** 0.15 to 0.30 s before any big move, peaking on arrival.
- **Bed ducking.** The music sits at -14 LUFS short-term under nothing and ducks 4 to 6 dB for 0.25 s on every hit (sidechain: attack 5 ms, release 250 ms). Under a voice it ducks 8 dB.
- **Drop.** If the track has a drop, the reveal is on it. A quiet breakdown goes under the feature beats; the full track returns for the end card.
- **Silence.** One beat of 0.3 to 0.5 s of silence before the reveal is worth more than any riser. Spend it once.
- **UI sounds.** Click 40 ms, toggle 60 ms, toast 120 ms, all quiet (-24 dB under the bed) and only on real interactions.

## Build recipe with the kit

1. Fill the storyboard below. Write the BPM and the beat count first.
2. For each beat pick a library piece (`motion-library`) or write a `render(t)` scene; give each a start time on the beat grid (`start = n * 60 / BPM`).
3. Set `window.DUR` per scene to its beat length plus its overlap; compose scenes in one master `render(t)` that calls each scene's draw with `t - start`.
4. Render wide first, then tall with `?w=1080&h=1920`; check every beat in both.
5. Build the sound track on the same grid; render, then mix.
6. Check against the list: dead beats, holds over the token, more than one accent, more than two weights, a crossfade.

## Storyboard template

Copy this block and fill it in. One row per beat.

```
FILM
  Title / purpose:
  Genre (showreel | launch | demo | loop):      Length (s):     BPM:     Beats:
  Platforms and shapes (wide / tall / square):
  Palette:  ink #______   paper #______   accent #______   (accent used on: ______)
  Type:     family ______   display weight ___   label weight ___
  Music:    track / feel ______   drop at ___ s   breakdown ___ to ___ s
  Voice:    none | script file ______

BEATS
  #  | start | len | what is on screen (one sentence) | the one thing that moves | camera | transition out | sound hit
  1  | 0.0   |     | HOOK:                           |                         |        |                |
  2  |       |     | REVEAL:                         |                         |        |                |
  3  |       |     | FEATURE 1 (real interaction):   |                         |        |                |
  4  |       |     | FEATURE 2:                      |                         |        |                |
  5  |       |     | FEATURE 3:                      |                         |        |                |
  6  |       |     | PROOF:                          |                         |        |                |
  7  |       |     | END CARD (holds 1.5 to 2 s):    |                         |        |                |

CHECKS
  [ ] something moves on every beat          [ ] no hold longer than the token
  [ ] accent only on the one word / button   [ ] one family, two weights
  [ ] every cut has a hit                    [ ] tall version composes
  [ ] end card readable for 1.5 s            [ ] copy has no real brand names unless the user supplied them
```

## Sources

Studied for structure and numbers; nothing was copied.
- motionvideo.xyz: the public catalogue API (639 videos with titles, prompts, content tags, models, extracted colours) and its MIT-licensed agent skill.
- revid.ai: the ranked launch-week wall of 64 videos (likes, lengths, categories: launch films, product demos, showreels, ads, explainers).
- Six preview clips from the catalogue were looked at as contact sheets to learn beat order only, then deleted from the working folder.
