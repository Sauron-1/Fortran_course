#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

class Lagrange:
    '''
    This class works as a function once initialed.
    '''
    
    def __init__(self, xs, ys):
        '''
        __init__(self, xs, ys)

        args:
            xs, ys: points for interpolate.
        '''
        self.xs = xs.reshape(xs.size, 1)
        self.ys = ys.reshape(ys.size, 1)

    def __call__(self, x):
        '''
        __call__(self, x)

        args:
            x: a number or a ndarray.

        returns:
            pridiction of x, using lagrange interpolate.
        '''
        ret = 0
        if isinstance(x, np.ndarray):
            x = x.reshape(1, x.size)
        else:
            x = np.array(x).reshape(1, 1)
        for i in range(len(xs)):
            ret += self.ys[i][0]*np.product(x-self.xs[:i], axis=0)* \
                      np.product(x-self.xs[i+1:], axis=0)/ \
                      np.product(self.xs[i][0]-self.xs[:i,0])/ \
                      np.product(self.xs[i][0]-self.xs[i+1:,0]) 
        return ret

if __name__ == '__main__':
    #Solve the question
    import sys
    xs = np.array([1.05, 1.1, 1.15, 1.2])
    ys = np.array([2.12, 2.2, 2.17, 2.32])

    f = Lagrange(xs, ys)
    x = np.linspace(1.05, 1.2, 100)
    y = f(x)
    plt.plot(x, y, lw=1)
    plt.minorticks_on()
    plt.tick_params(which='both',
                    direction='in',
                    top=True,
                    right=True)
    plt.xlim(x.min(), x.max())
    plt.xlabel(r'x')
    plt.ylabel(r'$f(x)$')
    if len(sys.argv) == 1:
        plt.show()
    else:
        plt.savefig(sys.argv[1], format='eps')
