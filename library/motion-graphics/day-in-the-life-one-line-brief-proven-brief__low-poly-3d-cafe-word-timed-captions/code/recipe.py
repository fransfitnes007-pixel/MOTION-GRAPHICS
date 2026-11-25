#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.2x) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.7
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(9)
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
T = dict(part=2.16, camp=3.06, open=4.08, line=5.22, lineHit=5.62, viral=6.44, no=[7.8, 8.54, 9.18, 10.06], nothing=10.86, stare=11.7, hours=13.3, ask=14.84, askHit=15.0, authHit=16.76,
         guess=17.6, flops=18.85, flopHit=19.1, fortyHit=20.16, cookedHit=21.1, found=21.92, foundG=22.55, brief=23.46, items=[25.1, 25.64, 26.28, 26.94, 28.1], detail=29.66,
         guessed=30.9, provenHit=32.46, n=[33.46, 34.18], nob=34.98, end=35.7)
add(T['part'], thud(120, 0.2), 0.14)
add(T['camp'] + 0.1, ding(1318.5), 0.09); add(T['camp'] + 0.22, ding(1760), 0.07)
add(T['open'], whoosh(0.3), 0.3); add(T['line'], whoosh(0.4), 0.35); add(T['lineHit'], thud(110, 0.2), 0.14)
for i in range(13): add(T['viral'] + i * 0.045, tone(1500, 0.02, 2), 0.035)                         # typing "make it viral"
for i, at in enumerate(T['no']): add(at, thud(150 - i * 8, 0.3), 0.22 + i * 0.03); add(at + 0.02, buzz(0.25), 0.06)
add(T['nothing'], thud(100, 0.5), 0.3)
add(T['stare'], whoosh(0.4), 0.25)
for i in range(9): add(T['hours'] + i * 0.165, tone(1000, 0.03, 2), 0.04)                           # two hours of clock
for k in range(3): add(T['askHit'] + [0, 0.15, 0.5][k], tone(1046.5, 0.07, 3), 0.05)
add(T['authHit'], tone(880, 0.12, 3), 0.07); add(T['authHit'] + 0.09, tone(1174.7, 0.16, 3), 0.07)
add(T['guess'], whoosh(0.3), 0.3); add(T['guess'] + 0.3, tone(700, 0.25, 2), 0.05); add(T['guess'] + 0.42, tone(930, 0.3, 2), 0.05)
add(T['flops'], whoosh(0.3), 0.3)
n = int(0.7 * SR); add(T['flopHit'], np.sin(2 * np.pi * np.cumsum(np.geomspace(700, 140, n)) / SR) * np.sin(np.linspace(0, np.pi, n)) ** 0.5, 0.06)   # sad slide down
add(T['fortyHit'], thud(150, 0.4), 0.3); add(T['fortyHit'] + 0.02, buzz(0.45), 0.1)
add(T['cookedHit'], thud(120, 0.45), 0.34)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['brief'], whoosh(0.5), 0.35)
for i, at in enumerate(T['items']): add(at - 0.1, whoosh(0.18), 0.18); add(at, ding(880 * 2 ** (i * 2 / 12), 0.5), 0.075)
add(T['detail'], whoosh(0.5), 0.35); 
for r in range(3): add(T['detail'] + 0.15 + r * 0.22, tone(1568 + r * 200, 0.06, 3), 0.05)
add(T['guessed'] - 0.1, whoosh(0.3), 0.3)
for k, f in enumerate([392, 523.3, 659.3, 784, 1046.5]): add(T['provenHit'] + k * 0.03, tone(f, 1.6, 4), 0.055)
add(T['provenHit'], thud(140, 0.3), 0.22)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
