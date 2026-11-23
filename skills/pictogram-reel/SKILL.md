---
name: pictogram-reel
description: "Build a faceless black-and-white pictogram parable reel (white stick-figure people on a dashed ground, capsule tags, counters, a glow, beats pinned to the voiceover, App Store end card) with the kit's canvas renderer. Use for explainer or \"why X happens\" story reels, or when the user wants the pictogram, parable or black-and-white faceless style."
---

# Pictogram parable reel

`KIT` = the repository root. The pipeline is `KIT/pipelines/pictogram-reel/`; its `README.md` has the full walk-through. A complete 20-beat example (script, cue map, beats) ships with it.

## The look
Pure black with a faint dot grid; one white pictogram person (round head, rounded body, no face) with a small marker so the hero is recognisable in a crowd; grey people for everyone else; a thin dashed ground line; white capsule tags with black caps text (never more than two at once); a soft radial glow behind the one thing the voice is talking about; counters that tick, text that types, lines that draw. Colour appears only on the end card (an App Store listing in dark mode with the brand's real icon). Palette: `pictogram-mono` in `KIT/palettes/`.

## Steps
1. **Script**: one paragraph per line in `script.txt`. Story shape: a relatable person, the common belief, years later nothing changed, why (two things play by opposite rules), the cost, the turn (the product makes the expensive step cheap), the contrast (someone with a worse idea wins), the payoff line.
2. **Voice**: `KIT/pipelines/voice/reel_vo.py m_smooth script.txt vo/voiceover.wav --f0 130-165` (a copy of the script with names spelled for pronunciation).
3. **Cues**: write `cues.map` (`cue_name: the words where it lands`), then `python3 tools/make_cues.py vo/voiceover.wav cues.map build/cues.js`.
4. **Beats**: `build/beats.js` has one function per beat (`b1`...`b20`) drawing with the kit in `build/kit.js` (`person`, `pill`, `bubble`, `bulb`, `phone`, `priceTag`, `card`, `noteCard`, `clock`, `rocket`, `dice`, `appStore`...). Times inside a beat use `at(i, C.cue)` so they move with the voice. Change words and drawings per beat; keep the motion rules (fade/slide in 0.24 s, out 0.13 s, slow push-in).
5. **Preview**: open `build/reel.html#play` in a browser. Stills: `python3 build/render.py x stills/ --stills 1.5,10,30` and look at them.
6. **Sound**: `python3 build/events.py build/events.json` then `python3 build/sfx.py build/events.json vo/voiceover.wav vo/mix.wav`.
7. **Render**: `python3 build/render.py vo/mix.wav out.mp4` (1080x1920, 30 fps, about 40 s per minute of video on a laptop).
8. **Check**: contact sheet, black-frame scan, end card shows the right icon and facts, handle correct.

The App Store card reads `BRAND.store` from `build/assets/brand.js`, which `apply_brand.py` writes from `brand.config.json`. Use real listing facts only.
