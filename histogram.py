# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 07:10:05 2019

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("rozdily all.txt")

Data=[]
for x in data:
    if(x<1e10):
        Data.append(x)

bins,fff,ggg=plt.hist(Data,bins=100,range=[min(Data),max(Data)])
plt.xlabel("čas [s]")
plt.yticks(ticks=range(1,int(np.amax(bins))+1,1))