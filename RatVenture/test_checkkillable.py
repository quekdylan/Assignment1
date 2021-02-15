#Unit Test Function for if the rat king is killable.
import pytest
from RatVenture_functions import *
from RatVenture_classes import *


#@pytest.mark.parametrize("player, enemy",[(p,r)])
def test_checkkillable():
#check initial player and enemy HP
    player = Entity("The Hero", 20, "7-9", 5, True)
    enemy = Entity('Rat King', 25, "8-12", 5)

    ehealth = enemy.health
    
    player, enemy, status = attack(player, enemy, player.orb)
    assert player.orb == true
    assert enemy.health < ehealth
                   





