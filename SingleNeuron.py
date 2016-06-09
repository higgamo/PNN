# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 23:28:26 2016

@author: Guanhao Wu
"""
from Neuron import Neuron
from NeuronParameters import NeuronParameters
import matplotlib.pyplot as plt
import numpy as np

T=60000
V=[]

N=Neuron()
P=NeuronParameters()
P.set_RS(N)

for t in range(T):
    if t>50:
        N.clamp_input(85)
        
    N.timestep()
    V.append(N.V)
    
plt.figure()
plt.plot(np.linspace(0,T*N.dt,T),V,'r')
plt.show()
