#Unit Test Function for if the rat king is killable.
import pytest
from RatVenture_functions import *
from RatVenture_classes import *


#@pytest.mark.parametrize("player, enemy",[(p,r)])
def test_checkkillable():
#check initial player and enemy HP
    player = Entity("The Hero", 20, "2-4", 1)
    enemy = Entity('Rat King', 25, "8-12", 5)

    #maybe a bool here for weather there is an orb?
    porb = player.orb
    ehealth = enemy.health
    
    player, enemy, status = attack(player, enemy)
    assert player.orb = true
    assert enemy.health < ehealth
                   





