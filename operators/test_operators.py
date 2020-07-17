from operators import *


def test_add():
    assert my_sum == x1 + y1,  "Did you use the right operator?"

def test_subtract():
    assert my_diff == x2 - y2,  "Did you use the right operator?"

def test_multiply():
    assert my_mul == x3 * y3,  "Did you use the right operator?"

def test_division():
    assert my_div == x4 / y4,  "Did you use the right operator?"