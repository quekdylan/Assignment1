import pytest
from RatVenture_functions import *
from RatVenture_classes import *

##attack##
def test_combat():
#check initial player and enemy HP
    phealth = player.health
    ehealth = enemy.health

    attack(player, enemy)
    assert player.health < phealth
    assert enemy.health < ehealth
                   
#check new HP
#if <=0

#check if game over screen?

#if NOT 0

#check enemy HP

#if enemy HP <=0

#return to map

#else check if both player and enemy HP went down

#check if it is using outdoor menu
    
##run##

#check if enemy instance HP went back to full

#check if outdoor menu is selected
