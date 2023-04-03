import math


def factorial(n: int):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("n must be positive")
    elif type(n) is not int:
        raise TypeError('n must be an integer')
    else:
        return n * factorial(n - 1)