#Unit Test Function for stats increase after obtaining the orb.
import pytest
from RatVenture_functions import *
from RatVenture_classes import *

def test_checkstats():
#check initial player and enemy HP
    initialplayer = Entity("The Hero", 20, "2-4", 1)
    player = pickorb(initialplayer)
    assert player.orb == true
    assert initialplayer.damage == "7-9"
    assert initialplayer.defence == "6"
    

    

    