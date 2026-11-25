#!/bin/bash
# The numbers a finished video must show before it counts as done (PLAYBOOK.md section 7).
# Usage: check_video.sh <clip.mp4> <out dir for the contact sheets>
# Prints duration, mean/max volume, black frames, and writes 1-frame-per-second contact sheets (7x3 tiles) to look at.
set -euo pipefail
V="${1:?clip.mp4}"; O="${2:?out dir}"; mkdir -p "$O"
FF="${FFMPEG:-ffmpeg}"
dur=$("$FF" -i "$V" 2>&1 | sed -n 's/.*Duration: \([0-9:.]*\).*/\1/p' | head -1 || true)
echo "duration $dur"
"$FF" -v info -i "$V" -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume" | sed 's/.*\] //'
blk=$("$FF" -v info -i "$V" -vf "blackdetect=d=0.2:pix_th=0.05" -an -f null - 2>&1 | grep -c black_start || true)
echo "black stretches over 0.2 s: $blk"
"$FF" -v error -y -i "$V" -vf "fps=1,scale=270:-2,tile=7x3" "$O/contact-%d.jpg"
ls "$O"/contact-*.jpg
echo "max_volume must not read 0.0 dB. Look at every contact sheet yourself; nobody has listened to the mix yet."
