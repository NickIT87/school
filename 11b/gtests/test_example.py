# File: test_example.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
