
def abs_mod(n):
    return n if n >= 0 else -n


def something(a):
    if type(a) == int:
        # if (a == 0):
        #     return None
        return a
    elif type(a) == bool:
        return True
    elif type(a) == str:
        return 'set of chars'
    else:
        return False


def UEFA_practice(kom):
    if kom == 1 or kom == 2 or kom == 5:
        return "Іспанія"
    else:
        if kom == 3 or kom == 7:
            return "Німеччина"
        else:
            if kom == 4 or kom == 9 or kom == 10:
                return "Англія"
            else:
                if kom == 6 or kom == 8:
                    return "Португалія"
                else:
                    return False
