# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:44:46 2020

@author: David
"""
import novevyhodnoceni as vhd
import numpy as np
import time
#import matplotlib.pyplot as plt
import os
from nabiraniA import naberDataA

# 1 SAMPLE = (12/245) us              

os.chdir(r"~/python/miony-mereni")
iter_count = 0
casy_mereni = list(np.loadtxt("casyMereni.txt"))
casy_mereni.append(0)
t1 = time.time()
cislo = 1

while(True):
    iter_count += 1
    if(iter_count % 30 == 0):
        casy_mereni[-1] = time.time() - t1
        np.savetxt("casyMereni.txt", casy_mereni)
    
    cas,napeti=naberDataA()
    napeti = -napeti
    
    index1, index1a, index2, index2a = vhd.vyhodnoceni(cas,napeti)
            
    proc=0.3
    
    cas1 = vhd.caspulsu(cas,napeti,index1,index1a,proc)    
    cas2 = vhd.caspulsu(cas,napeti,index2,index2a,proc)
    
    ROZDIL=(cas2-cas1)/1e3
    print("Časová vzdálenost pulsů: {:.2f} us".format(ROZDIL))
    print("čas pulsu 1: {:.2f} ns".format(cas1))
    print("čas pulsu 2: {:.2f} ns".format(cas2))
        
    if(cas1<0):
        print("Nabiraní vrátilo data bez žádného pulsu")
    elif(cas2<0):                 
        print("Čas 1 [ms]:",cas1)        
#        plt.figure(1)
#        plt.plot(cas[index1-30:index1+30],napeti[index1-30:index1+30])
#        plt.show()
    else:
        print("Čas 1 [ms]:",cas1)
        print("Čas 2 [ms]:",cas2)
        print("Rozdíl [ms]:",cas2-cas1)
        np.savetxt("rozpad {}.txt".format(cislo),(cas,napeti),delimiter=",")
        cislo+=1
#        plt.figure(2)
#        plt.plot(cas[index1-30:index2a+30],napeti[index1-30:index2a+30])
#        plt.show()