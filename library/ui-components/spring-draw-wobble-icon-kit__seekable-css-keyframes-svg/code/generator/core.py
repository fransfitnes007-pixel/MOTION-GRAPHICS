import re, math, json
EIO='cubic-bezier(.42,0,.58,1)'; EO='cubic-bezier(0,0,.58,1)'; EI='cubic-bezier(.42,0,1,1)'; LIN='linear'; EMD='cubic-bezier(.4,0,.2,1)'
# ---------- JSX -> tree ----------
def parse_jsx(src):
    """returns list of top-level child elements of the svg root: dict(tag, attrs, kids). skips non-string attrs."""
    i=0; n=len(src)
    stack=[{'tag':'ROOT','attrs':{},'kids':[]}]
    def skip_brace(i):
        d=0
        while i<n:
            if src[i]=='{': d+=1
            elif src[i]=='}':
                d-=1
                if d==0: return i+1
            i+=1
        return i
    # find first svg open
    m=re.search(r'<(motion\.|m\.)?svg\b',src); i=m.start()
    first=True
    while i<n:
        if src[i]=='{':   # expression child
            i=skip_brace(i); continue
        if src[i]!='<': i+=1; continue
        if src.startswith('</',i):
            j=src.index('>',i); closed=src[i+2:j].strip()
            node=stack.pop()
            if not stack: return node
            stack[-1]['kids'].append(node); i=j+1; continue
        j=i+1; m=re.match(r'[\w.]+',src[j:]); tag=m.group(0); j+=len(tag)
        attrs={}
        while True:
            while src[j].isspace(): j+=1
            if src.startswith('/>',j): selfclose=True; j+=2; break
            if src[j]=='>': selfclose=False; j+=1; break
            m=re.match(r'\{\.\.\.[^}]*\}',src[j:])
            if m: j+=len(m.group(0)); continue
            m=re.match(r'[\w-]+',src[j:]); name=m.group(0); j+=len(name)
            if j<n and src[j]=='=':
                j+=1
                if src[j]=='"':
                    k=src.index('"',j+1); attrs[name]=src[j+1:k]; j=k+1
                elif src[j]=='{':
                    k=skip_brace(j); raw=src[j+1:k-1].strip()
                    if re.fullmatch(r'-?[\d.]+',raw): attrs[name]=raw
                    j=k
            else: attrs[name]='true'
        t=tag.split('.')[-1]
        node={'tag':t,'attrs':attrs,'kids':[]}
        if selfclose:
            if stack: stack[-1]['kids'].append(node)
        else: stack.append(node)
        i=j
    return stack[0]
KEEP={'d','cx','cy','r','x','y','width','height','rx','ry','points','x1','x2','y1','y2','strokeWidth','stroke-width'}
def flat(node,out=None):
    out=[] if out is None else out
    for k in node['kids']:
        out.append(k); flat(k,out)
    return out
def attr_str(a):
    m={'strokeDasharray':'stroke-dasharray','strokeWidth':'stroke-width'}
    return ' '.join(f'{m.get(k,k)}="{v}"' for k,v in a.items() if k in KEEP)
# ---------- springs ----------
def sp(k,c,m=1.0):
    w=math.sqrt(k/m); z=c/(2*math.sqrt(k*m)); 
    def x(t):
        if z<1:
            wd=w*math.sqrt(1-z*z); return 1-math.exp(-z*w*t)*(math.cos(wd*t)+z*w/wd*math.sin(wd*t))
        return 1-math.exp(-w*t)*(1+w*t)
    T=0.01
    while T<10 and any(abs(1-x(T+s*.01))>0.003 for s in range(0,100,5)): T+=.01
    N=40; pts=[x(T*i/N) for i in range(N+1)]; pts[-1]=1
    return 'linear('+','.join(f'{p:.4f}' for p in pts)+')', round(T,2)
# ---------- tracks ----------
def A(t0,dur,ease=EIO,times=None,pre=None,**p):
    n=max(len(v) for v in p.values())
    times=times or [i/(n-1) for i in range(n)]
    r=[(round(t0+tt*dur,4),{k:v[i] for k,v in p.items()},ease) for i,tt in enumerate(times)]
    if pre is not None and pre<t0: r.insert(0,(pre,dict(r[0][1]),LIN))
    return r
def SPR(t0,k,c,m=1.0,pre=None,**p):
    e,T=sp(k,c,m); return A(t0,T,e,pre=pre,**p)
TF={'x':('translate','px'),'y':None,'rotate':None,'scale':None,'scaleX':None,'scaleY':None,'skewX':None,'skewY':None}
IDENT={'x':0,'y':0,'rotate':0,'scale':1,'scaleX':1,'scaleY':1,'skewX':0,'skewY':0}
def tf_str(v):
    s=[]
    if 'x' in v or 'y' in v: s.append(f"translate({v.get('x',0):g}px,{v.get('y',0):g}px)")
    if 'rotate' in v: s.append(f"rotate({v['rotate']:g}deg)")
    if 'scale' in v: s.append(f"scale({v['scale']:g})")
    if 'scaleX' in v or 'scaleY' in v: s.append(f"scale({v.get('scaleX',1):g},{v.get('scaleY',1):g})")
    if 'skewX' in v: s.append(f"skewX({v['skewX']:g}deg)")
    if 'skewY' in v: s.append(f"skewY({v['skewY']:g}deg)")
    return ' '.join(s)
def compile_track(track,L):
    pts=sorted(track,key=lambda p:p[0])
    keys=set(); [keys.update(p[1]) for p in pts]
    tfk=[k for k in keys if k in IDENT]
    # carry
    cur={k:IDENT[k] for k in tfk}; norm=[]
    carry={}
    for t,pr,e in pts:
        for k in keys:
            if k in pr: carry[k]=pr[k]
            elif k in IDENT: carry.setdefault(k,IDENT[k])
        norm.append((t,{k:carry[k] for k in keys if k in carry or k in pr},e))
    # first-pts back-fill for non-transform keys missing
    for k in keys:
        if k not in norm[0][1]:
            fv=next(p[1][k] for p in norm if k in p[1]); 
            for p in norm:
                if k not in p[1]: p[1][k]=fv
                else: break
    if norm[-1][0]>L+1e-6: raise ValueError(f'track ends at {norm[-1][0]} > L={L}')
    if norm[0][1]!=norm[-1][1]:
        last=dict(norm[-1][1]); t0=norm[0][0]
        norm.insert(0,(max(t0-0.001,0),dict(last),LIN))
        if t0-0.001>0: norm.insert(0,(0,dict(last),LIN))
    elif norm[0][0]>0: norm.insert(0,(0,dict(norm[0][1]),norm[0][2]))
    if norm[-1][0]<L: norm.append((L,dict(norm[-1][1]),LIN))
    out=[]
    for t,pr,e in norm:
        d=[]
        tf={k:pr[k] for k in tfk}
        if tf: d.append('transform:'+tf_str(tf))
        if 'opacity' in pr: d.append(f"opacity:{pr['opacity']:g}")
        if 'pl' in pr: d.append(f"stroke-dasharray:{pr['pl']:.4g} 1")
        if 'po' in pr: d.append(f"stroke-dashoffset:{-pr['po']:.4g}")
        if 'fo' in pr: d.append(f"fill-opacity:{pr['fo']:g}")
        if 'd' in pr: d.append(f'd:path("{pr["d"]}")')
        if 'sw' in pr: d.append(f"stroke-width:{pr['sw']:g}")
        out.append((t/L*100,d,e))
    return out, keys
def build(name,prefix,tree,L,spec,origins=None,extra=None):
    """spec: {idx|'root': [track,...]}; origins: {idx|'root':'12px 12px'} for view-box origins"""
    els=flat(tree); origins=origins or {}; extra=extra or {}
    css=[]; uid=f'{prefix}-{name}'
    def cls(i): return f'{uid}-{i}'
    def emit(key,tracks):
        c=cls(key); names=[]; usepl=False
        for j,tr in enumerate(tracks):
            kfs,keys=compile_track(tr,L); kn=f'{c}-k{j}'; names.append(kn)
            if keys&{'pl','po'}: usepl=True
            body=''.join(f"{p:.3f}%{{{';'.join(d)};animation-timing-function:{e}}}" for p,d,e in kfs)
            css.append(f'@keyframes {kn}{{{body}}}')
        org=origins.get(key)
        if org and org.startswith('fill:'): o=f'transform-box:fill-box;transform-origin:{org[5:]};'
        else: o=f'transform-box:view-box;transform-origin:{org};' if org else 'transform-box:fill-box;transform-origin:50% 50%;'
        if key=='root' and not org: o='transform-box:view-box;transform-origin:12px 12px;'
        css.append(f".{c}{{{o}animation:{','.join(f'{n} {L}s infinite' for n in names)}}}")
        return usepl
    pl=set()
    for key,tracks in spec.items():
        if emit(key,tracks): pl.add(key)
    def render(node,idx):
        s=''
        for k in node['kids']:
            i=idx[id(k)]; a=attr_str(k['attrs'])
            c=f' class="{cls(i)}"' if i in spec else ''
            plx=(' pathLength="1"' if i in pl else '')+''.join(f' {a}="{b}"' for a,b in extra.get(i,{}).items())
            inner=render(k,idx)
            s+=f'<{k["tag"]} {a}{c}{plx}'+(f'>{inner}</{k["tag"]}>' if inner else '/>')
        return s
    idx={id(e):i for i,e in enumerate(els)}
    body=render(tree,idx)
    if 'root' in spec: body=f'<g class="{cls("root")}">{body}</g>'
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" overflow="visible">{body}</svg>'
    return svg,''.join(css)
def load(path):
    s=open(path).read(); m=re.search(r'forwardRef<',s); 
    return parse_jsx(s[m.end() if m else 0:])['kids'][0]
def dump(path):
    t=load(path)
    return ' | '.join(f"{i}:{e['tag']}{'('+(e['attrs'].get('d') or e['attrs'].get('points') or e['attrs'].get('r') or '')[:12]+')' if e['kids']==[] else ''}" for i,e in enumerate(flat(t)))
if __name__=='__main__':
    import sys,glob
    for f in sorted(glob.glob(sys.argv[1]+'/*.tsx')): print(f.split('/')[-1][:-4],'::',dump(f))
