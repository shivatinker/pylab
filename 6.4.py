from scipy import integrate as int
import numpy as np
import matplotlib.pyplot as plt


def f(y, t):
    y0, y1, y2 = y
    return [y1, y2, 1 - 5 * y0 - 2 * y2]


t = np.linspace(0, 10, 50)
y0 = [3, -2, 5]
w = int.odeint(f, y0, t)
y1 = w[:, 0]  # y(x)
y2 = w[:, 1]  # y'(x)
y3 = w[:, 2]  # y''(x)
plt.plot(t, y1, '-r', t, y2, '-g', t, y3, '-b', lw=1)
plt.show()

