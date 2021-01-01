#Unit Test Function for rest Function.
import pytest
from RatVenture_functions import *


@pytest.mark.parametrize("hp,day,resultHp, resultDay",[(1,2,20,2), (3,10,20,4)])
def test_rest(hp, day, resultHp, resultDay):
    valueDay, valueHp =  rest(hp, day)
    assert valueDay == resultDay and valueHp == resultHp


