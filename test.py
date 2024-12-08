from sympy import symbols, I, log, exp, atanh, tanh, simplify, trigsimp

# Объявляем переменные
x, k, y = symbols('x k y')

# Записываем выражение
expr = (y/2 - I*log((k**2 + (k**2 - 1)*exp(4*atanh(tanh(x/2))) +
                     (2*k**2 + 2)*exp(2*atanh(tanh(x/2))) - 1)*exp(-2*atanh(tanh(x/2)))/(2*(k**2 + 1)))/2)

# Упрощаем выражение
simplified_expr = expr.rewrite(exp).simplify()

# Печатаем упрощенное выражение
print(simplified_expr)
