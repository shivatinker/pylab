import scipy as sp
import numpy as np
import scipy.integrate as spint
from scipy.misc import derivative
import scipy.linalg as spla


f = lambda x: np.sin(x)
print(derivative(f, np.pi))
print(derivative(f, np.pi, dx=1e-6))