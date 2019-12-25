import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

A = np.array([[1, -2, 3], [0, -4, 1], [-2, 5, 1]])
b = np.array([1, 2, 3])
x = spla.solve(A, b)
print(x)
P, L, U = spla.lu(A)
b = np.array([1., 2., 3.])
Pb = P.T.dot(b)
y = spla.solve_triangular(L, Pb, lower=True)
x = spla.solve_triangular(U, y, lower=False)
print(x)
invA = spla.inv(A)
x = np.dot(invA, b)
print(x)
