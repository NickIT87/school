def f(x, y, z):
    return not (x or y) and x and y or (x and not y) and z




print(f(False, False, False))
print(f(True, True, True))
print(f(True, False, False))
print(f(False, True, False))
print(f(False, False, True))
print(f(False, True, True))
print(f(True, False, True))
print(f(True, True, False))










# def a1(x1, x2) -> bool:
#     return x1 or x2

# def a2(a1) -> bool:
#     return not a1

# def a3(x1, x2) -> bool:
#     return x1 and x2

# def a4(a2, a3) -> bool:
#     return a2 and a3

# def a5(x2) -> bool:
#     return not x2

# def a6(x1, a5) -> bool:
#     return x1 and a5

# def a7(a6, x3) -> bool:
#     return a6 and x3

# def f(a4, a7) -> bool:
#     return a4 or a7


# x1, x2, x3 = 1, 0, 1

# if __name__ == "__main__":
#     #print(f(a4(a2(a1(x1, x2)), a3(x1, x2)), a7(a6(x1, a5(x2)), x3)))
#     print(
#         f(
#             a4(
#                 a2(
#                     a1(x1, x2)
#                 ), 
#                 a3(x1, x2)
#             ), 
#             a7(
#                 a6(
#                     x1, 
#                     a5(x2)
#                 ), 
#                 x3
#             )
#         )
#     )