#Unit Test Function for checking if the orb is in a city
from RatVenture_functions import *

#checks if orb is NOT in original town
def checkoriginalTown():
    result = setOrbLocation("0,0")
    assert result == null

#check orb location in towns
def checkorb():
    result1 = setOrbLocation("3,1")
    result2 = setOrbLocation("5,2")
    result3 = setOrbLocation("1,3")
    result4 = setOrbLocation("4,6")

    assert result1 = orb_location or result2 = orb_location or result3 = orb_location or result4 = orb_location
