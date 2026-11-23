#!/usr/bin/env bash
# Renders the library clips the showcase film plays, then cuts them into JPEG frame folders the film draws from.
set -euo pipefail
cd "$(dirname "$0")"; K=../..; R="node $K/engine/tools/render_demo.cjs video"
mkdir -p clips frames
clip() { # name demo w h
  [ -f "clips/$1.mp4" ] || $R "$K/library/$2/code/demo.html" "clips/$1.mp4" "$3" "$4"
  rm -rf "frames/$1"; mkdir -p "frames/$1"
  ffmpeg -y -loglevel error -i "clips/$1.mp4" -vf "fps=30,scale=${5:-540}:-2" -q:v 4 "frames/$1/%04d.jpg"
}
clip dino      motion-graphics/dino-runner-arizona-sunset__pixel-dithered-sky-mesa-parallax 1080 1920 405
clip ledword   motion-graphics/led-dot-rainbow-word__conic-gradient-dot-mask 1920 1080 640
clip wordmark  motion-graphics/chrome-wordmark-end-card__blur-resolve-cta 1920 1080 640
rm -rf frames/pictogram; mkdir -p frames/pictogram
ffmpeg -y -loglevel error -i ../media/example-reel.mp4 -vf "fps=30,scale=405:-2" -q:v 4 frames/pictogram/%04d.jpg
# extra pieces as name=slug, e.g. comma=comma-jump-number-input__digit-rise-comma-dip
for s in "$@"; do clip "${s%%=*}" "ui-components/${s#*=}" 1920 1080 640; done
# frame counts for the film
( printf "window.FRAMES={"; for d in frames/*/; do n=$(basename "$d"); printf "\"%s\":%s," "$n" "$(ls "$d" | wc -l | tr -d " ")"; done; printf "};\n" ) > assets/frames.js
echo done
