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

def test_mult():
    assert calcMult(1,4) == 4
    assert calcMult(-3,-5) == 15
    assert calcMult(4,-2) == -8
    assert calcMult(0,0) == 0

def test_div():
    assert calcDiv(3,1) == 3
    assert calcDiv(-6,2) == -3
    assert calcDiv(-12,-3) == 4
    assert calcDiv(0,1) == 0