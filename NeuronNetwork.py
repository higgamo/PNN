# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 23:21:17 2016

@author: Guanhao Wu
"""

from NetworkClass import Network
from Neuron import Neuron
from random import random,randint
from NeuronParameters import NeuronParameters
import networkx as nx
import matplotlib.pyplot as plt

Net=Network()
P=NeuronParameters()

n_excit=800
n_inhib=200
n_total=n_excit+n_inhib         #number of neurons
p_excit=.15
p_inhib=.25
I_clamp=150
n_clamp=50

w_excitmax=250
w_inhibmax=-500
d_excitmax=25
d_inhibmax=10

T=500

for n in range(n_excit):
    Net.add_node(n)
    Net.node[n]['model']=Neuron()
    P.set_RS(Net.node[n]['model'])
    
for n in range(n_excit,n_total):
    Net.add_node(n)
    Net.node[n]['model']=Neuron()
    P.set_CP(Net.node[n]['model'])
    
for n in Net.nodes():
    if n<n_excit:
        for m in Net.nodes():
            if n!=m and random()<p_excit:
                Net.add_edge(n,m,weight=w_excitmax*(1 - random()**2))
                Net[n][m]['delay']=randint(1,d_excitmax)
    else:
        for m in Net.nodes():
            if n!=m and random()<p_inhib:
                Net.add_edge(n,m,weight=w_inhibmax*(1 - random()**2))
                Net[n][m]['delay']=randint(1,d_inhibmax)

for n in Net.nodes():
    for m in Net.predecessors(n):
        Net.node[n]['model'].adjustMaxD(Net[m][n]['delay'])
    Net.node[n]['model'].delaygen()

for t in range(T):
    if t>50:
        for n in range(n_clamp):
            Net.node[n]['model'].clamp_input(I_clamp)
    #print(Net.node[0]['model'].I)
    #print(Net.node[0]['model'].give_V())
    Net.NetTimestep()

Net.print_Firings()
#plt.figure()
#nx.draw_spectral(Net)
    