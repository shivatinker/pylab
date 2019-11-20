import sympy as sp

x, y, z = sp.symbols('x y z')
print(sp.solve([x + y * z - 2, y + z * x - 2, z + x * y - 2]))
