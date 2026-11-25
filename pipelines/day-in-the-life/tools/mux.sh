#!/usr/bin/env bash
# Render, mix and mux one episode, then make the checks.
#   bash pipelines/day-in-the-life/tools/mux.sh <episode-folder> <out.mp4>
# <episode-folder> holds code/demo.html, code/recipe.py and code/voiceover.wav (from prep_voice.py).
# Writes media/silent-tall.mp4 (deleted at the end), media/sound.wav, <out.mp4>, media/poster.jpg, and two frame sheets
# (media/fr1.jpg, media/fr2.jpg: one frame a second, 7x3 each). Look at both sheets before calling it done.
set -euo pipefail
EP=$(cd "$1" && pwd); OUT=$2
KIT=$(cd "$(dirname "$0")/../../.." && pwd); FF=${FFMPEG:-ffmpeg}
mkdir -p "$EP/media"
node "$KIT/engine/tools/render_demo.cjs" video "$EP/code/demo.html" "$EP/media/silent-tall.mp4" 1080 1920
python3 "$EP/code/recipe.py" "$EP/media/sound.wav"
mux() { "$FF" -y -v error -i "$EP/media/silent-tall.mp4" -i "$EP/media/sound.wav" \
  -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -c:v libx264 -crf 17 -preset slow \
  -af "$1" -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"; }
mux "loudnorm=I=-16"
# Sharp effects can push the peak to 0 dB: mux again with a limiter (level=false, or it pushes back up to 0 dB).
if "$FF" -i "$OUT" -af volumedetect -f null - 2>&1 | grep -q "max_volume: 0.0 dB"; then
  mux "loudnorm=I=-16:TP=-2:LRA=11,alimiter=limit=0.8:level=false"; fi
"$FF" -i "$OUT" -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume"
"$FF" -y -v error -ss 22 -i "$OUT" -frames:v 1 -q:v 3 -vf "scale=540:-2" "$EP/media/poster.jpg"
"$FF" -y -v error -i "$OUT" -vf "fps=1,scale=216:384,tile=7x3" -frames:v 2 "$EP/media/fr%d.jpg"
rm -f "$EP/media/silent-tall.mp4"
echo "done: $OUT  sheets: $EP/media/fr1.jpg $EP/media/fr2.jpg"
