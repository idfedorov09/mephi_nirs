from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code, simplify, Eq

from o4_research.utils.common import invert_transformations

"""
Change coordinate model
"""
class CCModel:
    def __init__(self, metric, coords_old, coords_new):
        """
        :param metric: Исходный метрический тензор в старых координатах
        :param coords_old: Старые координаты (список символов)
        :param coords_new: Новые координаты (символы, которые будут вычисляться через transform)
        """
        self.metric = metric
        self.coords_old = coords_old
        self.coords_new = coords_new
        self._calculated_old_coords = None
        self._should_invesre = False
        self.transformation = None  # Функция преобразования координат

    def set_transformation(self, inverse=False):
        """Возвращает декоратор для установки функции преобразования с параметром inverse."""

        def decorator(func):
            self._should_invesre = inverse
            self.transformation = func
            return func

        return decorator

    def compute_jacobian(self):
        """Вычисляет Якобиан преобразования."""
        if self.transformation is None:
            raise ValueError("Transformation function is not defined.")

        old_coords = self._calc_old_cords()

        J = Matrix([
            [diff(old_coord, new_coord) for new_coord in self.coords_new]
            for old_coord in old_coords
        ])
        return J

    def change_metric(self):
        """Преобразует метрический тензор в новых координатах."""
        J = self.compute_jacobian()
        old_coords = self._calc_old_cords()
        metric_new = simplify(J.transpose() * self.metric.subs(dict(zip(self.coords_old, old_coords))) * J)
        return metric_new

    # Laze init
    def _calc_old_cords(self):
        if self._calculated_old_coords is None:
            self._calculated_old_coords = self._calc_old_cords1()
        return self._calculated_old_coords


    def _calc_old_cords1(self):
        if self._should_invesre:
            new_cords = self.transformation(*self.coords_old)
            equations = [
                Eq(new_cords[i], self.coords_new[i]) for i in range(len(self.coords_old))
            ]
            inverse_transformations = invert_transformations(equations, self.coords_old, self.coords_new)
            return inverse_transformations
        else:
            return self.transformation(*self.coords_new)
