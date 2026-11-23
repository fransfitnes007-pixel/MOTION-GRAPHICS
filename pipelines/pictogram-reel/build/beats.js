// Example reel: "The best app idea you've ever heard will never get built". Beat times come from the voiceover cues (cues.js).
const ME={marker:'bulb',glow:.22};
const TITLE_HOLD=0.9, END_CARD=3.9;
const B=[
 {s:0,fn:b1},{s:C.reason,fn:b2},{s:C.friend,fn:b3},{s:C.pitched,fn:b4},{s:C.everyone,fn:b5},{s:C.years,fn:b6},{s:C.nobody,fn:b7},
 {s:C.wrong,fn:b8},{s:C.idea_better,fn:b9},{s:C.priced,fn:b10},{s:C.course,fn:b11},{s:C.learned,fn:b12},{s:C.apps_other,fn:b13},
 {s:C.nobody_know,fn:b14},{s:C.stopped,fn:b15},{s:C.now,fn:b16},{s:C.while,fn:b17},{s:C.someone,fn:b18},{s:C.until,fn:b19},
 {s:C.end+TITLE_HOLD,fn:b20}];
B.forEach((b,i)=>{ b.e=i<B.length-1?B[i+1].s:b.s+END_CARD; });
const DURATION=B[B.length-1].e;
const at=(i,cue)=>cue-B[i].s;   // cue time local to beat i

function b1(t){ ground();
  const wx=lerp(-90,540,eo(pr(t,0,.85))), bob=Math.sin(t*15)*5*(1-pr(t,.55,.3));
  person(wx,GY+bob,1.15,{marker:'bulb',glow:.26});
  const bp=pr(t,.08,.7); glow(540,620,340,.2*eo(bp)); bulb(540,620,150,bp);
  pill('BEST IDEA',540,350,pr(t,.15,.35));
  al(eo(pr(t,.45,.3)),()=>{ txt('IDEAS',540,858,22,{w:700,ls:6,col:'#bdbdbd'}); txt(fmt(lerp(1,47,eio(pr(t,.45,1.5)))),540,935,100,{w:800}); });
  pill('GENIUS',245,520,pr(t,.95,.3),{size:22}); pill('WOW',835,480,pr(t,1.25,.3),{size:22}); pill('10/10',815,770,pr(t,1.55,.3),{size:22}); }

function b2(t){ ground(); person(540,GY,1.15,{marker:'bulb',glow:.24});
  const m=eio(pr(t,0,.5)), bx=lerp(540,285,m), bs=lerp(1,.68,m);
  glow(bx,620,300*bs,.17); bulb(bx,lerp(620,600,m),150*bs,1,5); pill('BEST IDEA',bx,lerp(350,420,m),1,{size:lerp(30,23,m)});
  txt('IDEAS',bx,lerp(858,795,m),20,{w:700,ls:6,col:'#bdbdbd'}); txt('47',bx,lerp(935,858,m),lerp(100,72,m),{w:800});
  al(eo(pr(t,.3,.4)),()=>{ glow(795,610,270,.16); phone(795,470,190,300); pill('NEVER BUILT',795,420,pr(t,.4,.35),{size:23});
    txt('APPS SHIPPED',795,795,20,{w:700,ls:6,col:'#bdbdbd'}); txt('0',795,858,72,{w:800}); });
  const qp=pr(t,1.0,.35), sw=pr(t,2.3,.3);
  al(eo(qp),()=>{ g.save(); g.strokeStyle='rgba(255,255,255,.6)'; g.lineWidth=2.5; g.setLineDash([7,8]); g.beginPath(); g.moveTo(500,985); g.lineTo(lerp(500,300,eo(qp)),lerp(985,905,eo(qp))); g.moveTo(580,985); g.lineTo(lerp(580,785,eo(qp)),lerp(985,905,eo(qp))); g.stroke(); g.restore();
    glow(540,1010,120,.3); al(1-sw,()=>{ g.fillStyle='#fff'; g.beginPath(); g.arc(540,1010,46*lerp(.6,1,back(qp)),0,7); g.fill(); txt('?',540,1013,54,{w:800,col:'#000'}); });
    al(sw,()=>appIcon(540,1010,92*lerp(.7,1,back(sw)))); });
  pill('WHY WORSE APPS WIN',540,250,pr(t,1.45,.35),{size:28}); }

function b3(t){
  al(eo(pr(t,0,.5)),()=>{ const gr=g.createLinearGradient(0,150,0,GY); gr.addColorStop(0,'rgba(255,255,255,.17)'); gr.addColorStop(1,'rgba(255,255,255,.03)'); g.fillStyle=gr; g.beginPath(); g.moveTo(450,120); g.lineTo(630,120); g.lineTo(880,GY); g.lineTo(200,GY); g.closePath(); g.fill(); });
  ground(); [190,365,540,715,890].forEach((x,i)=>{ const me=i===2; person(x,GY-42,me?1.08:.96,{col:me?'#fff':'#8f8f8f',glow:me?.34:0}); });
  g.save(); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4.5; rr(100,GY-128,880,118,16); g.fill(); g.stroke();
  g.strokeStyle='rgba(255,255,255,.7)'; g.lineWidth=3; [190,365,540,715,890].forEach(x=>{ g.beginPath(); g.ellipse(x,GY-92,44,11,0,0,7); g.stroke(); }); g.restore();
  const sp=pr(t,.55,.3); al(eo(sp),()=>{ glow(540,1068,90,.5); star(540,1068,26*lerp(.5,1,back(sp))); });
  pill('THE IDEA GUY',540,985,pr(t,.7,.35)); }

function b4(t){ ground(); person(250,GY,1.1,{col:'#a6a6a6'});
  person(600,GY,1.1,{glow:.3,arm:'point',flip:true,armP:eo(pr(t,.15,.3)),marker:'bulb'});
  al(eo(pr(t,.1,.3)),()=>{ g.save(); g.lineWidth=4.5; g.strokeStyle='#fff'; g.fillStyle='#000'; rr(140,560,800,176,18); g.fill(); g.stroke(); g.restore(); txt(typed("IT'S LIKE UBER, BUT FOR…",pr(t,.35,1.4),t),190,650,44,{w:800,a:'left',ls:2}); });
  pill('BEFORE THE FOOD CAME',540,470,pr(t,1.25,.35),{size:26});
  const wx=lerp(1230,965,eo(pr(t,.8,1.7))), wb=Math.sin(t*12)*4*(1-pr(t,2.2,.3));
  person(wx,GY+wb,1.0,{col:'#808080',arm:'point',flip:true,armP:.2});
  g.save(); g.strokeStyle='#9a9a9a'; g.fillStyle='#000'; g.lineWidth=4; g.beginPath(); g.arc(wx-98,GY-84+wb,30,Math.PI,0); g.fill(); g.stroke(); g.beginPath(); g.moveTo(wx-146,GY-84+wb); g.lineTo(wx-50,GY-84+wb); g.stroke(); g.restore(); }

function b5(t){ ground(); const xs=[165,350,540,730,915], lab=['MOM','ROOMMATE','','COWORKER','FRIENDS'], up=eo(pr(t,.2,.35));
  xs.forEach((x,i)=>{ const me=i===2; person(x,GY,1.0,me?{glow:.3,marker:'bulb'}:{col:'#b0b0b0',arm:'up',flip:i>2,armP:up}); if(!me) txt(lab[i],x,GY+36,16,{w:700,ls:4,col:'#8a8a8a'}); });
  pill('EVERYONE SAID IT',540,330,pr(t,.45,.35));
  const dp=eo(pr(t,.75,.9)); g.save(); g.strokeStyle='rgba(255,255,255,.75)'; g.lineWidth=3; g.setLineDash([8,9]); g.beginPath();
  for(let u=0;u<=dp;u+=.02){ const x=(1-u)*(1-u)*560+2*(1-u)*u*640+u*u*790, y=(1-u)*(1-u)*(GY-250)+2*(1-u)*u*820+u*u*640; u?g.lineTo(x,y):g.moveTo(x,y); } g.stroke(); g.restore();
  const ip=pr(t,1.5,.35); al(eo(ip),()=>{ glow(790,560,210,.34); appIcon(790,560,130*lerp(.7,1,back(ip)),{star:true}); });
  const bt=at(4,C.build_that); bubble('BUILD THAT!',215,1035,pr(t,bt,.25),{size:24}); bubble('BUILD THAT!',880,1045,pr(t,bt+.14,.25),{size:24}); bubble('YOU SHOULD BUILD THAT',540,950,pr(t,bt+.28,.25),{size:24}); }

function b6(t){ ground(); person(540,GY,1.0,ME);
  for(let i=0;i<10;i++){ const p=pr(t,i*.065,1.05); if(p<=0||p>=1) continue; const x=lerp(-70,W+70,p), y=330-Math.sin(p*Math.PI)*120+(i%3)*30; g.save(); g.translate(x,y); g.rotate((p*4+i)*.9); g.fillStyle='#fff'; rr(-27,-31,54,62,7); g.fill(); g.fillStyle='#000'; g.fillRect(-27,-31,54,15); g.restore(); }
  al(eo(pr(t,.08,.3))*(1-pr(t,1.0,.22)),()=>{ txt('YEARS LATER',540,600,24,{w:700,ls:7,col:'#bdbdbd'}); txt('+'+Math.round(lerp(1,3,eio(pr(t,.2,.65)))),540,715,150,{w:800}); });
  const np=eo(pr(t,1.0,.4)); al(np,()=>{ glow(540,760,430,.14); noteCard(240,lerp(560,470,np),600,540,5,'LAST EDITED 3 YEARS AGO'); });
  pill('STILL A NOTE',540,385,pr(t,1.4,.35)); }

function b7(t){ ground(); person(245,GY,1.0,{col:'#9a9a9a'}); person(395,GY,1.0,{col:'#9a9a9a'});
  al(eo(pr(t,.15,.3)),()=>{ txt('?',245,GY-245+Math.sin(t*3)*8,58,{w:800}); txt('?',395,GY-262+Math.sin(t*3+1.6)*8,58,{w:800}); });
  person(800,GY,1.05,ME); pill('NOBODY CAN EXPLAIN IT',540,1000,pr(t,.25,.35),{size:26});
  const cb=at(6,C.because); card(190,400,700,470,'WHAT WENT WRONG?',pr(t,cb-.4,.35));
  [['BUILT',false,cb+.15],['STILL A GREAT IDEA',true,cb+1.25],['STILL TALKS ABOUT IT',true,cb+2.6]].forEach((r,i)=>{ const y=540+i*115, p=pr(t,r[2],.3);
    al(eo(pr(t,r[2]-.15,.3)),()=>txt(r[0],240,y,34,{a:'left',w:800,ls:2})); r[1]?check(820,y,30,p):cross(820,y,30,p); }); }

function b8(t){ ground(); person(540,GY,1.05,ME); const op=at(7,C.opposite);
  pill('WHAT WENT WRONG?',540,330,pr(t,0,.3)*(1-pr(t,op-.25,.2)),{size:26});
  const dp=eo(pr(t,.25,.5)); g.save(); g.strokeStyle='rgba(255,255,255,.55)'; g.lineWidth=3; g.setLineDash([8,10]); g.beginPath(); g.moveTo(540,520); g.lineTo(540,lerp(520,1085,dp)); g.stroke(); g.restore();
  const a1=pr(t,.4,.35), a2=pr(t,.8,.35);
  al(eo(a1),()=>{ glow(270,730,240,.17); bulb(270,720,105,1,5.5); txt('IDEAS',270,925,42,{w:800,ls:9}); });
  al(eo(a2),()=>{ glow(810,730,240,.17); phone(810,600,150,250,{lw:5.5}); appIcon(810,715,66,{lw:4}); txt('APPS',810,925,42,{w:800,ls:9}); });
  const ap=eo(pr(t,op,.45)); if(ap>0){ g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineCap='round'; for(const d of [-1,1]){ const x0=540+d*78, x1=x0+d*230*ap; g.beginPath(); g.moveTo(x0,GY-100); g.lineTo(x1,GY-100); g.moveTo(x1-d*18,GY-114); g.lineTo(x1,GY-100); g.lineTo(x1-d*18,GY-86); g.stroke(); } g.restore(); }
  pill('OPPOSITE RULES',540,410,pr(t,op,.35)); }

function b9(t,d){ ground(); person(540,GY,1.05,{marker:'bulb',glow:.26}); const kp=at(8,C.kept);
  const n=3+Math.floor(pr(t,.15,kp)*3.99)+Math.floor(pr(t,kp,d-kp-.2)*4.99);
  glow(540,680,430,.13); noteCard(240,400,600,560,n,null);
  const dn=Math.round(lerp(1,12,pr(t,.2,d-.6))); g.save(); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4.5; g.beginPath(); g.arc(840,405,64,0,7); g.fill(); g.stroke(); g.restore(); txt('DRAFT',840,386,16,{w:700,ls:4,col:'#bdbdbd'}); txt(String(dn),840,422,40,{w:800});
  const sp=pr(t,.9,.3); al(eo(sp),()=>star(250,1035,20*lerp(.5,1,back(sp)))); pill('REWARDED FOR THINKING',575,1035,pr(t,.95,.35),{size:25});
  al(pr(t,kp,.2),()=>{ for(let i=0;i<3;i++){ g.fillStyle=`rgba(255,255,255,${.35+.65*Math.max(0,Math.sin(t*7-i*.9))})`; g.beginPath(); g.arc(640+i*30,GY-205-i*14,8+i*2,0,7); g.fill(); } }); }

function b10(t){ ground(); const fp=at(9,C.forty);
  person(290,GY,1.05,{marker:'bulb',glow:.2,rot:-.13*eo(pr(t,fp+.15,.4))});
  pill('DEVELOPER QUOTE',540,360,pr(t,.12,.35));
  const cp=pr(t,.08,.35); al(eo(cp),()=>{ glow(420,650,230,.2); g.save(); g.lineWidth=6; g.strokeStyle='#fff'; g.beginPath(); g.arc(420,650,98*lerp(.8,1,back(cp)),0,7); g.stroke(); g.restore(); txt('</>',420,654,64,{w:800}); txt('A DEVELOPER',420,790,21,{w:700,ls:6,col:'#bdbdbd'}); });
  const tp=pr(t,.5,.4); al(eo(tp),()=>{ g.save(); g.strokeStyle='#fff'; g.lineWidth=3; g.beginPath(); g.moveTo(488,722); g.lineTo(lerp(488,640,eo(tp)),lerp(722,900,eo(tp))); g.stroke(); g.restore();
    const v=lerp(400,40000,eio(pr(t,fp-.55,.6))), shown=v>1000?Math.round(v/100)*100:Math.round(v/10)*10, land=pr(t,fp+.05,.3);
    glow(790,935,230,.22*land); priceTag(790,935,'$'+fmt(shown),Math.sin(t*5)*.05*(1-pr(t,fp,.4))-.06,lerp(.9,1,tp)*(1+.14*Math.sin(Math.PI*land))); }); }

function b11(t){ ground(); person(540,GY,1.05,ME); const qp=at(10,C.quit);
  card(190,390,700,560,'LEARN TO CODE',pr(t,.03,.3));
  al(eo(pr(t,.1,.3)),()=>{ g.save(); g.strokeStyle='#fff'; g.lineWidth=3; rr(240,486,600,22,11); g.stroke(); g.fillStyle='#fff'; rr(240,486,lerp(8,24,pr(t,.3,1.1)),22,11); g.fill(); g.restore();
    for(let i=0;i<4;i++){ const y=572+i*84; txt('LESSON '+(i+1),250,y,34,{a:'left',w:800,ls:2,col:i<3?'#fff':'#9a9a9a'}); if(i<3) check(815,y,24,pr(t,.3+i*.28,.25)); }
    txt('LESSON 4 OF 120',540,905,19,{w:700,ls:6,col:'#8c8c8c'}); });
  if(t>qp){ g.save(); g.strokeStyle='#fff'; g.lineWidth=15; g.lineCap='round'; const a=eo(pr(t,qp,.16)), b=eo(pr(t,qp+.13,.16));
    g.beginPath(); g.moveTo(270,470); g.lineTo(lerp(270,810,a),lerp(470,890,a)); g.stroke(); if(b>0){ g.beginPath(); g.moveTo(810,470); g.lineTo(lerp(810,270,b),lerp(470,890,b)); g.stroke(); } g.restore(); }
  pill('QUIT',540,1040,pr(t,qp+.2,.3),{size:34}); }

function stepScene(h,label=1){ ground(GY,.55,0,600); if(h>3){ g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineJoin='round'; g.fillStyle='#000'; g.beginPath(); g.moveTo(600,GY+2); g.lineTo(600,GY-h); g.lineTo(W+10,GY-h); g.lineTo(W+10,GY+2); g.fill(); g.beginPath(); g.moveTo(600,GY+2); g.lineTo(600,GY-h); g.lineTo(W+10,GY-h); g.stroke(); g.restore(); al(cl(h/200)*label,()=>txt('BUILD',830,GY-h/2,58,{w:800,ls:12})); } else ground(GY,.55,600,W); }

function b12(t){ const ep=at(11,C.expensive); stepScene(330); person(330,GY,1.05,ME);
  const mp=eo(pr(t,.15,.55)); al(mp,()=>{ glow(820,GY-470,220,.2); priceTag(lerp(1150,820,mp),GY-470,'$40,000',-.07); });
  const xp=pr(t,.45,.3); al(eo(xp),()=>{ bubble('LESSON 4',470,GY-520,xp,{size:24}); g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineCap='round'; g.beginPath(); g.moveTo(385,GY-545); g.lineTo(555,GY-495); g.stroke(); g.restore(); });
  const up=eo(pr(t,.9,.5)); if(up>0){ g.save(); g.strokeStyle='rgba(255,255,255,.7)'; g.lineWidth=3; g.setLineDash([7,8]); g.beginPath(); g.moveTo(400,GY-150); g.quadraticCurveTo(470,GY-430,lerp(400,640,up),lerp(GY-150,GY-360,up)); g.stroke(); g.restore(); }
  pill('THE MOST EXPENSIVE STEP',540,400,pr(t,ep-.15,.35),{size:28}); }

function b13(t){ ground(); person(300,GY,1.05,ME); const k=pr(t,at(12,C.other)-.05,.38), sy=Math.abs(Math.cos(k*Math.PI)), second=k>.5;
  al(eo(pr(t,0,.3)),()=>{ glow(540,760,560,.2); g.save(); g.translate(540,760); g.scale(1,Math.max(sy,.03)); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=5; rr(-440,-112,880,224,22); g.fill(); g.stroke();
    txt(second?'APPS':'IDEAS',0,-64,23,{w:700,ls:8,col:'#bdbdbd'}); txt(second?'BUILD IT  →  THEN FIND OUT':'PERFECT IT  →  THEN BUILD',0,18,second?46:50,{w:800,ls:3}); g.restore(); }); }

function b14(t){ const ap=at(13,C.answer), tp=at(13,C.taps);
  if(t<ap+.2) al(1-pr(t,ap-.1,.28),()=>{ ground(); person(280,GY,1.05,ME);
    g.save(); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=4.5; rr(160,360,760,150,20); g.fill(); g.stroke(); g.restore(); txt('APPS',540,398,19,{w:700,ls:7,col:'#bdbdbd'}); txt('BUILD IT  →  THEN FIND OUT',540,452,38,{w:800,ls:2});
    pill('NOBODY CAN KNOW IN ADVANCE',540,585,pr(t,.2,.35),{size:25});
    const ip=pr(t,.45,.3); al(eo(ip),()=>{ glow(280,GY-340,120,.3); appIcon(280,GY-340,84*lerp(.7,1,back(ip))); txt('AN APP',280,GY-405,17,{w:700,ls:5,col:'#bdbdbd'}); });
    cloud(800,GY-150,1.35,.17*eo(pr(t,.3,.5))); al(eo(pr(t,.75,.3)),()=>txt('?',815,GY-160+Math.sin(t*3)*9,110,{w:800})); });
  if(t>=ap-.12) al(eo(pr(t,ap-.12,.35)),()=>{
    g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineJoin='round'; g.beginPath(); g.moveTo(-10,GY); g.lineTo(400,GY); g.lineTo(426,GY+80); g.lineTo(404,GY+170); g.lineTo(432,H+10); g.stroke(); g.restore();
    const wp=pr(t,ap+.3,tp-ap-.45), px=lerp(320,790,wp), nt=Math.ceil(Math.max(0,px-350)/116);
    for(let i=0;i<nt;i++){ const born=ap+.3+((350+i*116-320)/470)*(tp-ap-.45), q=pr(t,born,.18); al(eo(q),()=>{ glow(462+i*116,GY+4,70,.25*(1-pr(t,born,.6))); g.fillStyle='#fff'; rr(410+i*116,GY-5+(1-eo(q))*16,104,18,4); g.fill(); }); }
    person(px,GY-5-Math.abs(Math.sin(wp*Math.PI*5))*9*(wp<1?1:0),1.05,{glow:.28});
    pill('IT ONLY EXISTS ONCE SOMEONE TAPS',540,430,pr(t,ap+.15,.35),{size:24});
    const done=pr(t,tp,.4); cloud(905,GY-400,1.25,.18*(1-done)); glow(905,GY-400,200,.3*done); appIcon(905,GY-400,104);
    al(1-done,()=>txt('?',985,GY-470+Math.sin(t*3)*7,72,{w:800})); check(968,GY-462,30,done);
    if(done>0&&done<1){ g.save(); g.strokeStyle=`rgba(255,255,255,${1-done})`; g.lineWidth=5; g.beginPath(); g.arc(905,GY-400,lerp(50,170,eo(done)),0,7); g.stroke(); g.restore(); } }); }

function b15(t){ const h=lerp(330,0,eio(pr(t,.85,.95))); stepScene(h); const wp=eo(pr(t,1.85,.8)); person(lerp(330,760,wp),GY-Math.abs(Math.sin(wp*Math.PI*4))*8*(wp<1?1:0),1.05,ME);
  const v=lerp(40000,0,eio(pr(t,.25,.85))), fall=pr(t,1.15,.6); al(1-fall,()=>priceTag(820+fall*60,GY-470+h-330+fall*fall*520,'$'+fmt(Math.round(v/100)*100),-.07+fall*1.1));
  pill('THE STEP GOT CHEAP',540,400,pr(t,1.05,.35),{size:28}); }

function b16(t){ const vp=at(15,C.brand), dp=at(15,C.describe), wp=at(15,C.watch), np=at(15,C.nocode), inp=eo(pr(t,0,.4));
  g.save(); g.translate(0,(1-inp)*220); al(inp,()=>{ glow(540,930,760,.13); phone(540,430,520,1040,{lw:7});
    const s='a habit tracker for my gym';
    const op=pr(t,.35,.3), typing=t>=dp;
    al(eo(op),()=>{ g.fillStyle='#fff'; rr(325,540,430,86,43); g.fill(); txt(typing?typed(s,pr(t,dp,1.2),t):'Type your idea'+(Math.floor(t*3)%2?'|':''),358,584,29,{a:'left',w:600,col:typing?'#000':'#8a8a8a'}); });
    al(eo(pr(t,.5,.35))*(1-pr(t,dp+1.0,.25)),()=>{ const pu=1+.06*Math.sin(t*5); glow(540,930,240,.2); spark(540,930,70*pu); txt('WHAT SHOULD WE MAKE?',540,1050,22,{w:700,ls:5,col:'#bdbdbd'}); });
    if(t>dp+1.25&&t<wp+.9) txt('BUILDING'+'.'.repeat(1+Math.floor(t*5)%3),540,672,21,{w:700,ls:7,col:'#bdbdbd'});
    const part=(i,fn)=>{ const q=pr(t,wp+i*.15,.28); if(q<=0)return; al(eo(q),()=>{ g.save(); g.translate(540,0); g.scale(lerp(.86,1,back(q)),1); g.translate(-540,(1-eo(q))*26); fn(); g.restore(); }); };
    part(0,()=>{ g.strokeStyle='#fff'; g.lineWidth=3.5; rr(325,712,430,84,16); g.stroke(); txt('GYM HABITS',355,755,28,{a:'left',w:800,ls:3}); g.fillStyle='#fff'; g.beginPath(); g.arc(712,754,17,0,7); g.fill(); });
    ['Leg day','Protein','8 hours sleep'].forEach((r,i)=>part(1+i,()=>{ const y=826+i*112; g.strokeStyle='rgba(255,255,255,.75)'; g.lineWidth=3; rr(325,y,430,92,16); g.stroke(); txt(r,400,y+47,27,{a:'left',w:600}); const done=pr(t,wp+.9+i*.18,.2); g.strokeStyle='#fff'; g.beginPath(); g.arc(362,y+46,15,0,7); g.stroke(); if(done>0) check(362,y+46,15,done); }));
    part(4,()=>{ g.fillStyle='#fff'; rr(325,1178,430,92,46); g.fill(); txt('+ ADD HABIT',540,1225,26,{w:800,ls:4,col:'#000'}); });
    part(5,()=>{ g.strokeStyle='rgba(255,255,255,.6)'; g.lineWidth=3; g.beginPath(); g.moveTo(300,1318); g.lineTo(780,1318); g.stroke(); [400,540,680].forEach((x,i)=>{ g.fillStyle=i?'rgba(255,255,255,.45)':'#fff'; g.beginPath(); g.arc(x,1378,13,0,7); g.fill(); }); }); });
  g.restore();
  pill(BRAND.name.toUpperCase(),540,315,pr(t,vp,.35),{size:40}); pill('LIVE ON YOUR PHONE',540,1575,pr(t,wp+.95,.35),{size:27});
  const q=pr(t,np,.3); al(eo(q),()=>{ glow(930,640,150,.3); g.save(); g.translate(930,640); g.scale(lerp(.6,1,back(q)),lerp(.6,1,back(q))); g.fillStyle='#000'; g.strokeStyle='#fff'; g.lineWidth=5; g.beginPath(); g.arc(0,0,66,0,7); g.fill(); g.stroke(); txt('</>',0,3,40,{w:800}); g.lineWidth=7; g.lineCap='round'; g.beginPath(); g.moveTo(-46,46); g.lineTo(46,-46); g.stroke(); g.restore(); });
  pill('NO CODE',930,752,pr(t,np+.08,.3),{size:22}); }

function b17(t){ ground(); g.save(); g.strokeStyle='#fff'; g.lineWidth=5; g.lineCap='round'; g.beginPath(); g.moveTo(430,GY-150); g.lineTo(900,GY-150); g.moveTo(462,GY-150); g.lineTo(462,GY); g.moveTo(868,GY-150); g.lineTo(868,GY); g.stroke();
  const n=Math.round(lerp(7,15,pr(t,0,2.2))); g.lineWidth=3; for(let i=0;i<n;i++){ rr(486+rnd(i)*12,GY-164-i*11,170,9,2); g.fillStyle='#000'; g.fill(); g.stroke(); }
  g.lineWidth=4.5; g.save(); g.translate(770,GY-156); g.rotate(-.1); rr(-80,-118,160,112,8); g.fillStyle='#000'; g.fill(); g.stroke(); g.lineWidth=3; for(let i=0;i<3;i++){ g.beginPath(); g.moveTo(-58,-92+i*24); g.lineTo(-58+(70+rnd(i+Math.floor(t*6))*40),-92+i*24); g.stroke(); } g.restore(); g.restore();
  txt('DRAFT '+Math.round(lerp(41,47,pr(t,0,2))),572,GY-175-n*11-22,19,{w:700,ls:5,col:'#bdbdbd'});
  person(345,GY,1.05,{marker:'bulb',glow:.2,arm:'point',armP:.5});
  glow(540,650,170,.2); clock(540,650,74,t*10);
  for(let i=0;i<8;i++){ const q=pr(t,.25+i*.27,.55); if(q<=0) continue; const x=lerp(760,905+(i%3)*34,q), y=lerp(GY-250,GY-14-Math.floor(i/3)*24,q*q)-Math.sin(q*Math.PI)*90; g.save(); g.fillStyle='#fff'; g.beginPath(); g.arc(x,y,13,0,7); g.fill(); g.restore(); }
  pill('POLISHING THE PERFECT PLAN',540,470,pr(t,.35,.35),{size:26}); }

function b18(t){ const ty=at(17,C.types), sh=at(17,C.ships), fx=at(17,C.fixes), L=eio(pr(t,sh+.45,1.0)), ver=t<fx+.25?1:(t<fx+.95?2:3);
  if(L>0) for(let i=0;i<6;i++){ const y=((i*390+t*620)%2340)-200; cloud(i%2?150+rnd(i)*160:780+rnd(i)*180,y,.8+rnd(i)*.4,.06*L); }
  g.save(); g.translate(0,L*1250); al(1-pr(t,sh+.9,.4),()=>{ ground(); person(245,GY,1.05,{arm:'point',armP:1,glow:.22}); g.fillStyle='#fff'; rr(318,GY-132,30,52,7); g.fill();
    txt('WORSE IDEA',245,GY+38,17,{w:700,ls:5,col:'#9a9a9a'});
    const ps='to-do list, but ugly'; al(eo(pr(t,ty-.25,.25)),()=>{ g.fillStyle='#fff'; rr(95,GY-345,400,74,37); g.fill(); txt(typed(ps,pr(t,ty,.85),t),128,GY-307,28,{a:'left',w:600,col:'#000'}); });
    person(845,GY,.95,{col:'#8c8c8c'}); person(955,GY,.95,{col:'#8c8c8c'}); bubble('HA HA',815,GY-265,pr(t,ty+.75,.25)); bubble('HA HA',960,GY-325,pr(t,ty+.95,.25));
    pill('EMBARRASSING V1',590,GY-440,pr(t,sh-.1,.3),{size:26}); }); g.restore();
  const rp=pr(t,.25,.45), ry=lerp(GY-125,960,L)+(L>=1?Math.sin(t*5)*9:0), rx=lerp(590,540,L);
  al(eo(rp),()=>{ if(L>.2) glow(rx,ry,360,.16*L); rocket(rx,ry,1.3*lerp(1,1.22,L),{flame:pr(t,sh+.25,.4),t,patches:ver===1?4:ver===2?2:0}); });
  if(L>.55){ const vp=ver===1?pr(t,sh+1.2,.3):ver===2?pr(t,fx+.25,.25):pr(t,fx+.95,.25); pill('V'+ver,265,700,vp,{size:34});
    const msg=(s,st,fromX,toX,y)=>{ const q=pr(t,st,.42), hit=pr(t,st+.42,.25); if(q<=0||hit>=1) return; al(1-hit,()=>{ const x=lerp(fromX,toX,eo(q)), w=tw(s,24,{w:600})+52; g.fillStyle='#fff'; rr(x-w/2,y-30,w,60,30); g.fill(); txt(s,x,y+1,24,{w:600,col:'#000'}); }); };
    msg('make the button bigger',fx-.2,-260,400,1010); msg('add dark mode',fx+.5,W+220,700,930);
    pill('FIXES IT ALONG THE WAY',540,400,pr(t,fx-.05,.35),{size:26}); } }

function b19(t){ const lk=at(18,C.luck), ax=eo(pr(t,0,.45));
  g.save(); g.strokeStyle='rgba(255,255,255,.85)'; g.lineWidth=3; g.lineCap='round'; g.beginPath(); g.moveTo(170,GY); g.lineTo(170,lerp(GY,430,ax)); g.moveTo(170,GY); g.lineTo(lerp(170,1010,ax),GY); g.stroke(); g.restore();
  const cp=eio(pr(t,.3,2.2)), k=4.3, f=u=>[170+u*770,GY-(Math.exp(u*k)-1)/(Math.exp(k)-1)*850];
  g.save(); g.strokeStyle='#fff'; g.lineWidth=6; g.lineCap='round'; g.lineJoin='round'; g.beginPath(); for(let u=0;u<=cp+1e-6;u+=.008){ const p=f(Math.min(u,cp)); u?g.lineTo(p[0],p[1]):g.moveTo(p[0],p[1]); } g.stroke(); g.restore();
  const a=f(cp), b=f(Math.max(0,cp-.015)), ang=cp>.02?Math.atan2(a[1]-b[1],a[0]-b[0])+Math.PI/2:Math.PI/2;
  glow(a[0],a[1],170,.32); rocket(a[0],a[1],.46,{rot:ang,flame:1,t});
  al(eo(pr(t,.35,.3)),()=>{ txt('USERS',520,610,23,{w:700,ls:7,col:'#bdbdbd'}); txt(fmt(1+Math.pow(cp,3.2)*99999),520,690,96,{w:800}); });
  person(88,GY,.95,{glow:.25});
  const crowd=pr(t,1.55,.4); al(eo(crowd),()=>[330,455,580,705,830].forEach((x,i)=>person(x,GY+(1-eo(crowd))*40,.92,{col:'#a8a8a8',arm:'up',armP:eo(pr(t,1.75+i*.07,.3))})));
  bubble('LUCK!',315,GY-300,pr(t,2.15,.25),{size:23}); bubble('SO LUCKY',565,GY-345,pr(t,2.38,.25),{size:23}); bubble('PURE LUCK',805,GY-290,pr(t,2.6,.25),{size:23});
  const dq=pr(t,2.0,.4); al(eo(dq),()=>{ dice(300,850+Math.sin(t*2.2)*14,62,t*1.3); dice(770,960+Math.sin(t*2.6+1)*12,74,-t*1.1+.5); });
  const tp=pr(t,lk-.45,.4); al(eo(tp),()=>{ glow(540,285,520,.2); txt('THEY CALL IT LUCK',540,285+(1-eo(tp))*24,66,{w:800,ls:7}); }); }

// End card: the App Store listing, filled from brand.js (made from brand.config.json by engine/tools/apply_brand.py).
const STORE=BRAND.store;
const TAP=1.35, DL=.95;   // when Get is tapped (local seconds) and how long the download ring runs
function b20(t){ const p=pr(t,.1,.5), up=(1-eo(p))*36;
  g.save(); g.translate(0,up); al(eo(p),()=>appStore(700,{...STORE,icon:p,text:eo(pr(t,.22,.4)),strip:eo(pr(t,.42,.45)),tap:pr(t,TAP,.5),state:t<TAP+.12?0:pr(t,TAP+.12,DL)}));
  g.restore(); if(HANDLE) al(eo(pr(t,.9,.4)),()=>txt(HANDLE,540,1360,26,{w:600,col:'#8E8E93'})); }

function renderAt(T){ bg();
  B.forEach((b,i)=>{ if(T<b.s||T>=b.e) return; NOW=T; BI=i; const t=T-b.s, d=b.e-b.s, last=i===B.length-1, inn=eo(pr(t,0,.24)), out=last?1:1-pr(t,d-.13,.13);
    g.save(); g.globalAlpha=inn*out; const z=1+.028*(t/d); g.translate(W/2,H/2); g.scale(z,z); g.translate(-W/2+(1-inn)*(i%2?-1:1)*70-(1-out)*(i%2?-1:1)*-50,-H/2); b.fn(t,d); g.restore(); });
  if(HANDLE&&T<B[B.length-1].s) al(.85,()=>txt(HANDLE,930,150,22,{w:700,ls:2})); }
(ICON.decode?ICON.decode():Promise.resolve()).catch(()=>{}).then(()=>{ window.renderAt=renderAt; window.DURATION=DURATION;
  if(location.hash==='#play'){ const t0=performance.now(); (function loop(){ renderAt(((performance.now()-t0)/1000)%DURATION); requestAnimationFrame(loop); })(); } else renderAt(1); });
