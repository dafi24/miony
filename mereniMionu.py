# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:44:41 2019

@author: David
"""
import numpy as np
from nabiraniA import naberDataA
from vyhodnoceni import vyhodnoceni
import matplotlib.pyplot as plt

#rozdily=[]
cislo=1
while(True):
    cas,napeti = naberDataA()
    napeti = -napeti
    cas1,cas2,index1,index2a = vyhodnoceni(cas,napeti)
    if(cas2<0):                 
        print("Čas 1:",cas1)        
        plt.figure(1)
        plt.plot(cas[index1-30:index2a+30],napeti[index1-30:index2a+30])
        plt.show()     
    else:
        print("Čas 1:",cas1)
        print("Čas 2:",cas2)
        print("Rozdíl:",cas2-cas1)
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
        plt.plot(cas[index1-30:index1+30],napeti[index1-30:index1+30])
        plt.show()