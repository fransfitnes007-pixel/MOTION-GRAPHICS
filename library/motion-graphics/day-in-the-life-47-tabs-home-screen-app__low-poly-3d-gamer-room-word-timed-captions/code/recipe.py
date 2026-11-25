#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, take 2, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
gamer room: a computer fan hum and keyboard clicks. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.6
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(136)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35, f=92):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * f * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
def click(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
def slide(f0, f1, d=0.35):
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def pop(f=520): return slide(f, f * 1.9, 0.09)
def stampS(): return np.concatenate([thud(170, 0.12) * 0.8, click()[:800] * 0.6])
def squelch(d=0.35):
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(90) / 90, 'same') * np.exp(-np.linspace(0, 5, n)) * 6 + thud(90, d) * 0.5
def hum(d, f=58):
    n = int(d * SR); t = np.arange(n) / SR; s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.08 * np.convolve(rng.standard_normal(n), np.ones(30) / 30, 'same')
    e = np.ones(n); r = min(n // 4, int(0.3 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e
def vib(d=0.6):
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 150 * t) * (np.sin(2 * np.pi * 9 * t) > 0) * np.exp(-np.linspace(0, 1.5, n))
def fan(d): n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(80) / 80, 'same') * 3 + np.sin(2 * np.pi * 120 * t) * 0.15
def keys(d, rate=9):
    n = int(d * SR); s = np.zeros(n); i = 0
    while i < n - 900:
        s[i:i + 900] += click()[:900] * rng.uniform(0.3, 0.8); i += int(SR / rate * rng.uniform(0.6, 1.4))
    return s
def creak(d=1.2): n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * (180 + 40 * np.sin(2 * np.pi * 2.5 * t)) * t) * 0.4 * np.sin(np.linspace(0, np.pi, n))
T = dict(part=2.46, have=3.66, fsHit=4.32, brief=5.94, tabs=[5.94, 6.68, 7.7, 8.64, 10.48], smallHit=13.06, iconsHit=14.02, closeHit=15.18, uploadHit=16.36, ninety=17.26,
         found=18.56, foundG=19.3, sits=20.06, homeHit=20.62, appHit=21.5, tapHit=22.22, signedHit=23.62, cards=[24.5, 25.26, 25.96], n=[27.88, 28.72], nobHit=30.08, still=31.08, recipeHit=33.76, end=34.6)
add(0, fan(T['end'] + 1), 0.012)
add(0.2, keys(2.2), 0.05); add(T['have'], keys(1.6), 0.04)
add(T['part'], thud(120, 0.2), 0.14); add(T['fsHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
add(T['brief'], whoosh(0.3), 0.26)
for i, at in enumerate(T['tabs']): add(at + 0.05, pop(560 + i * 40), 0.05)
add(T['smallHit'], slide(900, 400, 0.4), 0.05); add(T['iconsHit'], pop(900), 0.05)
add(T['closeHit'], click(), 0.3); add(T['closeHit'] + 0.05, slide(800, 300, 0.25), 0.06)
add(T['uploadHit'], stampS(), 0.3); add(T['uploadHit'] + 0.1, tone(196, 0.6, 4, (1, 0.5)), 0.08)
add(T['ninety'], creak(1.3), 0.06)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['sits'], whoosh(0.3), 0.26); add(T['homeHit'], pop(620), 0.06); add(T['tapHit'], click(), 0.3); add(T['tapHit'] + 0.05, slide(600, 1200, 0.2), 0.05)
add(T['signedHit'], ding(1318.5, 0.5), 0.06); add(T['signedHit'] + 0.08, ding(1760, 0.5), 0.04)
for at in T['cards']: add(at, pop(600), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.25), 0.2); add(T['still'] + 0.3, keys(1.2), 0.04); add(T['recipeHit'], tone(988, 0.3, 4, (1, 0.4)), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
