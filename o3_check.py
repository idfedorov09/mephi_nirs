from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code

# Определение новых координат (y1, y2, y3) и старых (x1, x2, x3)
x, y = symbols('x y') # x, y
kappa, h = symbols('k h')
x1 = asin(kappa ** (-1) * tanh(x / 2)) # theta
x2 = y / 2 - I / 2 * log(1 - (1 - kappa ** 2) / (1 + kappa ** 2) * cosh(x))  # chi

g11 = 2*kappa / h * (1 - (h * kappa * (cos(x1))**2)/(1 - kappa**2 * (sin(x1))**2)) / (1 - kappa**2 * (sin(x1))**2)
g22 = 2*kappa / h * ((cos(x1))**2) / (1 - kappa**2 * (sin(x1))**2)
# Старый метрический тензор как функция старых координат
g_x = Matrix([
    [g11, 0],
    [0, g22],
])

g_y = g_x.subs({symbols('x1'): x1, symbols('x2'): x2})

# Якобиан преобразования
J = Matrix([
    [diff(x1, x), diff(x1, y)],
    [diff(x2, x), diff(x2, y)],
])

# Новый метрический тензор
g_new = J.transpose() * g_y * J
g_new.simplify()
print(g_new)

latex_output = latex(g_new)
print(latex_output)

mathematica_output = mathematica_code(g_new)
print(mathematica_output)
