import matplotlib.pyplot as plt
import numpy as np

xs = np.random.normal(size=20)
ys = np.random.normal(size=20)

#Becacue the default marker is circle, I choose
#a small 'num' value to show the difference.
#If the value is big enough, marker will be circles.
ts = np.linspace(0, 2*np.pi, 7)
vxs = np.cos(ts)[:, np.newaxis]
vys = np.sin(ts)[:, np.newaxis]
verts = np.concatenate((vxs, vys), axis=1)

plt.plot(xs, ys, linestyle='none', marker=verts, markerfacecolor='none')
#Or:
#plt.plot(xs, ys, linestyle='none', marker='o', markerfacecolor='none')
plt.show()
