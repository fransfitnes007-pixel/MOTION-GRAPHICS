#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.18x) plus
synthesised sounds on the demo's timeline (the T block in demo.html). No music.  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.4
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(8)
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
T = dict(part=2.5, yes=3.6, brand=6.0, now=7.92, n18=8.4, one=9.8, logs=[11.3, 11.96, 12.7], wrongHit=13.86, storHit=14.98, cant=15.64, post=17.08, dog=18.38, dogHit=18.7, doneHit=20.48,
         found=21.54, foundG=22.2, farm=23.28, real=24.82, their=25.84, zeroHit=27.84, steps=[28.72, 29.4, 30.1], posts=30.88, postHit=31.52, no=[32.66, 33.84], nob=34.56, end=35.4)
add(T['part'], thud(120, 0.2), 0.14)
for i in range(6): add(T['yes'] + 0.25 + i * 0.2, ding(880 * 2 ** (i * 2 / 12), 0.3), 0.05)        # six yeses
add(T['brand'], whoosh(0.35), 0.3)
for i in range(6): add(T['brand'] + 0.26 * i, tone(700, 0.04, 2), 0.04)
for i in range(12): add(T['now'] + 0.1 + i * 0.07, tone(700 + i * 40, 0.035, 2), 0.04)             # 6 to 18
add(T['one'], thud(110, 0.3), 0.2)
for i, at in enumerate(T['logs']): add(at, tone(1200 if i != 1 else 800, 0.06, 2), 0.06); add(at, whoosh(0.16), 0.2)
add(T['wrongHit'], thud(150, 0.4), 0.3); add(T['wrongHit'] + 0.02, buzz(0.45), 0.1)
add(T['storHit'], thud(140, 0.4), 0.3); add(T['storHit'] + 0.02, buzz(0.4), 0.1)
add(T['cant'] + 0.15, buzz(0.2), 0.06)
add(T['post'] - 0.1, whoosh(0.3), 0.3); add(T['dog'], whoosh(0.3), 0.3)
n = int(0.16 * SR); bark = np.sin(2 * np.pi * np.cumsum(np.geomspace(520, 300, n)) / SR) * np.exp(-np.linspace(0, 4, n)) * (1 + 0.6 * rng.standard_normal(n) * 0.2)
add(T['dogHit'] + 0.3, bark, 0.09); add(T['dogHit'] + 0.52, bark, 0.07)                            # the dog has questions
add(T['doneHit'], thud(120, 0.45), 0.34)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['farm'], whoosh(0.8), 0.4); add(T['farm'] + 0.1, tone(65.4, 1.4, 2), 0.12)
for i in range(20): add(T['real'] + i * 0.035, tone(1400 + (i % 5) * 120, 0.03, 2), 0.03)          # screens come on
for i in range(20): add(T['their'] + i * 0.03, tone(1800 + (i % 4) * 150, 0.025, 2), 0.025)
add(T['zeroHit'], ding(1568, 0.5), 0.07)
for i, at in enumerate(T['steps']): add(at, ding(1046.5 * 2 ** (i * 2 / 12), 0.5), 0.075); add(at - 0.1, whoosh(0.2), 0.2)
add(T['posts'], whoosh(0.5), 0.35)
for i in range(20): add(T['postHit'] + i * 0.04, tone(1318.5 * 2 ** ((i % 5) * 2 / 12), 0.05, 3), 0.03)
for k, f in enumerate([392, 523.3, 659.3, 784]): add(T['postHit'] + 0.3 + k * 0.03, tone(f, 1.4, 4), 0.05)
for at in T['no']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
