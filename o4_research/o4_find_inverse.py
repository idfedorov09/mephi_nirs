from math import exp

from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code, simplify, atanh, \
    Function
from o4_research.ccmodel import CCModel

r, phi1, phi2 = symbols('r phi1 phi2')
x, y, z = symbols('x y z')
kappa, h, a, b, c = symbols('k h a b c')

g11 = 2 * kappa / h * 1 / (1 - r ** 2) * 1 / (1 - kappa ** 2 * r ** 2)
g22 = 2 * kappa / h * (1 - r ** 2) / (1 - kappa ** 2 * r ** 2)
g33 = 2 * kappa / h * r ** 2
g_x = Matrix([
    [g11,  0,  0],
    [  0,g22,  0],
    [  0,  0,g33],
])

model = CCModel(metric=g_x, coords_old=[r, phi1, phi2], coords_new=[x, y, z])

FF = Function('F')(kappa)
GG = Function('G')(kappa)


@model.set_transformation(inverse = True)
def transform(r, phi1, phi2):
    x = log(r**2 / (1 - kappa**2 * r**2)) + log(FF)
    y = 2*log(tanh(phi2)) + log(GG)
    z = 2*phi1 - I * log ((1-kappa**2 * r**2) / (1-r**2))
    return x, y, z

# Преобразуем метрику
g_new = model.change_metric().rewrite(exp).simplify()

print("\nНовая метрика в новых координатах (mathematica output):")
mathematica_output = mathematica_code(g_new)
print(mathematica_output)
