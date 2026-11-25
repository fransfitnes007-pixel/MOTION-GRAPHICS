#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 2) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
bed of surf. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(71)
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
def pop(f=520): return slide(f, f * 1.9, 0.09)                                    # a message bubble
def swoosh_mail(): return np.concatenate([whoosh(0.3) * 0.8, tone(1568, 0.25, 6) * 0.25])
def clunk(f=220): return tone(f, 0.12, 6, (1, 0.6, 0.3))
def splash(d=0.6):                                                                 # a bottle hitting the water
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(14) / 14, 'same') * np.exp(-np.linspace(0, 6, n)) * 2.2
def surf(d):                                                                       # slow waves, a long way under the voice
    n = int(d * SR); t = np.arange(n) / SR; s = np.convolve(rng.standard_normal(n), np.ones(160) / 160, 'same') * 9; return s * (0.35 + 0.65 * np.sin(2 * np.pi * t / 6.2 + 0.6) ** 2)
T = dict(part=2.28, done=3.4, doneHit=3.9, send=4.56, sendHit=5.1, email=6.08, chip=6.3, largeHit=7.16, comp=8.38, compHit=8.5, mosaic=9.36, mosaicHit=9.86, wm=10.74, wmHit=11.72, face=12.54, faceHit=12.86,
         link=13.76, linkHit=14.28, cant=14.72, cantHit=15.1, fax=15.5, usb=16.04, usbHit=16.96, bottle=17.9, rel=18.0, bottleHit=18.5,
         found=18.9, foundG=19.52, drop=20.44, dropHit=20.9, appHit=21.7, posts=22.32, origHit=24.72, nowmHit=25.62, hqHit=26.05, chg=26.56, same=27.2, sameHit=27.42, resub=28.06, resubHit=28.34,
         n=[29.52, 30.4], nobHit=31.16, back=32.06, backHit=32.66, notes=33.26, notesHit=33.62, floppy=34.26, floppyHit=34.5, end=35.5)
bed = surf(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.03)
add(T['part'], thud(120, 0.2), 0.14)
add(T['done'], whoosh(0.3), 0.25); add(T['doneHit'], ding(1318.5, 0.5), 0.07); add(T['doneHit'] + 0.1, ding(1760, 0.6), 0.07)
add(T['send'], whoosh(0.3), 0.25); add(T['sendHit'], thud(140, 0.3), 0.26); add(T['sendHit'] + 0.05, slide(520, 260, 0.4), 0.06)
add(T['email'], whoosh(0.35), 0.3); add(T['chip'], pop(480), 0.07); add(T['largeHit'], thud(150, 0.45), 0.34); add(T['largeHit'] + 0.02, buzz(0.45), 0.11)
add(T['comp'], whoosh(0.35), 0.3)
for i in range(14): add(T['compHit'] + i * (T['mosaicHit'] - T['compHit']) / 14, buzz(0.07, 620 - i * 36), 0.05)                     # the video being crushed, lower each step
add(T['mosaicHit'], thud(150, 0.45), 0.32); add(T['mosaicHit'] + 0.02, buzz(0.4), 0.1)
add(T['wm'], whoosh(0.35), 0.3)
for k in range(4): add(T['wmHit'] + k * 0.09, tone(1400 + 300 * (k % 2), 0.07, 2), 0.035)                                          # a tacky jingle
add(T['face'], slide(300, 900, 0.34), 0.06); add(T['faceHit'], thud(150, 0.45), 0.34); add(T['faceHit'] + 0.02, buzz(0.45), 0.11)
add(T['link'], whoosh(0.35), 0.3); add(T['linkHit'], swoosh_mail(), 0.32)
add(T['cant'], pop(420), 0.05); add(T['cantHit'], pop(360), 0.08); add(T['cantHit'] + 0.03, thud(140, 0.3), 0.22)
add(T['fax'], pop(400), 0.08)
for i in range(8): add(T['fax'] + 0.1 + i * 0.045, tone(1100 if i % 2 else 2100, 0.045, 1), 0.022)                                 # a fax machine, briefly
add(T['usb'], whoosh(0.35), 0.3); add(T['usbHit'] - 0.2, slide(300, 700, 0.2), 0.05); add(T['usbHit'], click(), 0.35); add(T['usbHit'] + 0.02, thud(130, 0.3), 0.24)
add(T['bottle'], whoosh(0.25), 0.22); add(T['rel'], whoosh(0.4), 0.42); add(T['rel'] + 0.1, slide(500, 1100, 0.3), 0.04)
add(T['bottleHit'], splash(), 0.2); add(T['bottleHit'], thud(110, 0.3), 0.22); add(T['bottleHit'] + 0.12, pop(700), 0.05)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['drop'], whoosh(0.35), 0.3); add(T['dropHit'] - 0.2, slide(900, 300, 0.22), 0.05); add(T['dropHit'], thud(130, 0.3), 0.3); add(T['dropHit'] + 0.03, ding(1046.5, 0.5), 0.07)
add(T['appHit'], click(), 0.4); add(T['appHit'] + 0.04, slide(420, 1250, T['posts'] - 0.12 - T['appHit']), 0.045); add(T['posts'] - 0.12, ding(1760, 0.5), 0.07)
add(T['posts'], whoosh(0.35), 0.28); add(T['posts'] + 0.12, ding(1318.5, 0.6), 0.06)
for i, k in enumerate(['origHit', 'nowmHit', 'hqHit']): add(T[k] - 0.08, whoosh(0.14), 0.14); add(T[k], ding([1046.5, 1174.7, 1318.5][i], 0.45), 0.07); add(T[k], thud(130, 0.18), 0.12)
add(T['chg'], whoosh(0.3), 0.26); add(T['chg'] + 0.1, pop(520), 0.07); add(T['same'], pop(600), 0.06)
for i in range(12): add(T['sameHit'] + i * (T['resub'] - T['sameHit']) / 12 + (0.02 if i % 3 else 0), click(), 0.12)
add(T['resubHit'], click(), 0.4); add(T['resubHit'] + 0.03, ding(1760, 0.5), 0.07); add(T['resubHit'] + 0.16, pop(640), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['back'], whoosh(0.8), 0.34); add(T['backHit'], clunk(900), 0.1); add(T['backHit'] + 0.02, thud(140, 0.25), 0.2)
add(T['notes'], whoosh(0.3), 0.28); add(T['notesHit'], tone(2100, 0.25, 6), 0.07)
for i in range(3): add(T['notesHit'] + 0.08 + i * 0.07, click(), 0.12)                                                             # something rattling in the glass
add(T['floppy'], whoosh(0.35), 0.3); add(T['floppyHit'], thud(150, 0.45), 0.32); add(T['floppyHit'] + 0.02, buzz(0.4), 0.1)
for i in range(6): add(T['floppyHit'] + 0.28 + i * 0.075, buzz(0.05, 70 + (i % 2) * 22), 0.07)                                     # a disk drive grinding
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
