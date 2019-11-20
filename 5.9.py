import sympy as sp

a, t, x, b = sp.symbols('a t x b')
u = 1 / (2 * a * sp.sqrt(sp.pi * t) / sp.exp(-((x - b) ** 2 / (4 * a ** 2 * t))))
eq = u.diff(t) - a * a * u.diff(x, x)
print(sp.latex(u))
print(sp.simplify(eq))
