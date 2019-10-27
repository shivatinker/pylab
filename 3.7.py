import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl

x = np.linspace(0, np.pi)
y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)
Z = np.power(np.sin(X - 2 * Y), 2) * np.exp(-np.abs(Y))

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
ax.view_init(30, 30)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
ax.view_init(15, 60)

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(2, 1, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0, cmap=mpl.cm.plasma)
cb = fig.colorbar(p, shrink=0.8)
ax.view_init(30, 45)

ax = fig.add_subplot(2, 1, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=mpl.cm.plasma)
cb = fig.colorbar(p, shrink=0.8)

plt.show()
