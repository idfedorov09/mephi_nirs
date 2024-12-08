from sympy import symbols, Eq, solve, simplify


def invert_transformations(equations, x_vars, y_vars):
    """
    Находит обратные преобразования для заданных уравнений,
    выбирая наиболее простое решение.

    :param equations: Список уравнений в виде sympy.Eq
    :param x_vars: Список переменных x (независимые переменные)
    :param y_vars: Список переменных y (зависимые переменные)
    :return: Список выражений для обратных преобразований x = g(y)
    """
    if len(equations) != len(x_vars) or len(x_vars) != len(y_vars):
        raise ValueError("Количество уравнений, x и y переменных должно совпадать")

    # solutions = []
    solutions = solve(tuple(equations), tuple(x_vars))
    for i in range(len(solutions)):
        solutions[i] = simplify(solutions[i])

    return solutions[1]


# from sympy import symbols, Eq, sin, exp, log
#
# # Определяем переменные
# x1, x2, x3 = symbols('x1 x2 x3')
# y1, y2, y3 = symbols('y1 y2 y3')
#
# # Задаем уравнения
# equations = [
#     Eq(y1, sin(x1)),
#     Eq(y2, exp(x2)),
#     Eq(y3, log(x3 + 1))
# ]
#
# # Находим обратные преобразования
# inverse_transformations = invert_transformations(equations, [x1, x2, x3], [y1, y2, y3])
#
# # Вывод результата
# print(inverse_transformations)

