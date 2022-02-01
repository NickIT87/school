from math import pow

from ..schoolMath import factorial, bnc, n_binomial

# 1
def test_factorial():
    """should return positive integer number"""
    assert factorial(6) == 720
    assert factorial(0) == 1
    assert factorial(-6) == 1
    assert factorial(12) == 479001600

# 2
def test_bnc():
    """
    should return coefficients according to pascal's triangle
    """
    assert bnc(4, 10) == 210
    assert bnc(0, 0) == 1
    assert bnc(4, 10) == 210
    assert bnc(6, 14) == 3003

# 3
def test_n_binomial():
    """ should return a list of terms  """
    assert type(n_binomial(2, 2, 6)) == list
    assert sum(n_binomial(2, 2, 6)) == pow(2+2, 6)
    assert n_binomial(2, 2, 2) == [4.0, 8.0, 4.0]