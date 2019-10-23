import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

x1 = np.linspace(-1, 1, 10)
x2 = np.linspace(0, 1, 10)

# fig, ax = plt.subplots()
plt.title("Lab #3.1")

ax = plt.subplot(2, 2, 1)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x1, x1 ** 3 + 2 * x1 ** 2 + 1, "r--")
ax.legend(["$y=x^3+2x^2+1$"])

ax = plt.subplot(2, 2, 2)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x1, (x1 - 1) ** 4, "g")
ax.legend(["$(x-1)^4$"])

ax = plt.subplot(2, 2, 3)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x2, np.sqrt(x2), "b*-")
ax.legend(["$\sqrt{x}$"])

ax = plt.subplot(2, 2, 4)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x2, np.exp(-(x2**2)))
ax.legend(["$e^{-x^2}$"])

plt.show()
