from numbers import Number


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

