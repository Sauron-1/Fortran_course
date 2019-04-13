import numpy as np
import matplotlib.pyplot as plt

def myerrorbar(x, y=None, xerr=None, yerr=None, **kwargs):
    '''
    myerrorbar([x,] y, xerr=None, yerr=None, **kwargs)

    args:
        x, y: array-like or scalar
            List of coordinata. x and y should have same size.
            *x* value is optional. If not given, they default to
            ``[0, ..., N-1]``

        xerr, yerr: array-like, optional
            Err values of each x, y. Should have same size
            as x and y, or be None.

        kwargs:
            See matplotlib.pyplot.plot.

    returns:
        Same as matplotlib.pyplot.plot(x, y, **kwargs)

    '''
    #If no x is given, y is on x's position.
    if y is None:
        y = x
        x = np.arange(y.size)

    ret = plt.plot(x, y, **kwargs)
    color = ret[0].get_color()

    #x errors.
    if xerr is not None:
        for i in range(x.size):
            plt.plot([x[i]-xerr[i], x[i]+xerr[i]],
                     [y[i], y[i]],
                     color=color)

    #y errors.
    if yerr is not None:
        for i in range(x.size):
            plt.plot([x[i], x[i]],
                     [y[i]-yerr[i], y[i]+yerr[i]],
                     color=color)

    return ret
