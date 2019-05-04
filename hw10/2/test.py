import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from solve import Solver

#Boundary conditions
def fn(x):
    return 1.5 + np.tanh(x)

solver = Solver(101, [-2, 15], fn, CFL=0.01)

#Plot
line, = plt.plot(solver.xs, solver.u)
txt = plt.text(0.1, 0.9, 't = 0', transform=plt.gca().transAxes)
plt.xlabel('x')
plt.ylabel('y')
plt.minorticks_on()
plt.tick_params(which='both', top=True, right=True, direction='in')

#Animate
def animate(t):
    while solver.t < t:
        solver.next()
    txt.set_text('t = %f'%(solver.t))
    line.set_ydata(solver.u)

anim = animation.FuncAnimation(plt.gcf(), animate, 
                               frames=np.linspace(0, 5, 100),
                               interval=50)

#Save to gif
anim.save('test.gif', writer='pillow')
