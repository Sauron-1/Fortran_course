import sys
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

xs = np.array([1.05, 1.1, 1.15, 1.2])
ys = np.array([2.12, 2.2, 2.17, 2.32])

#call function
f = interp1d(xs, ys, kind=xs.size-1)

x = np.linspace(1.05, 1.2, 100)
y = f(x)
plt.plot(x, y, lw=1)
plt.minorticks_on()
plt.tick_params(which='both',
                direction='in',
                top=True,
                right=True)
plt.xlim(x.min(), x.max())
plt.xlabel(r'x')
plt.ylabel(r'$f(x)$')
if len(sys.argv) == 1:
    plt.show()
else:
    plt.savefig(sys.argv[1], format='eps')
