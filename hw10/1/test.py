import matplotlib.pyplot as plt
import numpy as np

#data
omegas = np.linspace(0, 1, 200)
thetas = np.linspace(0, 90, 5)

#fuction
def k(omega, theta):
    theta = theta / 180 * np.pi
    return omega * np.sqrt(1-5/(omega*(omega-np.cos(theta))))

lines = []
labels = []

#plot
for theta in thetas:
    line, = plt.plot(k(omegas, theta), omegas)
    lines.append(line)
    labels.append(r'$\theta=%.1f$'%(theta))

plt.ylabel(r'$\omega$')
plt.xlabel(r'$k$')
plt.ylim(0, 1)
plt.xlim(0, 30)
plt.minorticks_on()
plt.tick_params(which='both', top=True, right=True)
plt.legend(handles=lines, labels=labels)
plt.savefig('test.eps', format='eps')
