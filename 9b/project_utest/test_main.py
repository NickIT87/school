from main import factorial
import pytest


def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_positive_number():
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(7) == 5040

def test_factorial_of_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_non_integer_input():
    with pytest.raises(TypeError):
        factorial("abc")
    with pytest.raises(TypeError):
        factorial(3.14)
    with pytest.raises(TypeError):
        factorial(True)


