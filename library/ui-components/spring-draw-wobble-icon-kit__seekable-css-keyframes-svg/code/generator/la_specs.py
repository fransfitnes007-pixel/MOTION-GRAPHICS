from core import *
S=.15
def draw(t0=S,dur=.4,pre=S,od=.1,**x):   # pathLength+opacity draw-in
    return [A(t0,od,EIO,pre=pre,opacity=[0,1]),A(t0,dur,EIO,pre=pre,pl=[0,1],**x)]
def hold_ret(t_out,t_back,d,ease,**p):    # go to p[1] at t_out, return at t_back
    a=A(t_out,d,ease,**{k:[v[0],v[1]] for k,v in p.items()})
    b=A(t_back,d,ease,**{k:[v[1],v[0]] for k,v in p.items()})
    return a+b
SPEC={}
def icon(name,L=2,spec=None,origins=None,extra=None,tree=None): SPEC[name]=dict(L=L,spec=spec or {},origins=origins or {},extra=extra,tree=tree)
bars=lambda i:[A(S,.4,EIO,opacity=[1,0])+A(.55+.4*i,.6,EIO,opacity=[0,1])]
icon('battery-full',3,{2:bars(0),3:bars(1),4:bars(2)})
icon('bell',2,{'root':[A(S,.5,EIO,rotate=[0,-10,10,-10,0])]})
icon('bookmark',2,{0:[A(S,.6,EO,scaleY=[1,1.3,.9,1.05,1],scaleX=[1,.9,1.1,.95,1])]})
brainL=lambda a,b:[A(0,1.4,EIO,pl=[1,a,1],po=[0,b,0])]
icon('brain',1.5,{'root':[A(0,1.4,EIO,scale=[1,1.08,1],sw=[2,2.25,2])],0:brainL(.4,.25),1:brainL(.5,.25),2:brainL(.8,.07),3:brainL(.8,.07),5:brainL(.8,.14),7:brainL(.8,.14)})
icon('calendar-check',2,{4:draw(S,.4)[:0]+[A(S,.4,EIO,pl=[0,1],opacity=[0,1])]})
icon('cart',2,{'root':[[(S,{'scale':1,'y':0},EIO),(.25,{'scale':1.03,'y':0},EIO),(.45,{'scale':1.1,'y':-5},EIO),(.65,{'scale':1.1,'y':0},EIO),(.85,{'scale':1.1,'y':-5},EIO),(1.05,{'scale':1.1,'y':0},EIO),(1.5,{'scale':1,'y':0},EIO)]]})
icon('chart-column-increasing',2,{0:None,1:None,3:None})
SPEC['chart-column-increasing']['spec']={i:[A(S+.1*c,.3,EIO,opacity=[1,0],pl=[1,0])+A(.65+.1*c,.3,EIO,opacity=[0,1],pl=[0,1])] for i,c in ((3,0),(0,1),(1,2))}
icon('check-check',2,{0:[A(S,.1,EO,opacity=[0,1]),A(S,.4,EIO,pl=[0,1],scale=[.5,1])],1:[A(.25,.1,EO,pre=S,opacity=[0,1]),A(.25,.4,EIO,pre=S,pl=[0,1],scale=[.5,1])]})
icon('check',2,{0:[A(S,.1,EO,opacity=[0,1]),A(S,.4,EIO,pl=[0,1],scale=[.5,1])]})
icon('clock',2,{1:[A(S,.6,EMD,rotate=[0,360])],2:[A(S,.5,EIO,rotate=[0,45])+A(1.15,.5,EIO,rotate=[45,0])]},{1:'fill:0% 100%',2:'fill:0% 100%'})
icon('dollar-sign',2,{0:[A(S,.1,EO,opacity=[0,1]),A(S,.6,EIO,pl=[0,1])],1:[A(.65,.1,EO,pre=S,opacity=[0,1]),A(.65,.4,EIO,pre=S,pl=[0,1],po=[1,0])]})
for n,y in (('download',2),('upload',-2)):
    e,T=sp(200,10)
    icon(n,3,{1:[SPR(S,200,10,y=[0,y])+SPR(1.6,200,10,y=[y,0])]})
icon('droplet',2,{0:[A(.35,.1,EIO,pre=S,opacity=[0,1]),A(.35,.6,EIO,pre=S,pl=[0,1],po=[1,0])]})
icon('eye',2,{0:[A(S,.4,EIO,scaleY=[1,.1,1]),A(S,.4,EIO,opacity=[1,.3,1])],1:[A(S,.4,EIO,scale=[1,.3,1]),A(S,.4,EIO,opacity=[1,.3,1])]})
icon('flame',2,{0:[A(.25,.1,EIO,pre=S,opacity=[0,1]),A(.25,.4,EIO,pre=S,pl=[0,1])]})
icon('heart',2,{'root':[A(S,1.35,EIO,times=[0,1/6,2/6,3/6,4/6,5/6,1],scale=[1,1.08,1,1.08,1,1.08,1])]})
icon('home',2,{1:[A(S,.2,EIO,opacity=[0,1]),A(S,.6,EIO,pl=[0,1])]})
e,T=sp(400,10)
icon('message-circle',2,{0:None})
SPEC['message-circle']['spec']={'root':[A(S,.5,EIO,rotate=[0,-7,7,0],scale=[1,1.05,1.05,1.05])+A(1.15,.3,EIO,rotate=[0,0],scale=[1.05,1])]}
icon('mic',2,{2:[A(S,.6,EIO,y=[0,-3,0,-2,0])]})
icon('moon',2,{'root':[A(S,1.2,EIO,rotate=[0,-10,10,-5,5,0])]})
TR=dict(x=[-5,-3,-1.5,-.5,0],y=[5,3,1.5,.5,0])
dots=lambda:[A(S,.35,EO,opacity=[0,1]),A(S,.7,EIO,scale=[.5,.8,1,1.1,1],**TR)]
lines=lambda:[A(S,.35,EO,opacity=[0,1]),A(S,.7,EIO,pl=[0,.25,.5,.75,1],scale=[.3,.8,1,1.1,1],**TR)]
icon('party-popper',2,{0:[A(S,.45,EO,x=[-1.5,0],y=[1.5,0])],1:[A(S,.45,EO,x=[-1.5,0],y=[1.5,0])],
  2:dots(),3:dots(),4:dots(),5:dots(),6:lines(),7:lines(),8:lines()})
# dots: translateX[-5,0], translateY[5,0] (source); handled by dx,dy above -> y from +5
icon('phone',2,{'root':[A(S,.9,EIO,rotate=[10,20,-10,10,0],scale=[1,1.1,1.1,1.05,1])]})
icon('play',2,{0:[A(S,.5,EIO,times=[0,.2,.5,1],x=[0,-1,2,0],rotate=[0,-10,0,0])]})
icon('plus',2,{'root':[SPR(S,100,15,rotate=[0,180])]})
icon('refresh-cw',3,{'root':[SPR(S,250,25,rotate=[0,50])+SPR(1.4,250,25,rotate=[50,0])]})
fl0="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"
fl1="M4.5 16.5c-1.5 1.26-3 5.5-3 5.5s4.74-1 6-2.5c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"
fl2="M4.5 16.5c-1.5 1.26-2.2 4.8-2.2 4.8s3.94-0.3 5.2-1.8c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"
fl3="M4.5 16.5c-1.5 1.26-2.8 5.2-2.8 5.2s4.54-0.7 5.8-2.2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"
flame=[]
for k in range(3): flame+=A(2*k,2,EMD,times=[0,.2,.5,.8,1],d=[fl0,fl1,fl2,fl3,fl0])[:(5 if k==2 else 4)]
icon('rocket',6,{'root':[A(0,6,EIO,times=[0,.15,.3,.45,.6,.75,.9,1],x=[0,0,-3,2,-2,1,-1,0],y=[0,-3,0,-2,-3,-1,-2,0])],0:[flame]})
icon('search',2,{'root':[A(S,1,EIO,times=[0,.33,.66,1],x=[0,0,-3,0],y=[0,-4,0,0])]})
icon('send',2,{0:[A(S,.5,EO,x=[0,3],y=[0,-3],scale=[1,.8])+A(1.2,.3,EO,x=[3,0],y=[-3,0],scale=[.8,1])],
   3:[A(.25,.55,EO,x=[-3,0],y=[3,0])+A(1.2,.3,EO,x=[0,-3],y=[0,3]),A(.25,.55,EO,pl=[0,1],opacity=[0,1])+A(1.2,.3,EO,pl=[1,0],opacity=[1,0])]})
icon('settings',3,{'root':[SPR(S,50,10,rotate=[0,180])+SPR(1.7,50,10,rotate=[180,360])]})
icon('shield-check',2,{1:[A(S,.1,EO,opacity=[0,1]),A(S,.4,EIO,pl=[0,1],scale=[.5,1])]})
icon('sparkles',3,{0:[A(S,1,EIO,times=[0,.33,.66,1],y=[0,-1,0,0]),A(S,.4,EO,fo=[0,1])+A(2.4,.4,EO,fo=[1,0])],
  **{i:[A(1.15,1.6,EO,opacity=[0,1,0,0,0,0,1])] for i in (1,2,3,4)}},extra={0:{'fill':'currentColor','fill-opacity':'0'}})
icon('trending-up',2,{'root':[A(S,.5,EIO,x=[0,2,0],y=[0,-2,0])],0:[A(S,.1,EO,opacity=[0,1]),A(S,.4,EIO,pl=[0,1],po=[1,0])],1:[A(.45,.1,EO,pre=S,opacity=[0,1]),A(.45,.3,EIO,pre=S,pl=[0,1],po=[.5,0])]})
icon('user',2,{0:[A(S,.4,EIO,pl=[0,1],po=[1,0],scale=[.5,1])],1:[A(.35,.1,EO,pre=S,opacity=[0,1]),A(.35,.4,EIO,pre=S,pl=[0,1],po=[1,0])]})
icon('users',2,{2:[SPR(.25,200,13,pre=S,x=[-6,0])],3:[SPR(.25,200,13,pre=S,x=[-6,0])]})
icon('wallet',2,{'root':[A(S,.55,EIO,times=[0,.45,1],y=[0,-3,0],rotate=[0,-4,0])]})
wifi_tree={'tag':'svg','attrs':{},'kids':[{'tag':'path','attrs':{'d':d},'kids':[]} for d in ("M12 20h.01","M8.5 16.429a5 5 0 0 1 7 0","M5 12.859a10 10 0 0 1 14 0","M2 8.82a15 15 0 0 1 20 0")]}
icon('wifi',2,{i:[A(S,.2,EO,opacity=[1,0])+SPR(.45+.1*i,300,20,opacity=[0,1])] for i in (1,2,3)},tree=wifi_tree)
icon('x',2,{0:[A(S,.1,EO,opacity=[0,1]),A(S,.4,EIO,pl=[0,1])],1:[A(.35,.1,EO,pre=S,opacity=[0,1]),A(.35,.4,EIO,pre=S,pl=[0,1])]})
icon('zap',2,{0:[A(S,.1,EO,opacity=[0,1]),A(S,.6,EIO,pl=[0,1])]})
# lock pair
icon('lock',2,{'root':[A(S,1,EMD,times=[0,.33,.66,1],rotate=[-3,1,-2,0],scale=[.95,1.05,.98,1])],1:[A(S,.3,EMD,pl=[1,.7])+A(1.15,.3,EMD,pl=[.7,1])]})
icon('lock-open',2,{'root':[A(S,1,EMD,times=[0,.33,.66,1],rotate=[2,4,-2,0],scale=[1.05,.95,1.02,1])],1:[A(0,.001,LIN,pl=[.8,.8])+A(S,.3,EMD,pl=[.8,1])+A(1.15,.3,EMD,pl=[1,.8])]})
