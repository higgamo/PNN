# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:11:34 2016

@author: Guanhao Wu
"""

class Neuron():
    def __init__(self):
        self.k=.7
        self.vr=-60
        self.vt=-40
        self.vp=35
        self.I=0
        self.md=1
        self.delayI=[0]*self.md
        self.C=100
        self.a=.03
        self.b=-2
        self.c=-50
        self.d=100
        self.fired=False
        self.V=-50
        self.U=0
        self.dt=1
        self.t=0
#timestep phase        
    def updateI(self):
        self.I+=self.delayI[self.t%self.md]
        self.delayI[self.t%self.md]=0
        
    def dV(self):
        return (self.k*(self.V-self.vr)*(self.V-self.vt)-self.U+self.I)/self.C
        
    def dU(self):
        return self.a*(self.b*(self.V-self.vr)-self.U)
        
    def timestep(self): #called externally (public function)
        self.fired=False
        self.updateI()
        DV=self.dV()
        DU=self.dU()
        
        self.V+=self.dt*DV
        self.U+=self.dt*DU
        
        if self.V>=self.peak():
            self.fired=True
            self.v_reset()
            self.u_reset()
            
        self.reset_input()
        self.t+=1
            
    def peak(self):
        return self.vp        
        
    def v_reset(self):
        self.V=self.c
        
    def u_reset(self):
        self.U+=self.d
        
    def reset_input(self):
        self.I=0
#communication phase        
    def update_delayI(self,w,d): 
        self.delayI[(self.t-1+d)%self.md]+=w 
#network generation        
    def adjustMaxD(self,delay):
        self.md=max(self.md,delay)
        
    def delaygen(self):
        self.delayI=[0 for x in range(self.md)]
#helper function    
    def clamp_input(self,i):
        self.I+=i
        
    def give_V(self):
        return self.V
        
    def give_U(self):
        return self.U