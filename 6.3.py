import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

f = lambda x: np.sin(x)
h = 1e-6
x0 = np.pi / 2
print(derivative(f, x0))
print((f(x0 + h) - f(x0 - h)) / (2 * h))
print(derivative(f, x0, n=2))
print((f(x0 + h) - 2 * f(x0) + f(x0 - h)) / (h ** 2))
