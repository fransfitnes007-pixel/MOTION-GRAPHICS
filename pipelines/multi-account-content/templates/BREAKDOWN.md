# BREAKDOWN: <reference>, the style reference for <account>

Written <date>. Reference chosen by the owner: <url>. Read with eyes and scrapey (`KIT/docs/EYES-AND-SCRAPEY.md`) that
day: the public page in a browser (counts, with the date), the videos downloaded only where public and allowed, 10 fps
frames and 0.5 to 2 s contact sheets viewed one by one, ffmpeg cut detection and level stats. Nothing posted, liked or
followed. STYLE ONLY: copy the look, flow, pace, motion, type and sound, never the script, topic or character.
Keep this file and the downloaded media out of git (`research/` is ignored).

## 1. The videos studied
| # | url | views (date) | length | size / fps | look |
|---|---|---|---|---|---|

Which one to copy and why. Honest limit: one breakout is one data point; the topic may explain it as much as the look.

## 2. Measured
- Cuts: `ffmpeg -i v.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep pts_time` -> n per video.
- New idea every __ s; new small element every __ s; longest still moment __ s.
- Voice: words / speech seconds -> __ wpm; gaps (`silencedetect=noise=-40dB:d=0.3`); starts at __ s.
- Levels: mean __ dB, max __ dB (`volumedetect`). Music bed: yes / no / unknown (by level only; say so).

## 3. Beat sheet (time | on screen | caption | motion)
| t | on screen | caption | motion / change |
|---|---|---|---|

## 4. Camera and motion language
Camera, easing (overshoot %, frames), entrances and exits, characters, props, counters.

## 5. Typography
Caption font look, size at 1080 wide, case, band (y), words per chunk, said / unsaid / accent colours, stroke or plate.

## 6. Palette (sampled from full-size stills)
| Use | Hex |
|---|---|

## 7. Transitions
## 8. Sound (measured, not heard: confirm by ear)
## 9. Hook (first 1 to 2 s)
## 10. Ending / CTA
## 11. What makes it work (numbered, short)
## 12. How to rebuild it here
Library pieces to start from (`python3 KIT/engine/tools/find_skill.py <words>`), new pieces to build (add them to
`SHARED-PIECES.md`), and what to prove with stills before a full render.
