import scipy.interpolate as int
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [-2, 6, 8, 0, 1, 4]

p = int.lagrange(x, y)
print(p)
X = np.linspace(0, 5, 100)
L = p(X)  # значение интерполяционного многочлена Лагранжа в точках х

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, lw=2, label='Original function')
ax.plot(X, L, '--r', label='Lagrange polynomial')
ax.legend(loc=0)
# plt.show()

linear_interpolation = int.interp1d(x, y)  # линейная интерполяция (kind='linear')
y_interp1 = linear_interpolation(X)

cubic_interpolation = int.interp1d(x, y, kind='cubic')  # кубическая интерполяция
y_interp2 = cubic_interpolation(X)

# fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(X, y_interp1, 'r', label='Linear interpolation')
ax.plot(X, y_interp2, '--g', label='Cubic interpolation')
ax.legend(loc=0)
plt.show()
