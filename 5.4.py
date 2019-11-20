import sympy as sp

a, b, m, n, x = sp.symbols('alpha beta m n x')
print(sp.limit(((1 + a * x) ** (1 / m) - (1 + b * x) ** (1 / n)) / x, x, 0))
