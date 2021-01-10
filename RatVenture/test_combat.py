import pytest
from RatVenture_functions import *
from RatVenture_classes import *


@pytest.mark.parameterize("hp",[(20)])
    def test_combat("hp, resultHP"):
        valueHP = fight(hp)
        assert valueHP > resultHP
    
