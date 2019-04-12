import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(10)
ys = xs**2

err_xs = 0.05 * xs
err_ys = 0.05 * ys

plt.errorbar(xs, ys, xerr=err_xs, yerr=err_ys, capsize=2)
plt.show()
