#!/usr/bin/env bash
# Renders every library clip the showcase film plays (list in clips.txt: name | library path | width | height | frame width),
# at its own native shape, then cuts each into a JPEG frame folder the film draws from, and writes assets/frames.js.
#   ./render_clips.sh            all clips
#   ./render_clips.sh 0 2        every 2nd clip starting at 0 (run two in parallel: "0 2" and "1 2")
set -euo pipefail
cd "$(dirname "$0")"; K=../..; mkdir -p clips frames
part=${1:-0}; of=${2:-1}; i=0
while IFS='|' read -r name path w h fw; do
  name=$(echo $name | tr -d ' '); path=$(echo $path | tr -d ' '); w=$(echo $w | tr -d ' '); h=$(echo $h | tr -d ' '); fw=$(echo $fw | tr -d ' ')
  [ -z "$name" ] || [ "${name:0:1}" = "#" ] && continue
  i=$((i+1)); [ $(( (i-1) % of )) -eq "$part" ] || continue
  [ -f "clips/$name.mp4" ] || node "$K/engine/tools/render_demo.cjs" video "$K/library/$path/code/demo.html" "clips/$name.mp4" "$w" "$h"
  rm -rf "frames/$name"; mkdir -p "frames/$name"
  ffmpeg -y -loglevel error -i "clips/$name.mp4" -vf "fps=30,scale=$fw:-2" -q:v 4 "frames/$name/%04d.jpg"
  echo "framed $name"
done < clips.txt
if [ "$part" = 0 ] && [ ! -d frames/pictogram ]; then mkdir -p frames/pictogram; ffmpeg -y -loglevel error -i ../media/example-reel.mp4 -vf "fps=30,scale=405:-2" -q:v 4 frames/pictogram/%04d.jpg; fi
( printf "window.FRAMES={"; for d in frames/*/; do n=$(basename "$d"); printf '"%s":%s,' "$n" "$(ls "$d" | wc -l | tr -d ' ')"; done; printf "};\n" ) > assets/frames.js
echo done
