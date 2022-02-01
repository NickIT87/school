from numbers import Number
from math import pow

# 1
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

# 2
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

# 3
def factorial(n: int):
    """
    n: positive integer number.
    Function performs the calculation of the 
    product of integer, positive, natural numbers.
    """
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# 4
def bnc(j: int, n: int) -> Number:
    """
    (j = 0,1,2,... <= n = 0,1,2,...)
    The function calculates the binomial coefficient C
    C(j,n) = n! / j!(n-j)!
    """
    nf = factorial(n)
    jf = factorial(j)
    njf = factorial(n - j)
    return nf / (jf * njf)

# 5
def n_binomial(a: Number, b: Number, n: int) -> list:
    """    
    The function performs the expansion into 
    separate terms of an integer non-negative 
    power of the sum of two variables,
    in accordance with the binomial theorem.
    """
    ansv = []
    for j in range(0, n+1):
        ansv.append( bnc(j, n) * pow(a, n-j) * pow(b, j) )
    return ansv
