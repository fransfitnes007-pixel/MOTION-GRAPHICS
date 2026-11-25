# Shared pieces: build once, reuse everywhere

Pieces several accounts need. Before building one, check here. To claim one, write your session name under Owner and
set Status to `building`; when it works set `done`, add the path and one line on how to use it. One session keeps this
file (the lead or hub session); add finished pieces to `KIT/library` white-labelled (`KIT/engine/SKILL-SPEC.md`).

Rules for every piece: every frame is `render(t)`, a `CONFIG` block for words, colours and timings, no brand baked in
(the account passes it in), 1080x1920 at 30 fps. Never edit a library folder; copy it.

| # | Piece | Needed by | Start from | Owner | Status |
|---|---|---|---|---|---|
| 1 | Store CTA with live facts as parameters (search sequence and product page) | all | FORMATS.md section L, `tools/store_lookup.sh` | | open |
| 2 | Caption engine (variants in `KIT/docs/FACELESS-EXPLAINER-STYLES.md` section 3), reads word times or TTS alignment | all | `caption-word-reveal-highlight__ceil-word-count`, `bracket-caption-tag__fade-in` | | open |
| 3 | Neutral prompt box + chat step rows + result on a phone | all | `prompt-box-typed-send-zoom-out__eased-char-slice`, `ai-prompt-box-mode-pills__icon-grows-to-coloured-pill` | | open |
| 4 | Stick-figure rig (idle, point, shrug, hands-up, tap-phone, celebrate) + prop cards with a red-X overlay | | `skills/pictogram-reel` | | open |
| 5 | Glowing silhouette rig with a spotlight, mono palette | | | | open |
| 6 | Wireframe skeleton rig + 3D camera on a grid | | three.js | | open |
| 7 | Line-art diagram kit that redraws, with a persistent title | | `spotlight-vignette-joke__radial-gradient-mask` | | open |
| 8 | Home-screen widget kit with circle wipes between dark and light | | `dark-stage-circle-reveal__clip-path-circle-wipe`, `iris-transition__circle-mask-open-close` | | open |
| 9 | Card + live curve + 1/4-speed replay template | | | | open |
| 10 | Split-flap board + metro line | | `number-flip-reflection__split-flap-mirror-fade` | | open |
| 11 | Near-black stage + card kit with a before/after label flip | | | | open |
| 12 | Counters and odometers (count the problem, never money) | most | `mechanical-odometer__drum-carry-spring`, `odometer-number-roll__digit-column-translate` | | exists |
