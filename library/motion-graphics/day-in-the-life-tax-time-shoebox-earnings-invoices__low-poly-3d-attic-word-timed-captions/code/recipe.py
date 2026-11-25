#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 2, sped 1.219x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
attic: rain on the roof until the turn, then quiet candlelight. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.85
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(129)
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
def rainS(d):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same') * 0.5
    for at in rng.uniform(0, d, int(d * 40)):
        i = int(at * SR); k = click()[: n - i] * rng.uniform(0.1, 0.5); s[i:i + len(k)] += k
    e = np.ones(n); r = int(0.4 * SR); e[-r:] = np.linspace(1, 0, r); return s * e
def paper(d=0.25):
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(4) / 4, 'same') * np.sin(np.linspace(0, np.pi, n)) * 0.8
T = dict(part=2.5, tax=3.64, taxHit=3.82, my=4.8, numHit=5.92, what=6.7, earnHit=7.0, b1=8.42, bankHit=9.26, stmt=10.42, xferHit=11.38, b2=12.58, appHit=13.82, kevinHit=14.86,
         b3=15.88, candHit=17.08, found1=18.08, boxHit=18.46, was=19.92, shoesHit=20.08, found=20.88, foundG=21.66, every=22.62, earnHit2=23.92, every2=25.12, invHit=26.42,
         paidHit=27.78, showed=28.46, pageHit=29.26, n=[30.82, 31.64], nobHit=32.5, wrote=33.34, greatHit=34.2, now=34.86, year=35.28, end=35.85)
add(0, rainS(T['found'] + 0.3), 0.03)
add(T['part'], thud(120, 0.2), 0.14)
add(T['tax'], whoosh(0.3), 0.22); add(T['taxHit'], tone(196, 0.5, 4, (1, 0.5)), 0.08)
for k in ['my', 'b1', 'b2', 'every', 'every2', 'wrote']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.05, pop(540), 0.06)
add(T['numHit'], slide(500, 900, 0.2), 0.04)
add(T['what'], whoosh(0.25), 0.2); add(T['earnHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
for i in range(5): add(T['b1'] + 0.15 + i * 0.12, click(), 0.12)
add(T['xferHit'], tone(220, 0.35, 5, (1, 0.5)), 0.08); add(T['appHit'], ding(1318.5, 0.4), 0.05); add(T['kevinHit'], tone(220, 0.35, 5, (1, 0.5)), 0.08)
add(T['b3'], whoosh(0.3), 0.22); add(T['candHit'] - 0.02, thud(110, 0.4), 0.32)
for i in range(20): add(T['candHit'] + 0.05 + i / 22, slide(900 + (i % 4) * 80, 1500, 0.05), 0.012)
add(T['found1'], whoosh(0.3), 0.22); add(T['boxHit'], paper(0.3), 0.08); add(T['shoesHit'] - 0.2, paper(0.2), 0.08); add(T['shoesHit'], stampS(), 0.3); add(T['shoesHit'] + 0.4, slide(400, 150, 0.45), 0.05)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(3): add(T['every'] + 0.3 + i * 0.25, pop(600 + i * 60), 0.05)
add(T['earnHit2'], ding(1318.5, 0.5), 0.05)
for i in range(3): add(T['every2'] + 0.2 + i * 0.32, pop(560 + i * 60), 0.05)
add(T['invHit'], pop(700), 0.05)
for i in range(3): add(T['paidHit'] + i * 0.08, ding(1568 + i * 200, 0.35), 0.045)
add(T['showed'] + 0.05, whoosh(0.4), 0.2); add(T['pageHit'], ding(1046.5, 0.5), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['greatHit'], pop(620), 0.06); add(T['now'], pop(480), 0.07); add(T['year'], tone(196, 0.6, 4, (1, 0.5)), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
