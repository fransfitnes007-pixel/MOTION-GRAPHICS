"""Render reel.html frame by frame and join it to the voiceover.
Usage: python3 render.py <audio.wav> <out.mp4> [--stills 1.5,4.2,...] [--from 0 --to 10]"""
import sys, os, base64, subprocess, json
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); FPS = 30
args = sys.argv[1:]
def opt(n, d=None):
    if n in args: i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
    return d
stills = opt("--stills"); t_from = float(opt("--from", 0)); t_to = opt("--to")
audio, out = args[0], args[1]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto("file://" + os.path.join(HERE, "reel.html")); pg.wait_for_function("window.renderAt !== undefined", timeout=8000)
    dur = pg.evaluate("window.DURATION"); print("duration", round(dur, 2), flush=True)
    lit = lambda: pg.evaluate("()=>{renderAt(1.5);const d=g.getImageData(0,0,1080,1920).data;let s=0;for(let i=0;i<d.length;i+=4000)s+=d[i];return s}")
    for attempt in range(5):
        if lit() > 500: break
        pg.reload(); pg.wait_for_function("window.renderAt !== undefined", timeout=8000)
    else: sys.exit("canvas renders black")
    grab = lambda t: base64.b64decode(pg.evaluate("t=>{renderAt(t);return cv.toDataURL('image/jpeg',0.92)}", t).split(",", 1)[1])
    if stills:
        os.makedirs(out, exist_ok=True)
        for t in [float(x) for x in stills.split(",")]: open(os.path.join(out, f"t{t:06.2f}.jpg"), "wb").write(grab(t))
    else:
        end = float(t_to) if t_to else dur; n0, n1 = int(t_from * FPS), int(round(end * FPS))
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-", "-ss", str(t_from), "-i", audio,
                               "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-vf", "scale=in_range=pc:out_range=tv,format=yuv420p", "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-c:a", "aac", "-b:a", "192k", "-af", "apad", "-t", str((n1 - n0) / FPS), "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for f in range(n0, n1):
            ff.stdin.write(grab(f / FPS))
            if f % 300 == 0: print("frame", f, "/", n1, flush=True)
        ff.stdin.close(); ff.wait(); print("wrote", out)
    if errs: print("PAGE ERRORS:", errs[:5])
    b.close()
