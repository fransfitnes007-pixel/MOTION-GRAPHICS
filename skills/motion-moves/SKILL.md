---
name: motion-moves
description: "A named vocabulary of motion-design moves (timing, type, transitions, UI, vector, generative, camera, texture, data, sound), each with what it looks like, when it works, the exact formula in the kit's helpers and the library piece that demonstrates it. Use when animating and the request names a technique (squash and stretch, whip pan, iris, text scramble, count-up) or when you need to pick the right move for a moment."
---

# Motion moves

Apply a move by name: find it below, copy the formula, change the numbers. Every formula is written in the helpers of `engine/templates/demo-template.html`, plus two one-liners that most library demos add next to them.

```js
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x))
const seg = (t, a, b) => clamp((t - a) / (b - a))                 // 0..1 between times a and b
const eo  = x => 1 - Math.pow(1 - x, 3)                           // ease out
const eio = x => x < .5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2 // ease in out
const spring = (x, k = 7, f = 11) => x >= 1 ? 1 : x <= 0 ? 0 : 1 - Math.exp(-k * x) * Math.cos(f * x)
const back = (x, s = 1.9) => { const c3 = s + 1; return 1 + c3 * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2) }   // out with overshoot
const pr = (t, a, d) => seg(t, a, a + d)                          // progress of a move that starts at a and lasts d seconds
```
Also in the template: `eo5` (quintic out), `ei` (cubic in), `lerp(a, b, x)`. `spring` overshoots by about `e^(-k*pi/f)` (k 7, f 11 gives 13%; k 6.5, f 8 gives 8%) and starts with speed `k`. `back(x, s)` overshoots about `s * 4%` (1.9 gives about 9%). Every frame is a pure function of `t`: no timers, no unseeded random; for variation use `hsh(a, b) = fract(sin(a*127.1 + b*311.7) * 43758.5453)`.

Piece names below are folders under `~/motion-reel-kit/library/<category>/`. Pieces marked "(new)" are the library's demonstration for that move.

## Timing

**Squash and stretch.** An object stretches along its direction of travel when fast and flattens on impact, keeping its volume. Use for anything that should feel soft or alive (a ball, a button, a logo landing); avoid for rigid objects. Formula: flight `sy = 1 + .42 * clamp(|v| / vmax); sx = 1 / Math.sqrt(sy)`; contact `sq = .4 * Math.sin(Math.PI * u)` for `u = pr(t, tHit, .14)`, then `sy = 1 - sq`. Pin the bottom edge to the floor while scaling. Demo: `motion-graphics/squash-and-stretch-ball-drop__scale-xy-impact` (new); hover version in `ui-components/message-bubble-heart-icon__hover-heart-squash-spring`.

**Anticipation.** A small move opposite to the main action, so the viewer sees it coming. Use before any fast or large move; keep it 0.25 to 0.5s. Formula: pull `s = -D * eio(pr(t, a, .8))` with D about 20% of the travel, squash along the axis to `1 - .22 * pull`, hold 0.3s with a tremble `3 * Math.sin(t * 95)`, then release. Demo: `motion-graphics/anticipation-then-launch__pull-back-release` (new).

**Overshoot and settle.** The value goes past its target, then comes back. Use for arrivals of cards, chips and badges. Formula: `x = back(pr(t, a, .5), 1.9)` for about 9%, or `spring(pr(t, a, .8), 7, 11)` for 13% with a visible wobble. Demo: `motion-graphics/check-chip-trio-settle__spring-scale-row`.

**Follow-through and overlapping action.** Parts lag behind the main body and keep going after it stops. Use for hanging things, tails, labels on cards. Formula: child value = parent function sampled later and damped: `child = parent(t - .12) ` plus `A * Math.exp(-5 * dt) * Math.sin(14 * dt)` after the stop, `dt = t - tStop`. Demo: `ui-components/hanging-polaroids-on-a-string__snap-slide-pendulum-lag`.

**Spring animation.** Motion defined by stiffness and damping, not duration. Use for UI that responds to touch, drops and pops. Formula: `x = spring(seg(t, a, a + .9), k, f)`: k 5 to 8 sets how fast, f 8 to 14 sets how bouncy (f 8 with k 7 is soft, f 14 with k 5 wobbles). Demo: `motion-graphics/phone-drop-in__spring-fall`.

**Staggered timing.** The same move repeats on a list with a fixed offset. Use for lists, grids, letters, cards; offsets of 0.04 to 0.14s read as one gesture, over 0.2s reads as separate events. Formula: `p_i = eo(pr(t, t0 + i * .08, .6))`. Demo: `motion-graphics/notification-card-stack__staggered-spring-rise`.

**Slow in and slow out.** Start and end gently, move fastest in the middle. Use for anything that moves between two resting places (camera, panels, counters). Formula: `x = eio(pr(t, a, d))`; stronger: `x < .5 ? 16*x**5 : 1 - Math.pow(-2*x + 2, 5) / 2` (quintic). Demo: `motion-graphics/setup-step-progress-pill__eio-fill-counter`.

**Ease-out entrance.** New things arrive fast and decelerate; they never accelerate in. Use for every entrance; reverse (`ei`) for exits. Formula: `y = (1 - eo5(pr(t, a, .8))) * 60`, opacity `eo(pr(t, a, .4))`. Demo: `motion-graphics/browser-window-slide-up__eo5-rise`.

**Arcs.** Natural motion curves; straight lines look mechanical. Use for flying chips, thrown objects, cursor paths. Formula: `x = lerp(x0, x1, e); y = lerp(y0, y1, e) - H * Math.sin(Math.PI * e)` with `e = eio(pr(t, a, .9))` and H 12% of the distance. Demo: `motion-graphics/inquiry-chip-fly-to-inbox__lerp-path-badge-pop`.

**Moving hold.** A held shot never freezes: a slow drift keeps it alive. Use on every hold longer than 0.5s. Formula: `scale = 1 + .04 * pr(t, a, d)` or a periodic drift `A * Math.sin(2*Math.PI*t/DUR)` so loops stay seamless, A 10 to 30px. Demo: `motion-graphics/graded-photo-backdrop-slow-zoom__sepia-grade-cover-fit`.

**Secondary action.** A smaller motion that supports the main one: a glow pulse as a card lands, a ring after a slam. Use to add richness without changing the main read; start it 0.05 to 0.15s after the main move. Formula: `ring = pr(t, tHit + .05, .6); r = R * (1 + 1.8 * eo(ring)); opacity = (1 - ring) * .6`. Demo: `motion-graphics/bouncing-badge-and-done-word__damped-sine-bounce`.

**Animating on twos.** Hold each pose for two frames (12 fps drawn on 24 or 30), for a hand-made, snappy look. Use for characters, stop-motion tones, retro UI. Formula: `const tq = Math.floor(t * 12) / 12; render with tq instead of t`. No dedicated piece yet; the stepped pixel motion in `motion-graphics/dino-runner-game-over-then-endless-run__pixel-canvas-scripted-jumps` shows the feel.

## Type

**Staggered letter reveal.** Letters rise or pop in one after another. Use for short titles and end-card names. Formula: per letter `p = back(pr(t, a + i * .035, .5))`, `translateY((1 - p) * .5em)`, opacity `eo(pr(t, a + i * .035, .25))`. Demo: `motion-graphics/logo-domain-end-card__per-character-rise-back-pop`.

**Word by word reveal.** Words appear in the rhythm of speech. Use for captions and voice-led sentences; start each word 0.05s before it is spoken. Formula: `p = eo(pr(t, wordTime[i], .35))`, blur `(1 - p) * 10px`, rise `(1 - p) * 24px`. Demo: `motion-graphics/word-by-word-sentence-reveal__blur-rise-stagger`.

**Typewriter text.** Characters appear one at a time with a caret. Use for prompts, URLs, commands. Formula: `n = Math.floor(seg(t, a, b) * text.length); shown = text.slice(0, n)`; caret on when `Math.floor(t * 2) % 2 === 0`. Add jitter per character with `hsh(i, 3) * .04` for a human rhythm. Demo: `motion-graphics/url-pill-typewriter-caret__substring-blink`.

**Text scramble decode.** Random glyphs flicker, then lock into the real letters left to right. Use for tech, data and security tones. Formula: glyph `GL[Math.floor(hsh(i, Math.floor(t * 30)) * GL.length)]` until `settle_i = .65 + i * .062 + hsh(i, 7) * .4`; fixed-width cells so nothing shifts. Demo: `motion-graphics/text-scramble-decode__random-glyphs-settle` (new).

**Line mask text reveal.** Each line rises out of its own clipped box. Use as the clean default headline entrance. Formula: `.ln { overflow: hidden }`, child `translateY((1 - eo5(pr(t, .35 + i * .14, .95))) * 108%)`, small tilt `rotate((1 - p) * 5deg)`. Demos: `motion-graphics/line-mask-text-reveal__clip-rise-per-line` (new), `motion-graphics/masked-line-rise-headline__overflow-clip-translate`.

**Variable font weight animation.** The weight axis moves continuously, so letters swell and thin. Use for calm, ambient titles; needs a variable font. Formula: `weight_i = 650 + 250 * Math.sin(2*Math.PI*t/3 - i * .55)`; set `font-weight` per letter span. Demo: `motion-graphics/variable-weight-breathing-headline__font-weight-sine` (new).

**Rotating word swap.** One word in a fixed phrase flips to the next. Use for taglines that list benefits or audiences. Formula: out `p = eio(pr(ph, .78 + j * .045, .42))`, `rotateX(-90 * p)`, `translateY(-.45em * p)`; in the same with `eo`, 0.12s later, from `+90`; pill width `lerp(wA, wB, eio(pr(ph, .88, .4)))`. Demo: `motion-graphics/rotating-word-swap__flip-up-staggered` (new).

**Scale punch headline.** A word slams in oversize and settles, usually with a short shake. Use for one-word beats and hooks. Formula: `s = 1 + 2.2 * (1 - spring(pr(t, a, .6), 7, 11))` (starts 3.2x, lands at 1) then shake `6 * Math.exp(-9 * dt) * Math.sin(dt * 60)`. Demo: `motion-graphics/giant-black-slam-word__spring-scale-shake`.

## Transitions

**Match cut.** Two scenes joined by a shared shape or position, so the eye does not register the cut. Use between a click and its result. Formula: expand a circle from the click point, `r = rmax * eo5(pr(t, a, .5))`, filled with the next scene's colour, and place the next scene's key object where the circle began. Demo: `motion-graphics/click-ripple-fill-match-cut__expanding-circle`.

**Whip pan transition.** A fast sideways camera move with horizontal-only blur; the cut hides at peak blur. Use between two energetic shots. Formula: `x = W * eio5(pr(t, a, .72))`, speed `v = |dx/dt| / W`, blur `120 * clamp(v / 6) ** 1.1` as an SVG `feGaussianBlur stdDeviation="b 0"`, plus `scale(1 + .04 * sp)`. Demos: `motion-graphics/whip-pan-transition__directional-blur-cut` (new), `motion-graphics/whip-pan-directional-blur__svg-gaussian-axis`.

**Wipe transition.** A shape sweeps across and the next scene appears behind it. Use for chapter changes and fast list cuts. Formula: `x = -100 + 200 * eio(pr(t, a, .6))` as `translateX(x%)` for a curtain whose leading edge covers at `x = 0`; swap the scene at that moment. Demo: `motion-graphics/solid-curtain-sweep-wipe__translatex-percent`.

**Iris transition.** A circle closes onto a subject and opens again on the next scene. Use for film-style scene changes and open/close frames. Formula: `clip-path: circle(r at x y)`, `r = rmax(c) * (1 - eio5(pr(t, a, .8)))` closing with the centre sliding to the subject by `eio`, `r = rmax(P) * eo5(pr(t, b, 1))` opening. Demos: `motion-graphics/iris-transition__circle-mask-open-close` (new), `motion-graphics/dark-stage-circle-reveal__clip-path-circle-wipe`.

## UI

**Shared-element morph.** One element becomes another by animating its box instead of cross-fading. Use for selection, expand and reorder. Formula: interpolate `left, top, width, height, radius` with `e = spring(pr(t, a, .6), 7, 9)`; fade content in the last 40%. Demo: `ui-components/filter-chip-grid__shared-pill-layout-reflow`.

**Magnetic hover.** Items near the cursor grow and lift with a smooth falloff. Use for docks, tile rows, nav. Formula: `d = Math.abs(x - cx)`; `scale = 1 + .6 * Math.exp(-(d * d) / (2 * 90 * 90))`; follow the pointer with `spring` so it never snaps. Demo: `ui-components/gradient-tile-magnetic-dock__radius-scale-lift-idle-wave`.

**Bottom-sheet spring.** A panel rises from the bottom edge, overshoots slightly and settles; dismiss is a fast `ei`. Use for composers, menus, confirmations. Formula: `y = (1 - spring(pr(t, a, .7), 6, 9)) * sheetH`; scrim opacity `.5 * eo(pr(t, a, .3))`. Demo: `ui-components/agent-dock-composer__spring-height-expand-status-swap`.

**Press and release.** A button sinks on press and springs back, with a fill that follows. Use for every tap in a demo. Formula: `s = 1 - .06 * eo(pr(t, a, .08)) + .06 * (spring(pr(t, a + .1, .4), 7, 12))`, brightness `1 - .1 * press`. Demo: `ui-components/hold-to-commit-button__press-fill-progress-release`.

## Vector

**Stroke draw-on.** A line draws itself along its path. Use for ticks, arrows, underlines, route lines. Formula: path with `pathLength="1"`, `stroke-dasharray="1"`, `stroke-dashoffset = 1 - eo(pr(t, a, .6))`. Demos: `motion-graphics/handwritten-annotation__clip-wipe-arrow-draw`, `motion-graphics/ui-callout-leader-line__lerp-line-draw-label`.

**Shape morph.** One shape turns into another by interpolating matching points or rotating through a shared form. Use for icon state changes (plus to tick, play to pause). Formula: same number of points, `p_i = lerp(a_i, b_i, eio(pr(t, a, .35)))`; add `rotate(90 * e)` to hide the change. Demo: `ui-components/plus-to-tick-button__rotate-morph-check`.

**Mask reveal.** A clip-path shape grows to show the content beneath. Use for logos, images, panels. Formula: `clip-path: inset(0 ${(1 - eo5(pr(t, a, .7))) * 100}% 0 0)` for a wipe, or `circle(r at x y)` for a radial. Demo: `motion-graphics/wordmark-clip-path-reveal__inset-wipe-shrink-away`.

**Offset path follow.** An element rides a curve with its rotation following the tangent. Use for planes, cursors, comets. Formula: sample the path at `e = eio(pr(t, a, 1.2))`, angle `atan2(dy, dx)` from the difference of two samples 0.01 apart. Demo: `ui-components/glowing-border-light-chasing-around-frame__soft-comet-along-rectangle-perimeter`.

## Generative

**Noise field drift.** Soft shapes or particles drift through a slow noise field. Use for backgrounds and mood. Formula: positions `x_i = x0 + A * Math.sin(2*Math.PI*t/DUR + hsh(i, 1) * 6.28)`, `y_i` with a second phase, A 40 to 120px, blur 80 to 110px; whole periods per `DUR` keep loops closed. Demo: `motion-graphics/pastel-drifting-blobs-background__sine-drift-blur-110`; noise-eaten edge in `ui-components/card-burn-particle-dissolve__noise-edge-ember-sparks`.

**Particle burst.** Particles leave a point with random speed, then gravity and fade take over. Use for confirmation, celebration, impact. Formula: per particle `a = hsh(i, 1) * 6.28; v = 300 + 500 * hsh(i, 2)`, `x = x0 + Math.cos(a) * v * dt`, `y = y0 + Math.sin(a) * v * dt + 900 * dt * dt / 2`, `opacity = 1 - seg(dt, .3, 1.1)`. Demos: `motion-graphics/confetti-burst__radial-gravity-fade`, `motion-graphics/logo-slam-shake-spark-burst__scale-shake-radial-sparks`.

**Seeded scatter.** Items land at random-looking but repeatable positions. Use for photo walls, tile grids, confetti fields. Formula: `x_i = hsh(i, 1) * W; y_i = hsh(i, 2) * H; delay_i = hsh(i, 3) * .6`; fly in with `spring`. Same seed gives the same frame every time. Demo: `motion-graphics/creator-tile-grid-scatter__staggered-spring-fly`.

**Fibonacci distribution.** Evenly spread points on a disc or sphere with no grid look. Use for dot globes, starfields, sunflower patterns. Formula: `a_i = i * 2.39996; r_i = R * Math.sqrt(i / N)`; `x = cx + r * Math.cos(a)`. Demo: `ui-components/dotted-night-globe-with-pulsing-pins__fibonacci-land-dots-rotate`.

## Camera

**Push-in.** The camera moves toward a subject while the frame holds still. Use to focus on a detail or to build tension on a hold. Formula: `scale = 1 + .35 * eio(pr(t, a, 1.6))` with `transform-origin` at the subject. Demo: `motion-graphics/violet-ai-dashboard-score-ring-push-in__counting-ring-glow-brain`.

**Whip pan with blur.** See Transitions. The camera version is the same formula applied to a world layer. Demo: `motion-graphics/whip-pan-transition__directional-blur-cut` (new).

**Parallax rack.** Layers move at different speeds as the camera moves, giving depth. Use for photo walls and layered scenes. Formula: layer `n` moves `camX * (0.3 + n * 0.35)` with `camX = A * eio(pr(t, a, 2))`; far layers also blurrier and smaller. Demo: `ui-components/folded-photo-wall-unfurls-flat__3d-tilt-to-flat-column-parallax`.

**Focal zoom.** Zoom to a point of interest with its own transform origin, then back out. Use to read a UI detail. Formula: `s = 1 + 1.6 * eio(pr(t, a, .8)) * (1 - eio(pr(t, b, .8)))`, `transform-origin` at the target in layer pixels. Demo: `motion-graphics/browser-window-focal-camera-zoom__focal-point-transform`.

## Texture

**Film grain.** Fine moving noise over the frame. Use to unify layers and hide banding in gradients. Formula: SVG `feTurbulence` at `baseFrequency .8`, offset the layer by `(hsh(f, 1) * 40, hsh(f, 2) * 40)` with `f = Math.floor(t * 24)`, opacity .06 to .12. Demo: `motion-graphics/grain-vignette-fade-to-black__svg-noise-overlay`.

**Chromatic split.** Red and blue copies offset a few pixels, strongest on impact. Use on glitches, slams, scene hits. Formula: duplicate the element with `mix-blend-mode: screen`, tinted red and cyan, offset `±6 * Math.exp(-12 * dt)` px along x. No exact piece yet; the slice-and-blur glitch in `motion-graphics/logo-glitch-slice-blur-reveal__clip-path-inset-slices` is the nearest.

**Glow bloom.** A soft halo around bright things, pulsing with the action. Use for neon, rings, active states. Formula: stacked `box-shadow` or `text-shadow` of 20px and 80px in the accent at 35 to 60%, strength `0.6 + .4 * Math.sin(2*Math.PI*t/3)`. Demo: `dashboards/progress-ring__gradient-dash-offset-glow`.

**Shine sweep.** A bright diagonal band crosses a surface once. Use for logos, buttons, cards. Formula: `background-position = lerp(-100%, 200%, eio(pr(t, a, .9)))` on a gradient `transparent 40%, rgba(255,255,255,.6) 50%, transparent 60%`, masked to the shape. Demo: `motion-graphics/logo-shine-sweep__masked-gradient-position`.

## Data

**Count-up with snap.** A number counts up quickly, then snaps to its short form with a small pop. Use for big metrics. Formula: `n = Math.round(target * eo5(pr(t, a, 1.2)))` formatted with `toLocaleString`; at the end `scale = 1 + .08 * (1 - spring(pr(t, a + 1.2, .5), 7, 12))`. Demo: `motion-graphics/big-number-brand-counter__count-up-snap-short-form`.

**Bar grow.** Bars rise from the baseline, staggered, with the biggest last. Use for comparisons. Formula: `h_i = value_i * eo5(pr(t, a + i * .08, .8))`; bottom pinned; value label fades in at 80%. Demo: `ui-components/before-after-results-card__bar-grow-compare-sweep`.

**Line draw with scrub.** A line draws left to right, a cursor follows the tip and reads values. Use for trends. Formula: `n = Math.floor(seg(t, a, b) * pts.length)` points sliced into the path, or `clip-path: inset(0 ${100 - 100 * e}% 0 0)`; tooltip at the tip. Demos: `dashboards/analytics-bento-line-and-funnel__path-draw-day-scrub`, `motion-graphics/line-chart-grow__point-slice-path`.

**Ring fill.** A circular gauge fills to a value with a glowing head. Use for scores and progress. Formula: `stroke-dashoffset = C * (1 - value * eo5(pr(t, a, 1.2)))`, number `Math.round(value * 100 * e)`. Demo: `dashboards/progress-ring__gradient-dash-offset-glow`.

## Sound

**Hit on cut.** A short low thump exactly on a scene cut or slam. Use on every hard cut and every slam; put the transient on the frame. Recipe: sine pitched down from 120 to 45 Hz over 0.12s, with a noise tick, tail 0.25s, 0 to -6 dB. Demo: `sound/riser-into-slam__filtered-noise-sweep` (the slam end).

**Whoosh on move.** Filtered noise whose cutoff sweeps with the motion. Use on whips, wipes, big moves; start 0.05 to 0.18s before the visible move so it leads the eye. Recipe: noise through a low-pass sweeping 300 to 4000 Hz over the move length, volume peaking at the speed peak. Demo: `sound/whoosh-on-cut__lowpassed-noise-sweep`.

**Tick per item.** A tiny click for each item in a stagger or counter. Use for lists, counters, decoding text; vary pitch a little per item. Recipe: 8 to 15ms sine at 1800 to 2400 Hz, pitch `+ i * 20` Hz, -18 dB. Demo: `sound/keypress-ticks-under-counter__short-sine-tick-run`.

**Pop on reveal.** A soft pitched pop as each word or card lands. Use for word-by-word reveals and badges. Recipe: sine dropping from 700 to 320 Hz over 0.08s, fast attack, -12 dB. Demo: `sound/pop-on-word-reveal__pitch-dropping-sine`.

## Sources

motionvideo.xyz publishes a Moves catalogue (the names and posters are public, the write-ups are paid) and an MIT-licensed agent skill at github.com/motionvideohq/motionvideo.xyz. The move names in the Timing, Type and Transitions sections follow that vocabulary. Nothing from either is copied here: every explanation, formula and number is written from animation fundamentals and the kit's own code.
