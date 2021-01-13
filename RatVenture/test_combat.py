import pytest
from RatVenture_functions import *
from RatVenture_classes import *

##attack##

#check initial player and enemy HP

#check new HP

#if <=0

#check if game over screen?

#if NOT 0

#check enemy HP

#if enemy HP <=0

#return to map

#else check if both player and enemy HP went down

#check if it is using outdoor menu

@pytest.mark.parameterize("hp",[(20)])

    def test_combat("hp, resultHP"):
        valueHP = fight(hp)
        assert valueHP > resultHP
    
##run##

#check if enemy instance HP went back to full

#check if outdoor menu is selected
