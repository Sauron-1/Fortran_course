#!/usr/bin/python3
import numpy as np
from scipy.io import FortranFile
import matplotlib.pyplot as plt
import sys

#Get data file name from shell
f = FortranFile(sys.argv[1], 'r')
x = np.linspace(-2, 2, 101)

lines = []
labels = []

#Read file and draw
while True:
    try:
        data = f.read_reals(dtype=np.float32)
    except (TypeError):
        break
    labels.append('t = ' + str(data[0]))
    l, = plt.plot(x, data[1:])
    lines.append(l)

#Set picture style
plt.xlabel('x')
plt.ylabel('u')
plt.xlim(x.min(), x.max())
plt.ylim(0, 1)
plt.minorticks_on()
plt.tick_params(which='both', top=True, right=True)
plt.tick_params(which='both', direction='in')
plt.legend(handles=lines, labels=labels)
#Save picture as eps file
plt.savefig(sys.argv[1][:-4]+'.eps', format='eps')
