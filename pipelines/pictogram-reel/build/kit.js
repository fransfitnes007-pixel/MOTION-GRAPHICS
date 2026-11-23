// Drawing kit for the black-and-white pictogram reels. Everything is a pure function of time.
const W=1080,H=1920,GY=1330,cv=document.getElementById('c'),g=cv.getContext('2d');
const FONT='system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif';
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), lerp=(a,b,t)=>a+(b-a)*t;
const eo=t=>1-Math.pow(1-cl(t),3);
const eio=t=>{t=cl(t);return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2};
const back=t=>{t=cl(t);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2)};
const pr=(t,a,d)=>cl((t-a)/d);
const rnd=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)};
const fmt=n=>Math.round(n).toLocaleString('en-US');
// Sound-event recorder: with EV.on, the first frame each pop-in is drawn gets logged (build/events.py reads it).
const EV={on:false,seen:{},list:[],typ:{}}; let NOW=0,BI=0; window.EV=EV;
function mark(type,key,p){ if(!EV.on)return; const k=BI+type+key; if(EV.seen[k])return; EV.seen[k]=1; if(p<.9) EV.list.push({t:+NOW.toFixed(3),type,key,beat:BI}); }
function al(a,fn){ if(a<=0.004)return; g.save(); g.globalAlpha*=cl(a); fn(); g.restore(); }
function rr(x,y,w,h,r){ g.beginPath(); g.roundRect(x,y,w,h,r); }
function bg(){ g.setTransform(1,0,0,1,0,0); g.globalAlpha=1; g.fillStyle='#000'; g.fillRect(0,0,W,H);
  const gr=g.createRadialGradient(W/2,H*.42,0,W/2,H*.42,H*.8); gr.addColorStop(0,'rgba(255,255,255,0.06)'); gr.addColorStop(1,'rgba(255,255,255,0)'); g.fillStyle=gr; g.fillRect(0,0,W,H);
  g.fillStyle='rgba(255,255,255,0.075)'; for(let y=30;y<H;y+=44)for(let x=28;x<W;x+=44)g.fillRect(x,y,2,2); }
function glow(x,y,r,a){ if(a<=0)return; const gr=g.createRadialGradient(x,y,0,x,y,r); gr.addColorStop(0,`rgba(255,255,255,${a})`); gr.addColorStop(.45,`rgba(255,255,255,${a*.35})`); gr.addColorStop(1,'rgba(255,255,255,0)'); g.fillStyle=gr; g.fillRect(x-r,y-r,r*2,r*2); }
function txt(s,x,y,size,o={}){ g.font=`${o.w||600} ${size}px ${FONT}`; g.textAlign=o.a||'center'; g.textBaseline='middle'; g.letterSpacing=(o.ls||0)+'px'; g.fillStyle=o.col||'#fff'; g.fillText(s,x+((o.a||'center')==='center'?(o.ls||0)/2:0),y); g.letterSpacing='0px'; }
function tw(s,size,o={}){ g.font=`${o.w||600} ${size}px ${FONT}`; g.letterSpacing=(o.ls||0)+'px'; const w=g.measureText(s).width; g.letterSpacing='0px'; return w; }
function pill(s,x,y,p,o={}){ if(p<=0)return; mark('pill',s,p); const size=o.size||30, ls=size*.14, w=tw(s,size,{w:700,ls})+size*1.5, h=size*1.8, sc=lerp(.82,1,back(p));
  al(eo(p*1.6),()=>{ glow(x,y,w*.85,.26); g.save(); g.translate(x,y); g.scale(sc,sc); g.fillStyle='#fff'; rr(-w/2,-h/2,w,h,h/2); g.fill(); txt(s,0,1,size,{w:700,ls,col:'#000'}); g.restore(); }); }
function bubble(s,x,y,p,o={}){ if(p<=0)return; mark('bubble',s+x,p); const size=o.size||22, ls=size*.12, w=tw(s,size,{w:700,ls})+size*1.5, h=size*1.9, sc=lerp(.7,1,back(p));
  al(eo(p*1.6),()=>{ g.save(); g.translate(x,y); g.scale(sc,sc); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=3.5; rr(-w/2,-h/2,w,h,h*.42); g.fill(); g.stroke(); txt(s,0,1,size,{w:700,ls}); g.restore(); }); }
function ground(y=GY,a=.55,x0=0,x1=W){ g.save(); g.strokeStyle=`rgba(255,255,255,${a})`; g.lineWidth=3; g.setLineDash([11,10]); g.beginPath(); g.moveTo(x0,y); g.lineTo(x1,y); g.stroke(); g.restore(); }
function miniBulb(x,y,s){ glow(x,y,46*s,.5); g.save(); g.strokeStyle='#fff'; g.lineWidth=3.5*s; g.beginPath(); g.arc(x,y,12*s,0,7); g.stroke(); g.beginPath(); g.moveTo(x-5*s,y+14*s); g.lineTo(x+5*s,y+14*s); g.moveTo(x-4*s,y+19*s); g.lineTo(x+4*s,y+19*s); g.stroke(); g.restore(); }
function person(x,y,s=1,o={}){ const col=o.col||'#fff', bw=66*s, bh=96*s, hr=27*s, dir=o.flip?-1:1;
  g.save(); g.translate(x,y); if(o.rot) g.rotate(o.rot);
  if(o.glow) glow(0,-bh*.75,190*s,o.glow);
  const arm=(ang,len)=>{ g.save(); g.translate(dir*bw*.26,-bh*.72); g.rotate(-dir*ang); g.lineCap='round'; g.strokeStyle=col; g.lineWidth=17*s; g.beginPath(); g.moveTo(0,0); g.lineTo(dir*len*s,0); g.stroke(); g.restore(); };
  if(o.arm==='point') arm(.22*(o.armP??1),64);
  if(o.arm==='up') arm(lerp(.2,1.1,o.armP??1),62);
  g.fillStyle=col; g.beginPath(); g.moveTo(-bw/2,0); g.lineTo(-bw/2,-bh+bw/2); g.arc(0,-bh+bw/2,bw/2,Math.PI,0); g.lineTo(bw/2,0); g.closePath(); g.fill();
  g.beginPath(); g.arc(0,-bh-hr-5*s,hr,0,7); g.fill();
  if(o.marker==='bulb') miniBulb(0,-bh-hr*2-36*s,s);
  g.restore(); }
function bulb(x,y,r,p,lw=6){ if(p<=0)return; g.save(); g.strokeStyle='#fff'; g.lineWidth=lw; g.lineCap='round';
  g.beginPath(); g.arc(x,y,r,Math.PI*.5+.55,Math.PI*.5+.55+(Math.PI*2-1.1)*eo(p)); g.stroke();
  al(eo(pr(p,.55,.45)),()=>{ const bx=r*.5, by=y+r*.86; g.beginPath(); g.moveTo(x-bx,by); g.lineTo(x-bx*.8,by+r*.3); g.lineTo(x+bx*.8,by+r*.3); g.lineTo(x+bx,by); g.stroke();
    g.beginPath(); g.moveTo(x-bx*.62,by+r*.46); g.lineTo(x+bx*.62,by+r*.46); g.moveTo(x-bx*.4,by+r*.62); g.lineTo(x+bx*.4,by+r*.62); g.stroke();
    g.lineWidth=lw*.7; g.beginPath(); g.moveTo(x-r*.28,y+r*.5); g.lineTo(x-r*.18,y); g.lineTo(x,y+r*.22); g.lineTo(x+r*.18,y); g.lineTo(x+r*.28,y+r*.5); g.stroke(); });
  g.restore(); }
function phone(cx,top,w,h,o={}){ g.save(); g.strokeStyle='#fff'; g.fillStyle='#000'; g.lineWidth=o.lw||6; rr(cx-w/2,top,w,h,w*.15); g.fill(); g.stroke(); g.fillStyle='#fff'; rr(cx-w*.14,top+w*.06,w*.28,Math.max(6,w*.035),w*.02); g.fill(); g.restore(); }
function star(x,y,r,rot=-Math.PI/2){ g.save(); g.fillStyle='#fff'; g.beginPath(); for(let i=0;i<10;i++){ const a=rot+i*Math.PI/5, q=i%2?r*.45:r; g.lineTo(x+Math.cos(a)*q,y+Math.sin(a)*q); } g.closePath(); g.fill(); g.restore(); }
function spark(x,y,r){ g.save(); g.fillStyle='#fff'; g.beginPath(); for(let i=0;i<8;i++){ const a=-Math.PI/2+i*Math.PI/4, q=i%2?r*.3:r; g.lineTo(x+Math.cos(a)*q,y+Math.sin(a)*q); } g.closePath(); g.fill(); g.restore(); }
function appIcon(x,y,sz,o={}){ g.save(); g.strokeStyle='#fff'; g.fillStyle='#000'; g.lineWidth=o.lw||5; rr(x-sz/2,y-sz/2,sz,sz,sz*.25); g.fill(); g.stroke(); if(o.star) star(x,y,sz*.26); else spark(x,y,sz*.28); g.restore(); }
function check(x,y,r,p){ if(p<=0)return; mark('check',x+'_'+y,p); al(eo(p),()=>{ const s=lerp(.6,1,back(p)); g.save(); g.translate(x,y); g.scale(s,s); g.fillStyle='#fff'; g.beginPath(); g.arc(0,0,r,0,7); g.fill(); g.strokeStyle='#000'; g.lineWidth=r*.2; g.lineCap='round'; g.lineJoin='round'; g.beginPath(); g.moveTo(-r*.42,0); g.lineTo(-r*.1,r*.32); g.lineTo(r*.45,-r*.3); g.stroke(); g.restore(); }); }
function cross(x,y,r,p){ if(p<=0)return; mark('cross',x+'_'+y,p); al(eo(p),()=>{ const s=lerp(.6,1,back(p)); g.save(); g.translate(x,y); g.scale(s,s); g.strokeStyle='#fff'; g.lineWidth=r*.16; g.lineCap='round'; g.beginPath(); g.arc(0,0,r,0,7); g.stroke(); g.beginPath(); g.moveTo(-r*.38,-r*.38); g.lineTo(r*.38,r*.38); g.moveTo(r*.38,-r*.38); g.lineTo(-r*.38,r*.38); g.stroke(); g.restore(); }); }
function priceTag(x,y,s,rot=0,sc=1){ const size=44, w=tw(s,size,{w:800})+96, h=84; g.save(); g.translate(x,y); g.rotate(rot); g.scale(sc,sc); g.fillStyle='#fff'; g.beginPath(); g.moveTo(-w/2+38,-h/2); g.lineTo(w/2,-h/2); g.lineTo(w/2,h/2); g.lineTo(-w/2+38,h/2); g.lineTo(-w/2,0); g.closePath(); g.fill(); g.fillStyle='#000'; g.beginPath(); g.arc(-w/2+30,0,8,0,7); g.fill(); txt(s,24,2,size,{w:800,col:'#000'}); g.restore(); }
function cloud(x,y,s,a){ if(a<=0)return; g.save(); g.fillStyle=`rgba(255,255,255,${a})`; [[0,0,70],[80,-18,58],[-78,-8,52],[42,34,56],[-40,36,54],[130,20,44],[-125,22,40]].forEach(c=>{ g.beginPath(); g.arc(x+c[0]*s,y+c[1]*s,c[2]*s,0,7); g.fill(); }); g.restore(); }
function rocket(x,y,s,o={}){ g.save(); g.translate(x,y); g.rotate(o.rot||0); g.scale(s,s);
  if(o.flame){ const f=o.flame*(.85+.15*Math.sin((o.t||0)*42)); glow(0,110,170,.4*o.flame); g.fillStyle='#fff'; g.beginPath(); g.moveTo(-26,88); g.quadraticCurveTo(0,88+175*f,26,88); g.closePath(); g.fill(); }
  g.lineWidth=5; g.strokeStyle='#fff'; g.fillStyle='#000'; g.lineJoin='round';
  for(const d of [-1,1]){ g.beginPath(); g.moveTo(d*42,30); g.lineTo(d*86,96); g.lineTo(d*42,82); g.closePath(); g.fill(); g.stroke(); }
  g.beginPath(); g.moveTo(-44,88); g.lineTo(-44,-30); g.quadraticCurveTo(-44,-110,0,-150); g.quadraticCurveTo(44,-110,44,-30); g.lineTo(44,88); g.closePath(); g.fill(); g.stroke();
  g.beginPath(); g.arc(0,-48,17,0,7); g.stroke();
  const P=[[-24,2,26,17,-.3],[4,38,28,16,.25],[-30,56,24,15,.1],[12,-8,22,14,-.15]];
  for(let i=0;i<(o.patches||0);i++){ const p=P[i]; g.save(); g.translate(p[0],p[1]); g.rotate(p[4]); g.lineWidth=3.2; g.strokeRect(0,0,p[2],p[3]); g.beginPath(); g.moveTo(p[2]/3,0); g.lineTo(p[2]/3,p[3]); g.moveTo(2*p[2]/3,0); g.lineTo(2*p[2]/3,p[3]); g.stroke(); g.restore(); }
  g.restore(); }
function card(x,y,w,h,title,p){ if(p<=0)return; mark('card',title,p); al(eo(p),()=>{ g.save(); g.translate(0,(1-eo(p))*30); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4.5; rr(x,y,w,h,22); g.fill(); g.save(); rr(x,y,w,h,22); g.clip(); g.fillStyle='#fff'; g.fillRect(x,y,w,62); g.restore(); rr(x,y,w,h,22); g.stroke(); txt(title,x+w/2,y+33,22,{w:800,ls:5,col:'#000'}); g.restore(); }); }
function noteCard(x,y,w,h,lines,footer){ g.save(); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4.5; rr(x,y,w,h,22); g.fill(); g.stroke();
  txt('NOTES',x+44,y+52,20,{a:'left',w:700,ls:5,col:'#9a9a9a'}); txt('App idea',x+44,y+118,54,{a:'left',w:800});
  for(let i=0;i<lines;i++){ g.fillStyle=`rgba(255,255,255,${i<2?.55:.32})`; rr(x+44,y+176+i*40,(w-88)*(.55+.42*rnd(i+3)),13,6); g.fill(); }
  if(footer) txt(footer,x+w/2,y+h-40,18,{w:700,ls:4,col:'#8c8c8c'}); g.restore(); }
function clock(x,y,r,a){ g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineCap='round'; g.beginPath(); g.arc(x,y,r,0,7); g.stroke(); g.beginPath(); g.moveTo(x,y); g.lineTo(x+Math.sin(a)*r*.68,y-Math.cos(a)*r*.68); g.moveTo(x,y); g.lineTo(x+Math.sin(a/12)*r*.45,y-Math.cos(a/12)*r*.45); g.stroke(); g.restore(); }
function dice(x,y,s,rot){ g.save(); g.translate(x,y); g.rotate(rot); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4; rr(-s/2,-s/2,s,s,s*.2); g.fill(); g.stroke(); g.fillStyle='#fff'; [[-.25,-.25],[.25,.25],[0,0],[.25,-.25],[-.25,.25]].forEach(d=>{ g.beginPath(); g.arc(d[0]*s,d[1]*s,s*.07,0,7); g.fill(); }); g.restore(); }
function typed(s,p,t){ if(EV.on&&p>0&&p<1){ const e=EV.typ[BI+s]||(EV.typ[BI+s]={a:NOW,b:NOW,n:s.length,beat:BI}); e.b=NOW; } const n=Math.floor(cl(p)*s.length); return s.slice(0,n)+((n<s.length||Math.floor(t*3)%2)?'|':''); }

// ---- App Store listing (dark mode), drawn to the real layout: icon, name, subtitle, Get, share, info strip ----
const AS={blue:'#0A84FF',grey:'#8E8E93',line:'#38383A'};
function asIcon(x,y,sz){ g.save(); rr(x,y,sz,sz,sz*.2237); g.clip(); if(typeof ICON!=='undefined'&&ICON.complete&&ICON.naturalWidth) g.drawImage(ICON,x,y,sz,sz); else { g.fillStyle='#F2F2F2'; g.fillRect(x,y,sz,sz); } g.restore();
  g.save(); g.strokeStyle='rgba(255,255,255,.14)'; g.lineWidth=2; rr(x,y,sz,sz,sz*.2237); g.stroke(); g.restore(); }
function asShare(x,y,s){ g.save(); g.strokeStyle=AS.blue; g.lineWidth=5; g.lineCap='round'; g.lineJoin='round'; g.beginPath(); g.moveTo(x-s*.22,y-s*.12); g.lineTo(x-s*.36,y-s*.12); g.lineTo(x-s*.36,y+s*.5); g.lineTo(x+s*.36,y+s*.5); g.lineTo(x+s*.36,y-s*.12); g.lineTo(x+s*.22,y-s*.12); g.stroke();
  g.beginPath(); g.moveTo(x,y+s*.16); g.lineTo(x,y-s*.56); g.moveTo(x-s*.2,y-s*.36); g.lineTo(x,y-s*.56); g.lineTo(x+s*.2,y-s*.36); g.stroke(); g.restore(); }
function asStars(x,y,r,val){ const gap=r*2.25, x0=x-gap*2; for(let i=0;i<5;i++){ const f=cl(val-i); g.save(); g.globalAlpha*=.35; star(x0+i*gap,y,r); g.restore(); if(f>0){ g.save(); g.beginPath(); g.rect(x0+i*gap-r,y-r,r*2*f,r*2); g.clip(); star(x0+i*gap,y,r); g.restore(); } } }
// state: 0 Get, 0..1 while downloading (st in (0,1)), 1 Open. tap = 0..1 ripple progress
function asGet(cx,cy,st,tap){ const w=176,h=72; g.save(); g.translate(cx,cy); const dip=1-.07*Math.sin(Math.PI*cl(tap*2.2)); g.scale(dip,dip);
  if(st<=0||st>=1){ g.fillStyle=AS.blue; rr(-w/2,-h/2,w,h,h/2); g.fill(); txt(st>=1?'Open':'Get',0,2,36,{w:700}); }
  else { g.lineWidth=7; g.strokeStyle='#2C2C2E'; g.beginPath(); g.arc(0,0,31,0,7); g.stroke(); g.strokeStyle=AS.blue; g.lineCap='round'; g.beginPath(); g.arc(0,0,31,-Math.PI/2,-Math.PI/2+Math.PI*2*Math.max(.04,st)); g.stroke(); g.fillStyle=AS.blue; rr(-10,-10,20,20,4); g.fill(); }
  g.restore();
  if(tap>0&&tap<1){ g.save(); g.strokeStyle=`rgba(255,255,255,${.55*(1-tap)})`; g.lineWidth=5; g.beginPath(); g.arc(cx,cy,lerp(30,120,eo(tap)),0,7); g.stroke(); g.fillStyle=`rgba(255,255,255,${.22*(1-tap)})`; g.beginPath(); g.arc(cx,cy,lerp(26,60,eo(tap)),0,7); g.fill(); g.restore(); } }
function appStore(top,o){ const x0=84, sz=292, tx=x0+sz+40, R=W-x0;
  g.save(); const gr=g.createRadialGradient(x0+sz/2,top+sz/2,0,x0+sz/2,top+sz/2,520); gr.addColorStop(0,'rgba(255,122,60,.11)'); gr.addColorStop(1,'rgba(255,122,60,0)'); g.fillStyle=gr; g.fillRect(0,top-420,W,1100); g.restore();
  const s=lerp(.88,1,back(o.icon)); g.save(); g.translate(x0+sz/2,top+sz/2); g.scale(s,s); asIcon(-sz/2,-sz/2,sz); g.restore();
  al(o.text,()=>{ txt(o.name[0],tx,top+34,51,{a:'left',w:700}); if(o.name[1]) txt(o.name[1],tx,top+96,51,{a:'left',w:700}); txt(o.sub,tx,top+(o.name[1]?156:96),32,{a:'left',w:400,col:AS.grey});
    asGet(tx+88,top+sz-36,o.state,o.tap); al(o.state<=0?1:0,()=>{ txt('In-App',tx+196,top+sz-49,21,{a:'left',w:400,col:AS.grey}); txt('Purchases',tx+196,top+sz-23,21,{a:'left',w:400,col:AS.grey}); }); asShare(R-26,top+sz-40,50); });
  al(o.strip,()=>{ const y=top+sz+62; g.fillStyle=AS.line; g.fillRect(x0,y,R-x0,2); const cw=(R-x0)/3;
    o.cells.forEach((c,i)=>{ const cx=x0+cw*(i+.5); if(i){ g.fillStyle=AS.line; g.fillRect(x0+cw*i,y+34,2,150); }
      txt(c[0],cx,y+50,22,{w:600,ls:1,col:AS.grey});
      if(c[1]==='person'){ g.save(); g.fillStyle=AS.grey; g.beginPath(); g.arc(cx,y+96,15,0,7); g.fill(); g.beginPath(); g.arc(cx,y+146,30,Math.PI,0); g.fill(); g.restore(); }
      else if(c[1]==='cap'){ g.save(); g.fillStyle=AS.grey; g.beginPath(); g.moveTo(cx,y+84); g.lineTo(cx+46,y+106); g.lineTo(cx,y+128); g.lineTo(cx-46,y+106); g.closePath(); g.fill(); g.beginPath(); g.moveTo(cx-25,y+124); g.lineTo(cx-25,y+142); g.quadraticCurveTo(cx,y+158,cx+25,y+142); g.lineTo(cx+25,y+124); g.lineTo(cx,y+137); g.closePath(); g.fill(); g.restore(); }
      else txt(c[1],cx,y+112,54,{w:700,col:AS.grey});
      if(c[2]==='stars'){ g.save(); g.fillStyle=AS.grey; asStarsGrey(cx,y+168,11,o.rating); g.restore(); } else txt(c[2],cx,y+170,25,{w:400,col:AS.grey}); });
    g.fillStyle=AS.line; g.fillRect(x0,y+218,R-x0,2); }); }
function asStarsGrey(x,y,r,val){ const gap=r*2.3, x0=x-gap*2, st=(cx,a)=>{ g.save(); g.globalAlpha*=a; g.fillStyle=AS.grey; g.beginPath(); for(let i=0;i<10;i++){ const an=-Math.PI/2+i*Math.PI/5, q=i%2?r*.45:r; g.lineTo(cx+Math.cos(an)*q,y+Math.sin(an)*q); } g.closePath(); g.fill(); g.restore(); };
  for(let i=0;i<5;i++){ const f=cl(val-i); st(x0+i*gap,.3); if(f>0){ g.save(); g.beginPath(); g.rect(x0+i*gap-r,y-r,r*2*f,r*2); g.clip(); st(x0+i*gap,1); g.restore(); } } }
