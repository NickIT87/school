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


print(nod(45, 24))