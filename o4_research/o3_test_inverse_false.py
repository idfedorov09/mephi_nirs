from math import exp

from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code, simplify
from o4_research.ccmodel import CCModel
from o4_research.utils.check_matrix_exp import check_matrix_exp

theta, chi = symbols('theta chi')
x, y = symbols('x y')
kappa, h = symbols('k h')

g11 = 2 * kappa / h * (1 - (h * kappa * (cos(theta))**2) / (1 - kappa ** 2 * (sin(theta)) ** 2)) / (1 - kappa ** 2 * (sin(theta)) ** 2)
g22 = 2*kappa / h * ((cos(theta))**2) / (1 - kappa**2 * (sin(theta))**2)
g_x = Matrix([
    [g11,  0],
    [  0,g22]
])

model = CCModel(metric=g_x, coords_old=[theta, chi], coords_new=[x, y])

@model.set_transformation(inverse = False)
def transform(x, y):
    theta = asin(kappa ** (-1) * tanh(x / 2))
    chi = y / 2 - I / 2 * log(1 - (1 - kappa ** 2) / (1 + kappa ** 2) * cosh(x))
    return theta, chi

# Преобразуем метрику
g_new = model.change_metric().rewrite(exp).simplify()

is_success = check_matrix_exp(g_new, [x, y])
if is_success:
    print("SUCCESS")
else:
    print("такие преобразования не подходят.")

print("\nНовая метрика в новых координатах (mathematica output):")
mathematica_output = mathematica_code(g_new)
print(mathematica_output)
