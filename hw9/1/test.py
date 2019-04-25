import matplotlib.pyplot as plt
import numpy as np

from util import Shape, arc, line

def cos_p(theta, c, r):
    return r*np.cos(theta) + c

def sin_p(theta, c, r):
    return r*np.sin(theta) + c

ax = plt.gca()
ax.set_aspect(1)

#comma
comma = Shape()
comma.add_array(arc([0, -1], [1, 0], 1, major=True))
comma.add_array(arc([1, 0], [-1, -2], 2))
comma.add_array(arc([-1, -2], [0, -1], 1.5, out=False))
comma.loop(update=True)
#comma.fill(plt.gca(), facecolor='black')

#circle
thetas = np.linspace(0, 2*np.pi, 200)
circle = Shape()
circle.add_line(np.cos, np.sin, thetas)
circle.loop()
#circle.fill(plt.gca(), facecolor='red')

circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.move(0, -5.5).fill(ax, facecolor='black')
plt.show()
