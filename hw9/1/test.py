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
comma.rotate(20, update=True)

#circle
thetas = np.linspace(0, 2*np.pi, 200)
circle = Shape()
circle.add_line(np.cos, np.sin, thetas)
circle.loop()


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

#moon
moon = Shape()
moon.add_array(arc([0, 0], [0, 1], 0.53))
moon.add_array(arc([0, 1], [0, 0], 1, out=False))
moon.loop()

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

#leaf
leaf = Shape()
leaf.add_array(arc([1.5, 0], [-1.5, 0], 1.5))
leaf.add_array(arc([-1.5, 0], [0, 10], 15))
leaf.add_array(arc([0, 10], [1.5, 0], 15))

#horn
horn = Shape()
horn.add_array(line([0, 0], [0, 1]))
horn.add_array(arc([0, 1], [1, -1], 2))
horn.add_array(arc([1, -1], [0, 0], 1, out=False))

#3, 1
ax = axs[8]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
horn.scale(5, 5).move(0, 5).rotate(60).fill(ax, facecolor='black')
horn.scale(5, 5).move(0, 5).rotate(180).fill(ax, facecolor='black')
horn.scale(5, 5).move(0, 5).rotate(300).fill(ax, facecolor='black')
leaf.rotate(60).fill(ax, facecolor='#303030')
leaf.rotate(180).fill(ax, facecolor='#303030')
leaf.rotate(300).fill(ax, facecolor='#303030')
circle.fill(ax, facecolor='red')

#half_oval
def kcos(x, k):
    return k*np.cos(x)
def ksin(x, k):
    return k*np.sin(x)
half_oval = Shape()
thetas = np.linspace(0, np.pi, 100)
half_oval.add_line(kcos, ksin, thetas, argx={'k':4}, argy={'k':10})
half_oval.add_array(line([-4, 0], [-3, 0]))
thetas = thetas[::-1]
half_oval.add_line(kcos, ksin, thetas, argx={'k':3}, argy={'k':9})
half_oval.add_array(line([3, 0], [4, 0]))

#3, 2
ax = axs[9]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
circle.scale(6, 6).fill(ax, facecolor='black')
circle.scale(5, 5).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')
for t in range(6):
    half_oval.rotate(t*60).fill(ax, facecolor='white')
    half_oval.rotate(t*60).plot(ax, color='white', lw=0.5)

#spiral
def xcosp(x, p=0):
    return x*np.cos(x)+p
def xsinp(x, p=0):
    return x*np.sin(x)+p
spiral = Shape()
thetas = np.linspace(0, 10.25, 100)
spiral.add_line(xcosp, xsinp, thetas, 
                argx={'p':0.25*np.cos(thetas)}, 
                argy={'p':0.25*np.sin(thetas)})
thetas = thetas[::-1]
spiral.add_line(xcosp, xsinp, thetas, 
                argx={'p':-0.25*np.cos(thetas)}, 
                argy={'p':-0.25*np.sin(thetas)})
spiral.loop()

#3, 3
ax = axs[10]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
spiral.rotate(-60).fill(ax, facecolor='black')

#3, 4
ax = axs[11]
circle.scale(11, 11).fill(ax, facecolor='black')
circle.scale(10, 10).fill(ax, facecolor='red')
for t in range(2, -1, -1):
    circle.scale(3.5+2.25*t, 3.5+2.25*t).fill(ax, facecolor='black')
    circle.scale(3.0+2.25*t, 3.0+2.25*t).fill(ax, facecolor='red')
circle.fill(ax, facecolor='black')

fig.tight_layout(pad=0.1)
fig.savefig('test.eps', format='eps')
