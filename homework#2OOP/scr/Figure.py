class Figure:
    NAME = None

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("transferred is not a geometric figure")
        return self.area + figure.area
