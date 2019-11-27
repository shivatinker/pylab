import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: (x - 4) ** 2 + (x + 1) ** 2
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
ax.plot(x, f(x))
plt.show()

x1 = opt.fmin_bfgs(f, 0.0)
x2 = opt.brent(f, full_output=True)
x3 = opt.fminbound(f, -10, 10, disp=3)

print(x1, x2, x3)
