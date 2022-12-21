from main import *


def test_factorial():
    assert factorial(4) == 24   
    assert factorial(0) == 1    # перевірка факту 0! == 1
    assert factorial(1) == 1    # 1! == 1


def test_armstrong():
    assert check_for_armstrong(153) == True
    assert check_for_armstrong(154) == False