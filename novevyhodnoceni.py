# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:59:43 2020

@author: David
"""

import numpy as np

def caspulsu(cas, napeti, puls_index, proc):
    puls = [abs(napeti[i]) for i in puls_index]
    amplitudaindex = puls_index[0] + np.where(puls == max(puls))[0][0]
    nap = napeti[amplitudaindex] * proc
    
    for i in range(len(puls)):
        if(puls[i] > nap):
            index_napeti = puls_index[0] + i
            
            U1 = abs(napeti[index_napeti-1])
            U2 = abs(napeti[index_napeti])
            if(U1 > U2):
                return -999e6
            t1 = cas[index_napeti-1]
            t2 = cas[index_napeti]
            a = (U1 - U2) / (t1 - t2)
            b = U1 - (a * t1)
            cas = (nap - b) / a
            return cas
        
    return -999e6

def vyhodnoceni(cas, napeti):
    pulses, pulses_index, trigger = [], [], 50
        
    puls_index, puls = [], []
    adding, pulse_expect, reset = False, False, False
    for i in range(len(napeti)):
        if(not reset):
            if(len(pulses) == 1):
                reset = (abs(napeti[i]) < trigger)
                
        pulse_expect_test = False
        if(pulse_expect and reset):
            pulse_expect_test = (abs(napeti[i]) > trigger)
        
        if(napeti[i] > trigger or pulse_expect_test):
            presvih = (len(pulses) == 1 and max(abs(napeti)) > 400 and cas[i] - cas[pulses_index[0][0]] < 350)
            if(not presvih):
                adding = True
                puls.append(napeti[i])
                puls_index.append(i)
        else:
            if(adding):
                adding = False
                pulse_expect = True
                pulses.append(puls)
                pulses_index.append(puls_index)
                puls_index, puls = [], []
    return pulses, pulses_index
"""
if(__name__=="__main__"):
    puls=np.loadtxt("puls SiPM - kopie.csv",delimiter=";")
    cas=puls[:,0]
    napeti=puls[:,1]
    
    plt.plot(cas,napeti)
    plt.show()
    vyhodnoceni(cas,napeti)
"""