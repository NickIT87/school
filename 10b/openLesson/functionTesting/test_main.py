from main import *


def test_factorial():
    assert factorial(4) == 24


def test_armstrong():
    assert check_for_armstrong(153) == True
    assert check_for_armstrong(154) == False