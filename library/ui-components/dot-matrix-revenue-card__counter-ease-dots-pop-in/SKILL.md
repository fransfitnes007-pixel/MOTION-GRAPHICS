---
name: dot-matrix-revenue-card-counter-ease-dots-pop-in
description: A minimal revenue card: a big +326% counter easing up over a chart made of tiny dots that pop in column by column. Use for a growth number reveal: revenue, followers, signups.
---

# Dot-matrix revenue card

**Code name:** Counter ease, dots pop in.

## What you see
Light grey page, a soft white card with a small caps label REVENUE, a big thin +326% and three tabs top right (DAILY WEEKLY MONTHLY, the active one black). Underneath, a chart of 4px dots stacked in 49 columns fades out toward the right. From 0.25s the number counts 0 to 326 over one second (fast start, slow end) while each column pops in left to right, each dot bouncing up from below with a little overshoot; the first 23 columns are pale grey (last month), the rest dark (this month). At 2.7s a hover dims all other columns to a quarter and enlarges the hovered column's dots, with a small black tooltip over it. At 4.6s WEEKLY: the number counts down to +84% and a new set of columns pops; DAILY at 7.8s counts to +12%. 12s loop.

## When to use it
A single growth number that should feel earned: revenue up, followers up, saves up. The dot field is quiet, so it works as a calm second beat after a louder hook. Month view is the strongest at 9:16.

## How it works
Pure CSS in the original, so every number below is copied from its stylesheet.

```css
.dot { width:4px; height:4px; border-radius:50%; opacity:0;
       animation: popIn .4s cubic-bezier(0.34,1.56,0.64,1) forwards }
@keyframes popIn { 0% {opacity:0; transform:translateY(10px) scale(0)} 100% {opacity:1; transform:none} }
.graph-col { display:flex; flex-direction:column-reverse; gap:5px }   /* dots stack upward */
.graph-container:hover .graph-col { opacity:.25 }   .graph-col:hover { opacity:1 }
.graph-col:hover .dot { transform:scale(1.4) }
```

Delays: column i starts at `i x 0.02s`, dot j in the column at `+ j x 0.04s`. Columns are 4px wide on a 9px pitch (49 columns is 441px in a 396px container, so a right-edge mask fades them out). Dot counts for all three tabs are in `CONFIG.periods`. The counter eases for 1.0s on an ease-out cubic from the previous value to the new one (measured: 84, 156, 210, 250, 279, 299, 311, 319 at 0.1s steps). The overshoot curve is solved in the demo, so `render(t)` is repeatable.

The tooltip's wording did not appear in the preview, so the text ("Jun 28  $1,274") is a placeholder.

## Numbers that matter
| | |
|---|---|
| Dot | 4px, 5px gap; column pitch 9px |
| Pop | 0.4s cubic-bezier(0.34,1.56,0.64,1), from translateY(10px) scale(0) |
| Stagger | 0.02s per column, 0.04s per dot |
| Counter | 1.0s ease-out cubic |
| Hover | others 25%, dots x1.4 |
| Colours | dots #c4c4c4 / #555; page #e5e5e5; card #f9f9f9 |

## Sound
A tiny tick per column as the dots pop; one soft chime when the counter lands.

## Adapt it
- `CONFIG.periods` (value, labels, dot counts, how many pale columns), `plan`, `hovers`, `label`. Dot counts above 13 need a taller chart (raise `MAXD`).

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Dot Graph Card (cue-dot-graph-card)" by aloksivastava1025 (https://21st.dev/@aloksivastava1025/components/cue-dot-graph-card), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.
