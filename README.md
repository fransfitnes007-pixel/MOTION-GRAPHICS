# motion-reel-kit

Make motion-graphics videos with Claude Code: Instagram Reels, TikToks, YouTube Shorts, X videos and long-form brand films, from a one-line prompt or a fully specified brief. White-label: put your brand in one file and every scene, logo, end card and template follows.

This repository is the main plugin: the single home for every motion-graphics skill, library piece, pipeline and rule. It is built to be run by agents, many at once: one session per video or per account, subagents building in parallel, a lead agent checking every frame before anything ships (see [`AGENTS.md`](AGENTS.md)).

[![motion-reel-kit showcase film](docs/media/showcase-preview.gif)](docs/media/showcase.mp4)

**▶ The 62-second showcase, with sound:**

https://github.com/user-attachments/assets/a635e51f-ae3a-49c3-8d3e-e540e5399195

The film was made with this kit: every frame is code, every cut is pinned to the voiceover's word times, the library pieces play inside it, and the music and sound effects are synthesised. Full quality: [`docs/media/showcase.mp4`](docs/media/showcase.mp4). Source: [`docs/showcase/`](docs/showcase/).

The film credits [growthkit.net](https://growthkit.net), whose team made the kit, and plays that team's own reels and films inside it. Everything else in the repository is white-label.

Second example: [`docs/media/example-reel.mp4`](docs/media/example-reel.mp4), a 70-second 9:16 pictogram reel made end to end (local voice, beats pinned to the words, 277 sound effects, App Store end card), still on the placeholder brand.

## What's new (1.1, 25 Nov 2026)

- **Multi-account content pipeline** ([`pipelines/multi-account-content/`](pipelines/multi-account-content/)): one agent session per account, a locked format per account, and a single `GO` that makes one finished vertical video per sub niche with parallel subagents, checks every contact sheet, and drops caption and video into the folder your posting system watches. Account pack template (FORMAT LOCK + log), an ElevenLabs helper that reads its key from the OS keychain, word-time, beat-fill, contact-sheet and check tools, and a safe drop-folder hand-off. New `/go` command and `multi-account-content` skill.
- **32 new library pieces** (390 in all): a mechanical odometer, a liquid-glass sidebar, three icon kits (88 animated, seekable SVG icons plus 36 static), an AI chat with a model menu, a dither donut, an isometric bar chart, a diagonal-wave KPI board, a holographic business card, an upload queue and more in `ui-components/`; and 13 motion graphics rebuilt by eye from the most-shared AI-made launch films: notification storm, wordmark squeeze into a pill, six-blade iris, paper-map grid unfold, habit-grid logo, two-phone sync arc, slot-roll stat stack, theme-toggle flood, UI state morph chain, log-zoom follow camera, unit dot grid, easing lanes board, Truchet wave.
- **Rules docs:** [`docs/MOTION-RULES.md`](docs/MOTION-RULES.md) (measured cut rates, lengths, colours, easing curves, build rules, motion blur, the 15-second vertical recipe) and [`docs/EYES-AND-SCRAPEY.md`](docs/EYES-AND-SCRAPEY.md) (watch frame by frame, screenshot every frame, read DOM/CSS/JS, scrape politely, rebuild, run until it matches; quotas and paywalls never shrink the output; site terms always win), with an `eyes-and-scrapey` skill.
- **Agents at once:** [`AGENTS.md`](AGENTS.md): one build folder per agent, directory locks for shared resources, render caps, cheaper models for mechanical steps, one index rebuild at the end, a leak scan before every commit.
- **Licence gate** written down: what was held back and why is in [`docs/LOCAL-LIBRARY-ONLY.md`](docs/LOCAL-LIBRARY-ONLY.md).

## What is inside

| Part | What you get |
|---|---|
| **18 Claude Code skills** | A to Z reel making, multi-account batches, viral-format recreation, the animation library, motion moves, showreels and launch films, eyes-and-scrapey reference reading, local voiceover, sound design, brand setup, short-form writing rules, transcription, ffmpeg recipes, AI image and video, UGC formats, video breakdowns, cloud voice |
| **6 slash commands** | `/reel`, `/go`, `/recreate`, `/motion`, `/voice`, `/rebrand` |
| **Animation library** | 390 pieces: 149 motion graphics, 177 UI components and micro-interactions, 44 dashboards, 20 sound recipes. Each is a runnable `demo.html` where every frame is `render(t)`, plus a guide with the exact numbers, timings and colours |
| **Multi-account content pipeline** | Many accounts, one kit: account packs with a FORMAT LOCK and log, a GO routine that builds one video per sub niche with parallel subagents, checks, and a drop-folder hand-off to any posting system |
| **Motion rules** | Measured cut rates, lengths, palettes and easing curves from the most-shared AI-made motion videos, build rules, motion blur, and a 15-second vertical recipe made only of library pieces |
| **Pictogram reel pipeline** | A code-drawn, 20-beat faceless parable reel with beats pinned to the voiceover, synthesised sound effects and an App Store end card |
| **Local voice pipeline** | Fast, natural voiceovers on Apple Silicon (Qwen3-TTS, Kokoro) at a set pace and pitch, line-by-line recording, voice design from a description |
| **Reference analysis** | Measure any video you want to copy: cuts, words per minute, pauses, voice pitch, and the clicks, swishes, hits and music bed under the voice |
| **Interaction pack** | 20 app-grade micro-interactions written from scratch for video: comma-jump number input, card burn, 3D card flip, border comet pulse, hold to commit, OTP success fill, split-flap counter, readiness gauge, flag ring shuffle, card-ready glint and more |
| **Motion moves** | A named vocabulary of 45+ motion techniques (timing, type, transitions, camera, texture, data, sound) with the exact easing and spring numbers, each tied to a demo |
| **Showreel and launch-film playbook** | Beat structures, timing tokens, palette and type rules learned from the most-shared AI-made showreels and launch films, with a storyboard template |
| **Palettes** | 10 named signature looks (including `arizona-sunset` and the film's `sunset-ink`) and the colours of every library piece |
| **Formats and prompts** | 24 video formats written up beat by beat with what went wrong and how it was fixed, and a short and a detailed prompt for 23 of them |

## Install

You need [Claude Code](https://claude.com/claude-code), Node 18+, Python 3.9+ and ffmpeg. Google Chrome is used for rendering (or set `BROWSER_CHANNEL=chromium` after `npx playwright install chromium`).

**As a plugin** (skills and commands load in every project):
```
/plugin marketplace add fransfitnes007-pixel/MOTION-GRAPHICS
/plugin install motion-reel-kit@motion-reel-kit
```

**Or clone it** and open Claude Code inside the folder:
```bash
git clone https://github.com/fransfitnes007-pixel/MOTION-GRAPHICS.git motion-reel-kit
cd motion-reel-kit
cd engine && npm install && cd ..
pip install -r requirements.txt && playwright install chromium
claude
```

Optional, for free local voices on a Mac with Apple Silicon (about 5 GB of models):
```bash
bash pipelines/voice/setup.sh
```

## Make it yours (two minutes)

1. Edit `brand.config.json`: name, domain, handle, colours, and your App Store listing details and icon.
2. Run:
```bash
python3 engine/tools/apply_brand.py
python3 engine/tools/build_index.py
```
Every `YourBrand`, `yourbrand.com` and `@yourbrand` in the library and pipelines becomes yours. A liquid-chrome monogram and wordmark are rendered from your name, and the pictogram reel's App Store card takes your listing. Run it again any time you change the config. In Claude Code you can just type `/rebrand` instead.

## Use it

Simple:
```
/reel a 40 second reel about why most side projects never launch, ending on our app
```
```
/recreate reference/viral.mp4 same format, about our product
```
```
/motion dino sunset, our colours, 30 seconds
```
```
/go my-account
```

Detailed:
```
Make a 60 s 9:16 reel at 30 fps. Hook in 2 s with no brand name. Script below, one line per beat.
Voice m_smooth at 5.0 syllables a second, recorded line by line. Pin every beat to the voice's word times.
Look: arizona-sunset palette, pixel style, type inside x 70-1010 / y 250-1480. Sound: click on every tag,
swish on every cut, a thud on the slam words, a boom on the end card. End card: our App Store listing.
Deliver tall and wide, a contact sheet, and the numbers you measured.
```

More in [`prompts/PROMPTS.md`](prompts/PROMPTS.md): a short and a detailed prompt for 23 of the 24 formats in [`docs/FORMATS.md`](docs/FORMATS.md).

## How the videos are made

Every scene is a web page whose whole picture is a pure function of time, `render(t)`. A headless browser steps through it frame by frame and ffmpeg encodes the frames with the audio. That makes renders exact and repeatable, lets one scene compose at 1080x1920 and 1920x1080, and lets beats be pinned to the voiceover's word times instead of guessed.

```
idea or reference ─▶ script ─▶ voiceover ─▶ word times ─▶ beats pinned to words ─▶ frames ─▶ sound on logged events ─▶ mix ─▶ MP4
```

Try one now:
```bash
open library/LIBRARY.html                                   # browse all 390 pieces, live
node engine/tools/render_demo.cjs video \
  library/motion-graphics/dino-runner-arizona-sunset__pixel-dithered-sky-mesa-parallax/code/demo.html \
  out/dino.mp4 1080 1920
```

### Pictogram reel quick start

The black-and-white parable reel in `pipelines/pictogram-reel` needs a Python with Playwright (`pip install -r requirements.txt && playwright install chromium`):
```bash
cd pipelines/pictogram-reel
python3 build/render.py none stills/ --stills 2,50,69        # look at three frames, no audio needed
../voice/.venv/bin/python ../voice/reel_vo.py m_smooth script.txt vo/voiceover.wav --f0 130-165
python3 tools/make_cues.py vo/voiceover.wav cues.map build/cues.js
python3 build/events.py build/events.json
python3 build/sfx.py build/events.json vo/voiceover.wav vo/mix.wav
python3 build/render.py vo/mix.wav out.mp4
```

## Many agents at once

The kit is made to be run by several agents in parallel, on one machine or several:

- **One session per job.** A session per video, or per account in the multi-account pipeline. Each builds in its own folder; the library stays read-only during builds (copy a piece, change its `CONFIG`).
- **Subagents for the mechanical work.** On `GO`, the lead session writes the scripts, then sends one subagent per video (on a cheaper model) to fill beats, render stills, mix and render. Each returns paths to its stills and contact sheets, length and loudness; the lead looks at every sheet before anything ships.
- **Locks, not timers.** Anything only one agent can use (a shared browser tab, a web app, a device) is guarded by `mkdir <dir>/.<name>.lock`. Waiting agents do other work; nothing wakes a model on a timer.
- **Render caps.** 2 or 3 full video renders per machine at once; stills are cheap.
- **One writer for the index.** New library pieces are added one agent at a time, then `build_index.py` runs once.

Details in [`AGENTS.md`](AGENTS.md).

## Repository map

```
.claude-plugin/        plugin.json and marketplace.json (installable plugin)
brand.config.json      your brand: the only file you have to edit
AGENTS.md              how agents work here, several at once
commands/              /reel /go /recreate /motion /voice /rebrand
skills/                the 18 skills Claude loads
library/               390 animation, UI, dashboard and sound pieces; LIBRARY.html, INDEX.md, catalog.json
engine/                render, find, verify, poster, index, rebrand and chrome-logo tools; the demo template and spec
pipelines/
  multi-account-content/  account packs, the GO routine playbook, tts/account-info/drop helpers, beat and check tools
  pictogram-reel/      the code-drawn reel renderer, example script, cues, sound effects
  voice/               local TTS: voice.py, reel_vo.py, design.py, pitch check, setup
  reference-analysis/  measure a reference video
palettes/              PALETTES.md, palettes.json, index.html swatches
docs/FORMATS.md        24 formats, beat by beat, with lessons
docs/MOTION-RULES.md   measured timings, easing, cut rates, build rules, the 15-second recipe
docs/EYES-AND-SCRAPEY.md  how every reference is read and rebuilt
docs/LOCAL-LIBRARY-ONLY.md  pieces held back by the licence gate, and why
prompts/PROMPTS.md     ready-to-paste prompts
```

## Skills

| Skill | Use it for |
|---|---|
| `reel-maker` | The whole job, idea to exported file |
| `multi-account-content` | Many accounts: FORMAT LOCK per account, GO = one video per sub niche with parallel subagents, checks, drop-folder hand-off |
| `eyes-and-scrapey` | Read any reference before rebuilding it: frame-by-frame screenshots, DOM/CSS/JS, polite scraping, terms first |
| `recreate-viral-format` | "Make one like this": measure a reference and map a new story onto its beats |
| `motion-library` | Find and adapt a scene, transition, UI animation, dashboard or sound |
| `pictogram-reel` | The black-and-white faceless parable format |
| `motion-moves` | Named motion techniques with their numbers: squash and stretch, overshoot, scramble decode, whip pan, iris… |
| `showreel-and-launch-film` | Plan and build a 15 to 60 s showreel, launch film or product demo |
| `short-form-principles` | Hooks, scripts and honesty rules |
| `voiceover-local` | Free local narration with set pace and pitch |
| `voiceover-elevenlabs` | Cloud narration with your own key |
| `sound-design` | Clicks, swishes, thuds, booms, beds and the final mix |
| `brand-setup` | White-label everything, apply palettes |
| `transcribe` | Word timestamps with faster-whisper |
| `media-processing` | ffmpeg recipes: crop, captions, loudness, export |
| `video-breakdown` | Why a video worked, as a reusable recipe |
| `ugc-video-playbook` | Creator-style formats and scripts |
| `ai-image-video` | Generated images and footage, local first, your own keys |

## Adding your own pieces

Follow [`engine/SKILL-SPEC.md`](engine/SKILL-SPEC.md), then:
```bash
node engine/tools/make_posters.cjs <slug>
python3 engine/tools/build_index.py
node engine/tools/verify_library.cjs <slug>      # runs the demo and checks every frame is a pure function of time
```

## Keys and privacy

The render tools start Chrome with `--allow-file-access-from-files` so a demo can load its own fonts and scripts from disk. They only ever open the kit's local demo files.


Nothing in the kit calls a paid service unless you ask for it. Cloud tools read keys from environment variables (`ELEVENLABS_API_KEY`, `FAL_KEY` and similar) or, for the multi-account voice helper, the OS keychain, and never from files. Account packs, voice aliases and builds in the multi-account pipeline are git-ignored. Reference videos, recordings and renders go in git-ignored folders (`reference/`, `out/`, `vo/`). See `.gitignore`.

## Troubleshooting

- **Render says Chrome is missing:** install Google Chrome, or `npx playwright install chromium` and `export BROWSER_CHANNEL=chromium`.
- **Fonts look different from the posters:** some pieces use the system display font (SF Pro on Apple devices). Other systems fall back to Helvetica or Arial.
- **The voice sounds childlike or slow:** measure it with `python3 pipelines/voice/tools/f0.py out.wav`; see `skills/voiceover-local`.
- **A piece still says YourBrand:** run `python3 engine/tools/apply_brand.py` after editing `brand.config.json`.

## Licence

MIT for the kit's own code and docs. 108 pieces are credited recreations of MIT and Apache-licensed 21st.dev components, 6 follow MIT/ISC code or icon sets (notices in `LICENSES/`), and 13 are original code recreating motion seen in public videos, credited to their creators (see each piece's Credit section). Components with no licence shown are not published ([`docs/LOCAL-LIBRARY-ONLY.md`](docs/LOCAL-LIBRARY-ONLY.md)). Bundled fonts and three.js keep their own licences: see [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Use your own brand assets and real facts on end cards.
