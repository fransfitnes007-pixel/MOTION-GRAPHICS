#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.18x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 41.2
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(10)
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
def shutter():                                                                    # a phone screenshot: two quick clicks
    n = int(0.05 * SR); c = rng.standard_normal(n) * np.exp(-np.linspace(0, 9, n)); out = np.zeros(int(0.16 * SR)); out[:n] += c; out[int(0.07 * SR):int(0.07 * SR) + n] += c * 0.8; return out
def key(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
T = dict(part=2.5, years=3.66, make=5.2, mathHit=7.24, shot=8.38, snaps=[8.9, 9.94, 10.9], sheet=11.64, tab=13.0, tabHit=13.38, inv=14.04, invHit=14.42, lowerHit=16.56, againHit=17.72, stamp=18.56, stampHit=19.22,
         notc=20.18, acct=21.46, acctHit=21.64, found=23.24, foundG=23.9, paste=25.1, pasteHit=25.64, once=25.86, tracks=27.06, earnedHit=29.5, paysHit=30.66, n=[31.68, 32.68], nob=33.76, del_=34.6, delHit=34.9, off=35.45, end=36.2)
add(T['part'], thud(120, 0.2), 0.14); add(T['years'], thud(100, 0.25), 0.12)
add(T['make'], whoosh(0.5), 0.25)
add(T['mathHit'], thud(130, 0.35), 0.28); 
for i in range(6): add(T['mathHit'] + 0.15 + i * 0.07, key(), 0.09)                                # calculator keys
add(T['shot'], whoosh(0.35), 0.3)
for at in T['snaps'] + [T['againHit'], T['stampHit'] + 0.3]: add(at, shutter(), 0.3)
for i in range(16): add(T['sheet'] + 0.1 + i * 0.075, key(), 0.07)                                 # typing into cells
for i in range(14): add(T['tab'] + i * 0.03, tone(900 + i * 60, 0.025, 2), 0.035)                  # tabs flying to 31
add(T['tabHit'] + 0.2, thud(140, 0.3), 0.24)
add(T['inv'], whoosh(0.3), 0.3); add(T['invHit'], tone(1046.5, 0.08, 3), 0.06)
add(T['lowerHit'], tone(880, 0.12, 3), 0.07); add(T['lowerHit'] + 0.09, tone(740, 0.2, 3), 0.07); add(T['lowerHit'] + 0.1, thud(110, 0.25), 0.16)
add(T['stamp'], whoosh(0.25), 0.25)
for i in range(4): add(T['stamp'] + 0.25 + i * 0.16, tone(1200, 0.03, 2), 0.05)                    # the clock she holds up
add(T['notc'], thud(100, 0.3), 0.16)
add(T['acct'], whoosh(0.4), 0.3); add(T['acctHit'], thud(130, 0.4), 0.3)
for i in range(8): add(T['acctHit'] + 0.3 + i * 0.1, key(), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['pasteHit'], key(), 0.2); add(T['pasteHit'] + 0.12, ding(1568, 0.5), 0.07); add(T['once'], thud(120, 0.25), 0.2)
add(T['tracks'] - 0.36, whoosh(0.45), 0.35)
for i in range(22): add(T['tracks'] + 0.1 + i * 0.09, tone(1800 + (i % 4) * 120, 0.02, 2), 0.022)   # counters ticking
for i in range(3): add(T['earnedHit'] - 0.1 + i * 0.1, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
add(T['paysHit'] - 0.1, ding(1568, 0.7), 0.08); add(T['paysHit'] - 0.1, thud(150, 0.18), 0.14)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['del_'], whoosh(0.3), 0.3); add(T['delHit'], key(), 0.25); add(T['delHit'] + 0.1, whoosh(0.5), 0.3)
n = int(0.4 * SR); add(T['delHit'] + 0.15, np.sin(2 * np.pi * np.cumsum(np.geomspace(600, 160, n)) / SR) * np.sin(np.linspace(0, np.pi, n)), 0.05)
add(T['off'], whoosh(0.35), 0.35); add(T['off'] + 0.1, ding(1318.5, 0.5), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
