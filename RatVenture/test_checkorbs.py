#Unit Test Function for rest Function.
import pytest
from RatVenture_functions import *

def checkoriginalTown():
    result = checkLocation("0,0")
    assert result == "a town"

def checkorb():
    result1 = checkLocation("3,1")
    result2 = checkLocation("5,2")
    result3 = checkLocation("1,3")
    result4 = checkLocation("4,6")

    assert result1 = "a town with orb" or result2 = "a town with orb" or result3 = "a town with orb" or result4 = "a town with orb"
