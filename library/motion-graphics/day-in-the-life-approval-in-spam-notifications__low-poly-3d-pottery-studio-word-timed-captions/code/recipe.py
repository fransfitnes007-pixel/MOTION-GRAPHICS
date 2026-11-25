#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, take 1, pauses capped
at 0.3 s, then sped 1.3x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet pottery
studio: the wheel's motor hum while it spins. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 42.2
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
def stampS(): return np.concatenate([thud(170, 0.12) * 0.8, click()[:800] * 0.6])
def squelch(d=0.35):
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(90) / 90, 'same') * np.exp(-np.linspace(0, 5, n)) * 6 + thud(90, d) * 0.5
def hum(d, f=58):
    n = int(d * SR); t = np.arange(n) / SR; s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.08 * np.convolve(rng.standard_normal(n), np.ones(30) / 30, 'same')
    e = np.ones(n); r = min(n // 4, int(0.3 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e
def vib(d=0.6):
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 150 * t) * (np.sin(2 * np.pi * 9 * t) > 0) * np.exp(-np.linspace(0, 1.5, n))
T = dict(part=2.2, make=3.18, potHit=3.36, sent=4.48, nineHit=5.26, now=5.98, wordHit=6.96, email=7.54, noth1=8.16, insta=8.78, noth2=9.22, req=10.04, sungHit=11.38,
         group=12.3, thanks=13.38, thanksHit=14.34, every=15.12, check=15.54, fallsHit=16.34, four=17.18, pmHit=17.26, spam=17.86, apprHit=18.8, at=19.38, post=20.46, noonHit=20.8,
         found=21.4, foundG=22.1, draft=22.84, draftHit=22.98, when=24.06, apprHit2=24.28, notif=25.12, disc=26.22, discHit=26.8, hands=27.46, clayHit=28.44, there=28.98, contentHit=29.82,
         n=[31.14, 32.04], nobHit=32.86, done=33.48, doneHit=33.84, buzz=34.44, buzzHit=34.76, jump=35.3, jumpHit=35.4, ash=35.98, ashHit=36.24, end=37.2)
for a, b in [(0, T['sent']), (T['every'], T['four']), (T['hands'], T['there']), (T['done'], T['jump'] + 0.4), (T['ash'], T['end'])]: add(a, hum(b - a), 0.018)
add(T['part'], thud(120, 0.2), 0.14)
add(T['make'], whoosh(0.3), 0.24); add(T['potHit'], ding(1318.5, 0.5), 0.05)
add(T['sent'], whoosh(0.3), 0.24); add(T['nineHit'], click(), 0.5); add(T['nineHit'] + 0.02, ding(1046.5, 0.4), 0.05)
add(T['now'], whoosh(0.3), 0.22); add(T['wordHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
for k in ['email', 'insta', 'req', 'group']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.05, pop(520), 0.06); add(T[k] + 0.15, squelch(0.18), 0.05)
for k in ['noth1', 'noth2']: add(T[k], tone(220, 0.35, 5, (1, 0.5)), 0.08)
add(T['sungHit'] - 0.1, pop(600), 0.07); add(T['sungHit'], slide(900, 400, 0.3), 0.05)
for i in range(9): add(T['thanks'] + i / 9, pop(560 + (i % 3) * 60), 0.035)
add(T['every'], whoosh(0.3), 0.24); add(T['fallsHit'] - 0.05, squelch(0.45), 0.16); add(T['fallsHit'] + 0.05, slide(400, 150, 0.4), 0.05)
add(T['four'], whoosh(0.3), 0.24); for_ = [add(T['four'] + i * 0.05, click(), 0.25) for i in range(8)]; add(T['pmHit'] + 0.15, thud(150, 0.3), 0.2)
add(T['spam'], whoosh(0.3), 0.26); add(T['apprHit'], ding(1318.5, 0.5), 0.06); add(T['at'], pop(700), 0.06); add(T['post'], pop(480), 0.07)
add(T['noonHit'], stampS(), 0.32); add(T['noonHit'] + 0.22, squelch(0.5), 0.22); add(T['noonHit'] + 0.24, thud(110, 0.4), 0.2)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['draft'], whoosh(0.35), 0.28); add(T['draftHit'], pop(560), 0.06)
add(T['when'], whoosh(0.35), 0.28); add(T['apprHit2'], ding(1568, 0.5), 0.06); add(T['notif'], pop(620), 0.07); add(T['notif'] + 0.05, slide(700, 1400, 0.2), 0.04)
add(T['disc'], whoosh(0.35), 0.28); add(T['discHit'], tone(880, 0.3, 6, (1, 0.3)), 0.07); add(T['discHit'] + 0.09, tone(1175, 0.35, 6, (1, 0.3)), 0.07)
add(T['hands'], whoosh(0.3), 0.22); add(T['clayHit'], squelch(0.25), 0.05)
add(T['there'], whoosh(0.3), 0.22); add(T['contentHit'] - 0.06, vib(0.35), 0.05); add(T['contentHit'], ding(1318.5, 0.6), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['done'], whoosh(0.3), 0.22); add(T['doneHit'], ding(1046.5, 0.5), 0.06); add(T['doneHit'] + 0.08, ding(1568, 0.6), 0.05)
add(T['buzz'], whoosh(0.25), 0.2); add(T['buzzHit'], vib(0.6), 0.12)
add(T['jumpHit'], slide(500, 1300, 0.18), 0.06); add(T['jumpHit'] + 0.02, squelch(0.35), 0.18)
add(T['ash'], whoosh(0.25), 0.2); add(T['ashHit'], slide(480, 220, 0.5), 0.06); add(T['ashHit'] + 0.02, thud(150, 0.3), 0.18)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
