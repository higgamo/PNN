# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:27:58 2016

@author: Gary
"""

import networkx as nx
import random

class NetworkGenerator():
    def __init__(self):
        pass
    
    
    def DirectedSmallWorld(self,Net,w_clockMax = 300, dist = random.random N = 1000,k=10,p=0.01):
        Net.add_nodes_from(range(N))
        kclock = int(k/2)
        kcount = k - kclock
        for n in Net.nodes():
            for m in range(kclock):
                N.add_edge(n,(m+1+n)%N,weight=w_clockMax * dist())
        pass