# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:49:43 2021

@author: David
"""

from novevyhodnoceni import vyhodnoceni, caspulsu
from nabiraniB import naberDataB
import numpy as np
import matplotlib.pyplot as plt

cas, napeti = naberDataB()
plt.plot(cas, napeti)
pulses, pulses_index = vyhodnoceni(cas, napeti)
print([caspulsu(cas, napeti, i, 0.3) for i in pulses_index])

plt.figure(1)
plt.plot(cas[100:200], napeti[100:200])
plt.savefig("plot.png")