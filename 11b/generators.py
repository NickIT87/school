def some(number):
    return [ i for i in range(number)]

print(some(5))

def some_gen(number):
    for i in range(number):
        yield i

get_val = some_gen(5)

print(next(get_val))
print(next(get_val))
print(next(get_val))
print(next(get_val))
print(next(get_val))
print(next(get_val))