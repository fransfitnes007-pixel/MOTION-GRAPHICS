#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.13x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
playroom: a quiet room tone, a ticking nap timer until the nap is over. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.6
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(131)
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
def tick(): return click()[:500] * 0.5
def bell2(): return np.concatenate([tone(988, 0.35, 4, (1, 0.4)), tone(784, 0.6, 4, (1, 0.4))])
def bark(): n = int(0.16 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(np.geomspace(520, 260, n)) / SR) * np.sign(np.sin(2 * np.pi * 90 * t)) * 0.5 * np.exp(-np.linspace(0, 5, n))
def snap(): return np.concatenate([click()[:900] * 1.2, thud(260, 0.08) * 0.6])
def cry(d=0.9): n = int(d * SR); t = np.arange(n) / SR; f = 520 + 80 * np.sin(2 * np.pi * 3 * t); return np.sin(2 * np.pi * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sin(2 * np.pi * 5 * t)) * np.sin(np.linspace(0, np.pi, n))
T = dict(part=2.68, mom=3.88, twoHit=4.28, get=5.16, napHit=5.7, minHit=7.04, take=[8.29, 10.05, 11.91], doorHit=9.02, dogHit=10.92, sonHit=12.84, prodHit=13.8, then=14.78,
         brollHit=15.66, screen=16.52, recHit=17.02, over=17.92, overHit=18.7, found=19.7, foundG=20.56, brief=21.58, bankHit=22.68, clips=23.68, ready=25.34, only=26.17,
         partHit=27.0, takeHit=27.92, napHit2=28.78, n=[29.82, 30.64], nobHit=31.46, loved=32.4, lovedHit=32.82, asked=33.86, availHit=34.72, end=35.6)
for i in range(int((T['overHit'] - T['get']) * 2)): add(T['get'] + i * 0.5, tick(), 0.05)
add(T['part'], thud(120, 0.2), 0.14); add(T['twoHit'], ding(1318.5, 0.4), 0.05); add(T['napHit'], pop(600), 0.05); add(T['minHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
for at in T['take']: add(at, snap(), 0.3)
add(T['doorHit'], bell2(), 0.08); add(T['doorHit'] + 0.15, stampS(), 0.25)
for i in range(3): add(T['dogHit'] - 0.15 + i * 0.22, bark(), 0.14)
add(T['dogHit'] + 0.15, stampS(), 0.25)
add(T['sonHit'], pop(700), 0.06); add(T['prodHit'] + 0.1, stampS(), 0.25)
for k in ['then', 'brief', 'clips', 'loved']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.05, pop(540), 0.06)
add(T['brollHit'], pop(480), 0.06); add(T['recHit'], pop(440), 0.06)
add(T['over'], whoosh(0.25), 0.2); add(T['overHit'] - 0.1, cry(1.0), 0.06); add(T['overHit'] + 0.05, thud(110, 0.4), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['bankHit'], ding(1318.5, 0.5), 0.05)
for i in range(6): add(T['clips'] + 0.1 + i * 0.12, pop(560 + i * 40), 0.04)
add(T['ready'], ding(1568, 0.6), 0.06)
add(T['only'], snap(), 0.3); add(T['takeHit'], ding(1046.5, 0.5), 0.05); add(T['napHit2'], ding(1318.5, 0.5), 0.05); add(T['napHit2'] + 0.08, ding(1760, 0.5), 0.04)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['lovedHit'], pop(620), 0.06); add(T['asked'] + 0.2, pop(500), 0.07); add(T['availHit'], ding(1318.5, 0.5), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
