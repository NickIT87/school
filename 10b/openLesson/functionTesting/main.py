# Рекурсивна функція обчислення факторіалу числа.
# в якості аргумента приймає ціле число та
# має повернути значення факторіалу цього числа.
# Факторіал натурального числа n визначається як 
# добуток усіх натуральних чисел від 1 до n включно:
def factorial(n: int) -> int:
    """
    n: positive integer number.
    Function performs the calculation of the 
    product of integer, positive, natural numbers.
    """
    # якщо число меньше або дорівнює одиниці то відповідь є 1
    if n <= 1:      # 0! == 1 && 1! == 1
        return 1
    else:
        return n*factorial(n-1)


# функції що обчислюють належність числа до "числа Армстронга".
# Число Армстронга (також самозакохане число, досконалий цифровий інваріант; 
# англ. pluperfect digital invariant, PPDI) - натуральне число, 
# яке в даній системі числення дорівнює сумі своїх цифр, зведених у ступінь, 
# що дорівнює кількості його цифр.

# 1 реалізація алгоритму з використанням 
# виключно стандартних операторів мови програмування
def count_numbers(nmb: int) -> int:
    i: int = 0       # кількість цифр у числі
    while nmb > 0:
        nmb //= 10
        i+=1
    return i    # функція повертає необхідний показник степеню 

# перевірка числа на належність то "числа Армстронга"
def check_for_armstrong(nmb: int) -> bool:
    num: int        = nmb                   # актуальне число
    ansver: int     = 0           
    i: int          = count_numbers(nmb)    # показник степеню
    
    while nmb > 0:  
        numeric = nmb % 10
        nmb //= 10
        ansver += numeric ** i
    # повертає булеве значення відповідно до належності до множини Армстронга
    return ansver == num  


# 2 реалізація алгоритму за допомогою функцій стандартної бібліотеки мови програмування:
def isArmstrong(number: int) -> bool:
    return sum((int(digit) ** len(str(number)) for digit in str(number))) == number
