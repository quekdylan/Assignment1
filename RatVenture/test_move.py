import pytest
from RatVenture_functions import *


def test_move():
    updatedLocation, updatedDay = move("0,0", "d", 1)
    assert updatedLocation == "1,0"
    assert updatedDay == 2

def test_capital_input():
    updatedLocation, updatedDay = move("0,0", "S", 1)
    assert updatedLocation == "0,1"
    assert updatedDay == 2

def test_invalid_input():
    value = move("0,0", "g", 1)
    assert value == 0

def test_out_of_bounds():
    value = move("0,0", "w", 1)
    assert value == 0