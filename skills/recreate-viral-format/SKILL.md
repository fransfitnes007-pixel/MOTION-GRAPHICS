---
name: recreate-viral-format
description: "Recreate a viral video's format for a different product or story, as close to the original's editing, pacing, structure and sound as possible, with new copy and tags. Use when the user shares a reference reel or TikTok and says \"make one like this\", \"same format\", \"copy this style\" or \"recreate this for our brand\"."
---

# Recreate a viral format

`KIT` = the repository root, two folders up from this skill. The output is a plan the user can approve, then the built video. Copy the format, never the content: new story, new words, new drawings, no footage or audio from the original.

## 1. Get the reference
- A local file: use it. A public link: `yt-dlp <url>`. If the platform blocks the download without a login, ask the user for the original file. Never log in, use someone's cookies or work around a block.
- Keep it in a `reference/` folder that is git-ignored. It is for measurement only.

## 2. Measure it (numbers, not impressions)
```bash
python3 KIT/pipelines/reference-analysis/analyze_reference.py reference/example.mp4 reference/analysis
```
You get scene cuts, mean shot length, words per minute, syllables per second, pauses, voice pitch, and from the voice-cancelled side channel: click times, swish times, low hits, the music bed's beat, and the end-card hit. Look at the `spectrum_*.png` strips yourself. Also pull stills: `ffmpeg -i ref.mp4 -vf fps=1,scale=360:-1,tile=6x5 sheet.jpg` and read every frame.

## 3. Break it down
Write `PLAN.md` with:
1. **What it is:** length, words, format, colours (hex), type, how many scenes and how often the picture changes.
2. **How it holds attention:** the recurring visual grammar (a character, a ground line, capsule tags, counters, a glow, a camera move) and the argument shape (setup, twist, payoff).
3. **Beat table:** time, the voice line, what is on screen, the tags. One row per beat.
4. **Sound:** voice pace and pitch, bed (bpm, when it drops in), effect families with their timings, the ending.

## 4. Map the new story onto the beats
A two-column table: original beat on the left, ours on the right, same order, same job. Then write the script (see `short-form-principles`), keeping the original's sentence rhythm and its payoff line shape. Replace every tag and animation with one that fits the new story. Put the product where the original turns, and name the moment.

## 5. Build
Pick the closest pipeline (`pictogram-reel` for faceless parables; library pieces from `motion-library` for product films; `ugc-video-playbook` for creator formats). Then follow `reel-maker` steps 3 to 7. Recording the voice first and pinning beats to its word times is what makes it feel like the original.

## 6. Compare
Measure your render with the same tool and put the two reports side by side: pace, shot length, effect counts and loudness. Close the biggest gaps. State what you could not judge (you cannot hear it; ask the user to).
