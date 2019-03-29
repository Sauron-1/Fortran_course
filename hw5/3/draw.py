import numpy as np
from scipy.io import FortranFile
import matplotlib.pyplot as plt

f = FortranFile('data.dat', 'r')
x = np.linspace(-2, 2, 101)

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
plt.savefig('data.eps', format='eps')
