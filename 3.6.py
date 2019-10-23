import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

plt.title("Lab #3.6")

x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)
f = (X * X + Y * Y) ** 2 - 7 * (X * X - Y * Y)

fig = plt.figure()
plt.grid()
plt.contour(X, Y, f, [0])

plt.show()
