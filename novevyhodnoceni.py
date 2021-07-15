# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:59:43 2020

@author: David
"""

import numpy as np

def caspulsu(cas, napeti, puls_index, proc):
    puls = [np.absolute(napeti[i]) for i in puls_index]
    amplitudaindex = puls_index[0] + np.where(puls == np.amax(puls))[0][0]
    nap = napeti[amplitudaindex] * proc
    
    for i in range(np.size(puls)):
        if puls[i] > nap:
            index_napeti = puls_index[0] + i
            
            U1 = np.absolute(napeti[index_napeti-1])
            U2 = np.absolute(napeti[index_napeti])
            if U1 > U2:
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
    adding, pulse_expect, reset, presvih = False, False, False, False
    presvih_possible = (np.amax(np.absolute(napeti)) > 400)
    for i in range(np.size(napeti)):
        if not reset:
            if np.size(pulses) == 1:
                reset = (np.absolute(napeti[i]) < trigger)
                
        pulse_expect_test = False
        if pulse_expect and reset:
            pulse_expect_test = (np.absolute(napeti[i]) > trigger)
        
        if napeti[i] > trigger or pulse_expect_test:
            if(presvih_possible):
                presvih = (np.size(pulses) == 1 and cas[i] - cas[pulses_index[0][0]] < 350)
            if not presvih:
                adding = True
                puls.append(napeti[i])
                puls_index.append(i)
        else:
            if adding:
                adding = False
                pulse_expect = True
                pulses.append(puls)
                pulses_index.append(puls_index)
                puls_index, puls = [], []
    return pulses, pulses_index

def vyhodnoceni_umelepulsy(cas, napeti):
    pulses, pulses_index = [], []
    saving = False
    for i in range(len(napeti)):
        if napeti[i] > 200:
            if not saving:
                pulses.append([])
                pulses_index.append([])
                print('trigger')
            saving = True
            pulses[-1].append(napeti[i])
            pulses_index[-1].append(i)
            print('i')
        else:
            if saving:
                saving = False
                print('konec pulsu')
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