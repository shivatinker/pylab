import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

xy = np.linspace(-10, 10)
X, Y = np.meshgrid(xy, xy)
Z = (1 + X * Y)/(3 - X) * (4 - Y)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
plt.show()
