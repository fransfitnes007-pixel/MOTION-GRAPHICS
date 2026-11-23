#!/usr/bin/env bash
# Local text-to-speech on Apple Silicon (MLX). Creates .venv, installs pinned packages, downloads pinned model revisions (about 5 GB).
# On other hardware use Kokoro through its own package, or the cloud fallback in skills/voiceover-elevenlabs.
set -euo pipefail
cd "$(dirname "$0")"
command -v uv >/dev/null || { echo "install uv first: https://docs.astral.sh/uv/"; exit 1; }
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
mkdir -p models
# repo@revision: the exact versions this kit was tested with
while read -r repo rev; do
  [ -z "$repo" ] && continue
  dir="models/${repo/\//__}"
  [ -d "$dir" ] || .venv/bin/hf download "$repo" --revision "$rev" --local-dir "$dir"
done <<'MODELS'
mlx-community/Kokoro-82M-bf16 a71e4d38b236d968966a2002c4c895dbd12b1c3c
mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-8bit 41d3337e8b7f2843a75841595fc14e4b9a7a4b96
mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit f90d617701d9f7f4ca499291e0b57f2b3c2fd2ee
mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit e7dd0585652209fa0d7783659aad4e8a324de11c
MODELS
echo "ready: .venv/bin/python voice.py f_heart example.txt out.wav"
