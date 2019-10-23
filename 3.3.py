import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

x1 = np.linspace(1, np.e, 50)
x2 = np.linspace(np.e, 9, 50)
x3 = np.linspace(9, 12, 50)


def f(x):
    if 1 <= x <= np.e:
        return np.log(x)
    if np.e < x <= 9:
        return x / np.e
    if 9 < x <= 12:
        return 9 * np.exp(8 - x)


def vf(x):
    return np.array(list(map(f, x)))


# fig, ax = plt.subplots()
plt.title("Lab #3.3")

ax = plt.subplot(1, 1, 1)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x1, vf(x1), "r")
ax.plot(x2, vf(x2), "g")
ax.plot(x3, vf(x3), "b")

plt.show()
