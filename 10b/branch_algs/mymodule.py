
def abs_mod(n):
    return n if n >= 0 else -n


def something(a):
    if type(a) == int:
        return a
    elif type(a) == bool:
        return True
    elif type(a) == str:
        return 'set of chars'
    else:
        return False