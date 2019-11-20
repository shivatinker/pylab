import sympy as sp

a = sp.symbols('a')
z = ((1 - 2 * a + a ** 2) * (a ** 2 - 1) * (a - 1)) ** (1 / 4.0) / ((a ** 2 + 2 * a - 3) / ((a + 1) ** (1 / 4.0)))
z = sp.cancel(sp.factor(sp.simplify(z), deep=True))
print(z)
print(z.evalf(subs={a: 3}))
