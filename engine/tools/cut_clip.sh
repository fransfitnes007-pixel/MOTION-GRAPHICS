#!/bin/bash
# Cuts one moment out of a finished film into a skill's media/ folder.
#   cut_clip.sh <source.mp4> <start-sec> <end-sec> <skill-folder> [wide|tall|square] [poster-sec]
# Writes media/clip-<layout>.mp4 and, if the source has sound, media/sound.m4a. Writes media/poster.jpg from the midpoint
# (at poster-sec if given, or 62% through) only when there is no poster yet. Re-encodes so cuts land on the exact frame. Never touches the source file.
set -euo pipefail
FF="${FFMPEG:-ffmpeg}"
SRC="$1"; A="$2"; B="$3"; DIR="$4"; LAYOUT="${5:-wide}"
MEDIA="$DIR/media"; mkdir -p "$MEDIA"
DUR=$(python3 -c "print(round($B-$A,3))")
MID="${6:-$(python3 -c "print(round($A+($B-$A)*0.62,3))")}"
INFO=$("$FF" -hide_banner -i "$SRC" 2>&1 || true)   # ffmpeg -i with no output always exits non-zero
if echo "$INFO" | grep -q 'Stream.*Audio'; then
  "$FF" -y -loglevel error -ss "$A" -i "$SRC" -t "$DUR" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$MEDIA/clip-$LAYOUT.mp4"
  [ -f "$MEDIA/sound.m4a" ] || "$FF" -y -loglevel error -ss "$A" -i "$SRC" -t "$DUR" -vn -c:a aac -b:a 160k "$MEDIA/sound.m4a"
else
  "$FF" -y -loglevel error -ss "$A" -i "$SRC" -t "$DUR" -an -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -movflags +faststart "$MEDIA/clip-$LAYOUT.mp4"
fi
[ -f "$MEDIA/poster.jpg" ] || "$FF" -y -loglevel error -ss "$MID" -i "$SRC" -frames:v 1 -q:v 3 -vf "scale='min(960,iw)':-2" "$MEDIA/poster.jpg"
echo "cut $DUR s -> $MEDIA/clip-$LAYOUT.mp4"
