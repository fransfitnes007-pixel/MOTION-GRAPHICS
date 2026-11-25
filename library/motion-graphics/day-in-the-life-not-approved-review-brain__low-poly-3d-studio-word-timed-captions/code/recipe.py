#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.12x) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(6)
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
T = dict(part=2.36, film=3.3, send=4.4, na=[5.54, 9.64, 11.62, 14.34], reason=6.34, again=7.9, hook=10.84, pers=12.36, wait=15.12, pop=17.34, popHit=17.66, wtf=18.86,
         found=20.1, foundG=20.75, up=21.74, upHit=22.5, brain=22.88, tells=23.9, fixW=25.24, where=25.84, fix=[26.6, 28.14], fixit=29.3, again2=30.04, ok=31.18, no=[32.04, 32.82], nob=33.64, end=34.5)
add(T['part'], thud(120, 0.2), 0.14)
for at in (T['film'], T['again'], T['fixit']): add(at - 0.1, whoosh(0.3), 0.3)
add(T['send'], whoosh(0.4), 0.35); add(T['send'] + 0.75, ding(1568, 0.4), 0.06)
for i, at in enumerate(T['na']): add(at, thud(150 - i * 8, 0.4), 0.26 + i * 0.03); add(at + 0.02, buzz(0.42), 0.09 + i * 0.01)
add(T['reason'], thud(100, 0.2), 0.12)
add(T['hook'], tone(2093, 0.5, 7, (1, 0.5, 0.3)), 0.06)                                           # the hook, a metal ting
for k in range(8): add(T['pers'] + 0.1 + k * 0.17, tone(523.3 * 2 ** ((k % 4) * 3 / 12), 0.1, 3), 0.04)   # a new personality
for i in range(13): add(T['wait'] + i * 0.165, tone(1000, 0.03, 2), 0.04)                         # three days of clock
add(T['pop'], whoosh(0.3), 0.3); add(T['popHit'], tone(880, 0.12, 3), 0.07); add(T['popHit'] + 0.09, tone(1174.7, 0.16, 3), 0.07)
add(T['wtf'], thud(120, 0.45), 0.34)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.2, 4), 0.055)
add(T['upHit'], ding(1568, 0.5), 0.07)
n = int(0.95 * SR); add(T['brain'], np.sin(2 * np.pi * np.cumsum(220 + 180 * np.sin(np.linspace(0, 7 * 0.95, n))) / SR) * np.sin(np.linspace(0, np.pi, n)) ** 2, 0.05)   # the scan
add(T['brain'], whoosh(0.5), 0.3)
for i in range(2): add(T['fixW'] + i * 0.12, tone(1760, 0.08, 3), 0.06); add(T['where'] + i * 0.1, tone(1320, 0.08, 3), 0.05)
for at in T['fix']: add(at, thud(160, 0.18), 0.16); add(at, ding(987.8, 0.5), 0.06)
add(T['again2'], whoosh(0.35), 0.3)
for k, f in enumerate([392, 523.3, 659.3, 784, 1046.5]): add(T['ok'] + k * 0.03, tone(f, 1.6, 4), 0.055)
add(T['ok'], thud(140, 0.3), 0.22)
for at in T['no']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
