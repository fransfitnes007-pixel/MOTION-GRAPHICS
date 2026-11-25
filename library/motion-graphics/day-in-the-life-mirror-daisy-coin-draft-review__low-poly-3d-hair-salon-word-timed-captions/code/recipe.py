#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.251x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet salon: a hood dryer humming
somewhere behind her. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.6
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(127)
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
def shimmer(): return sum(tone(f, 0.9, 5) * 0.3 for f in [1568, 2093, 2637, 3136])                      # a mirror "speaking"
def pluck(): return np.concatenate([click()[:600] * 0.8, slide(900, 1400, 0.06) * 0.6])                       # a petal pulled
def ping(): return tone(2637, 0.6, 3, (1, 0.6, 0.2, 0.1))                                                    # the coin
def dryer(d): n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * 5 + np.sin(2 * np.pi * 120 * t) * 0.15
T = dict(part=2.3, ask=3.74, mirror=5.22, mirrorHit=5.74, says=6.46, tiredHit=7.78, daisy=8.7, daisyHit=9.74, p1=10.56, dont=11.34, p2=12.04, flip=12.86, coinHit=13.24, heads=13.92,
         post=14.58, viewsHit=15.88, left=16.72, twoHit=17.56, found=18.26, foundG=18.85, upload=19.72, draftHit=20.28, postHit=21.18, says2=21.86, noHit=22.56,
         hook=24.4, lateHit=25.22, dead=26.02, fourHit=26.66, fix=27.42, bothHit=27.66, yesHit=28.38, n=[30.04, 30.78], nobHit=31.64, still=32.5, tired2=33.68, rightHit=35.04, end=35.6)
bed = dryer(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.012)
add(T['part'], thud(120, 0.2), 0.14)
add(T['ask'], whoosh(0.3), 0.24); add(T['ask'] + 0.6, tone(660, 0.25, 4), 0.04); add(T['ask'] + 0.8, tone(740, 0.3, 4), 0.04)               # a small "hmm?"
add(T['mirror'], whoosh(0.35), 0.3); add(T['says'], shimmer(), 0.06); add(T['tiredHit'], thud(150, 0.45), 0.3); add(T['tiredHit'] + 0.03, slide(520, 260, 0.45), 0.07)
add(T['daisy'], whoosh(0.3), 0.26); add(T['daisyHit'], pop(700), 0.06)
for i, (k, good) in enumerate([('p1', 1), ('dont', 0), ('p2', 1)]): add(T[k] - 0.12, pluck(), 0.22); add(T[k] + 0.02, ding(1568, 0.3) if good else buzz(0.25, 110), 0.06 if good else 0.07)
add(T['coinHit'] - 0.05, click(), 0.3); add(T['coinHit'], ping(), 0.07)
for i in range(6): add(T['coinHit'] + 0.08 + i * 0.1, whoosh(0.06), 0.06)
add(T['heads'] - 0.04, click(), 0.35); add(T['heads'], ding(1318.5, 0.4), 0.07)
add(T['post'], whoosh(0.35), 0.3); add(T['viewsHit'], pop(420), 0.07); add(T['viewsHit'] + 0.02, thud(130, 0.2), 0.14)
add(T['left'], slide(900, 160, 0.9), 0.06); add(T['twoHit'], thud(150, 0.45), 0.34); add(T['twoHit'] + 0.02, buzz(0.45), 0.11)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['upload'], whoosh(0.35), 0.3); add(T['draftHit'] - 0.2, slide(900, 300, 0.22), 0.05); add(T['draftHit'], thud(130, 0.3), 0.28); add(T['draftHit'] + 0.03, ding(1046.5, 0.5), 0.07)
add(T['postHit'], click(), 0.4); add(T['postHit'] + 0.04, slide(420, 1250, T['says2'] - 0.14 - T['postHit']), 0.045)
add(T['says2'], whoosh(0.3), 0.26); add(T['noHit'], tone(660, 0.35, 5, (1, 0.4)), 0.08); add(T['noHit'] + 0.12, tone(587, 0.4, 5, (1, 0.4)), 0.07)        # "not yet"
add(T['lateHit'], pop(520), 0.07); add(T['lateHit'] + 0.03, thud(130, 0.2), 0.14); add(T['fourHit'], buzz(0.2, 140), 0.05); add(T['fourHit'] + 0.02, pop(380), 0.07)
add(T['fix'], whoosh(0.25), 0.2)
for i in range(2): add(T['bothHit'] + i * 0.12, ding(1318.5 * 2 ** (i * 4 / 12), 0.4), 0.07)
add(T['yesHit'], ding(1318.5, 0.5), 0.07); add(T['yesHit'] + 0.1, ding(1760, 0.6), 0.07); add(T['yesHit'] + 0.2, ding(2093, 0.8), 0.06); add(T['yesHit'], thud(130, 0.2), 0.16)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.35), 0.3); add(T['tired2'] - 0.4, shimmer(), 0.05); add(T['rightHit'], thud(150, 0.45), 0.3); add(T['rightHit'] + 0.03, slide(480, 220, 0.5), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
