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
