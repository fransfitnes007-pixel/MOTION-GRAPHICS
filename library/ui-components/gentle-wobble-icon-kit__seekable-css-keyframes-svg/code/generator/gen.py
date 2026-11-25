# Builds <pack>.json (svg + css per icon) from the upstream .tsx files.
# Usage: put the upstream files you need in ./SRC/<name>.tsx (LA: pqoqubbw/icons icons/<name>.tsx; AI: Avijit07x/animateicons icons/lucide/<name>-icon.tsx saved as <name>.tsx),
#        then: python3 gen.py   -> writes out.json. Needs core.py and ai_specs.py next to it.
import json,sys,os
from core import *
import ai_specs as specmod
def gen(prefix, srcdir, specmod):
    out={}
    for name,sp_ in specmod.SPEC.items():
        tree=sp_['tree'] or load(f'{srcdir}/{name}.tsx')
        spec={k:v for k,v in sp_['spec'].items() if v}
        svg,css=build(name,prefix,tree,sp_['L'],spec,sp_['origins'],sp_['extra'])
        out[name]={'svg':svg,'css':css,'L':sp_['L']}
    return out
if __name__=='__main__':
    o=gen('ai', os.path.join(os.path.dirname(os.path.abspath(__file__)),'SRC'), specmod)
    json.dump(o,open('out.json','w')); print(len(o),'icons')
