

def print_data(x, y):
    print ("not x: ", not x )           # заперечення
    print ("x or y: ", x or y)          # диз'юнкція
    print ("x and y: ", x and y)        # кон'юнкція
    print ("x ^ y: ", x ^ y)            # xor (ділення по модулю 2) "виключне або"
    print ("x is y", x is y)            # еквіваленція
    print ("x -> y", not x or y)        # імплікація

    print("\n################################################################\n")



print_data(False, False)
print_data(True, False)
print_data(False, True)
print_data(True, True)


# a = {1, 3, 5, 7}

# b = {2, 4, 6, 8}

# c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# d = set()

# print( not d )
# print( d or b )
# print( a and b )
# print(a ^ b)
# print(d ^ d)