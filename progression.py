### arithmetic progression 

# sum ((n+1) / 2) * (a0 + an)
def s(n):
    for j in range(n+1):
        print('iterator: {0}, value: {1}'.format(j, ((j + 1)/2)*j))
    print('final value: {}'.format(((n + 1)/2)*n))

#s(100)

# Если а0 - первый член, а d - постоянная разность между след. и пред. членами (разность прогрессии)
# то aj = a0 + jd; (j = 0, 1, 2, ...)

def arithmetic_progression(a0, d, n):
    for j in range(n):
        print(a0 + j * d)
    return a0 + n * d

#print(arithmetic_progression(12, 123, 10))
#print(arithmetic_progression(0, 1, 10))

def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return None
    else:
        return n*factorial(n-1)

#print(factorial(4))


def geometry_progression(a0, r, n):
    Sn = 0
    for j in range(n+1):
        print(a0 * r ** j)
        Sn += a0 * r ** j
    print("Sn: {}".format(Sn))
    return (a0 - ((a0 * r ** n) * r)) / (1 - r)

print("Snr: {}".format(geometry_progression(1, 2, 4)))