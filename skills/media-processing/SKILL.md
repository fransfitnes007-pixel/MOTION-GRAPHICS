---
name: media-processing
description: "ffmpeg and ffprobe recipes for the video work around motion graphics: probing, trimming, vertical fitting, speed changes, concatenation, captions, audio mixing, loudness, compression, frame and audio extraction. Use whenever a video or audio file has to be converted, cut, fitted or checked."
---

# Media processing with ffmpeg

Replace `in.mp4`, `out.mp4` and paths with the real ones. Quote every path. Never overwrite the source; write to a new file.

## Inspect first
```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration -of default=nw=1 in.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 in.mp4
```
If ffprobe is missing, `ffmpeg -hide_banner -i in.mp4 2>&1 | grep -E "Duration|Video:|Audio:"`.

## Standard delivery spec (Reels, TikTok, Shorts)
1080x1920, 30 fps (or 60 for UI/screen content), H.264, yuv420p, AAC 48 kHz, faststart, under about 60 s for the broadest reach.
```bash
ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black" \
  -r 30 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart out.mp4
```
Fill the frame instead of letterboxing (crop to 9:16):
```bash
ffmpeg -i in.mp4 -vf "scale=-2:1920,crop=1080:1920" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy out.mp4
```
Blurred-background fill for landscape clips:
```bash
ffmpeg -i in.mp4 -filter_complex "[0:v]scale=1080:1920,boxblur=30:5[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:a copy out.mp4
```

## Cut and join
```bash
ffmpeg -ss 00:00:03.5 -to 00:00:09 -i in.mp4 -c:v libx264 -crf 18 -c:a aac out.mp4   # accurate trim (re-encode)
ffmpeg -ss 3.5 -i in.mp4 -t 5.5 -c copy out.mp4                                       # fast trim, keyframe-snapped
printf "file 'a.mp4'\nfile 'b.mp4'\n" > list.txt && ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4   # clips must share codec/size/fps
```

## Speed
```bash
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=PTS/2[v];[0:a]atempo=2[a]" -map "[v]" -map "[a]" fast.mp4   # 2x
ffmpeg -i in.mp4 -vf "setpts=PTS/4" -an timelapse.mp4                                                    # 4x, no audio
```

## Captions and overlays
```bash
ffmpeg -i in.mp4 -vf "subtitles=captions.srt:force_style='FontName=Arial,FontSize=14,Bold=1,Outline=3,Alignment=2,MarginV=260'" -c:a copy out.mp4
ffmpeg -i in.mp4 -i logo.png -filter_complex "overlay=W-w-40:40" -c:a copy out.mp4
```
Keep captions inside the platform safe area: about 250 px clear at the bottom, 150 px at the top, 60 px at the sides.

## Audio
```bash
ffmpeg -i in.mp4 -vn -ac 1 -ar 16000 audio.wav                                   # for transcription
ffmpeg -i in.mp4 -vn -c:a libmp3lame -q:a 2 audio.mp3                            # extract
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy out.mp4             # normalise to -14 LUFS
ffmpeg -i voice.wav -i music.mp3 -filter_complex "[1:a]volume=0.15[m];[0:a][m]amix=inputs=2:duration=first" mix.m4a   # music under voice
ffmpeg -i voice.wav -i music.mp3 -filter_complex "[1:a][0:a]sidechaincompress=threshold=0.05:ratio=8[m];[0:a][m]amix=inputs=2:duration=first" ducked.m4a   # auto-duck
ffmpeg -i in.mp4 -af silenceremove=stop_periods=-1:stop_duration=0.4:stop_threshold=-40dB trimmed.wav   # cut long silences
```
Replace a video's audio: `ffmpeg -i v.mp4 -i a.m4a -map 0:v -map 1:a -c:v copy -shortest out.mp4`.

## Frames and analysis
```bash
ffmpeg -i in.mp4 -vf fps=1,scale=480:-2 frames/f_%03d.jpg                                   # 1 frame per second
ffmpeg -ss 2 -i in.mp4 -frames:v 1 frame.png                                                # one frame
ffmpeg -i in.mp4 -vf "select='gt(scene,0.3)',showinfo" -an -f null - 2>&1 | grep pts_time   # cut detection
ffmpeg -i in.mp4 -vf "fps=2,scale=270:-2,tile=6x4" -frames:v 1 sheet.jpg                    # contact sheet
```

## GIF and previews
```bash
ffmpeg -i in.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" out.gif
```

## Compress for sharing
```bash
ffmpeg -i in.mp4 -c:v libx264 -crf 26 -preset medium -vf scale=-2:1280 -c:a aac -b:a 128k -movflags +faststart small.mp4
```
Platforms re-encode, so upload a high-quality file (CRF 16 to 20) rather than a pre-compressed one.

## Checks before delivering
- Resolution, fps, duration and audio stream present (`ffprobe`).
- First 3 seconds and last 3 seconds by frame grab.
- Audio not clipping, loudness near -14 LUFS, speech clear over music.
- No black frames at the ends: `ffmpeg -i out.mp4 -vf blackdetect -an -f null -`.
- Captions inside the safe area.

## Screen recordings of apps
Fit phone-shaped recordings to 1080x1920 with the pad command above, hide cursors, record at 60 fps if there is scrolling, and speed up waiting or loading moments (2x to 8x) rather than cutting them so the process still reads as real.
