#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.17x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
tennis court: birds, a far rally, the ball machine's thunk. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.9
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(137)
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
def chirp(): n = int(0.12 * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(2600, 3800, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def thunk(): return thud(260, 0.12) * 0.9 + np.pad(click()[:800], (0, int(0.12 * SR) - 800)) * 0.4
def pock(): return tone(900, 0.07, 12, (1, 0.4)) + np.pad(click()[:600], (0, int(0.07 * SR) - 600)) * 0.5
def blip(): return slide(500, 900, 0.1)
def bark(): n = int(0.16 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(np.geomspace(520, 260, n)) / SR) * np.sign(np.sin(2 * np.pi * 90 * t)) * 0.5 * np.exp(-np.linspace(0, 5, n))
T = dict(part=2.66, deal=4.14, vnHit=4.9, shots=[5.72, 7.64, 8.84, 11.4], hits=[6.32, 8.24, 9.44, 12.8], dogHit=13.04, scroll=13.96, deleted=16.5, delHit=16.76,
         found=17.8, foundG=18.6, deal2=19.54, agrHit=20.44, readHit=22.26, signHit=23.02, counterHit=24.02, every=25.08, termHit=25.38, campHit=26.94, remHit=28.04,
         n=[29.8, 30.68], nobHit=31.56, brand=32.6, vn2Hit=33.68, dog2Hit=35.12, end=35.9)
for i in range(14): add(1.0 + i * 2.7 + (i % 3) * 0.4, chirp(), 0.012)
for i in range(10): add(0.6 + i * 1.6, pock(), 0.015)
add(T['part'], thud(120, 0.2), 0.14)
add(T['deal'], whoosh(0.3), 0.26); add(T['deal'] + 0.1, blip(), 0.06); add(T['vnHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
for a, b in zip(T['shots'], T['hits']): add(a, thunk(), 0.25); add(b, pock(), 0.3)
add(T['dogHit'], bark(), 0.08)
add(T['scroll'], whoosh(0.3), 0.26)
for i in range(18): add(T['scroll'] + 0.2 + i * 0.12, click(), 0.06)
for i in range(9): add(T['deleted'] + i * 0.08, thunk(), 0.12); add(T['deleted'] + 0.45 + i * 0.08, pock(), 0.12)
add(T['delHit'], stampS(), 0.3); add(T['delHit'] + 0.5, thud(110, 0.4), 0.28)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['deal2'], whoosh(0.3), 0.26); add(T['agrHit'], stampS(), 0.2)
add(T['readHit'], ding(1046.5, 0.4), 0.05); add(T['signHit'], slide(400, 900, 0.5), 0.04); add(T['signHit'] + 0.5, ding(1318.5, 0.4), 0.05); add(T['counterHit'], ding(1568, 0.6), 0.07); add(T['counterHit'] + 0.08, ding(2093, 0.5), 0.05)
add(T['every'], whoosh(0.3), 0.26); add(T['termHit'], pop(620), 0.06); add(T['campHit'], ding(1318.5, 0.5), 0.05); add(T['remHit'], pop(700), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['brand'], whoosh(0.3), 0.26); add(T['brand'] + 0.1, blip(), 0.06); add(T['vn2Hit'], tone(220, 0.4, 5, (1, 0.5)), 0.06)
add(T['dog2Hit'], bark(), 0.1); add(T['dog2Hit'] + 0.25, bark(), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
