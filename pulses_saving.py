# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:47:34 2021

@author: David
"""
from novevyhodnoceni import vyhodnoceni_umelepulsy, caspulsu
from nabiraniB import naberDataB
import numpy as np
#import matplotlib.pyplot as plt

casy = []

num = int(input("Počet časů: "))
nazev = input("Název souboru: ")

count = 0
while len(casy) < num:
    cas, napeti = naberDataB()
    #cas, napeti = np.loadtxt("2.txt", delimiter=";")
    
    napeti= -napeti
    
    pulses, pulses_index = vyhodnoceni_umelepulsy(cas, napeti)
    casy_ = [caspulsu(cas, napeti, i, 0.3) for i in pulses_index]
    for i in range(len(casy_) - 1):
        casy_rozdil = casy_[i+1] - casy_[i]
        #print(casy_rozdil)
        casy.append(casy_rozdil)
    print(count)
    count += 1
    if count % 50 == 0:
        np.savetxt(nazev + ".txt", casy, delimiter=";")

np.savetxt(nazev + ".txt", casy, delimiter=";")

#plt.hist(casy, bins=200)
#plt.show()