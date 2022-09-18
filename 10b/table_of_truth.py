

def print_data(x, y):
    print("not x: ", not x )
    print ("x or y: ", x or y)
    print ("x and y: ", x and y)
    print ("x ^ y: ", x ^ y)
    print("################################################################")



# print_data(False, False)
# print_data(True, False)
# print_data(False, True)
# print_data(True, True)


a = {1, 3, 5, 7}

b = {2, 4, 6, 8}

c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

d = set()

# print( not d )
# print( d or b )
# print( a and b )
print(a ^ b)
print(d ^ d)