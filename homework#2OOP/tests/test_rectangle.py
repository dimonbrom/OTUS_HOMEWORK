from conftest import *


@pytest.mark.parametrize("arg, exp", [
    ((7, 8), 30),
    ((1, 3), 8),
    ((4.5, 4), 17)
])
def test_checking_the_perimeter(arg, exp):
    rectangle = Rectangle(*arg)
    rectangle.perimeter
    assert rectangle.perimeter == exp


@pytest.mark.parametrize("arg, exp", [
    ((11, 3), 33),
    ((0, 4), 0),
    ((4, 4), 16)
])
def test_checking_the_area(arg, exp):
    rectangle = Rectangle(*arg)
    rectangle.area
    assert rectangle.area == exp


def test_sum_of_the_areas_positive1():
    rectangle = Rectangle(4, 3)
    square = Square(5)
    rectangle.add_area(square)
    assert rectangle.add_area(square) == 37


def test_sum_of_the_areas_positive3():
    rectangle = Rectangle(4, 2)
    triangle = Triangle(5, 7, 9)
    rectangle.add_area(triangle)
    assert rectangle.add_area(triangle) >= 25


def test_sum_of_the_areas_negative(default_figure):
    rectangle = Rectangle(11, 9)
    with pytest.raises(ValueError):
        rectangle.add_area(default_figure)
