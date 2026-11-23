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

## Motion vocabulary and showreel research

- The `motion-moves` skill uses the technique vocabulary that [motionvideo.xyz](https://motionvideo.xyz) catalogues as "Moves"; every explanation and demo here is written from scratch. motionvideo.xyz also publishes an MIT agent skill (github.com/motionvideohq/motionvideo.xyz) and a public catalogue API, which were read for structure only.
- The `showreel-and-launch-film` skill was informed by the public catalogues of AI-made motion videos on motionvideo.xyz and revid.ai's ranked wall. Nothing from either is copied.

## The showcase film

`docs/media/showcase.mp4` and its preview credit growthkit.net, whose team made this kit, and show that team's own reels and films. Those clips and the G mark are theirs; everything else in the repository stays white-label.
