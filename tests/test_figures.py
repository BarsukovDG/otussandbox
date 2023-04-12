import pytest

from secondOOP.src.Figure import Figure
from secondOOP.src.Rectangle import Rectangle
from secondOOP.src.Square import Square
from secondOOP.src.Triangle import Triangle
from secondOOP.src.Circle import Circle


"""Creating figures block"""
rectangle = Rectangle(5, 10)
square = Square(10)
triangle = Triangle(13, 14, 15)
circle = Circle(10)

"""Creating non-geometric objects"""
rook = Figure(name='rook')


"""
Rectangle tests
"""


def test_rectangle_perimeter():
    """check rectangle has a perimeter"""
    assert rectangle.perimeter > 0


def test_rectangle_perimeter_hardcoded():
    """check rectangle perimeter with values from creating part"""
    assert rectangle.perimeter == 30


def test_rectangle_area():
    """check rectangle has an area"""
    assert rectangle.area > 0


def test_rectangle_area_hardcoded():
    """check rectangle area with values from creating part"""
    assert rectangle.area == 50


def test_rectangle_add_non_geometric_figure_area():
    """negative check by adding non-geometrical object area"""
    with pytest.raises(ValueError):
        rectangle.add_area(rook)


def test_rectangle_add_square_area_hardcoded():
    """check sum of rectangle and square areas with values from creating part"""
    assert rectangle.add_area(square) == 150


def test_rectangle_add_triangle_area():
    """check sum of rectangle and triangle is more than rectangle area"""
    assert rectangle.add_area(triangle) > 50


def test_create_impossible_triangle():
    with pytest.raises(ValueError):
        assert Triangle(1, 1, 3), "triangle with these attributes is actually valid"