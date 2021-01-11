# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:34:27 2019

@author: David
"""
import numpy as np

def caspulsu(cas,napeti,index,indexa,proc):
    puls = napeti[index:indexa]
    if(len(puls)==0 or index >= 2449):
        cas = -9999e6
    else:
        amplitudaindex = np.where(puls==np.amax(puls))[0][0] + index
        nap = proc*napeti[amplitudaindex]
        ind = 0
        for x in puls:
            ind += 1
            if(x>nap):
                break
    #    if(amplituda1index == index1+1):
    #        U11 = napeti[index1+ind1-1]
    #        U21 = napeti[index1+ind1]
    #        t11 = cas[index1+ind1-1]
    #        t21 = cas[index1+ind1]
    #    else:
        U1 = napeti[amplitudaindex-1]
        U2 = napeti[amplitudaindex]
        t1 = cas[amplitudaindex-1]
        t2 = cas[amplitudaindex]
        a = (U1-U2)/(t1-t2)
        b = U1-(a*t1)
        cas = (nap-b)/a
    return cas
def vyhodnoceni(cas, napeti):
    trigger = 50
    reset = 20
    sampleTime = 12*1e3/245
        
    index1=0
    for x in napeti:
        if(abs(x)>trigger):
            break
        index1+=1
    index1 -= 1
        
    index1a=index1+1
    for x in napeti[index1+1:]:
        index1a+=1
        if(x<reset):
            break
    
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
    return index1, index1a, index2, index2a
    #index2a -= 1
    # index2a bude vždy minimálně o 1 větší, než index2, což může být problém, pokud index2 je poslední sample z napětí (až se tohle vyřeší, teprve potom bude fungovat casPulsu)    
    #casPulsu1 = caspulsu(cas,napeti,index1,index1a,0.3)/1e6
    #casPulsu2 = caspulsu(cas,napeti,index2,index2a,0.3)/1e6
"""
if(__name__=="__main__"):
    puls=np.loadtxt("puls SiPM - kopie.csv",delimiter=";")
    cas=puls[:,0]
    napeti=puls[:,1]
    
    plt.plot(cas,napeti)
    plt.show()
    vyhodnoceni(cas,napeti)
"""