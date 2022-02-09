# Двовимірні масиви

# a = [1, 2, 3, 4, 5, "f"]
# print(
#     a[5]
# )

# b = [ 
#     [1, 2, 7],  # 0 
#     [3, 4, 8],  # 1
#     [5, 6, 9]   # 2
# ]

# print(
#     b[1][0]
# )

# for i in b:
#     for j in i:
#         print(j)


# генераторы двумерных списков
# print(
#     [ [1] * 3 for i in range(3)]
# )

#gen = [ [i * j for j in range(6)] for i in range(5) ] 

# for i in gen:
#     print(i)

# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8 10
# 0  3  6  9 12 15
# 0  4  8 12 16 20


# Определитель матрицы: ad - bc
# matrix = [
#     ["a", "c"],
#     ["b", "d"]
# ]

# способ саррюса (правило)
# a1b2c3 + a3b1c2 + a2b3c1 - a3b2c1 - a1b3c2 - a2b1c3
# three_m = [
#     ["a1", "b1", "c1"],
#     ["a2", "b2", "c1"],
#     ["a3", "b3", "c3"]
# ]

# pip install numpy   # библиотека для научных вычислений
# import numpy as np
# from numpy import linalg as LA

# m = np.array([
#     [5, 1, 0],
#     [7, 6, 0],
#     [0, 1, 1]
# ])

# print(type(m))

# print( LA.det(m) )
# print(LA.matrix_rank(m))

# s = np.array([
#     [ -1,   0,   0,   4,  11,   5,   4, -23],
#     [  1,   1,   1,   0,  -1,  -3,  -4,  -7],
#     [  1,  -2,  -9,  -1,   5,  22,  60,  10],
#     [  0,   0,  -1,   1,   7,  -2,  -8, -26]
# ])

# print(LA.matrix_rank(s))

# A = np.array([
#     [1, 2, 1], 
#     [0, 1, 3], 
#     [1, -1, -1]
# ])

# B = np.array([
#     [1],
#     [-1],
#     [0]
# ])

# print(A.dot(B))         # умножение
# print(A + B)            # сложение

m1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

m2 = [
    [0, 0, 0],  # 0
    [0, 0, 0],  # 1
    [0, 0, 0]   # 2
]

def main_diag_fill_ones(m):
    for i in range(len(m)):
        m[i][i] = 1

def rev_diag_ones(m):
    cnt = len(m) - 1
    for i in range(len(m)):  
        m[i][cnt] = 1
        cnt -= 1

main_diag_fill_ones(m1)
rev_diag_ones(m2)

# formated output
print("m1: \n")
for i in m1:
    print(i)
print("\n")
print("m2: \n")
for i in m2:
    print(i)
