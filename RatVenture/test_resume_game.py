import pytest
from RatVenture_functions import *
from RatVenture_classes import *


def test_resume_without_save():
    player, location, day = resumeGame("abcd.txt")
    assert player.name == "The Hero"
    assert player.health == 20
    assert player.damage == "2-4"
    assert player.defence == 1
    assert location == "0,0"
    assert day == 1