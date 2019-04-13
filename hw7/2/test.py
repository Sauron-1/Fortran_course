from errorbar import myerrorbar
import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(10)
ys = xs**2

err_xs = 0.05 * xs
err_ys = 0.05 * ys

#Self-implied.
my, = myerrorbar(xs, ys, xerr=err_xs, 
        yerr=err_ys, color='blue')
plt.minorticks_on()
plt.tick_params(which='both',
                top=True,
                right=True)
plt.savefig('my.eps', format='eps')
my.remove()
#Call matplotlib function
plt.errorbar(xs, ys, xerr=err_xs, yerr=err_ys, 
        capsize=2, color='blue', ecolor='blue')
plt.savefig('lib.eps', format='eps')
