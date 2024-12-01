from sympy import symbols, Matrix, diff, tanh, asin, log, cosh, I, sin, cos, latex, mathematica_code, simplify

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
        self.transformation = None  # Функция преобразования координат

    def set_transformation(self, func):
        """Устанавливает функцию преобразования координат."""
        self.transformation = func

    def compute_jacobian(self):
        """Вычисляет Якобиан преобразования."""
        if self.transformation is None:
            raise ValueError("Transformation function is not defined.")

        old_coords = self.transformation(*self.coords_new)

        J = Matrix([
            [diff(old_coord, new_coord) for new_coord in self.coords_new]
            for old_coord in old_coords
        ])
        return J

    def change_metric(self):
        """Преобразует метрический тензор в новых координатах."""
        J = self.compute_jacobian()
        old_coords = self.transformation(*self.coords_new)
        metric_new = simplify(J.transpose() * self.metric.subs(dict(zip(self.coords_old, old_coords))) * J)
        return metric_new