
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


def UEFA_practice():
    kom = int(input("Увести номер команди: "))
    if kom == 1 or kom == 2 or kom == 5:
        kr = "Іспанія"
    else:
        if kom == 3 or kom == 7:
            kr = "Німеччина"
        else:
            if kom == 4 or kom == 9 or kom == 10:
                kr = "Англія"
            else:
                if kom == 6 or kom == 8:
                    kr = "Португалія"
                else:
                    kr = "Рейтинг невідомий"
    print("Країна - ", kr)
    input()