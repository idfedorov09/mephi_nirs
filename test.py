from sympy import exp
from sympy.core import Add, Mul, Derivative, Pow
from sympy import log, diff

def check_factor(factor, coords) -> bool:
    lfactor = log(factor)
    first_derivatives = [diff(lfactor, coord) for coord in coords]
    dd = [
        [diff(cur_dif, coord) for coord in coords] for cur_dif in first_derivatives
    ]
    return all(all(d == 0 for d in sublist) for sublist in dd)

def is_linear_combination_of_exps(expr, coords):
    if isinstance(expr, Mul) or isinstance(expr, Add) or isinstance(expr, Pow):
        return all(is_linear_combination_of_exps(arg, coords) for arg in expr.args)
    if isinstance(expr, Derivative):
        return False
    cur_factor_check_result = check_factor(expr, coords)
    if not cur_factor_check_result:
        return False
    return True


def check_matrix_linear_combination(matrix, coords):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            elem = matrix[i, j].simplify().rewrite(exp)
            if not is_linear_combination_of_exps(elem, coords):
                return False
    return True
