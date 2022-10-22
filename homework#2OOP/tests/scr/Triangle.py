from scr.Figure import Figure


class Triangle(Figure):
    NAME = 'triangle'

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise AssertionError('The side of a triangle cannot be 0')
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError('creation of a triangle is impossible')

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        s = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5
        return round(s, 1)



