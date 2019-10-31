# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:16:17 2019

@author: David
"""
import numpy as np
from nabirani import naberData
from vyhodnoceni import vyhodnoceni
import matplotlib.pyplot as plt

rozdily=[]
cislo=1
while(True):
    cas,napeti=naberData()
    cas1,cas2 = vyhodnoceni(cas,napeti)
    if(cas2<0):                 
        print("Čas 1:",cas1)
    else:
        print("Čas 1:",cas1)
        print("Čas 2:",cas2)
        print("Rozdíl:",cas2-cas1)
        np.savetxt("rozpad {}.txt".format(cislo),(cas,napeti),delimiter=",")
        cislo+=1
        rozdily.append(cas2-cas1)
        np.savetxt("rozdily.txt",rozdily,delimiter=",")
        plt.figure(1)
        hodnoty,hranice,_=plt.hist(rozdily,bins=11,range=[min(rozdily),max(rozdily)])