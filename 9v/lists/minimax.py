primes = [2, 3, 5, 7, 11, 13]
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']


def get_max(a):
    element = 0
    for i in a:
        if element < i:
            element = i
    return element


print(get_max(primes))

primes.reverse()

print(primes)