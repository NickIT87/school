import numpy as np

# x0 + 2x1 = 1
# 3x0 + 5x1 = 2:

# a = np.array([
#     [1, 2], 
#     [3, 5]
# ])
# b = np.array([1, 2])

# x = np.linalg.solve(a, b)

# print(x)

# 2x1 + 6x2 + 4x3 = 8
# x1 + 5x2 + 4x3 = 8
# x1 + 5x2 + 7x3 = 17

a = np.array([
    [2, 6, 4],
    [1, 5, 4],
    [1, 5, 7]  
])

b = np.array([ 8, 8, 17 ])

x = np.linalg.solve(a, b)
# x1 = 1, x2 = -1, x3 = 3

print(x)