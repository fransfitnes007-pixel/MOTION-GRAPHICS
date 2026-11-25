from core import *
S=.15
SPEC={}
def icon(name,L=2,spec=None,origins=None,extra=None,tree=None): SPEC[name]=dict(L=L,spec=spec or {},origins=origins or {},extra=extra,tree=tree)
V=lambda x,y:f'{x}px {y}px'
icon('bell-ring',2,{'root':[A(S,1.1,EIO,rotate=[0,-12,10.2,-6,3,0])],0:[A(S,1.1,EIO,x=[0,1.7,-1.4,.8,-.4,0])],
  1:[A(S+.07,1.1,EO,times=[0,.18,.385,.59,.795,1],opacity=[1,.5,1,.25,1,1],scale=[1,.6,1.15,.7,1.15,1])],
  3:[A(S+.07,1.1,EO,times=[0,.18,.385,.59,.795,1],opacity=[1,.5,1,.25,1,1],scale=[1,.6,1.15,.7,1.15,1])]},
  {'root':V(12,0),1:'fill:0% 100%',3:'fill:100% 100%'})
icon('book-open',2,{1:[A(S,.8,EIO,times=[0,.3,.72,1],scaleX=[1,.8,1.05,1])]},{1:V(12,12)})
icon('camera',2,{0:[A(S,.35,EIO,scaleY=[1,.97,1])],1:[A(S,.7,EIO,times=[0,.35,.7,1],scale=[1,.6,1.15,1])]},{0:V(12,13),1:V(12,13)})
icon('crown',2,{0:[A(S,.8,EIO,times=[0,.3,.7,1],y=[0,-5,.8,0],rotate=[0,-8,4,0]),A(S,.8,EIO,times=[0,.3,.6,1],opacity=[1,0,1,1])],1:[A(S,.8,EIO,times=[0,.6,.72,.86,1],scaleX=[1,1,.8,1.06,1])]},{0:V(12,17),1:V(12,21)})
icon('dumbbell',2,{0:[A(S,.8,EIO,rotate=[0,-16,0,-16,0],scale=[1,.92,1,.92,1])]},{0:V(12,12)})
icon('film',2,{3:[A(S,.8,EIO,times=[0,.4,.5,1],y=[0,3,-3,0],opacity=[1,0,0,1])]})
icon('flag',2,{0:[A(S,.8,EIO,skewY=[0,11,-7,3,0])]},{0:V(4,12)})
icon('gamepad',2,{0:[A(S,.6,EIO,rotate=[0,-4,4,-3,2,0])],2:[A(S,.5,EIO,times=[0,.35,.7,1],scale=[1,.7,1.08,1])],5:[A(S+.15*.3*0+.15,.3,EIO,scale=[1,2,1])],6:[A(S+.33,.3,EIO,scale=[1,2,1])]},{0:V(12,12),2:V(8,11),5:V(15,12),6:V(18,10)})
icon('ghost',2,{0:[A(S,1,EIO,y=[0,1.2,-.8,.6,0],rotate=[0,-4,3,-2,0])],1:[A(S,1,EIO,x=[0,-1.2,1.2,1.2,0])],2:[A(S,1,EIO,x=[0,-1.2,1.2,1.2,0])]},{0:V(12,12)})
icon('gift',2,{0:[A(S,.7,EIO,times=[0,.4,.75,1],scaleY=[1,1.06,1,1])],2:[A(S,.7,EIO,times=[0,.4,.75,1],rotate=[0,-5.5,1.5,0])],3:[A(S,.7,EIO,times=[0,.4,.75,1],scaleY=[1,.92,1,1])]},{0:V(12,21),2:V(3,11),3:V(12,7)})
icon('globe',2,{1:[A(S,.9,EIO,scaleX=[1,-1,1])]},{1:V(12,12)})
icon('hand-heart',2,{0:[A(S,.8,EIO,y=[0,-.8,0])],3:[A(S,.8,EIO,times=[0,.3,.6,1],y=[0,-1.5,-1.5,0],scale=[1,1.2,.95,1])]},{3:V(16,8)})
icon('heart-plus',2,{0:[A(S,.8,EIO,scale=[1,1.13,.97,1.07,1])],1:[A(S,.5,EIO,times=[0,.5,1],rotate=[0,45,90],scale=[1,1.2,1])]},{0:V(12,12),1:V(18,15)})
icon('image-plus',2,{0:[A(S,.5,EIO,times=[0,.5,1],rotate=[0,45,90],scale=[1,1.2,1])],3:[A(S+.1,.6,EIO,times=[0,.35,.7,1],scale=[1,1.35,.9,1])]},{0:V(19,5),3:V(9,9)})
icon('key',2,{0:[A(S,.7,EIO,times=[0,.4,.75,1],rotate=[0,11,-5,0])]},{0:V(7.5,15.5)})
icon('lightbulb',2,{0:[A(S,.6,EIO,times=[0,.35,.7,1],scale=[1,1.08,.97,1])],1:[A(S,.7,EIO,opacity=[1,.35,1,.6,1])]},{0:V(12,9)})
icon('link',2,{0:[A(S,.9,EIO,x=[0,2,0],rotate=[0,3,0])],1:[A(S,.9,EIO,x=[0,-2,0],rotate=[0,-3,0])]})
icon('map-pin',2,{0:[A(S,.7,EIO,times=[0,.3,.6,.85,1],y=[0,1,.3,0,0],rotate=[0,-9,7,-3,0])]},{0:V(12,22)})
icon('medal',2,{4:[A(S,.9,EIO,rotate=[0,20,-14,7,0])]},{4:V(12,12)})
icon('megaphone',2,{0:[A(S,.8,EIO,rotate=[0,-8,6,-3,0],x=[0,1.2,-.5,.3,0])]},{0:V(5,11)})
icon('music',2,{0:[A(S,.8,EIO,rotate=[0,-6,0,5,0],y=[0,-2,0,-1.2,0])],2:[A(S,.8,EIO,scale=[1,1.2,1,1,1])],3:[A(S,.8,EIO,scale=[1,1,1,1.2,1])]},{0:V(12,12),2:V(6,18),3:V(18,16)})
st=lambda dl:[A(S+.1+dl,.55,EIO,times=[0,.3,.7,1],scale=[1,.88,1.06,1])]
cf=lambda dl:[A(S+.25+dl,.4,EIO,scale=[1,1.7,1])]
icon('party-popper',2,{0:[A(S,.6,EIO,times=[0,.3,.65,1],rotate=[0,-7,3,0])],3:st(0),4:st(.06),5:st(.03),6:cf(0),7:cf(.05),8:cf(.1),9:cf(.15)},
  {0:V(2,22),3:V(10,15),4:V(10,15),5:V(10,15),6:V(4,3),7:V(15,2),8:V(22,8),9:V(22,20)})
icon('share',2,{0:[A(S,.6,EIO,times=[0,.3,.7,1],y=[0,1.5,-1,0])],3:[A(S,.6,EIO,times=[0,.3,.7,1],scaleY=[1,.94,1.02,1])]},{3:V(12,22)})
icon('star',2,{0:[A(S,.8,EIO,rotate=[0,-12,10,-5,0],scale=[1,1.06,.97,1.02,1])]},{0:V(12,12.5)})
icon('sun',2,{'root':[A(S,.8,EIO,times=[0,.4,.75,1],rotate=[0,14,-6,0])],0:[A(S,.8,EIO,scale=[1,1.18,1])],**{i:[A(S,.8,EIO,opacity=[1,.7,1])] for i in range(1,9)}})
icon('target',2,{0:[A(S+.2,.5,EIO,scale=[1,1.08,1])],1:[A(S+.1,.5,EIO,scale=[1,1.22,1])],2:[A(S,.5,EIO,scale=[1,1.7,1])]},{0:V(12,12),1:V(12,12),2:V(12,12)})
icon('thumbs-up',2,{'root':[A(S,.855,EIO,scale=[1,1.08,.98,1.03,1],rotate=[0,-8,6,-4,0])],0:[A(S+.072,.63,EIO,scaleY=[1,.92,1.04,1]),A(S+.072,.63,EIO,opacity=[1,.85,1])],1:[A(S+.045,.855,EIO,rotate=[0,-8,6,-4,0],y=[0,-4,-8,-4,0],scale=[1,1.05,1.1,1.04,1])]})
icon('trophy',2,{0:[A(S,.8,EIO,y=[0,-2,0,-1,0],rotate=[0,-8,6,-3,0])]},{0:V(12,22)})
icon('video',2,{0:[A(S,.7,EIO,scaleY=[1,.1,1,.1,1])]},{0:V(19,12)})
sp_=lambda i:[A(S+.15+i*.12,.5,EO,times=[0,.25,.65,1],scale=[1,0,1.3,1],opacity=[1,0,1,1])]
icon('wand-sparkles',2,{0:[A(S,.7,EIO,rotate=[0,-8,5,-2,0])],3:sp_(0),6:sp_(1),9:sp_(2)},{0:V(3,21),3:V(5,8),6:V(10,3),9:V(19,16)})
