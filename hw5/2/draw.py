import numpy as np
from scipy.io import FortranFile
import matplotlib.pyplot as plt
import sys

f = FortranFile(sys.argv[1], 'r')
x = np.linspace(-2, 14, 101)

lines = []
labels = []

while True:
    try:
        data = f.read_reals(dtype=np.float32)
    except (TypeError):
        break
    labels.append('t = ' + str(data[0]))
    l, = plt.plot(x, data[1:])
    lines.append(l)

plt.xlabel('x')
plt.ylabel('u')
plt.legend(handles=lines, labels=labels)
plt.savefig(sys.argv[1][:-4]+'.eps', format='eps')
