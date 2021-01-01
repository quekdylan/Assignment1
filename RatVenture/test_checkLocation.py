import pytest
from RatVenture_functions import *


def checkTown():
    result = checkLocation("0,0")
    assert result == "a town"

def checkOpen():
    result = checkLocation("1,0")
    assert result == "the open"

def checkOrb():
    result = checkLocation("7,7")
    assert result == "the orb"