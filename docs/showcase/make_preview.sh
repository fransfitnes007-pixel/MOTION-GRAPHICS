#!/usr/bin/env bash
# Silent looping preview of the showcase film for the README (GitHub autoplays GIFs, not videos stored in the repo).
set -euo pipefail
cd "$(dirname "$0")"; IN=../media/showcase.mp4; OUT=../media/showcase-preview.gif
# the five strongest moments, about 17 s
SEG="3.0:6.4 9.4:12.9 16.95:19.9 38.4:41.6 43.95:46.8"
i=0; : > clips/preview_list.txt
for s in $SEG; do a=${s%:*}; b=${s#*:}; i=$((i+1))
  ffmpeg -y -loglevel error -ss "$a" -to "$b" -i "$IN" -an -vf "fps=10,scale=640:-2:flags=lanczos" "clips/pv_$i.mp4"
  echo "file 'pv_$i.mp4'" >> clips/preview_list.txt; done
ffmpeg -y -loglevel error -f concat -safe 0 -i clips/preview_list.txt -c copy clips/preview.mp4
ffmpeg -y -loglevel error -i clips/preview.mp4 -vf "split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" -loop 0 "$OUT"
ls -la "$OUT"
