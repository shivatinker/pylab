import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

f = lambda x: np.log(x)
print(spint.quad(f, 0, 1))
print(spint.fixed_quad(f, 0, 1, n=10))
print(spint.quadrature(f, 0, 1, tol=1e-3))
