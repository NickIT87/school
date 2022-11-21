def f(x):
    y = x*2
    if y > 4:
        return y
    return f(y)


#print(f(2))


def st(x, n):
    if n == 0:
        return 1
    else:
        return st(x, n-1)*x


#print(st(2, 4))


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


#print(nod(45, 24))
result:list = []

def recurs_find_even(num_list: list) -> list:
    global result
    if not num_list:
        return 
    else:
        first_element: int = num_list[0]
        if first_element % 2 == 0:  #додатне, якщо ділится на два без залишку
            result.append(first_element)
        recurs_find_even(num_list[1:])


def recurs_find_key(key, obj):
    if key in obj:
        return obj[key] 
    for k, v in obj.items ( ):
        if type (v) == dict:
            result = recurs_find_key(key, v)
            if result is not None:
                return result