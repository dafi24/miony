# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:49:43 2021

@author: David
"""

from novevyhodnoceni import vyhodnoceni_umelepulsy, caspulsu
from nabiraniB import naberDataB
import numpy as np
import matplotlib.pyplot as plt

cas, napeti = naberDataB()
plt.plot(cas, napeti)
plt.show()
pulses, pulses_index = vyhodnoceni_umelepulsy(cas, napeti)
print([caspulsu(cas, napeti, i, 0.3) for i in pulses_index])

plt.figure(1)
print(cas[200:320])
print(napeti[200:320])
plt.savefig("plot.png")
plt.show()
np.savetxt('testdata.txt', (cas[200:320], napeti[200:320]), delimiter=';')