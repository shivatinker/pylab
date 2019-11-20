import sympy as sp

x = sp.symbols('x')
f = x ** 3 * sp.cos(x)
I = sp.integrate(f)
print(I.evalf(subs={x: sp.pi / 2}) - I.evalf(subs={x: 0}))
