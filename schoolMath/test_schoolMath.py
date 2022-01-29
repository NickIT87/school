from schoolMath import *

def test_arithmetic_progression():
    assert arithmetic_progression(0, 1, 5) == 5
    assert type(arithmetic_progression(0, 1, 5, True)) == list
    assert arithmetic_progression(1, 1, 5, True) == [1, 2, 3 ,4, 5]
    # sum of progression ((n+1) / 2) * (a0 + an)
    assert sum(arithmetic_progression(1, 1, 100, True)) == ((100 + 1)/2)*100
