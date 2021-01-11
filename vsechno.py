# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:44:46 2020

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt
import os.path as op
from nabiraniA import naberDataA

# 1 SAMPLE = (12/245) us              

#nazev = "Rozpad 27.txt"
cislo = 1    
while(True):
    
    cas,napeti=naberDataA()
#    plt.plot(cas,napeti)
#    plt.show()
    napeti = -napeti
            
    trigger = 50
    reset = 20
    sampleTime = 12*1e3/245
        
    index1=0
    for x in napeti:
        if(abs(x)>trigger):
            break
        index1+=1
    index1 -= 1
#    plt.plot([cas[index1],cas[index1]],[-500,200], "g")    
    index1a=index1+1
    for x in napeti[index1+1:]:
        index1a+=1
        if(x<reset):
            break
#    plt.plot([cas[index1a],cas[index1a]],[-500,200], "r") 

#    plt.show()
    
    # index1:index1a = kladná (resp. záporná) část prvního pulsu
    # index1 - jeden prvek před překročení triggeru
    # index1a - reset (první prvek menší než 20)
       #  and (abs(x)-abs(napeti[index2]))/sampleTime>1 
    index2=index1a
    for x in napeti[index1a:]:
        if(abs(x)>trigger and (abs(x)-abs(napeti[index2-1]))/sampleTime>1):
            break
        index2+=1
    index2-=1
        
    index2a=index2
    for x in napeti[index2:]:
        index2a+=1
        if(x<reset):
            break
    #index2a -= 1
    # index2a bude vždy minimálně o 1 větší, než index2, což může být problém, pokud index2 je poslední sample z napětí (až se tohle vyřeší, teprve potom bude fungovat casPulsu)    
    #casPulsu1 = caspulsu(cas,napeti,index1,index1a,0.3)/1e6
    #casPulsu2 = caspulsu(cas,napeti,index2,index2a,0.3)/1e6
    
    proc=0.3
    
    puls1 = napeti[index1:index1a]
    if(len(puls1)==0 or index1 >= 2449):
        cas1 = -9999e6
    else:
        amplituda1index = np.where(puls1==np.amax(puls1))[0][0] + index1
        nap1 = proc*napeti[amplituda1index]
        ind1 = 0
        for x in napeti[index1:index1a]:
            ind1 += 1
            if(x>nap1):
                break
    #    if(amplituda1index == index1+1):
    #        U11 = napeti[index1+ind1-1]
    #        U21 = napeti[index1+ind1]
    #        t11 = cas[index1+ind1-1]
    #        t21 = cas[index1+ind1]
    #    else:
        U11 = napeti[amplituda1index-1]
        U21 = napeti[amplituda1index]
        t11 = cas[amplituda1index-1]
        t21 = cas[amplituda1index]
        a1 = (U11-U21)/(t11-t21)
        b1 = U11-(a1*t11)
        cas1 = (nap1-b1)/a1
    
    
    puls2 = napeti[index2:index2a+1]
    if(len(puls2)==0 or index2 >= 2449):
        cas2 = -9999e6
    else:
        amplituda2index = np.where(puls2==np.amax(puls2))[0][0] + index2
        nap2 = proc*napeti[amplituda2index]
        ind2 = 0
        for x in napeti[index2:index2a]:
            ind2 += 1
            if(x>nap2):
                break
        U12 = napeti[amplituda2index-1]
        U22 = napeti[amplituda2index]
        t12 = cas[amplituda2index-1]
        t22 = cas[amplituda2index]
        a2 = (U12-U22)/(t12-t22)
        b2 = U12-(a2*t12)
        cas2 = (nap2-b2)/a2
    
    ROZDIL=(cas2-cas1)/1e3
    print("Časová vzdálenost pulsů: {:.2f} us".format(ROZDIL))
    print("čas pulsu 1: {:.2f} ns".format(cas1))
    print("čas pulsu 2: {:.2f} ns".format(cas2))
    #    print("Amplituda: {:.2f} mV".format(np.amax(napeti[index1:index1a])))
    #    casamp=np.where(napeti==np.amax(napeti))[0][0]
    #    print("Čas dosažení amplitudy: {:.2f} ms".format(cas[casamp]/1e6))
    """
    plt.figure(nazev+" zoom")
    plt.plot(cas[index1-30:index2a+30],napeti[index1-30:index2a+30],"b.")
    plt.plot([cas1,cas1],[0,np.amax(napeti)],"g-")
    plt.plot([cas1,cas1],[0,np.amin(napeti)],"g-")
    plt.plot([cas2,cas2],[0,np.amax(napeti)],"r-")
    plt.plot([cas2,cas2],[0,np.amin(napeti)],"r-")
    plt.xlabel("Čas [ns]")
    plt.ylabel("Napětí [mV]")
    plt.title(str(ROZDIL)+" us")
    plt.savefig(op.basename(nazev).split(".")[0]+" zoom.png")
    plt.close  
        
    plt.figure(nazev)
    plt.plot(cas,napeti)
    plt.xlabel("Čas [ns]")
    plt.ylabel("Napětí [mV]")
    plt.savefig(op.basename(nazev).split(".")[0]+".png")
    plt.close
    """
    if(cas1<0):
        print("Nabiraní vrátilo data bez žádného pulsu")
    elif(cas2<0):                 
        print("Čas 1:",cas1)        
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
