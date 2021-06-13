# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:47:34 2021

@author: David
"""
from novevyhodnoceni import vyhodnoceni, caspulsu
from nabiraniB import naberDataB
import numpy as np
#import matplotlib.pyplot as plt

casy = []

num = int(input("Počet časů: "))

while len(casy) < num:
    cas, napeti = naberDataB()
    #cas, napeti = np.loadtxt("2.txt", delimiter=";")
    
    napeti= -napeti
    
    pulses, pulses_index = vyhodnoceni(cas, napeti)
    casy_ = [caspulsu(cas, napeti, i, 0.3) for i in pulses_index]
    for i in range(len(casy_)-1):
        casy_rozdil = casy_[i+1] - casy_[i]
        if casy_rozdil < 500 and casy_rozdil > 450:
            casy.append(casy_rozdil)

nazev = input("Název souboru: ")
np.savetxt(nazev + ".txt", casy, delimiter=";")

#plt.hist(casy, bins=200)
#plt.show()