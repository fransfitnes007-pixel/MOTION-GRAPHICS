#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
greenhouse: rain on the glass before the turn, birds after it. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.4
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
def rain(d):
    n = int(d * SR); out = np.convolve(rng.standard_normal(n), np.ones(8) / 8, 'same') * 0.6; k = 0
    while k < n - 600: out[k:k + 300] += rng.standard_normal(300) * np.exp(-np.linspace(0, 8, 300)) * 2.5; k += int(SR * (0.01 + rng.random() * 0.05))
    return out
def chirp(f): return np.concatenate([slide(f, f * 1.5, 0.06), np.zeros(int(0.03 * SR)), slide(f * 1.1, f * 1.6, 0.05)])
def shine(): return sum(tone(f, 0.6, 5) * 0.3 for f in [2093, 2637, 3136])
T = dict(part=2.28, make=3.6, gardenHit=3.92, offers=5.38, shampooHit=6.3, bald=7.2, baldHit=7.5, stroller=8.12, kidsHit=9.56, wax=10.4, bikeHit=11.58, yes=12.3, yesHit=12.6, asked=14.14, hairHit=15.5,
         found=16.12, foundG=16.8, pick=17.7, intHit=18.2, gardHit=19.35, every=20.24, fitsHit=21.42, notfit=22.14, nfHit=22.44, applyHit=23.98, so=24.68, seeds=26.1, soil=27.1, trowel=28.44,
         n=[29.58, 30.4], nobHit=31.32, brand2=32.34, emailsHit=33.48, still=34.3, baldHit2=34.58, end=35.4)
r = rain(T['found'] + 0.8); r[-int(0.8 * SR):] *= np.linspace(1, 0, int(0.8 * SR)); r[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, r, 0.012)
for at in [17.4, 19.9, 22.9, 25.3, 27.9, 30.9, 33.1]: add(at, chirp(2400 + rng.random() * 800), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['make'], whoosh(0.3), 0.26); add(T['gardenHit'], ding(1318.5, 0.5), 0.06)
add(T['offers'], whoosh(0.35), 0.3)
for k in ['shampooHit', 'stroller', 'wax']: add(T[k], pop(520), 0.07)
add(T['bald'], whoosh(0.25), 0.2); add(T['baldHit'], shine(), 0.06); add(T['baldHit'] + 0.05, thud(140, 0.3), 0.2)
for k in ['kidsHit', 'bikeHit']: add(T[k], stampS(), 0.3)
add(T['stroller'] - 0.02, stampS(), 0.26)                                                                                   # the BALD stamp, seen on the cut back
add(T['yes'], whoosh(0.3), 0.26); add(T['yesHit'], pop(640), 0.08); add(T['yesHit'] + 0.05, slide(800, 1600, 0.2), 0.04)
add(T['hairHit'] - 0.1, pop(480), 0.07); add(T['hairHit'], pop(420), 0.08); add(T['hairHit'] + 0.25, thud(150, 0.45), 0.3); add(T['hairHit'] + 0.27, buzz(0.4), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['pick'], whoosh(0.35), 0.3)
for i in range(10): add(T['intHit'] - 0.1 + i * 0.04, pop(500 + i * 25), 0.03)
add(T['gardHit'], click(), 0.4); add(T['gardHit'] + 0.03, ding(1568, 0.5), 0.07)
add(T['every'], whoosh(0.35), 0.3); add(T['every'] + 0.05, pop(560), 0.06); add(T['every'] + 0.21, pop(600), 0.06)
add(T['nfHit'], tone(660, 0.35, 5, (1, 0.4)), 0.08); add(T['nfHit'] + 0.12, tone(587, 0.4, 5, (1, 0.4)), 0.07)
add(T['applyHit'], click(), 0.4); add(T['applyHit'] + 0.03, ding(1318.5, 0.4), 0.07)
add(T['so'], whoosh(0.3), 0.24)
add(T['seeds'], pop(700), 0.07); add(T['seeds'] + 0.05, ding(1046.5, 0.4), 0.06); add(T['soil'] - 0.1, whoosh(0.2), 0.2); add(T['soil'] + 0.05, thud(100, 0.35), 0.3); add(T['soil'] + 0.05, ding(1318.5, 0.4), 0.05)
add(T['trowel'], slide(800, 1600, 0.2), 0.05); add(T['trowel'] + 0.3, shine(), 0.07); add(T['trowel'] + 0.3, ding(1568, 0.6), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['brand2'], whoosh(0.3), 0.26); add(T['brand2'] + 0.1, pop(480), 0.07); add(T['emailsHit'], pop(520), 0.07); add(T['emailsHit'] + 0.35, pop(560), 0.07)
add(T['still'], whoosh(0.25), 0.2); add(T['baldHit2'], shine(), 0.07); add(T['baldHit2'] + 0.03, thud(150, 0.4), 0.28); add(T['baldHit2'] + 0.1, slide(480, 220, 0.5), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
