import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import FortranFile

#Read file, according to codes given in the slides
f = FortranFile('COEFF_DAY.DAT', 'r')
nx = f.read_ints()[0]
ny = f.read_ints()[0]
xy = f.read_reals(dtype=np.float32)
x = xy[:nx]
y = xy[nx:]
bdxx = f.read_reals(dtype=np.float32).reshape((nx, ny))
bdyy = f.read_reals(dtype=np.float32).reshape((nx, ny))
bdxy = f.read_reals(dtype=np.float32).reshape((nx, ny))
X, Y = np.meshgrid(x, y)
f.close()

bdyy = bdyy / Y**2
bdxy = bdxy / Y

alpha = X/np.pi*180
Ek = 0.511*(np.sqrt(Y*Y+1)-1)

#Just plot.
norm = colors.LogNorm(vmin=1e-8, vmax=1e-2)
plt.pcolormesh(alpha, Ek, bdxx, cmap='jet', norm=norm)
plt.xlabel(r'$\alpha(Deg)$')
plt.ylabel(r'$E_k$')
plt.yscale('log')
plt.minorticks_on()
plt.tick_params(which='both',
                top=True,
                right=True)
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$D_{xx}$')
cbar.ax.set_yscale('log')
plt.savefig('color.eps', format='eps')
