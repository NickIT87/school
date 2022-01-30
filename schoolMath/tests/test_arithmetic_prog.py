from ..schoolMath import arithmetic_progression

# 1
def test_should_return_positive_number():
    assert arithmetic_progression(0, 1, 5) == 5

# 2
def test_should_return_negative_number():
    assert arithmetic_progression(0, -1, 5) == -5

# 3
def test_debug():
    assert type(arithmetic_progression(0, 1, 5, True)) == list
    assert arithmetic_progression(1, 1, 5, True) == [1, 2, 3 ,4, 5]

# 4
def test_sum_of_progression():
    # sum of progression ((n+1) / 2) * (a0 + an)
    assert sum(arithmetic_progression(1,1,100,True)) == ((100 + 1)/2)*100

# 5
def test_negative():
    assert arithmetic_progression(0, 0, 0) == 0
    assert arithmetic_progression(0, 0, 0, True) == []