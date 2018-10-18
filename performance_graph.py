#!/usr/bin/python

import Graphs
import os
import sys
import matplotlib.pyplot as plt
import numpy as np


x_inc , y_inc = np.loadtxt ("salida_incremental.txt", delimiter=',', usecols = (0,1), unpack = True)
x_dc , y_dc = np.loadtxt ("salida_dc.txt", delimiter=',', usecols = (0,1), unpack = True)
x_jarvis , y_jarvis = np.loadtxt ("salida_jarvis.txt", delimiter=',', usecols = (0,1), unpack = True)

p1 = plt.plot(x_inc, y_inc)
p2 = plt.plot(x_dc, y_dc)
p3 = plt.plot(x_jarvis, y_jarvis)

plt.ylabel("Tiempo")
plt.xlabel("N")
plt.title("Rendimiento")
plt.legend((p1[0], p2[0], p3[0]), ("Incremental", "DC", "Jarvis"))

plt.show()
