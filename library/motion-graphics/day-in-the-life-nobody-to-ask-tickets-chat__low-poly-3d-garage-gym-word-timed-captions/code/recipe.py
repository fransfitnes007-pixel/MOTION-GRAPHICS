#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.16x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). The only music
is the hold music, which is a joke in the story.  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(12)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * 92 * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
def beep(f, d=0.07):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * f * t)) * np.exp(-np.linspace(0, 2, n)) * 0.5
def hold_music(d):                                                                # thin, cheerful, endless
    out = np.zeros(int(d * SR)); seq = [523.3, 659.3, 784, 659.3, 587.3, 698.5, 880, 698.5]; step = 0.21
    for i in range(int(d / step)):
        s = tone(seq[i % 8], 0.2, 4, (1, 0.5)); j = int(i * step * SR); s = s[:len(out) - j]; out[j:j + len(s)] += s
    lo = np.convolve(out, np.ones(10) / 10, 'same'); return lo * np.minimum(1, np.linspace(0, 8, len(lo))) * np.minimum(1, np.linspace(8, 0, len(lo)))
T = dict(part=2.3, done=3.26, doneHit=3.88, qHit=5.14, tag=6.04, tagHit=6.66, email=7.36, oooHit=8.98, weeksHit=9.9, chat=10.6, botHit=12.24, meanHit=13.36, call=14.36, queue=15.46, queueHit=15.82, yn=17.34,
         guessHit=19.2, wrong=20.0, down=20.54, found=21.44, foundG=22.05, ticket=22.96, ticketHit=23.46, pingHit=24.5, disc=25.34, discHit=26.7, teamHit=27.52, askHit=28.44, humanHit=29.44, n=[30.38, 31.3], nob=32.04, still=32.88, end=34.45)
add(T['part'], thud(120, 0.2), 0.14)
add(T['done'], whoosh(0.35), 0.3); add(T['doneHit'], ding(1568, 0.5), 0.07)
add(T['qHit'], thud(110, 0.2), 0.14)
add(T['tag'], whoosh(0.3), 0.25); add(T['tagHit'], tone(700, 0.2, 2), 0.05); add(T['tagHit'] + 0.12, tone(930, 0.28, 2), 0.05)
add(T['email'], whoosh(0.4), 0.3)
for k, f in enumerate([523.3, 659.3, 784]): add(T['oooHit'] - 0.1 + k * 0.09, tone(f, 0.5, 5, (1, 0.6, 0.3)), 0.06)   # a holiday jingle for the auto-reply
add(T['weeksHit'], thud(120, 0.3), 0.24)
add(T['chat'], whoosh(0.4), 0.3); add(T['chat'] + 0.3, tone(1046.5, 0.07, 3), 0.05)
for k, f in enumerate([880, 1320, 990]): add(T['botHit'] - 0.05 + k * 0.08, beep(f), 0.05)       # the bot wakes up
for k, f in enumerate([990, 740]): add(T['meanHit'] - 0.05 + k * 0.1, beep(f, 0.1), 0.05); 
add(T['meanHit'] + 0.1, thud(110, 0.25), 0.18)
add(T['call'], whoosh(0.3), 0.25)
for k in range(2): add(T['call'] + 0.4 + k * 0.45, tone(440, 0.3, 1.2, (1, 0.4)) * np.sin(2 * np.pi * 20 * np.arange(int(0.3 * SR)) / SR) ** 2, 0.06)   # ringing
add(T['queue'], hold_music(T['yn'] - T['queue'] - 0.05), 0.045); add(T['queueHit'], thud(120, 0.3), 0.22)
add(T['yn'], thud(100, 0.3), 0.2)
add(T['guessHit'] - 0.2, tone(700, 0.2, 2), 0.05)
add(T['wrong'], thud(150, 0.45), 0.34); add(T['wrong'] + 0.02, buzz(0.5), 0.12)
n = int(0.5 * SR); add(T['down'] + 0.2, np.sin(2 * np.pi * np.cumsum(np.geomspace(600, 180, n)) / SR) * np.sin(np.linspace(0, np.pi, n)) ** 0.5, 0.05)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(7): add(T['ticket'] + 0.05 + i * 0.06, rng.standard_normal(int(0.03 * SR)) * np.exp(-np.linspace(0, 8, int(0.03 * SR))), 0.07)
add(T['ticketHit'], ding(1568, 0.5), 0.07)
add(T['pingHit'], ding(1760, 0.35), 0.08); add(T['pingHit'] + 0.11, ding(2349, 0.5), 0.07)       # the ping
add(T['disc'], whoosh(0.45), 0.35)
for i in range(3): add(T['teamHit'] - 0.1 + i * 0.08, tone(880 * 2 ** (i * 3 / 12), 0.12, 3), 0.05)
add(T['askHit'], tone(1046.5, 0.07, 3), 0.06)
for k, f in enumerate([392, 523.3, 659.3, 784]): add(T['humanHit'] - 0.05 + k * 0.03, tone(f, 1.4, 4), 0.055)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.35), 0.3); add(T['still'] + 0.1, hold_music(T['end'] - T['still'] - 0.2), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
