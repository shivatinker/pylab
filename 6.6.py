import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla

A = np.array([[1, 2], [-3, 0], [4, -1]])
b = np.array([1, 1, 1])
A2 = A.T.dot(A)
b2 = A.T.dot(b)
x = spla.solve(A2, b2)
print(x)
x, res, rank, s = spla.lstsq(A, b)
print(x)
Ainv = spla.pinv(A)
print(Ainv.dot(b))
Ainv = spla.pinv2(A)
print(Ainv.dot(b))
Q, R = spla.qr(A, mode='economic')
x = spla.inv(R).dot(Q.T.dot(b))
print(x)
