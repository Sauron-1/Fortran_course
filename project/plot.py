import numpy as np
from scipy.io import FortranFile
import matplotlib.pyplot as plt

#The given frequency.
fs = [0.019, 0.051, 0.082, 0.113, 0.144, 0.175]

#Open file and read data.
f = FortranFile('test.dat')

thetas = f.read_reals(dtype=np.float64)
s = f.read_reals(dtype=np.float64)

ys = []
for _ in fs:
    ys.append(f.read_reals(dtype=np.float64))

#Plot xi-theta
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True,
                        subplot_kw=dict(xlim=[thetas[0], thetas[-1]]))
axs = axs.reshape(6)

for i in range(len(ys)):
    axs[i].plot(thetas, ys[i])
    axs[i].text(0.05, 0.9, '$f=%.3f$'%fs[i], transform=axs[i].transAxes)
    axs[i].set_xticks([np.pi/4, np.pi/2, 3*np.pi/4])
    axs[i].set_xticklabels([r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$'])
    axs[i].set_yticks([0])
    axs[i].set_yticklabels(['0'])
    axs[i].tick_params(direction='in', right=True)
    axs[i].plot(thetas, np.zeros(thetas.shape), color='black', 
                linestyle='--', lw=0.5)

for i in [0, 3]:
    axs[i].set_ylabel(r'$\xi$')
for i in [3, 4, 5]:
    axs[i].set_xlabel(r'$\theta$')

fig.tight_layout(pad=0.1)

plt.savefig('xi-theta.eps', format='eps')

#Plot xi-s
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True,
                        subplot_kw=dict(xlim=[s[0], s[-1]]))
axs = axs.reshape(6)

for i in range(len(ys)):
    axs[i].plot(s, ys[i])
    axs[i].text(0.05, 0.9, '$f=%.3f$'%fs[i], transform=axs[i].transAxes)
    axs[i].set_xticks([0.7*s.min(), 0, 0.7*s.max()])
    axs[i].set_yticks([0])
    axs[i].set_yticklabels(['0'])
    axs[i].tick_params(direction='in', right=True)
    axs[i].plot(s, np.zeros(s.shape), color='black', 
                linestyle='--', lw=0.5)

for i in [0, 3]:
    axs[i].set_ylabel(r'$\xi$')
for i in [3, 4, 5]:
    axs[i].set_xlabel(r'$s$')

fig.tight_layout(pad=0.1)

plt.savefig('xi-s.eps', format='eps')
