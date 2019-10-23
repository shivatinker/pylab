import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

plt.title("Lab #3.4")

ax = plt.subplot(1, 1, 1)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
t = np.linspace(0, 20 * np.pi, 500)
ax.plot(9 * np.sin(t / 10) - 1 / 2 * np.sin(9 * t / 10), 9 * np.cos(t / 10) + 1 / 2 * np.cos(9 * t / 10), "r")

plt.show()
