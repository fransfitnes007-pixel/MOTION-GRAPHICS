#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.3x, take 1)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 41.3
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(14)
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
def click(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
T = dict(part=2.3, dealHit=4.02, need=4.84, logoHit=5.5, clipHit=6.62, link=7.6, linkHit=8.02, exp=8.6, expHit=8.86, link2=10.06, link2Hit=10.62, req=11.3, reqHit=11.56, ireqHit=12.84, nothing=13.8, files=14.74, f=[16.54, 17.5, 18.54],
         crim=19.26, maskHit=19.7, crimHit=21.02, found=21.8, foundG=22.45, bank=23.42, items=[25.32, 26.2, 27.2], oneHit=28.08, sharedHit=29.06, n=[30.16, 31.32], nob=32.6, appr=33.28, apprHit=33.64, endedHit=35.36, end=36.3)
add(T['part'], thud(120, 0.2), 0.14)
add(T['dealHit'], ding(1318.5), 0.09); add(T['dealHit'] + 0.12, ding(1760), 0.07)
add(T['need'], whoosh(0.3), 0.25); add(T['logoHit'], tone(880, 0.1, 3), 0.06); add(T['clipHit'], tone(1046.5, 0.1, 3), 0.06)
add(T['link'], whoosh(0.4), 0.3); add(T['linkHit'], tone(880, 0.12, 3), 0.07); add(T['linkHit'] + 0.09, tone(1174.7, 0.16, 3), 0.07)
add(T['exp'], whoosh(0.3), 0.3); add(T['expHit'], thud(150, 0.4), 0.3); add(T['expHit'] + 0.02, buzz(0.4), 0.1)
add(T['link2'], whoosh(0.3), 0.25); add(T['link2Hit'], tone(880, 0.12, 3), 0.07); add(T['link2Hit'] + 0.09, tone(1174.7, 0.16, 3), 0.07)
add(T['req'], whoosh(0.35), 0.3); add(T['reqHit'], thud(110, 0.3), 0.22)
add(T['ireqHit'], click(), 0.25); add(T['ireqHit'] + 0.05, tone(1046.5, 0.07, 3), 0.05)
add(T['nothing'], whoosh(1.4), 0.32)                                                               # wind for the tumbleweed
for i in range(6): add(T['nothing'] + 0.15 + i * 0.14, thud(90, 0.08), 0.05)
add(T['files'], whoosh(0.35), 0.3)
for i, at in enumerate(T['f']): add(at, thud(150 - i * 10, 0.3), 0.22 + i * 0.03); add(at + 0.02, buzz(0.2), 0.05 + i * 0.01)
add(T['crim'], whoosh(0.3), 0.25); add(T['maskHit'], thud(110, 0.2), 0.16)
for i in range(4): add(T['maskHit'] + 0.3 + i * 0.33, tone(1320, 0.06, 2), 0.05)                   # REC blinking
add(T['crimHit'], thud(120, 0.4), 0.3)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['bank'], whoosh(0.5), 0.35)
for i, at in enumerate(T['items']): add(at - 0.1, whoosh(0.18), 0.18); add(at, ding(880 * 2 ** (i * 2 / 12), 0.5), 0.075)
add(T['oneHit'], thud(120, 0.3), 0.24)
for k, f in enumerate([392, 523.3, 659.3, 784]): add(T['sharedHit'] - 0.05 + k * 0.03, tone(f, 1.4, 4), 0.055)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['appr'], whoosh(0.35), 0.3); add(T['apprHit'] - 0.05, ding(1568, 0.5), 0.08)
n = int(0.5 * SR); add(T['endedHit'] - 0.05, np.sin(2 * np.pi * np.cumsum(np.geomspace(600, 170, n)) / SR) * np.sin(np.linspace(0, np.pi, n)) ** 0.5, 0.06); add(T['endedHit'], thud(110, 0.35), 0.24)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
