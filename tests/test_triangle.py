from conftest import *


@pytest.mark.parametrize("test_data", [
    (0.5, 1, 3),
    (1, 2, 4),
    (3, 9, 6)
])
def test_create_triangle_negative1(test_data):
    with pytest.raises(ValueError):
        Triangle(*test_data)


@pytest.mark.parametrize("test_data", [
    (0, 1, 3),
    (-1, 2, 4),
    (0, 0, -6)
])
def test_create_triangle_negative2(test_data):
    with pytest.raises(AssertionError):
        Triangle(*test_data)


@pytest.mark.parametrize("arg, exp", [
    ((7, 8, 9), 24),
    ((2, 3, 4), 9),
    ((4.5, 4, 6), 14.5)
])
def test_checking_the_perimeter(arg, exp):
    triangle = Triangle(*arg)
    triangle.perimeter
    assert triangle.perimeter == exp


@pytest.mark.parametrize("arg, exp", [
    ((11, 10, 9), 42.4),
    ((3, 5, 7), 6.5),
    ((4, 4, 4), 6.9)
])
def test_checking_the_area(arg, exp):
    triangle = Triangle(*arg)
    triangle.area
    assert triangle.area == exp


def test_sum_of_the_areas_positive1():
    triangle = Triangle(4, 3, 2)
    square = Square(5)
    triangle.add_area(square)
    assert triangle.add_area(square) == 27.9


def test_sum_of_the_areas_positive2():
    triangle = Triangle(6, 7, 8)
    circle = Circle(3)
    triangle.add_area(circle)
    assert triangle.add_area(circle) != 0


def test_sum_of_the_areas_positive3():
    rectangle = Rectangle(4, 2)
    triangle = Triangle(5, 7, 9)
    triangle.add_area(triangle)
    assert triangle.add_area(rectangle) >= 25


def test_sum_of_the_areas_negative(default_figure):
    triangle = Triangle(11, 9, 10)
    with pytest.raises(ValueError):
        triangle.add_area(default_figure)
