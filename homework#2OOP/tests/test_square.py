from conftest import *


@pytest.mark.parametrize("arg, exp", [
    ((7), 28),
    ((0), 0),
    ((4.2), 16.8)
])
def test_checking_the_perimeter(arg, exp):
    square = Square(arg)
    square.perimeter
    assert square.perimeter == exp


@pytest.mark.parametrize("arg, exp", [
    ((11), 121),
    ((0), 0),
    ((4), 16)
])
def test_checking_the_area(arg, exp):
    square = Square(arg)
    square.area
    assert square.area == exp


def test_sum_of_the_areas_positive1():
    square = Square(4)
    rectangle = Rectangle(3, 6)
    square.add_area(rectangle)
    assert square.add_area(rectangle) == 34


def test_sum_of_the_areas_positive3():
    square = Square(9)
    triangle = Triangle(5, 7, 9)
    square.add_area(triangle)
    assert square.add_area(triangle) >= 98


def test_sum_of_the_areas_negative(default_figure):
    square = Square(3)
    with pytest.raises(ValueError):
        square.add_area(default_figure)
