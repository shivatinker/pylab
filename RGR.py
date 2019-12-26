import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# Base function
def fn(x, y):
    return 1.0 / (100 + np.power(np.cos(x), 2) + np.power(np.cos(y), 2))


# Continued function
def fp(x, y):
    return fn(x, y) * (1.0 if abs(x) + abs(y) <= 10 else 0.0)


# Quadratic integration
def trap_int(f, x0, x1, n):
    dx = (x1 - x0) / float(n)
    I = 0.0
    for i in range(n):
        a = x0 + dx * i
        b = a + dx
        I += (f(a) + f(b)) / 2.0 * dx
    return I


def double_int(f, x0, x1, y0, y1, n):
    g = lambda x: trap_int(lambda y: f(x, y), y0(x), y1(x), n)
    return trap_int(g, x0, x1, n)


# Cubic integration
def cube_int(f, x0, x1, y0, y1, n):
    dx = (x1 - x0) / float(n)
    dy = (y1 - y0) / float(n)
    I = 0.0
    for i in range(n):
        for j in range(n):
            x00, y00 = x0 + dx * i, y0 + dy * j
            I += dx * dy * (f(x00, y00) + f(x00 + dx, y00) + f(x00, y00 + dy) + f(x00 + dx, y00 + dy)) / 4.0
    return I


# 3D Plot
a, b = -10, 10
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.linspace(a, b)
Y = np.linspace(a, b)
X, Y = np.meshgrid(X, Y)
ax.plot_wireframe(X, Y, fn(X, Y))  # np.where(abs(X) + abs(Y) <= 10, fn(X, Y), 0))
ax.view_init(70, 75)
plt.show()

# Testing
def calc(n):
    print("N = %d" % n)
    di = double_int(fn, -10, 10, lambda x: (np.abs(x) - 10), lambda x: (-np.abs(x) + 10), n)
    ci = cube_int(fp, -10, 10, -10, 10, n)
    print("Quadratic: %.3f\nCubic: %.3f\nDiff: %.3f\n" % (di, ci, abs(di - ci)))


for n in [20, 100, 200, 300]:
    calc(n)
