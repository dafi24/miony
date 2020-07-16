# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:47:58 2019

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt
from novevyhodnoceni import caspulsu
from novevyhodnoceni import vyhodnoceni
import os.path as op


# 1 SAMPLE = (12/245) us
    

def rozpadGraf(nazev):
    cas,napeti=np.loadtxt(nazev,delimiter=",")
    """    
    trigger=50
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
    
    """    
    
    
    cas1,cas2,index1,index2a = vyhodnoceni(cas,napeti)
    
    
    
    ROZDIL=float((cas2-cas1)/1e3)
    print("Časová vzdálenost pulsů: {:.2f} us".format(ROZDIL))
    print("čas puls 1",cas1)
    print("čas puls 2",cas2)
#    print("Amplituda: {:.2f} mV".format(np.amax(napeti[index1:index1a])))
#    casamp=np.where(napeti==np.amax(napeti))[0][0]
#    print("Čas dosažení amplitudy: {:.2f} ms".format(cas[casamp]/1e6))

    napeti = -napeti
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

rozpadGraf("rozpad 30.txt")