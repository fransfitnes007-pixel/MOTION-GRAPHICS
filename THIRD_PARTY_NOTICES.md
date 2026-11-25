# Third-party notices

The kit's own code and docs are MIT (see `LICENSE`). These parts come from others and keep their own licences:

| What | Where | Licence |
|---|---|---|
| Playfair Display, Rye, Great Vibes fonts | `library/**/code/fonts/` | SIL Open Font License 1.1 (`LICENSES/*-OFL.txt`) |
| Special Elite font | `library/**/code/fonts/` | Apache License 2.0 (`LICENSES/SpecialElite-Apache-2.0.txt`) |
| three.js (bundled build) | `library/**/code/three.global.js` | MIT (`LICENSES/three.js-MIT.txt`) |
| Lucide icon paths (inline SVG in some UI and dashboard pieces) | `library/**/code/demo.html` | ISC License, Copyright (c) Lucide Contributors (https://lucide.dev/license) |
| playwright-core | `engine/` (installed by npm, not committed) | Apache License 2.0 |

Tools the kit calls but does not include, each under its own licence: ffmpeg, Playwright, faster-whisper (MIT), mlx-audio (MIT), Qwen3-TTS and Kokoro model weights (see each model card on Hugging Face), yt-dlp (Unlicense), NumPy, SciPy, Pillow.

The dino-runner pieces are inspired by the offline dinosaur game in Chrome; every pixel is drawn new. App Store-style end cards imitate the store's layout for a listing you own: use your own app's real name, icon and figures.

Recommended reading that is not bundled: [blader/humanizer](https://github.com/blader/humanizer) (MIT) for editing captions and scripts.

The 12-piece interaction pack recreates common iOS micro-interaction patterns. [60fps.design](https://60fps.design), a catalogue of iOS app animations, was used to choose which patterns to build. None of its code, videos or images are included; every piece here is written from scratch.

The showcase film's voiceover was generated with ElevenLabs.

## Recreations credited to 21st.dev authors

95 library pieces are original recreations, written from the public preview, of components published on [21st.dev](https://21st.dev) under the MIT or Apache-2.0 licence. Each piece's `meta.json` has a `credit` block (author, link, licence) and its `SKILL.md` ends with a Credit section. Components whose pages state no licence were not recreated.

## Added 25 Nov 2026: 19 UI components and 13 motion graphics

Every piece below keeps its credit in its own `meta.json` (`credit`) and `SKILL.md` (Credit section).

**MIT / ISC sources** (code-level notices in `LICENSES/third-party-components-MIT.txt` and `LICENSES/Lucide-ISC.txt`):

| Piece | Source | Author | Licence |
|---|---|---|---|
| `mechanical-odometer__drum-carry-spring` | 21st.dev Mechanical Odometer | cipriantitire | MIT (formulas followed; numerals font Big Shoulders, SIL OFL 1.1, not bundled) |
| `liquid-glass-expandable-sidebar__flip-expand-glass-rail` | 21st.dev Liquid Glass Expandable Sidebar | Troy Lorents / Automate Flows | MIT |
| `animated-and-static-icon-pack__line-md-smil-plus-lucide` | line-md (animated) and Lucide (static) | Vjacheslav Trushkin; Lucide Contributors | MIT; ISC |
| `spring-draw-wobble-icon-kit__seekable-css-keyframes-svg` | Lucide Animated | pqoqubbw (dmytro on 21st.dev); Lucide Contributors | MIT; ISC |
| `gentle-wobble-icon-kit__seekable-css-keyframes-svg` | AnimateIcons / Lucide | Avijit Dey; Lucide Contributors | MIT; ISC |
| `icon-in-context-scenes__chips-tab-bar-notification-9x16` | original scenes using the Lucide Animated kit | pqoqubbw; Lucide Contributors | MIT; ISC |

**Recreated by eye from the public preview of MIT components on 21st.dev** (original code; nothing copied):
`animated-number` (ikascom), `trading-price-ticker-card` (shadcnspace, number-ticker-07), `product-tour-card-with-live-pictures`
(aadixc0de), `holographic-business-card` (aakashmehra; photo and details replaced with placeholders), `pendant-lamp-rail`
(dhxwhy; lamps drawn in SVG), `stacked-cell-kpi-board` (kedhareswer), `isometric-line-bars` (abhishek-mallick),
`dither-donut-chart` (su2491251), `dot-matrix-revenue-card` (aloksivastava1025), `chat-with-model-menu` (ephraimduncan),
`ask-bar-greeting-composer` (ham7a311), `upload-queue-triage` (ham7a311), `progress-button` (joseestevez520).

**Recreated by eye from public motion videos** (watched in the browser; no video, frame, audio or prompt text is
included; every demo is original code with placeholder copy). Videos belong to their creators:
| Piece | Creator (post on X) |
|---|---|
| `easing-lanes-comparison-board`, `truchet-arc-tile-field-radial-recolor` | @stephanlivera |
| `wordmark-squeeze-into-period-pill`, `iris-blade-aperture-photo-open`, `photo-tile-grid-paper-map-unfold` | @twoclipping |
| `ui-state-morph-chain` | @twoclipping, @thednyx |
| `habit-tile-grid-diagonal-pop-logo`, `two-phone-cloud-sync-arc` | @sebastianroehl |
| `notification-storm-then-one-card` | @dhruvalgolakiya |
| `stat-stack-slot-roll-landing-ring` | @robj3d3 |
| `theme-toggle-dark-flood` | @likithareddy |
| `ball-guided-ui-world-camera` | @rossaxbt |
| `unit-dot-grid-fill-count` | @jesscaroline7 |
The videos were found through the public galleries at revid.ai and motionvideo.xyz; the post links are in each `meta.json`.

**Held back (local library only, not in this repository):**
- 13 recreations of 21st.dev components whose pages show no licence (an AI chat stream, a toast stack, a stacked toast
  pile, an alert card list, a bar chart, an upload progress ring, two onboarding checklists, a seven-segment ticker, a
  currency ticker, an icon pill bar, a state icon grid, sequential chat bubbles). Same rule as before: no licence shown,
  not published.
- 1 pattern studied on 60fps.design (an orbit-to-pinwheel intro). Its terms of use (21 Nov 2026) forbid building a
  reference library from it, so nothing derived from it after that date is added here.

## Motion vocabulary and showreel research

- The `motion-moves` skill uses the technique vocabulary that [motionvideo.xyz](https://motionvideo.xyz) catalogues as "Moves"; every explanation and demo here is written from scratch. motionvideo.xyz also publishes an MIT agent skill (github.com/motionvideohq/motionvideo.xyz) and a public catalogue API, which were read for structure only.
- The `showreel-and-launch-film` skill was informed by the public catalogues of AI-made motion videos on motionvideo.xyz and revid.ai's ranked wall. Nothing from either is copied.

## The showcase film

`docs/media/showcase.mp4` and its preview show the authoring team's own reels and films. Those clips and any marks in them are theirs; everything else in the repository stays white-label.
