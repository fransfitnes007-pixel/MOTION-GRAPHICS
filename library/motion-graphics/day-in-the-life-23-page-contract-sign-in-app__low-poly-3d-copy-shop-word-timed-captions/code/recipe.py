#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.173x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.8
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(16)
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
def motor(d, f=70):                                                                # the copier feeding paper
    n = int(d * SR); t = np.arange(n) / SR; return (np.sign(np.sin(2 * np.pi * f * t)) * 0.3 + 0.5 * np.convolve(rng.standard_normal(n), np.ones(30) / 30, 'same')) * np.minimum(1, np.linspace(0, 10, n)) * np.minimum(1, np.linspace(10, 0, n))
def scratch(d=0.18):                                                               # a pen
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same') * np.sin(np.linspace(0, np.pi, n)) * (0.6 + 0.4 * np.sin(np.linspace(0, 40, n)))
T = dict(part=2.26, deal=3.12, email=4.02, emailHit=4.54, pages=5.4, pagesHit=5.96, steps=[7.0, 7.7, 8.3, 8.9], printerHit=10.34, drive=10.94, jam=12.68, jamHit=13.08, init=13.86, allHit=15.88, scan=16.58, scanHit=17.28, thumbHit=18.02,
         small=19.84, smallHit=20.06, v2Hit=20.94, againHit=21.84, found=22.5, foundG=23.1, agr=23.96, agrHit=24.08, read=25.96, signHit=26.6, thereHit=27.32, after=[28.0, 29.14, 30.36], n=[31.6, 32.34], nob=33.16, coast=33.88, coastHit=34.92, end=35.8)
add(T['part'], thud(120, 0.2), 0.14)
add(T['deal'] + 0.15, ding(1318.5), 0.09); add(T['deal'] + 0.27, ding(1760), 0.07)
add(T['emailHit'], tone(880, 0.12, 3), 0.07); add(T['emailHit'] + 0.09, tone(1174.7, 0.16, 3), 0.07)
add(T['pages'], whoosh(0.4), 0.3); add(T['pagesHit'], thud(120, 0.4), 0.28)
for i, at in enumerate(T['steps']): add(at, thud(150 - i * 8, 0.25), 0.2 + i * 0.02)
add(T['printerHit'], thud(100, 0.3), 0.18)
add(T['drive'], whoosh(0.4), 0.3); add(T['drive'] + 0.6, click(), 0.2); add(T['drive'] + 0.8, motor(T['jam'] - T['drive'] - 0.8), 0.06)
for i in range(4): add(T['drive'] + 0.9 + i * 0.2, whoosh(0.16), 0.14)
n = int(0.5 * SR); add(T['jam'], rng.standard_normal(n) * np.exp(-np.linspace(0, 5, n)) * (0.5 + 0.5 * np.sign(np.sin(np.linspace(0, 120, n)))), 0.12)   # crunch
add(T['jamHit'], thud(150, 0.45), 0.32); add(T['jamHit'] + 0.02, buzz(0.5), 0.11)
for k in range(3): add(T['jamHit'] + 0.3 + k * 0.2, tone(1500, 0.07, 2), 0.04)
add(T['init'], whoosh(0.35), 0.3)
for i in range(12): add(T['init'] + 0.2 + i * 0.14, scratch(0.12), 0.1)
add(T['allHit'], thud(120, 0.3), 0.22)
add(T['scan'], whoosh(0.35), 0.3); add(T['scanHit'], click(), 0.3); add(T['scanHit'] + 0.07, click(), 0.25)
add(T['thumbHit'] - 0.1, whoosh(0.25), 0.25); add(T['thumbHit'] + 0.05, thud(110, 0.25), 0.18)
for i in range(3): add(T['thumbHit'] + 0.3 + i * 0.18, tone(1046.5, 0.05, 3), 0.04)
add(T['small'], whoosh(0.3), 0.3); add(T['smallHit'], tone(880, 0.12, 3), 0.07); add(T['v2Hit'], tone(880, 0.12, 3), 0.07); add(T['v2Hit'] + 0.09, tone(740, 0.2, 3), 0.07)
add(T['againHit'], thud(150, 0.45), 0.34); add(T['againHit'] + 0.02, buzz(0.5), 0.11)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['agr'], whoosh(0.45), 0.35); add(T['agrHit'], ding(1046.5, 0.5), 0.06)
add(T['read'], whoosh(0.3), 0.15)
add(T['signHit'], scratch(0.5), 0.16)
add(T['thereHit'], ding(1568, 0.6), 0.08); add(T['thereHit'], thud(140, 0.2), 0.16)
for i, at in enumerate(T['after']): add(at - 0.1, whoosh(0.18), 0.18); add(at, ding(1046.5 * 2 ** (i * 2 / 12), 0.5), 0.075)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['coast'], whoosh(0.35), 0.3); add(T['coast'] + 0.3, thud(180, 0.15), 0.2); add(T['coastHit'], ding(1318.5, 0.5), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
