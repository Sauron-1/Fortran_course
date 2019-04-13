import matplotlib.pyplot as plt
import numpy as np

#Random xs and ys
xs = np.random.normal(size=20)
ys = np.random.normal(size=20)

#Verts of a polygon
ts = np.linspace(0, 2*np.pi, 20, endpoint=True)
vxs = np.cos(ts)[:, np.newaxis]
vys = np.sin(ts)[:, np.newaxis]
verts = np.concatenate((vxs, vys), axis=1)

plt.plot(xs, ys, linestyle='none', marker=verts, markerfacecolor='none')
#Or:
#plt.plot(xs, ys, linestyle='none', marker='o', markerfacecolor='none')

plt.minorticks_on()
plt.tick_params(which='both',
                top=True,
                right=True)
plt.savefig('circle-marker.eps', format='eps')
