import pytest

from scr.Circle import Circle
from scr.Square import Square
from scr.Triangle import Triangle
from scr.Rectangle import Rectangle


@pytest.fixture
def default_figure():
    a = 5
    b = 7
    return a * b




