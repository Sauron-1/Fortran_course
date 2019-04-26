import matplotlib.pyplot as plt
import numpy as np

from util import Shape, arc, line

def cos_p(theta, c, r):
    return r*np.cos(theta) + c

def sin_p(theta, c, r):
    return r*np.sin(theta) + c

fig, axs = plt.subplots(3, 4)
axs = axs.reshape(3*4)
for ax in axs:
    ax.tick_params(bottom=False, left=False,
                   labelbottom=False, labelleft=False)
    ax.set_aspect(1)
    ax.set_xmargin(0.05)
    ax.set_ymargin(0.05)

#comma
comma = Shape()
comma.add_array(arc([0, -1], [1, 0], 1, major=True))
comma.add_array(arc([1, 0], [-1, -2], 2))
comma.add_array(arc([-1, -2], [0, -1], 1.5, out=False))
comma.loop(update=True)
comma.rotate(20, update=True)
#comma.fill(plt.gca(), facecolor='black')

#circle
thetas = np.linspace(0, 2*np.pi, 200)
circle = Shape()
circle.add_line(np.cos, np.sin, thetas)
circle.loop()
#circle.fill(plt.gca(), facecolor='red')


#1, 1
ax = axs[0]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(30).fill(ax, facecolor='black')

#1, 2
ax = axs[1]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(30).fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(210).fill(ax, facecolor='black')

#1, 3
ax = axs[2]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(60).fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(180).fill(ax, facecolor='black')
comma.move(0, -5.5).rotate(300).fill(ax, facecolor='black')

#1, 4
ax = axs[3]
circle.scale(10, 10).fill(ax, facecolor='black')
circle.scale(9, 9).fill(ax, facecolor='red')
circle.scale(7, 7).fill(ax, facecolor='black')
circle.scale(6, 6).fill(ax, facecolor='red')
circle.scale(4, 4).fill(ax, facecolor='black')
circle.scale(3, 3).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.scale(0.7, 0.7).move(0, -3.5).rotate(60).fill(ax, facecolor='black')
comma.scale(0.7, 0.7).move(0, -3.5).rotate(180).fill(ax, facecolor='black')
comma.scale(0.7, 0.7).move(0, -3.5).rotate(300).fill(ax, facecolor='black')
comma.scale(1.2, 1.2).move(0, -6.5).rotate(0).fill(ax, facecolor='black')
comma.scale(1.2, 1.2).move(0, -6.5).rotate(120).fill(ax, facecolor='black')
comma.scale(1.2, 1.2).move(0, -6.5).rotate(240).fill(ax, facecolor='black')
comma.move(0, -9.5).rotate(60).fill(ax, facecolor='black')
comma.move(0, -9.5).rotate(180).fill(ax, facecolor='black')
comma.move(0, -9.5).rotate(300).fill(ax, facecolor='black')

#2, 1
ax = axs[4]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(0).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(0).fill(ax, facecolor='white')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(120).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(120).fill(ax, facecolor='white')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(240).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(240).fill(ax, facecolor='white')

#block
theta=15/180*np.pi
block = Shape()
block.add_array(line([-np.sin(theta), 0], [np.sin(theta), 0]))
block.add_array(line([np.sin(theta), 0], [np.sin(theta), -np.cos(theta)]))
block.add_array(arc([np.sin(theta), -np.cos(theta)], [-np.sin(theta), -np.cos(theta)], 1))
block.add_array(line([-np.sin(theta), -np.cos(theta)], [-np.sin(theta), 0]))
block.loop()
#block.fill(ax, facecolor='black')

#moon
moon = Shape()
moon.add_array(arc([0, 0], [0, 1], 0.53))
moon.add_array(arc([0, 1], [0, 0], 1, out=False))
moon.loop()
#moon.fill(ax)

#2, 2
ax = axs[5]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
block.rotate(60).scale(10.1, 10.1).fill(ax, facecolor='black')
block.rotate(180).scale(10.1, 10.1).fill(ax, facecolor='black')
block.rotate(300).scale(10.1, 10.1).fill(ax, facecolor='black')
circle.fill(ax, facecolor='white')

#2, 3
ax = axs[6]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5.5, 5.5).fill(ax, facecolor='red')
circle.scale(5, 5).fill(ax, facecolor='black')
moon.scale(10, 10).rotate(0).fill(ax, facecolor='black')
moon.scale(10, 10).rotate(120).fill(ax, facecolor='black')
moon.scale(10, 10).rotate(240).fill(ax, facecolor='black')
circle.fill(ax, facecolor='white')

#2, 4
ax = axs[7]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
block.rotate(-30).scale(10.1, 10.1).fill(ax, facecolor='black')
block.rotate(90).scale(10.1, 10.1).fill(ax, facecolor='black')
block.rotate(210).scale(10.1, 10.1).fill(ax, facecolor='black')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(0).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(0).fill(ax, facecolor='white')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(120).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(120).fill(ax, facecolor='white')
comma.scale(1.3, 1.3).rotate(-30).move(5.5, 0).rotate(240).fill(ax, facecolor='black')
circle.scale(0.7, 0.7).move(5.5, 0).rotate(240).fill(ax, facecolor='white')

fig.tight_layout(pad=0.1)
plt.show()
