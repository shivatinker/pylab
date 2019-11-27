import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

t = lambda y, x: x * np.sin(y)
print(spint.dblquad(t, 0, np.pi / 2, lambda x: x - np.pi / 6, lambda x: x + np.pi / 6))