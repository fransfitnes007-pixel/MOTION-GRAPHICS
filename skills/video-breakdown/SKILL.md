---
name: video-breakdown
description: "Analyse a reference short-form video (Reel, TikTok, Short) to explain why it worked: hook, beat structure, cut rhythm, pacing, audio, text, and what to copy or avoid. Use when the user shares a video file or public link and wants to understand it or reproduce its style."
---

# Break down a reference video

Goal: turn one video into a reusable recipe, grounded in what is actually on screen, never in guesses.

## 1. Get it and prepare it
- Only public posts or files the user owns. No logins, no cookies, no private accounts.
- Run the helper (needs ffmpeg; yt-dlp for links):
```bash
bash scripts/breakdown_prep.sh "<file-or-public-url>" ./breakdown
```
It produces: `probe.txt` (size, fps, duration), `cuts.txt` (cut timestamps), `sheet.jpg` (contact sheet), `hook/` (first 3 s at 4 fps), `audio.wav`.
- Transcribe with the `transcribe` skill for the spoken words and timing.
- Look at the images (open `sheet.jpg` and `hook/`). Do not describe frames you have not seen.

## 2. Measure
| Measure | How |
|---|---|
| Length | `probe.txt` |
| Cuts and average shot length | count of `cuts.txt` lines vs duration |
| Time to first value | first frame or line that delivers something useful or surprising |
| Words per second | transcript word count / duration |
| Loudness and music | listen; note where music starts, drops, or ducks |
| Text on screen | frames with captions or titles: size, position, timing |
| Engagement numbers (if public) | views, likes, comments, shares, saves, with the date read |

Say plainly when a number cannot be read. Never fill one in.

## 3. Write the breakdown
```
HOOK (0-3 s): what is seen, what is said, what question it opens
BEATS: table of start, end, what happens, shot type, purpose
RHYTHM: cuts per 10 s, longest held shot, where pace speeds up or slows
AUDIO: voice style, music, sound effects, silences
TEXT/GRAPHICS: what appears, when, how it moves
LOOPS: where a new question opens, where each is paid off, how it ends
WHY IT WORKS: 3 to 5 reasons, each tied to a timestamp or a number
WHAT TO COPY: structural moves that transfer
WHAT NOT TO COPY: anything tied to the creator's face, voice, audience or brand
RECIPE: a beat template for the user's own video, with target timings
```

## 4. Judge with principles, not formulas
- Judge it by general attention mechanics: how fast value arrives, whether open questions get paid off, how specific the language is.
- Strong signals to look for: a concrete object or number in the hook, value landing within 5 to 10 s, a new question opened about two thirds in, visuals that change every 1 to 3 s.
- Save and share rates tend to say more about distribution than likes. Compare to the account's typical posts, not just absolute views.
- Do not clone. Extract the mechanism and apply it to the user's own idea, footage and voice. Do not reproduce another creator's script, footage or music.
