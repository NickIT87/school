#import math


def factorial(n: int):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("n must be positive")
    elif type(n) is not int:
        raise TypeError('n must be an integer')
    else:
        return n * factorial(n - 1)


# технічні вимоги до ф-ї факторіал
# 1. факторіал 0 має дорівнювати 1
# 2. функція не має працювати з від'ємними числами
# 3. функція має працювати тільки з цілими числами
# 4. функція має коректно обчислювати факторіал цілого числа