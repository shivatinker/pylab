import sympy as sp

y = sp.Function('y')
x = sp.Symbol('x')
eq = y(x).diff(x, x) + 2 * y(x).diff(x) + y(x) - sp.exp(-x) * sp.sqrt(x + 1)
print(sp.dsolve(eq, y(x)))
