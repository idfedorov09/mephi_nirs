from math import exp

from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code, simplify
from o4_research.ccmodel import CCModel
from o4_research.utils.check_matrix_exp import check_matrix_exp

r, phi1, phi2 = symbols('r phi1 phi2')
x, y, z = symbols('x y z')
kappa, h = symbols('k h')

g11 = 2 * kappa / h * 1 / (1 - r ** 2) * 1 / (1 - kappa ** 2 * r ** 2)
g22 = 2 * kappa / h * (1 - r ** 2) / (1 - kappa ** 2 * r ** 2)
g33 = 2 * kappa / h * r ** 2
g_x = Matrix([
    [g11,  0,  0],
    [  0,g22,  0],
    [  0,  0,g33],
])

model = CCModel(metric=g_x, coords_old=[r, phi1, phi2], coords_new=[x, y, z])

@model.set_transformation
def transform(x, y, z):
    r = x
    phi1 = y
    phi2 = z
    return r, phi1, phi2

# Преобразуем метрику
g_new = model.change_metric().rewrite(exp).simplify()

is_success = check_matrix_exp(g_new, [x, y, z])
if is_success:
    print("SUCCESS")
else:
    print("такие преобразования не подходят.")

print("\nНовая метрика в новых координатах (mathematica output):")
mathematica_output = mathematica_code(g_new)
print(mathematica_output)
