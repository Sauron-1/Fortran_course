import matplotlib.pyplot as plt
import numpy as np
from scipy.io import FortranFile
from rebin import rebin

f = FortranFile('COEFF_DAY.DAT', 'r')
nx = f.read_ints()[0]
ny = f.read_ints()[0]
xy = f.read_reals(dtype=np.float32)
x = xy[:xy.size//2]
y = xy[xy.size//2:]
bdxx = f.read_reals(dtype=np.float32).reshape((nx, ny))
bdyy = f.read_reals(dtype=np.float32).reshape((nx, ny))
bdxy = f.read_reals(dtype=np.float32).reshape((nx, ny))
X, Y = np.meshgrid(x, y)
f.close()

bdyy = bdyy / Y**2
bdxy = bdxy / Y

alpha = X/np.pi*180
Ek = 0.511*(np.sqrt(Y*Y+1)-1)

plt.pcolormesh(alpha, Ek, bdxx, cmap='jet')
#plt.contour(alpha, Ek, bdxx, cmap='jet')
plt.xlabel(r'$\alpha(Deg)$')
plt.ylabel(r'$E_k$')
plt.yscale('log')
plt.minorticks_on()
plt.tick_params(which='both',
                top=True,
                right=True)
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$D_{xx}$')
plt.show()
