from conftest import *


@pytest.mark.parametrize("arg, exp", [
    ((3), 18.8),
    ((0), 0),
    ((4.5), 28.3)
])
def test_checking_the_perimeter(arg, exp):
    circle = Circle(arg)
    circle.perimeter
    assert circle.perimeter == exp


@pytest.mark.parametrize("arg, exp", [
    ((10), 314),
    ((0), 0),
    ((4), 50.2)
])
def test_checking_the_area(arg, exp):
    circle = Circle(arg)
    circle.area
    assert circle.area == exp


def test_sum_of_the_areas_positive1():
    circle = Circle(4)
    rectangle = Rectangle(3, 6)
    circle.add_area(rectangle)
    assert circle.add_area(rectangle) == 68.2


def test_sum_of_the_areas_positive2():
    square = Square(8)
    circle = Circle(2)
    circle.add_area(square)
    assert circle.add_area(square) != 0


def test_sum_of_the_areas_positive3():
    circle = Circle(9)
    triangle = Triangle(5, 7, 9)
    circle.add_area(triangle)
    assert circle.add_area(triangle) >= 98


def test_sum_of_the_areas_negative(default_figure):
    circle = Circle(3)
    with pytest.raises(ValueError):
        circle.add_area(default_figure)
