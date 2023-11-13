def factorize(n: int) -> list[int]:
    factors = []
    # Перебираємо всі числа від 2 до квадратного кореня з n
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            # якщо число ділится на i, додаємо i до факторів
            factors.append(i)
            n //= i
    # якщо n залишилось простим, та воно більше 1, то додаємо його до факторів
    if n > 1:
        factors.append(n)
    return factors

# Приклад
number_to_factorize = 56
result = factorize(number_to_factorize)
print(f"Факторы числа {number_to_factorize}: {result}")


def fermat_factorization(n):
    # n = a^2 − b^2 = (a+b)(a−b).
    a = int(n**0.5) + 1
    b2 = a**2 - n

    while not (b2**0.5).is_integer():
        a += 1
        b2 = a**2 - n

    b = int(b2**0.5)
    factor1 = a + b
    factor2 = a - b

    return factor1, factor2

# Приклад
number_to_factorize = 56
result = fermat_factorization(number_to_factorize)
print(f"Факторы числа {number_to_factorize}: {result}")


# факторизація за допомогою бібліотеки
from sympy import factorint

number_to_factorize = 56
factors = factorint(number_to_factorize)

print(f"Факторы числа {number_to_factorize}: {factors}")

