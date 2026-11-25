#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.199x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(43)
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
def slide(f0, f1, d=0.35):
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def pop(f=520): return slide(f, f * 1.9, 0.09)                                    # a message bubble
def tick(f=1400): return tone(f, 0.04, 3) * 0.8                                   # the clock she is racing
def crickets(d):                                                                   # night falls
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 4300 * t) * (np.sin(2 * np.pi * 34 * t) > 0.2) * (np.sin(2 * np.pi * 1.6 * t) > 0) * np.minimum(1, np.linspace(0, 6, n)) * np.minimum(1, np.linspace(6, 0, n))
def birds(d):                                                                      # and a morning after it
    n = int(d * SR); s = np.zeros(n)
    for k in range(7): i = int((0.1 + k * 0.13 + rng.uniform(0, 0.05)) * d * SR); c = slide(2400 + rng.uniform(0, 900), 3400 + rng.uniform(0, 900), 0.09) ; s[i:i + len(c)] += c[:n - i]
    return s
T = dict(part=2.36, forty=3.98, fortyHit=4.24, login=6.28, loginHit=7.02, wrongHit=8.16, reset=9.16, resetHit=9.34, code=10.18, cantHit=11.4, tooHit=12.88, prove=13.98, humanHit=14.44, c1=15.6, c2=16.05, pole=16.96, poleHit=17.3, knowsHit=19.08,
         missedHit=20.16, gone=21.06, goneHit=21.84, found=22.98, foundG=23.7, sign=24.9, onceHit=25.46, add=26.08, addHit=26.66, tap=27.54, tapHit=27.64, opens=28.64, opensHit=28.8, signedHit=29.84, n=[31.1, 32.06], nob=32.86, still=33.88, human2=34.86, end=35.5)
for i in range(int((T['goneHit'] - T['fortyHit']) / 0.5)): add(T['fortyHit'] + i * 0.5, tick(1400 if i % 2 else 1100), 0.03 + 0.0012 * i)   # it gets louder as the light goes
add(16.5, crickets(T['found'] - 16.5 + 0.4), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['forty'], whoosh(0.3), 0.25); add(T['fortyHit'], ding(1318.5, 0.5), 0.07)
add(T['login'], whoosh(0.35), 0.3)
for i in range(10): add(T['login'] + 0.12 + i * 0.09, click(), 0.12)
add(T['wrongHit'], buzz(0.45), 0.11); add(T['wrongHit'], thud(150, 0.4), 0.3)
add(T['resetHit'], click(), 0.35); add(T['resetHit'] + 0.15, pop(520), 0.07)
add(T['code'], whoosh(0.3), 0.28); add(T['code'] + 0.15, pop(560), 0.07); add(T['cantHit'] - 0.1, whoosh(0.2), 0.2); add(T['cantHit'], thud(140, 0.3), 0.26); add(T['cantHit'], tone(587, 0.25, 3, (1, 0.4)), 0.06)
add(T['tooHit'] - 0.1, whoosh(0.2), 0.2); add(T['tooHit'], thud(150, 0.4), 0.32); add(T['tooHit'], tone(440, 0.3, 3, (1, 0.4)), 0.07); add(T['tooHit'] + 0.02, buzz(0.35), 0.08)
add(T['prove'], whoosh(0.35), 0.3); add(T['humanHit'], pop(480), 0.07)
add(T['c1'], click(), 0.4); add(T['c1'] + 0.03, tone(880, 0.1, 3), 0.06); add(T['c2'], click(), 0.4); add(T['c2'] + 0.03, tone(988, 0.1, 3), 0.06)
add(T['poleHit'], slide(420, 640, 0.2), 0.06); add(T['poleHit'] + 0.2, slide(440, 680, 0.2), 0.06)
add(T['knowsHit'], slide(520, 260, 0.4), 0.08); add(T['knowsHit'], thud(130, 0.3), 0.22)
add(T['missedHit'], buzz(0.5), 0.12); add(T['missedHit'], thud(150, 0.45), 0.34)
add(T['gone'], whoosh(0.4), 0.3); add(T['goneHit'], thud(120, 0.6), 0.34); add(T['goneHit'], tone(110, 1.0, 2, (1, 0.5, 0.3)), 0.09)
add(T['found'], whoosh(0.7), 0.4); add(T['found'] + 0.5, birds(1.6), 0.03)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(6): add(T['sign'] + 0.1 + i * 0.07, click(), 0.12)
add(T['onceHit'], ding(1318.5, 0.5), 0.07); add(T['onceHit'] + 0.1, ding(1760, 0.5), 0.07)
add(T['add'], whoosh(0.35), 0.3); add(T['addHit'], click(), 0.35); add(T['addHit'] + 0.03, ding(1568, 0.5), 0.07)
add(T['tap'] - 0.2, pop(620), 0.08); add(T['tapHit'], click(), 0.45); add(T['tapHit'] + 0.02, thud(120, 0.14), 0.16)
add(T['opens'], whoosh(0.35), 0.3); add(T['opensHit'] + 0.1, ding(1046.5, 0.5), 0.06); add(T['signedHit'], ding(1568, 0.6), 0.08); add(T['signedHit'], thud(130, 0.22), 0.18)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.3), 0.25); add(T['human2'], slide(520, 240, 0.45), 0.08); add(T['human2'], thud(140, 0.4), 0.3)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
