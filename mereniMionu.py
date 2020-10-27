# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:44:41 2019

@author: David
"""
import numpy as np
from nabiraniA import naberDataA
from vyhodnoceni import vyhodnoceni
from vyhodnoceni import caspulsu
import matplotlib.pyplot as plt

#rozdily=[]
cislo=1
while(True):
    cas,napeti = naberDataA()
    napeti = -napeti
    index1,index1a,index2,index2a = vyhodnoceni(cas,napeti)
    cas1 = caspulsu(cas, napeti, index1, index1a, 0.3)
    cas2 = caspulsu(cas, napeti, index2, index2a, 0.3)
    if(cas1<0):
        print("Nabiraní vrátilo data bez žádného pulsu")
    elif(cas2<0):                 
        print("Čas 1:",cas1)        
        plt.figure(1)
        plt.plot(cas[index1-30:index1+30],napeti[index1-30:index1+30])
        plt.show()
    else:
        print("Čas 1 [ms]:",cas1)
        print("Čas 2 [ms]:",cas2)
        print("Rozdíl [ms]:",cas2-cas1)
        np.savetxt("rozpad {}.txt".format(cislo),(cas,napeti),delimiter=",")
        cislo+=1
#        rozdily.append(cas2-cas1)
#        rozdilyAll.append(cas2-cas1)
#        np.savetxt("rozdily.txt",rozdily,delimiter=",")
#        np.savetxt("rozdily all.txt",rozdilyAll,delimiter=",")
#        plt.figure(1)
#        hodnoty,hranice,_=plt.hist(rozdily,bins=11,range=[min(rozdily),max(rozdily)])
#        plt.plot(plt.hist(rozdilyAll,bins=11,range=[min(rozdilyAll),max(rozdilyAll)]))
        plt.figure(2)
        plt.plot(cas[index1-30:index2a+30],napeti[index1-30:index2a+30])
        plt.show()     
