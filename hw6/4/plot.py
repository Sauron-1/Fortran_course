import numpy as np
from scipy.io import FortranFile
import matplotlib.pyplot as plt

f = FortranFile('res.dat', 'r')

x = f.read_reals(dtype=np.float32)
y = f.read_reals(dtype=np.float32)

plt.plot(x, y)
#plot more beautiful
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(x.min(), x.max())
plt.minorticks_on()
plt.tick_params(which='both',
                top=True,
                right=True,
                direction='in')
plt.savefig('res.eps', format='eps')
f.close()
