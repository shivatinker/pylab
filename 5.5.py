import sympy as sp

x = sp.symbols('x')
print(sp.limit(sp.tan(sp.pi / 8 + x) ** sp.tan(2 * x), x, sp.pi / 4, dir="+"))
