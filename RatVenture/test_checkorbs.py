#Unit Test Function for checking if the orb is in a city
from RatVenture_functions import *

#checks if orb is NOT in original town
def checkoriginalTown():
    result = setOrbLocation(["0,0"])
    assert result == NULL

#check that the orb will be set on places other than the starter town(0,0) even when 0,0 is an option
def checkorb():
    result = setOrbLocation(["0,0","1,3"])
    assert result == "1,3"
    
