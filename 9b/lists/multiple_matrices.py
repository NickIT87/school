import numpy as np

A = np.array([
    [0],
    [1]
])

B = np.array([
    [0, 1]
])

C = A.dot(B)
D = B.dot(A)

print(C)
print(D)