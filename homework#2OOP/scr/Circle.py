from scr.Figure import Figure


class Circle(Figure):
    NAME = 'circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        p = 2 * 3.14 * self.radius
        return round(p, 1)

    @property
    def area(self):
        a = 3.14 * (self.radius ** 2)
        return round(a, 1)


