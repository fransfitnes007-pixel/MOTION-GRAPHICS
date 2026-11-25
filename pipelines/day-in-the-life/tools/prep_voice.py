#!/usr/bin/env python3
"""Speed a raw voice take to the series pace and make it 48 kHz mono.
  python3 prep_voice.py take1.mp3 voiceover.wav [--target 37]
speed = raw seconds / 37, kept between 1.1 and 1.3 (both voices). Aim for 36 to 37 s of voice; if the raw take is longer
than about 48 s even 1.3x leaves the reel long: shorten the script (about 540 characters) instead of speeding more."""
import subprocess, sys, os
src, dst = sys.argv[1], sys.argv[2]
target = float(sys.argv[sys.argv.index('--target') + 1]) if '--target' in sys.argv else 37.0
FF = os.environ.get('FFMPEG', 'ffmpeg'); FP = os.environ.get('FFPROBE', 'ffprobe')
raw = float(subprocess.check_output([FP, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src]).decode())
speed = round(min(1.3, max(1.1, raw / target)), 3)
subprocess.run([FF, '-y', '-v', 'error', '-i', src, '-af', f'atempo={speed}', '-ar', '48000', '-ac', '1', dst], check=True)
print(f'raw {raw:.2f} s -> speed {speed}x -> {raw / speed:.2f} s : {dst}')
