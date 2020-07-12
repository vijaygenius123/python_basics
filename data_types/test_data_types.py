from data_types import *


def test_int():
    assert type(my_int) == int, "Value Should be an integer"

def test_float():
    assert type(my_float) == float, "Value Should be a float"

def test_complex():
    assert type(my_complex) == complex, "Value Should be a complex value, did you forget to add j??"

def test_string():
    assert type(my_string) == str, "Value Should be a string"