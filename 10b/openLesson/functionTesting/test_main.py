from main import *


def test_factorial():
    assert factorial(4) == 24


def test_fib():
    a = []
    for i in range(5):
        a.append(fibonacci_ser(i))
    assert a == [0, 1, 1, 2, 3]
    