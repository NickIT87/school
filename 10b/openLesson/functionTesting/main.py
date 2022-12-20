# Рекурсивна функція обчислення факторіалу числа.
# в якості аргумента приймає ціле число та
# має повернути значення факторіалу цього числа.
def factorial(n: int) -> int:
    """
    n: positive integer number.
    Function performs the calculation of the 
    product of integer, positive, natural numbers.
    """
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


# Рекурсивна функція яка обчислює "число Фібоначчі".
def fibonacci_ser(m: int) -> int:
    if(m <= 1):
        return m
    else:
        return fibonacci_ser(m-1) + fibonacci_ser(m-2)
