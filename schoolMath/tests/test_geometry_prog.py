from ..schoolMath import geometry_progression

# 1
def test_should_return_positive_number():
    assert geometry_progression(1, 2, 3) == 8
    assert geometry_progression(1, 2, 2) == 4
    assert geometry_progression(1, -2, 4) == 16

# 2
def test_should_return_negative_number():
    assert geometry_progression(-1, 2, 4) == -16
    assert geometry_progression(1, -2, 5) == -32

# 3
def test_debug():
     assert type(geometry_progression(1, 2, 5, True)) == list
     assert geometry_progression(1, 2, 5, True) == [1, 2, 4, 8, 16]
     assert geometry_progression(1, -2, 5, True) == [1, -2, 4, -8, 16]
     assert geometry_progression(-1, 2, 5, True) == [-1, -2, -4, -8, -16]

# 4
def test_sum_of_progression():
    # (A0 - An * r) / (1 - r) 
    assert sum(geometry_progression(1, 2, 4, True)) == (1 - 8*2)/(1-2)
    assert sum(geometry_progression(1, 2, 4, True)) == 15
    # A0 * ( (1-r**n {+1} ) / (1-r) )
    assert sum(geometry_progression(1, 2, 4, True)) == 1 * ( (1-2**4) / (1-2) )

# 5
def test_negative():
    assert geometry_progression(0, 2, 4) ==  0
    assert geometry_progression(0, 2, 4, True) ==  [0, 0, 0, 0]
    assert geometry_progression(0, 0, 0, True) ==  []