import numpy as np

class Solver(object):
    '''
    Solve the equation of this problem. Should been written by
    Fortran but windows 10's environment for f2py is so annoying...
    '''

    def __init__(self, n, x_range, initial_fn, CFL=0.1):
        self.n = n
        self.x_range = x_range
        self.CFL = CFL
        self.initial_fn = initial_fn

        self.dx = (x_range[1] - x_range[0]) / n
        self.u_t = np.zeros((n+2))
        self.a_t = np.zeros((n+1))
        self.t = 0.

        self.xs = np.linspace(x_range[0], x_range[1], n)
        self.u = initial_fn(self.xs)

    def next(self):
        '''
        Next time.
        '''
        self.u_t[1:-1] = self.u
        self.u_t[0] = self.initial_fn(self.x_range[0])
        self.u_t[-1] = self.initial_fn(self.x_range[1])

        self.a_t[...] = 0.5 * (self.u_t[:-1] + self.u_t[1:])

        dt = self.CFL * self.dx / np.max(np.abs(self.a_t))

        self.u = self.u - dt/4/self.dx * (self.u_t[2:]**2 - self.u_t[:-2]**2) + \
            0.25*(dt/self.dx)**2 * (self.a_t[1:]*(self.u_t[2:]**2 - \
            self.u_t[1:-1]**2) - self.a_t[:-1]*(self.u_t[1:-1]**2 - \
            self.u_t[:-2]**2))

        self.t += dt
