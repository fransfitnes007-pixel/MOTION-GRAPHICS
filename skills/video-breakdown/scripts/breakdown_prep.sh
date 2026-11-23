#!/usr/bin/env bash
# Prepare a reference video for analysis: metadata, cut list, contact sheet, audio, transcript.
# Usage: breakdown_prep.sh <video-file-or-public-url> <outdir>
# Needs ffmpeg. URLs need yt-dlp (public posts only). Transcript needs the transcribe skill's venv.
set -euo pipefail
src="$1"; out="${2:-./breakdown}"; mkdir -p "$out"
if [[ "$src" =~ ^https?:// ]]; then
  yt-dlp -f "mp4/best" -o "$out/source.%(ext)s" --write-info-json "$src"
  src=$(ls "$out"/source.* | grep -v '\.json$' | head -1)
fi
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate -of default=nw=1 "$src" | tee "$out/probe.txt"
# Cuts: timestamps where the picture changes a lot
ffmpeg -hide_banner -i "$src" -vf "select='gt(scene,0.3)',showinfo" -an -f null - 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$out/cuts.txt" || true
echo "cuts: $(wc -l < "$out/cuts.txt")"
# One frame every 0.5 s as a contact sheet (first 30 s)
ffmpeg -hide_banner -loglevel error -y -i "$src" -t 30 -vf "fps=2,scale=216:-2,tile=8x8" -frames:v 1 "$out/sheet.jpg"
# First 3 seconds at 4 fps: the hook
mkdir -p "$out/hook"; ffmpeg -hide_banner -loglevel error -y -i "$src" -t 3 -vf "fps=4,scale=540:-2" "$out/hook/h_%02d.jpg"
ffmpeg -hide_banner -loglevel error -y -i "$src" -vn -ac 1 -ar 16000 "$out/audio.wav"
echo "done: $out (probe.txt cuts.txt sheet.jpg hook/ audio.wav). Transcribe with the transcribe skill."
