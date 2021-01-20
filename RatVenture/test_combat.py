import pytest
from RatVenture_functions import *
from RatVenture_classes import *


##attack##
#@pytest.mark.parametrize("player, enemy",[(p,r)])
def test_combat():
#check initial player and enemy HP
    player = Entity("The Hero", 20, "2-4", 1)
    enemy = Entity('Rat', 10, '1-3', 1)
    phealth = player.health
    ehealth = enemy.health  

    player, enemy, status = attack(player, enemy)
    assert player.health <= phealth
    assert enemy.health < ehealth
                   

#check if player wins
#@pytest.mark.parametrize("player, enemy",[Entity("The Hero", 20, "2-4", 1), Entity('Rat', 1, '1-3', 1)])
def testWin():
    player = Entity("The Hero", 20, "2-4", 1)
    enemy = Entity('Rat', 1, '1-3', 1)
    player, enemy, status = attack(player, enemy)
    assert status == 0
    
    
#check if player loses
#@pytest.mark.parametrize("player, enemy",[Entity("The Hero", 1, "2-4", 0), Entity('Rat', 10, '1-3', 1)])
def testLose():
    player = Entity("The Hero", 1, "2-4", 0)
    enemy = Entity('Rat', 10, '1-3', 1)
    player, enemy, status = attack(player, enemy)
    assert status == 1
