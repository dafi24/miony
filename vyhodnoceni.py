# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:34:27 2019

@author: David
"""
import numpy as np

def caspulsu(cas,napeti,indexZ,indexK,proc):
    puls = napeti[indexZ:indexK]
    if(len(puls)==0):
#        print("BACHA: chybi puls")
        return -9999e6
    nap=proc*np.amax(puls)
    ind=0
    for x in napeti[indexZ:indexK]:
        if(x>nap):
            break
        ind+=1
    U1=napeti[indexZ+ind-1]
    U2=napeti[indexZ+ind]
    t1=cas[indexZ+ind-1]
    t2=cas[indexZ+ind]
    a=(U1-U2)/(t1-t2)
    b=U1-(a*t1)
    t=(nap-b)/a
    return t

def vyhodnoceni(cas, napeti):
    #indexy
    
    trigger=100
    
    index1=0
    for x in napeti:
        # index1 = ZAČÁTEK PRVNÍHO PULZU
        if(x>trigger):
    #        index=np.where(x==napeti)
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
        index2+=1
        # index2 = ZAČÁTEK DRUHÉHO PULZU
        if(x>trigger):
            break
    
    index2a=index2
    for x in napeti[index2:]:
        index2a+=1
        # index2a = KONEC DRUHÉHO PULZU
        if(x<trigger):
            break
    
#    print("Čas. vzdálenost pulsů: {:.2f} ms".format((caspulsu(index2,index2a,0.3)-caspulsu(index1,index1a,0.3))/1e6))
    #print("čas 1 puls",caspulsu(index2,index2a,0.3))
    #print("čas 2 puls",caspulsu(index1,index1a,0.3))
#    print("Amplituda: {:.2f} mV".format(np.amax(napeti[index1:index1a])))
#    casamp=np.where(napeti==np.amax(napeti))[0][0]
#    print("Čas dosažení amplitudy: {:.2f} ms".format(cas[casamp]/1e6))
    
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

    casPulsu1 = caspulsu(cas,napeti,index1,index1a,0.3)/1e6
    casPulsu2 = caspulsu(cas,napeti,index2,index2a,0.3)/1e6
    return casPulsu1,casPulsu2,index1,index2a

#    print("Začátek pulsu 1: {:.2f} ms".format(casPulsu1))
#    print("Začátek pulsu 2: {:.2f} ms".format(casPulsu2))
    
    #OBSAH PULSŮ
"""    
    S1=0
    S2=0
    for x in range(index1,index1a):
        S1+=napeti[x]*(cas[x]-cas[x-1])
    for x in range(index2,index2a):
        S2+=napeti[x]*(cas[x]-cas[x-1])
#    print("Obsah pulsů: {:.2f} uVs, {:.2f} uVs".format(S1*1e-6,S2*1e-6))
"""    
"""
if(__name__=="__main__"):
    puls=np.loadtxt("puls SiPM - kopie.csv",delimiter=";")
    cas=puls[:,0]
    napeti=puls[:,1]
    
    plt.plot(cas,napeti)
    plt.show()
    vyhodnoceni(cas,napeti)
"""