import matplotlib.pyplot as plt
import numpy as np

from util import Shape

def cos_p(theta, c, r):
    return r*np.cos(theta) + c

def sin_p(theta, c, r):
    return r*np.sin(theta) + c

thetas = np.linspace(3*np.pi/2., 0, 100)
s = Shape()
s.add_line(np.cos, np.sin, thetas, update=True)
s.add_line(cos_p, sin_p, np.linspace(0, -np.pi/2, 50),
          {'c':-1, 'r':2}, {'c':0, 'r':2}, update=True)
s.loop(update=True)
s.fill(plt.gca(), facecolor='black')
plt.show()
