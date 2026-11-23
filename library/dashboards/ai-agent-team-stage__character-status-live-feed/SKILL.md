---
name: ai-agent-team-stage-character-status-live-feed
description: "Eight small animated agents on a grid stage that wake one after another, bob, show a status label and drop a check badge, beside a live feed that narrates what each did. Use it for any 'a team of AI agents is working on it' moment."
---

# AI agent team stage

**Code name:** Character states and live narration feed.

## What you see
A header, "Watch your team work", with a progress bar and 0/8 counter at top right. The stage is a dark panel with a violet radial glow and a faint 32px grid, and a one-pixel violet scan line sweeping down it while anything is running. Eight characters (diamond, rounded square, ellipse, blob, capsule, flame, cog, hexagon) each in its own colour sit in four columns. They start dimmed with a grey "Waiting" label. One by one an agent brightens, floats and tilts, two aura rings pulse outwards, its label becomes "Working..." with a pulsing dot, and a speech bubble above the footer says what it is doing. After about a second it settles, a round check badge pops in on a spring, the label reads "Done · 4s" and the progress bar advances. One agent (Ember) fails: it shakes, turns red and shows a cross. The feed on the right gets a row at each start and finish, sliding in 10px from the right.

## When to use it
Automation and AI products: showing several agents without showing code. It tells the story of a handoff chain. Keep it at 8 or fewer characters; each needs its own colour. A single agent is better served by the thinking-orb style loaders.

## How it works
Each character is procedural SVG in a 100 x 100 box scaled to `size * 0.78`. State drives everything: PENDING body opacity 0.5; RUNNING floats `y [0,-7,0]` with `rotate [0,1.5,0,-1.5,0]` over 1.6s easeInOut, plus two rings `scale [1,1.35]`, `opacity [0.6,0]` over 1.4s easeOut (the second delayed 0.7s); COMPLETED shows the check badge, `scale 0 to 1` on `spring {stiffness 400, damping 18}`; FAILED shakes `x [0,-3,3,-2,0]` three times and swaps to red `239,68,68`. Idle float is `y [0,-4,0]` over `4 + (shape % 3)` seconds. The eyes blink with `scaleY [1,1,0.1,1,1]` at times `[0,0.45,0.5,0.55,1]` over 4s then a 1.5s pause.

Body fill is a radial gradient from the agent colour at 0.95 to 0.55 opacity; the stroke is the colour at 0.9. The cog's teeth rotate once per 6s while running.

Keyframe arrays are evaluated per segment with the easeInOut curve; `ease()` in the demo does exactly that. The scan line is `y [0,460,0]` over 6s while active. Feed rows are `motion.div initial {opacity:0,x:10}`. The progress pill is a 112px by 8px track with a `linear-gradient(90deg,#8B5CF6,#10B981)` fill.

## Numbers that matter
- Agent colours (r,g,b): 139,92,246; 16,185,129; 245,158,11; 236,72,153; 59,130,246; 239,68,68; 20,184,166; 99,102,241.
- Character size 92px idle, 104px active.
- Status label: 10px, tinted pill at 12% of the colour; Working uses `167,139,250`.
- Check badge 28px; spring 400 / 18.
- Demo timing: agent n starts at 1.0 + 1.25n seconds and works 1.05s.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- The `AG` array: name, codename, colour, thinking line, finish line.
- `T0`, `STEP`, `RUN` set the pacing; `statusAt` can make any agent fail.
- `SHAPES` holds the eight silhouettes; replace paths for your own mascots.
- The feed width and the stage height (520px).

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the agent names and lines are the app's own mascots with new narration text. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.
