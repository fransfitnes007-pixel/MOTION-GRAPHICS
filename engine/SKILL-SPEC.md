# Skill folder spec

Every skill in this library follows this exactly, so any one can be grabbed and used on its own.

## Where it goes

| Folder | What belongs there |
|---|---|
| `motion-graphics/` | Scenes and effects from video work: kinetic type, transitions, cards, counters, end cards |
| `ui-components/` | Animated or distinctive interface pieces from real apps and sites |
| `dashboards/` | Dashboard screens, charts, stat tiles, data panels |
| `sound/` | Sound effects, synth recipes, music beds, voice treatment |

## Name

`<visual-name>__<code-name>` in lowercase kebab-case, joined by two underscores.

- **visual-name**: what you would call it after seeing it once. `led-dot-rainbow-word`, `giant-black-slam-word`, `notification-card-stack`.
- **code-name**: the technique that makes it work. `conic-gradient-dot-mask`, `spring-scale-overshoot`, `staggered-spring-slide`.

Good: `led-dot-rainbow-word__conic-gradient-dot-mask`. Bad: `scene-4__render-branch`, `acme-intro__animation`. No client or product names in the folder name; it describes the effect so it can be reused for anyone.

## Contents

```
<visual-name>__<code-name>/
├── SKILL.md              how it looks, when to use it, how it works, how to adapt it
├── meta.json             machine-readable facts for the library index
├── code/
│   ├── demo.html         self-contained, runnable; opens in a browser and loops
│   └── source-excerpt.*  the original code, verbatim, with the source path at the top
└── media/
    ├── clip-wide.mp4     the real moment from the real film, or a render of demo.html
    ├── clip-tall.mp4     when a tall version exists
    ├── sound.m4a         the audio of that moment, when the source has sound
    └── poster.jpg        one good frame
```

## demo.html rules

Start from `engine/demo-template.html`. Keep its helpers and only write between the SKILL markers.

1. Every frame is a pure function of time: `window.render(t)`. No `setTimeout`, no CSS transitions, no CSS keyframes, no `Math.random()` without a fixed seed. Calling `render(1.5)` twice must draw the same frame.
2. Set `window.DUR` to the loop length, 2 to 8 seconds usually.
3. Self-contained. No network requests, no CDN, no imports. Replace client photos and logos with CSS, SVG or gradient placeholders. Use the template's system font stack unless the font is the point of the effect; if it is, copy the font into `code/fonts/` and load it by relative path.
4. Support wide and tall: use `W`, `H`, `CX`, `CY`, `K`, `TALL`, so `?w=1080&h=1920` still composes properly.
5. Copy text in demos is neutral placeholder copy, unless the wording is the effect.
6. Reproduce the source faithfully: same easing, same timings, same colours, same proportions. It is a working extraction of the effect, not a new design inspired by it. Copy formulas from the source.

For React components with framer-motion or Recharts: `code/source-excerpt.tsx` is the verbatim component. `demo.html` still follows the rules above: rebuild the look with `render(t)` so it can be rendered to video and run with no build step. Map framer-motion spring and transition values across as closely as you can.

## Media rules

- Motion graphics with a finished film: cut the real moment. `engine/tools/cut_clip.sh <source.mp4> <start> <end> <skill-folder> <wide|tall>`. Include half a second of lead-in when a moment is very short, so it reads.
- Anything without a finished video: render the demo. `node engine/tools/render_demo.cjs video <demo.html> <skill>/media/clip-wide.mp4 1920 1080`. UI components may use a size that suits them, such as 1280x800.
- Then create the poster if there is none: `ffmpeg -ss <t> -i media/clip-wide.mp4 -frames:v 1 -q:v 3 -vf "scale='min(960,iw)':-2" media/poster.jpg`. `ffmpeg -i file` prints duration and streams.
- **Look at the poster.** Read `media/poster.jpg` as an image. The default time can land on the neighbouring scene or a blank frame. Pass an explicit `poster-sec` to `cut_clip.sh` and delete the old poster to replace it.
- **Check the cut.** Scene comments in source are often approximate. Confirm with stills at the start and end of the range that the clip shows the effect.
- **Compare demo to source.** Render a still of `demo.html` with `render_demo.cjs still` and read it next to a frame from the real clip. Fix anything that does not match. A loop exposes flaws a split-second film moment hides, such as a rotating layer revealing its edges; fix those in the demo and say so in SKILL.md under How it works.
- **Run the checker** on every skill you finish: `node engine/tools/verify_library.cjs <slug>`.
- Source files are read-only. Never modify, move or delete anything outside this library.
- Footage from client films stays out of a shared or public copy of the library: ship rendered demo clips there instead, and keep `sources` paths out of public `meta.json`.

## meta.json

```json
{
  "slug": "led-dot-rainbow-word__conic-gradient-dot-mask",
  "visual_name": "LED dot rainbow word",
  "code_name": "Conic gradient dot mask",
  "category": "motion-graphics",
  "summary": "One sentence on what you see.",
  "aliases": ["rainbow word", "led word", "dot word"],
  "tags": ["kinetic-type", "dark", "transition"],
  "tech": ["vanilla-js", "css-mask"],
  "duration_sec": 3,
  "has_sound": true,
  "demo_kind": "exact-formula",
  "sources": [
    { "project": "Product film v3", "file": "relative/path/index.html", "lines": "57, 80-83, 375-380", "film": "relative/path/film.mp4", "time": [7.42, 8.3] }
  ],
  "variants_elsewhere": []
}
```

`tags` come from: `kinetic-type`, `transition`, `card`, `counter`, `cursor`, `phone`, `browser-window`, `background`, `end-card`, `cta`, `logo`, `chart`, `stat-tile`, `table`, `nav`, `hero`, `form`, `modal`, `loader`, `3d`, `scroll`, `hover`, `carousel`, `marquee`, `dark`, `light`, `sfx`, `music`, `voice`, plus any others that clearly help.

`demo_kind`: `exact-formula` when the formulas are copied from source, `rebuilt` when React or library behaviour was recreated in `render(t)`, `rebuilt-by-eye` when it was recreated from watching a video with no source available, `original-build` when it was made new for this library.

`aliases`: 3 to 6 short words or phrases you would actually say for this thing, in lowercase. `find_skill.py` searches these first, so write them as plain speech: what it is ("folder"), what it does ("fan out"), what it looks like ("polaroid").

## SKILL.md

Must start with frontmatter so Claude can load it as a real skill:

```markdown
---
name: <slug with __ replaced by ->
description: <one or two sentences: what it looks like and when to reach for it>
---

# <Visual name>

**Code name:** <technique>. **From:** <project>, <timestamp or component>.

## What you see
Frame-by-frame description, plain language, with the timing in seconds.

## When to use it
What moment in a video or which kind of screen this suits, and when it would be wrong.

## How it works
The technique, with the key formula or code in a short block. The part someone would otherwise have to rediscover.

## Numbers that matter
Timings, easing, sizes, colours, as a table or short list.

## Sound
What it sounds like and what to pair it with. Say "silent" if nothing applies.

## Adapt it
The three or four values to change to reuse it for another brand or message.

## Files
Paths to the demo, clip and source.
```

Write plainly. Describe real numbers from the code, not impressions. Do not call anything stunning, seamless or premium.

## Granularity

One skill is one thing you would ask for by name. A scene that contains a card burst, a stamped word and a cursor click is three skills if each is independently reusable. A short combination that only works as a unit stays one skill. If two moments look the same with different words, that is one skill; list the second under `sources`.

Check `ls` of the category folder before creating a skill. If another skill already covers the same look, add yours to its `sources` instead of making a new folder. If it is a real variation, make it and name the sibling in `variants_elsewhere`.

## Where each shape is posted

`media/clip-wide.mp4` (1920x1080) suits X and YouTube. `media/clip-tall.mp4` (1080x1920) suits Instagram Reels, Facebook, TikTok, YouTube Shorts and Snapchat. A reel made for posting gets both files.
