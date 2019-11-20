import sympy as sp

x = sp.symbols('x')
f = (x ** 3 - 6) / (x ** 4 + 6 * x ** 2 + 8)
print(f)
i = sp.integrate(f, x)
print(i)
d = i.diff(x)
print(d)
print(sp.simplify(f - d))
