import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

x = np.linspace(0, 2 * np.pi, 50)

plt.title("Lab #3.2")

ax = plt.subplot(1, 1, 1, polar=True)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, 1 - np.sin(x), 'r', marker='o', linewidth=3)
ax.legend(["$1-\sin \phi$"])

plt.show()
