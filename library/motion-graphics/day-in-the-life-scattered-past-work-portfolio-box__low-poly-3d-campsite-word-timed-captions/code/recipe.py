#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, take 1, sped 1.123x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
campsite: a crackling fire under everything, louder after the turn. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.8
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(128)
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
def crackle(d, dens=14):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * 0.6
    for at in rng.uniform(0, d, int(d * dens)):
        i = int(at * SR); k = click()[: n - i] * rng.uniform(0.2, 1.0); s[i:i + len(k)] += k
    return s
def splash(d=0.9):
    n = int(d * SR); w = rng.standard_normal(n); w = np.convolve(w, np.ones(12) / 12, 'same') * np.exp(-np.linspace(0, 4.5, n)); return w * 2.4 + thud(90, d) * 0.6
T = dict(part=2.42, film=3.46, campHit=3.7, brand=4.66, pastHit=5.56, made=6.52, threeHit=6.82, one=8.0, pnfHit=9.8, two=10.52, delHit=11.42, three=12.36, lapHit=13.06, homeHit=13.98,
         out=14.64, sigHit=15.54, so=16.3, coolerHit=17.1, canoe=17.72, canoeHit=17.82, tree=18.4, treeHit=18.52, replied=19.18, linkHit=20.32, fell=21.24, lakeHit=21.8,
         found=22.54, foundG=23.28, port=24.18, profHit=25.38, link=26.22, pdfHit=26.94, once=28.04, every=28.6, applyHit=29.16, thereHit=30.14,
         n=[31.16, 32.0], nobHit=32.76, fish=33.6, bootHit=34.32, stay=34.9, stayHit=35.12, end=35.8)
add(0, crackle(T['found']), 0.02); add(T['found'], crackle(T['end'] - T['found'] + 0.4, 22), 0.035)
add(T['part'], thud(120, 0.2), 0.14); add(T['campHit'], ding(1318.5, 0.5), 0.05)
for k in ['brand', 'one', 'two', 'three', 'replied', 'port', 'every']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.05, pop(540), 0.06)
add(T['pastHit'], slide(500, 900, 0.2), 0.04); add(T['threeHit'], pop(660), 0.06)
for k in ['pnfHit', 'delHit', 'homeHit']: add(T[k], tone(220, 0.35, 5, (1, 0.5)), 0.08)
add(T['lapHit'], pop(600), 0.05)
add(T['out'], whoosh(0.3), 0.2); add(T['sigHit'], buzz(0.3, 70), 0.05)
for k in ['so', 'canoe', 'tree']: add(T[k], whoosh(0.3), 0.22); add(T[k] + 0.08, thud(200, 0.12), 0.2); add(T[k] + 0.2, thud(180, 0.12), 0.16)
for i, k in enumerate(['coolerHit', 'canoeHit', 'treeHit']): add(T[k], tone(660 + i * 220, 0.25, 7, (1, 0.3)), 0.05)
for i in range(3): add(T['treeHit'] + 0.2 + i * 0.12, slide(700, 1300, 0.12), 0.03)
add(T['linkHit'], tone(330, 0.4, 5, (1, 0.4)), 0.07)
add(T['lakeHit'] - 0.48, slide(1200, 300, 0.5), 0.07); add(T['lakeHit'], splash(1.0), 0.32); add(T['lakeHit'] + 0.05, stampS(), 0.18)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['profHit'], pop(620), 0.06); add(T['link'], click(), 0.2); add(T['link'] + 0.62, ding(1318.5, 0.5), 0.06); add(T['pdfHit'], ding(1568, 0.5), 0.06)
add(T['once'], whoosh(0.25), 0.2); add(T['once'] + 0.08, ding(1046.5, 0.5), 0.05)
add(T['applyHit'], click(), 0.2); add(T['thereHit'], ding(1318.5, 0.6), 0.07); add(T['thereHit'] + 0.08, ding(1760, 0.5), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['fish'], whoosh(0.25), 0.2); add(T['bootHit'] - 0.05, splash(0.3), 0.1)
for i in range(6): add(T['bootHit'] + 0.32 + i * 0.13, thud(260, 0.08), 0.12 - i * 0.015)
add(T['stay'], whoosh(0.25), 0.18); add(T['stayHit'], ding(1046.5, 0.5), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
