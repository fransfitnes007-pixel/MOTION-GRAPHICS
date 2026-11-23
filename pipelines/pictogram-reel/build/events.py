"""Play the reel silently and log when every pop-in, tick and typing run is first drawn.
Usage: python3 events.py events.json   (needs: pip install playwright && playwright install chromium)"""
import sys, os, json
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + os.path.join(HERE, "reel.html")); pg.wait_for_function("window.renderAt !== undefined", timeout=8000)
    ev = pg.evaluate("""()=>{ EV.on=true; for(let f=0; f<DURATION*60; f++) renderAt(f/60);
      return {list:EV.list, typ:Object.values(EV.typ), B:B.map(b=>b.s), C, DURATION, TAP, DL}; }""")
    b.close()
json.dump(ev, open(sys.argv[1], "w"), indent=1); print(len(ev["list"]), "pop-ins,", len(ev["typ"]), "typing runs, duration", round(ev["DURATION"], 2))
