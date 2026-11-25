#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, take 1, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
street corner: a sizzling grill under everything. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.2
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(132)
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
def sizzle(d):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(3) / 3, 'same') * 0.35
    for at in rng.uniform(0, d, int(d * 30)):
        i = int(at * SR); k = click()[: n - i] * rng.uniform(0.1, 0.4); s[i:i + len(k)] += k
    return s
def roll(d=0.6): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * 5 * (0.6 + 0.4 * np.sin(np.linspace(0, 16 * np.pi, n)))
def clip_(): return np.concatenate([click()[:700], np.zeros(300), click()[:500] * 0.6])
T = dict(part=2.48, run=3.48, truckHit=4.1, my=5.04, contactHit=5.4, mon=7.4, h=[9.2, 11.76, 15.66], wed=9.92, fri=12.54, briefHit=16.62, again=17.44, sent=18.3, elevenHit=19.1,
         so=20.48, paintHit=21.12, truckHit2=21.72, found=22.4, foundG=23.2, quest=24.24, ticketHit=24.96, whole=25.46, threadHit=27.04, teamHit=27.68, nothing=29.08, lostHit=29.48,
         n=[30.54, 31.2], nobHit=31.98, back=33.06, backHit=33.3, h4=34.48, end=35.2)
add(0, sizzle(T['end'] + 1), 0.018)
add(T['part'], thud(120, 0.2), 0.14); add(T['truckHit'], ding(1318.5, 0.4), 0.05); add(T['contactHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
for k in ['mon', 'wed', 'fri', 'quest', 'whole']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.15, pop(540), 0.06)
for at in T['h']: add(at, slide(700, 1300, 0.12), 0.05); add(at + 0.02, clip_(), 0.2)
add(T['briefHit'], pop(480), 0.07); add(T['briefHit'] + 0.02, clip_(), 0.2)
add(T['again'] + 0.05, stampS(), 0.3)
add(T['sent'], whoosh(0.25), 0.2)
for i in range(7): add(T['elevenHit'] + i * 0.06, clip_(), 0.12)
add(T['so'], whoosh(0.25), 0.2); add(T['paintHit'] - 0.1, roll(0.8), 0.08); add(T['truckHit2'] + 0.1, stampS(), 0.3)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['ticketHit'], ding(1318.5, 0.5), 0.06)
for i in range(3): add(T['whole'] + 0.1 + i * 0.35, pop(560 + i * 50), 0.05)
add(T['threadHit'], ding(1046.5, 0.5), 0.05); add(T['teamHit'], ding(1568, 0.5), 0.06)
add(T['lostHit'], ding(1318.5, 0.5), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['back'], whoosh(0.25), 0.2); add(T['backHit'], tone(988, 0.3, 4, (1, 0.4)), 0.05); add(T['h4'], tone(196, 0.6, 4, (1, 0.5)), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
