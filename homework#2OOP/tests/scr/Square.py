from scr.Figure import Figure


class Square(Figure):
    NAME = 'square'

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4
