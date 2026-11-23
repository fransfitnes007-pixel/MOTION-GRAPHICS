"""Pitch check: median f0 and range in semitones. Adult male narrators sit near 95-150 Hz, adult women 165-240 Hz.
A voice that reads childlike is usually too high or too wide. Usage: python3 tools/f0.py a.wav b.wav"""
import sys, numpy as np, wave, subprocess, os, math
for p in sys.argv[1:]:
    tmp=p+'.16k.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',p,'-ac','1','-ar','16000',tmp])
    w=wave.open(tmp); sr=16000; x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768; os.remove(tmp)
    fr=640; f0=[]
    for i in range(0,len(x)-fr,320):
        s=x[i:i+fr]
        if np.sqrt(np.mean(s**2))<0.02: continue
        s=s-s.mean(); ac=np.correlate(s,s,'full')[fr-1:]; ac/=ac[0]+1e-9; k=np.argmax(ac[40:228])+40
        if ac[k]>0.5: f0.append(sr/k)
    f0=np.array(f0); lo,hi=np.percentile(f0,10),np.percentile(f0,90)
    print(f"{os.path.basename(p):28} {len(x)/sr:5.1f}s f0={np.median(f0):.0f}Hz ({lo:.0f}-{hi:.0f}, {12*math.log2(hi/lo):.1f} st)")
