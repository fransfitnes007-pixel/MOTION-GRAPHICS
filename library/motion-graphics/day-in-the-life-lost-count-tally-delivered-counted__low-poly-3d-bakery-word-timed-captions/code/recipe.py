#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.259x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet bakery before opening: a low
oven hum. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.7
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(101)
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
def tick(f=1500): return tone(f, 0.035, 3) * 0.8
def chalk(d=0.13):                                                                 # one stroke on a board
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same') * np.sin(np.linspace(0, np.pi, n)) * (1 + 0.5 * np.sin(np.linspace(0, 60, n)))
def hum(d): n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 58 * t) * 0.6 + np.convolve(rng.standard_normal(n), np.ones(400) / 400, 'same') * 8
T = dict(part=2.2, con=3.62, twelveHit=4.44, cnt=5.76, cntHit=5.9, eleven=7.22, again=7.9, againHit=8.04, thirteen=9.06, brand=9.9, brandHit=10.24, nine=11.22,
         three=11.96, threeHit=12.22, job=13.48, jobHit=13.9, some=14.74, someHit=15.22, nobody=15.7, whichHit=16.28, tally=17.1, tallyHit=17.98, wall=18.45, wallHit=18.8,
         found=19.6, foundG=20.16, page=21.22, pageHit=22.0, deliv=23.14, sevenHit=23.64, twelve2=24.16, days=24.9, nineHit=25.32, every=26.54, cHit=27.46, ncHit=28.68,
         n=[29.82, 30.46], nobHit=31.24, it=32.4, itHit=32.6, baker=33.7, dozenHit=34.1, force=34.8, habitHit=35.04, end=35.7)
bed = hum(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.014)
add(T['part'], thud(120, 0.2), 0.14)
add(T['con'], whoosh(0.35), 0.3); add(T['twelveHit'], ding(1318.5, 0.5), 0.07); add(T['twelveHit'], thud(130, 0.2), 0.16)
add(T['cnt'], whoosh(0.35), 0.3)
for i in range(11): add(T['cntHit'] + (i + 0.5) * (T['eleven'] - T['cntHit']) / 11, tick(1000 + i * 45), 0.05)                        # counting: one, two, three...
add(T['eleven'], thud(140, 0.35), 0.28); add(T['eleven'] + 0.02, ding(1046.5, 0.4), 0.05)
for i in range(13): add(T['againHit'] + (i + 0.5) * (T['thirteen'] - T['againHit']) / 13, tick(1000 + i * 45), 0.05)
add(T['thirteen'], thud(150, 0.45), 0.32); add(T['thirteen'] + 0.02, buzz(0.4), 0.1)
add(T['brand'], whoosh(0.35), 0.3); add(T['brandHit'], pop(520), 0.07); add(T['nine'], thud(150, 0.45), 0.34); add(T['nine'] + 0.02, buzz(0.45), 0.11)
add(T['three'], whoosh(0.3), 0.26)
for i in range(3): add(T['threeHit'] + i * 0.14, pop(600 - i * 90), 0.08)
add(T['jobHit'], thud(140, 0.35), 0.26); add(T['jobHit'] + 0.03, slide(520, 240, 0.45), 0.07)
add(T['some'], whoosh(0.35), 0.3)
for i in range(6): add(T['someHit'] - 0.06 + i * 0.07, pop(480 + i * 30), 0.055)
add(T['whichHit'], thud(150, 0.45), 0.34); add(T['whichHit'] + 0.02, buzz(0.45), 0.11)
add(T['tally'], whoosh(0.3), 0.26)
for i in range(13): add(T['tally'] + 0.15 + (i / 13.2) * (T['wallHit'] - T['tally'] - 0.15), chalk(0.14 if i % 5 != 4 else 0.2), 0.16)   # thirteen chalk strokes
add(T['wallHit'], thud(150, 0.4), 0.3); add(T['wallHit'] + 0.03, slide(480, 220, 0.5), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['page'], whoosh(0.35), 0.3); add(T['pageHit'] - 0.1, pop(560), 0.07); add(T['pageHit'], pop(620), 0.07)
for i in range(7): add(T['deliv'] + (i / 7.99) * (T['twelve2'] - T['deliv']), tone(880 * 2 ** (i / 12), 0.12, 4), 0.05)              # seven ticks filling in
add(T['sevenHit'], ding(1318.5, 0.5), 0.07); add(T['sevenHit'], thud(130, 0.18), 0.14); add(T['nineHit'], ding(1568, 0.5), 0.07); add(T['nineHit'], thud(130, 0.18), 0.14)
add(T['every'], whoosh(0.35), 0.3)
for i in range(3): add(T['cHit'] - 0.06 + i * 0.1, whoosh(0.12), 0.12); add(T['cHit'] + i * 0.1, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
add(T['ncHit'], pop(420), 0.08); add(T['ncHit'] + 0.02, tone(660, 0.3, 5), 0.06); add(T['ncHit'] + 0.25, ding(1760, 0.5), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['it'], whoosh(0.3), 0.26); add(T['itHit'] + 0.22, thud(170, 0.2), 0.22); add(T['itHit'] + 0.26, pop(700), 0.06); add(T['itHit'] + 0.42, thud(170, 0.12), 0.1)
add(T['baker'], whoosh(0.3), 0.26); add(T['dozenHit'], ding(1318.5, 0.5), 0.07); add(T['habitHit'], ding(1568, 0.5), 0.07); add(T['habitHit'] + 0.1, ding(2093, 0.7), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
