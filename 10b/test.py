
# from ctypes import cast
# from distutils.log import error



# def convert(n):
#     try:
#         return int(n)
#     except:
#         #raise ValueError("Invalid number")
#         print("cannot convert n to int")
#     finally:
#         print("do something")


# convert('12')

# condition = 0

# if (condition):
#     print("condition is true")
# elif (not condition and type(condition) != int):
#     print("not condition is true")
# else:
#     print("condition is 0")


def abs(n):
    return n if n >= 0 else -n

assert abs(-4) == 4
assert abs(0) == 0

# print(abs(-45))


# def test(n, b=None):
#     if b:
#         if n < 0:
#             return False
#         else:
#             return True
    
#     if n < 0:
#         return abs(n)


# test(12, b=141)

