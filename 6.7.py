import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

A = np.array([[1, -2, 3], [0, -4, 1], [-2, 5, 1]])
print(spla.norm(A, ord=2))
U, s, VT = spla.svd(A, full_matrices=False)
print(np.amax(s))
