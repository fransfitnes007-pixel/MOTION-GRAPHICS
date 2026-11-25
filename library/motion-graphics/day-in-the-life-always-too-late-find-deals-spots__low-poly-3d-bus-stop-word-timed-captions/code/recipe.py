#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, take 1, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
bus stop: street traffic, a bus that hisses and pulls away. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.4
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(134)
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
def traffic(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(300) / 300, 'same') * 7
def engine(d, f0=60, f1=110):
    n = int(d * SR); f = np.linspace(f0, f1, n); s = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.5 + 0.3 * np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * 4
    e = np.ones(n); r = int(0.2 * SR); e[:r] = np.linspace(0, 1, r); e[-n // 3:] = np.linspace(1, 0, n // 3); return s * e
def hiss(d=0.6): n = int(d * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 4, n)) * 0.6
def steps(d, rate=7): n = int(d * SR); s = np.zeros(n); [s.__setitem__(slice(int(i / rate * SR), int(i / rate * SR) + 3000), thud(220, 0.0625)[:3000] * 0.8) for i in range(int(d * rate)) if int(i / rate * SR) + 3000 < n]; return s
def stampx(): return stampS()
T = dict(part=2.54, lateHit=4.2, weeksHit=5.72, d=[6.84, 8.84, 11.84], full=8.2, tueHit=11.04, bfHit=14.32, groupHit=7.3, threeHit=12.9, ran=15.32, busHit=16.42, missed=17.18,
         found=18.2, foundG=18.94, find=19.94, every=20.98, spotsHit=24.2, three=25.26, applyHit=26.54, applied=27.9, n=[28.84, 29.76], nobHit=30.64, bus2=31.48, leavesHit=32.06,
         driver=33.14, wavesHit=33.44, end=34.4)
add(0, traffic(T['end'] + 1), 0.012)
add(T['part'], thud(120, 0.2), 0.14); add(T['lateHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06); add(T['weeksHit'], tone(196, 0.5, 4, (1, 0.5)), 0.07)
for at in T['d']: add(at, whoosh(0.3), 0.26); add(at + 0.12, pop(540), 0.06)
add(T['groupHit'], slide(700, 1300, 0.12), 0.05)
for at in [T['full'], T['tueHit'] + 0.1, T['bfHit']]: add(at, stampx(), 0.3)
add(T['ran'], steps(T['busHit'] + 0.25 - T['ran']), 0.12); add(T['busHit'] - 0.4, hiss(0.6), 0.08); add(T['busHit'] - 0.3, engine(2.2), 0.06)
add(T['missed'], tone(220, 0.4, 5, (1, 0.5)), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['find'], whoosh(0.3), 0.26)
for i in range(3): add(T['every'] + 0.15 + i * 0.2, pop(560 + i * 50), 0.05)
add(T['spotsHit'], ding(1318.5, 0.5), 0.05); add(T['three'], pop(700), 0.06); add(T['applyHit'], click(), 0.25); add(T['applied'], ding(1568, 0.6), 0.07); add(T['applied'] + 0.08, ding(2093, 0.5), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['bus2'], steps(T['leavesHit'] - T['bus2']), 0.1); add(T['leavesHit'] - 0.3, hiss(0.6), 0.08); add(T['leavesHit'] - 0.2, engine(3.6, 55, 95), 0.06)
add(T['wavesHit'], tone(988, 0.3, 4, (1, 0.4)), 0.05); add(T['wavesHit'] + 0.15, tone(1318.5, 0.3, 4, (1, 0.4)), 0.04)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
