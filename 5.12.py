import sympy as sp
import sympy.plotting as splot

u, v = sp.symbols('u v')

splot.plot3d_parametric_surface(4 + (3 + sp.cos(v)) * sp.sin(u), 4 + (3 + sp.cos(v)) * sp.cos(u), 4 + sp.sin(v),
                                (u, -0, 2 * sp.pi),
                                (v, -0, 2 * sp.pi))
splot.plot3d_parametric_surface(8 + (3 + sp.cos(v)) * sp.cos(u), 3 + sp.sin(v), 4 + (3 + sp.cos(v)) * sp.sin(u),
                                (u, -0, 2 * sp.pi),
                                (v, -0, 2 * sp.pi))
