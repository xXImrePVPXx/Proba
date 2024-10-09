import pytest
from calculator import calcSum, calcSub, calcMult, calcDiv

def test_sum():
    assert calcSum(1,2) == 3
    assert calcSum(-1,2) == 1
    assert calcSum(-1,-2) == -3
    assert calcSum(0,0) == 0

def test_sub():
    assert calcSub(5,2) == 3
    assert calcSub(-1,2) == -3
    assert calcSub(-1,-2) == 1
    assert calcSub(0,0) == 0