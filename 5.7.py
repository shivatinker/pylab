import sympy as sp

x, y = sp.symbols('x y')
f = sp.atan((x + y) / (1 - x * y))
ds = [f.diff(x), f.diff(y), f.diff(x, y), f.diff(y, x), f.diff(x, x), f.diff(y, y)]
print([sp.simplify(z) for z in ds])
