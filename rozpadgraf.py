# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:47:58 2019

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt
from vyhodnoceni import caspulsu
from vyhodnoceni import vyhodnoceni
import os.path as op

def rozpadGraf(nazev):
    cas,napeti=np.loadtxt(nazev,delimiter=",")
    
    trigger=100
    napeti=-napeti
#    cas1,cas2,x,xx=vyhodnoceni(cas,napeti)
#    print(cas1,cas2)    
    index1=0
    for x in napeti:
        # index1 = ZAČÁTEK PRVNÍHO PULZU
        if(x>trigger):
            break
        index1+=1
        
    index1a=index1
    for x in napeti[index1:]:
        index1a+=1
        # index1a = KONEC PRVNÍHO PULZU
        if(x<trigger):
            break
        
    index2=index1a
    for x in napeti[index1a:]:
        # index2 = ZAČÁTEK DRUHÉHO PULZU
        if(x>trigger):
            break
        index2+=1
        
    index2a=index2
    for x in napeti[index2:]:
        index2a+=1
        # index2a = KONEC DRUHÉHO PULZU
        if(x<trigger):
            break
    
    cas1 = caspulsu(cas,napeti,index1,index1a,0.3)
    cas2 = caspulsu(cas,napeti,index2,index2a,0.3)

    ROZDIL=(cas2-cas1)/1e3
    print("Čas. vzdálenost pulsů: {:.2f} us".format(ROZDIL))
    print("čas puls 1",cas1)
    print("čas puls 2",cas2)
    print("Amplituda: {:.2f} mV".format(np.amax(napeti[index1:index1a])))
    casamp=np.where(napeti==np.amax(napeti))[0][0]
    print("Čas dosažení amplitudy: {:.2f} ms".format(cas[casamp]/1e6))

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

        #NALEZENÍ ČASU PULSU
        
    """
    #hodnota=int(input("Napětí U:"))
    trigger=0.3
    hodnota=trigger*np.amax(napeti[index1:index1a])
    index=index1-10
    for x in napeti[index+1:index1a]:
        if(x>hodnota):
            break
        index+=1
        #index = HODNOTA PŘED PŘEKROČENÍM HODNOTY NAPĚTÍ
            
    U1=napeti[index]
    U2=napeti[index+1]
    t1=cas[index-1]
    t2=cas[index]
    a=(U1-U2)/(t1-t2)
    b=U1-(a*t1)
    t=(hodnota-b)/a
    """
    """
    #casPulsu1 = caspulsu(cas,napeti,index1,index1a,0.3)/1e6
    #casPulsu2 = caspulsu(cas,napeti,index2,index2a,0.3)/1e6
    #    print("Začátek pulsu 1: {:.2f} ms".format(casPulsu1))
    #    print("Začátek pulsu 2: {:.2f} ms".format(casPulsu2))
        
        #OBSAH PULSŮ
        
    S1=0
    S2=0
    for x in range(index1,index1a):
        S1+=napeti[x]*(cas[x]-cas[x-1])
    for x in range(index2,index2a):
        S2+=napeti[x]*(cas[x]-cas[x-1])
    #    print("Obsah pulsů: {:.2f} uVs, {:.2f} uVs".format(S1*1e-6,S2*1e-6))
    """
rozpadGraf("rozpad 1.txt")