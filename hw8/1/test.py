import matplotlib.colors as colors
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
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

bdyy = np.abs(bdyy)
bdxy = np.abs(bdxy)

alpha = X/np.pi*180
Ek = 0.511*(np.sqrt(Y*Y+1)-1)

#Just plot.
norm = colors.LogNorm(vmin=1e-8, vmax=1e-2)
fig, axs = plt.subplots(3, 1, sharex=True, sharey=True)
fig.set_size_inches(8, 18, forward=True)
pxx = axs[0].pcolormesh(alpha, Ek, bdxx, cmap='jet', norm=norm)
axs[0].text(0.01, 0.95, r'(a) $D_xx$', transform=axs[0].transAxes)
pxy = axs[1].pcolormesh(alpha, Ek, bdxy, cmap='jet', norm=norm)
axs[1].text(0.01, 0.95, r'(a) $D_xy$', transform=axs[1].transAxes)
pyy = axs[2].pcolormesh(alpha, Ek, bdyy, cmap='jet', norm=norm)
axs[2].text(0.01, 0.95, r'(a) $D_yy$', transform=axs[2].transAxes)
fig.tight_layout(rect=(0.01, 0.025, 1, 1), pad=1)
fig.colorbar(pxx, ax=axs, aspect=30, shrink=0.66,
             fraction=0.06, pad=0.02)
axs[2].set_xlabel(r'$\alpha(Deg)$')
for ax in axs:
    ax.set_ylabel(r'$E_k$')
    ax.set_yscale('log')
    ax.minorticks_on()
    ax.tick_params(which='both', right=True, 
                   top=True, direction='in')
plt.show()
