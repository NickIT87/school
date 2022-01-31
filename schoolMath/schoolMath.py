from numbers import Number
from math import pow


def arithmetic_progression(a0:Number, d:Number, n:int, debug:bool=False):
    """
        a0:     int/float   -   initial element of progression
        d:      int/float   -   difference of progression elements
        n:      int         -   number of elements
        debug:  bool        -   by default == False. If debug == True, 
                                function return the list of numbers

        by default, the function returns a number indicating 
        the result of the progression calculation. 
        If the debug flag is set to true, then the function 
        will return a list of progression elements
    """
    if debug:
        a_prog = []
        for j in range(n):
            a_prog.append(a0 + j * d)
        return a_prog
    return a0 + n * d   # arithmetic progression formula 


def geometry_progression(a0:Number, r:Number, n:int, debug:bool=False):
    """
        a0:     int/float   -   initial element of progression
        r:      int/float   -   the denominator of the progression
                (constant ratio of the next term to the previous one)
        n:      int         -   number of elements
        debug:  bool        -   by default == False. If debug == True, 
                                function return the list of numbers

        by default, the function returns a number indicating 
        the result of the progression calculation. 
        If the debug flag is set to true, then the function 
        will return a list of progression elements
    """
    if debug:
        g_prog = []
        for j in range(n):
            g_prog.append(a0 * r ** j)
        return g_prog
    return a0 * r ** n  # geometry progression formula


def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def C(j, n):
    nf = factorial(n)
    jf = factorial(j)
    njf = factorial(n - j)
    return int(nf / (jf * njf))


def binom_n(a, b, n):
    ansv = []
    for j in range(0, n+1):
        #print(C(j, n) * (a**(n-j)) * (b**j))
        ansv.append((C(j, n) * pow(a, n-j) * pow(b, j)))
    return ansv


print(factorial(-3))
print("(a+b)**n: {}".format(pow(2+2, 6)))
print(binom_n(2, 2, 6))

