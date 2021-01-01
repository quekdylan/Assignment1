#Unit Test Function for saveGame Function.
import pytest
from RatVenture_functions import *

@pytest.mark.parametrize("health, location, day, fullpath,resultHealth, resultLocation, resultDay",[(20,"1,2",2,(os.getcwd() + "\\" + "save.txt"),20,"1,2",2)])
def test_saveGame(health, location, day, fullpath,resultHealth, resultLocation, resultDay):
    saveGame(health, location, day, fullpath)

    with open(fullpath, 'r') as f:
        data = f.read().split('\n')
        v_hp, v_location, v_day = int(data[0]), data[1], int(data[2])
        
        assert v_hp == resultHealth and v_location == resultLocation and v_day == resultDay