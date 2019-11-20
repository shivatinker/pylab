import sympy as sp

x, y = sp.symbols('x y')
f = x ** 2 - x * y + y * y
grad = [sp.diff(f, x), sp.diff(f, y)]
print(grad)
grad_p = [z.evalf(subs={x: 1, y: 1}) for z in grad]
print(grad_p)
a = [3, -2]
d = grad_p[0] * a[0] + grad_p[1] * a[1]
print(d)
print("Yes" if d > 0 else "No")
