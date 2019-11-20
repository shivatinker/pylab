import sympy as sp

x = sp.symbols('x')
eq = sp.sin(x)**4 - sp.cos(x)**4
print(sp.solve(eq - 0.5, x))