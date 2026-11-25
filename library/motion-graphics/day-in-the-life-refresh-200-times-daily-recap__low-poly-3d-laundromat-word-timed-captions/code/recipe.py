#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.9
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(23)
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
def drum(d):                                                                       # washers turning behind him: a slow slosh
    n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(160) / 160, 'same') * (0.6 + 0.4 * np.sin(2 * np.pi * 1.3 * t)) * np.minimum(1, np.linspace(0, 8, n)) * np.minimum(1, np.linspace(8, 0, n))
T = dict(part=2.25, post=3.44, refreshHit=5.6, countEnd=6.7, viewsHit=7.94, good=8.9, idk1Hit=10.06, mom=10.7, momHit=11.1, reply=11.7, proudHit=12.16, whatHit=12.72, last=13.12, greatHit=14.42, idk2Hit=15.4,
         copy=16.04, copyHit=16.52, flopHit=17.6, idk3Hit=18.94, found=19.86, foundG=20.4, tracked=21.52, trackedHit=22.04, recap=22.88, cardIn=23.12, recapHit=24.82, topHit=25.58, why=26.5, whyHit=27.42,
         next=27.96, bulb=28.6, nextHit=29.02, n=[30.14, 31.08], nob=31.74, laundry=32.78, doneHit=33.38, hoursHit=34.02, end=34.9)
add(0.0, drum(T['found'] + 0.6), 0.5)
add(T['part'], thud(120, 0.2), 0.14)
add(T['post'], whoosh(0.35), 0.3); add(T['post'] + 0.5, pop(700), 0.06)
for i in range(16): add(T['refreshHit'] + (i / 16) ** 0.75 * (T['countEnd'] - T['refreshHit']), slide(500 + i * 25, 900 + i * 35, 0.06), 0.05)   # pull to refresh, faster and faster
add(T['countEnd'], thud(140, 0.3), 0.22)
add(T['viewsHit'], thud(130, 0.3), 0.24); add(T['viewsHit'], tone(660, 0.2, 3), 0.05)
add(T['good'], whoosh(0.3), 0.25); add(T['good'] + 0.25, slide(400, 620, 0.25), 0.06)
add(T['idk1Hit'], slide(520, 300, 0.3), 0.07); add(T['idk1Hit'], thud(130, 0.25), 0.18)
add(T['mom'], whoosh(0.35), 0.3); add(T['momHit'], pop(620), 0.08)
for i in range(3): add(T['reply'] + i * 0.13, click(), 0.08)
add(T['proudHit'], pop(480), 0.09); add(T['proudHit'] + 0.03, ding(1568, 0.5), 0.05); add(T['whatHit'], pop(440), 0.09)
add(T['last'], whoosh(0.35), 0.3); add(T['greatHit'] - 0.45, slide(300, 900, 0.5), 0.06); add(T['greatHit'], ding(1318.5, 0.6), 0.07)
add(T['idk2Hit'], slide(520, 260, 0.35), 0.08); add(T['idk2Hit'], thud(130, 0.3), 0.22)
add(T['copy'], whoosh(0.3), 0.3); add(T['copyHit'] - 0.2, whoosh(0.2), 0.2); add(T['copyHit'], click(), 0.3); add(T['copyHit'] + 0.06, click(), 0.25)
add(T['flopHit'] - 0.2, slide(700, 150, 0.35), 0.08); add(T['flopHit'], thud(150, 0.45), 0.34); add(T['flopHit'] + 0.02, buzz(0.45), 0.1)
add(T['idk3Hit'] - 0.4, whoosh(0.3), 0.25); add(T['idk3Hit'], slide(520, 220, 0.45), 0.09); add(T['idk3Hit'], thud(130, 0.4), 0.3)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(12): add(T['tracked'] + 0.2 + i * 0.05, tone(500 + i * 45, 0.06, 3), 0.03)
add(T['trackedHit'], ding(1318.5, 0.5), 0.07); add(T['trackedHit'], thud(130, 0.2), 0.16)
add(T['recap'], whoosh(0.4), 0.3); add(T['cardIn'], pop(560), 0.09); add(T['cardIn'] + 0.1, tone(880, 0.12, 3), 0.06); add(T['cardIn'] + 0.2, tone(1174.7, 0.2, 3), 0.06)
add(T['recapHit'], thud(130, 0.2), 0.16)
for i in range(3): add(T['topHit'] + i * 0.14 - 0.05, whoosh(0.14), 0.14); add(T['topHit'] + i * 0.14, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.06)
add(T['why'], whoosh(0.25), 0.2); add(T['why'] + 0.2, ding(1568, 0.5), 0.06); add(T['whyHit'], thud(130, 0.3), 0.24); add(T['whyHit'], ding(2093, 0.6), 0.06)
add(T['next'], whoosh(0.3), 0.25); add(T['bulb'], ding(2637, 0.5), 0.07); add(T['bulb'], click(), 0.2); add(T['nextHit'], thud(130, 0.25), 0.2); add(T['nextHit'], ding(1318.5, 0.5), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['laundry'], whoosh(0.35), 0.3)
for k in range(3): add(T['doneHit'] + k * 0.28, tone(1975.5, 0.12, 2), 0.05)                                                      # the washer's finished beep, still going
add(T['hoursHit'], thud(150, 0.4), 0.3); add(T['hoursHit'] + 0.25, slide(500, 250, 0.4), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
