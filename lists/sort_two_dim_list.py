import numpy as np


c = np.array([ 
    [3,1,1,2,3,1,1,3,3,1,3,3,1,2,1,2,3,1,1,3], 
    [4,6,6,4,4,6,5,4,5,4,6,6,4,6,5,4,6,5,4,5], 
    [3,5,4,3,5,3,5,4,3,3,3,5,5,5,4,5,4,3,4,5] 
])


a = [ 
    [3,1,1,2,3,1,1,3,3,1,3,3,1,2,1,2,3,1,1,3], 
    [4,6,6,4,4,6,5,4,5,4,6,6,4,6,5,4,6,5,4,5], 
    [3,5,4,3,5,3,5,4,3,3,3,5,5,5,4,5,4,3,4,5] 
]

for i in a:
    i.sort()

a.sort()
print(a)

c = np.array(a)
print(c)

b = c.transpose()
print(b)

from numpy import linalg as LA

print(LA.matrix_rank(b))

d = np.array([
    [3, 5, 6],
    [3, 5, 6],
    [3, 5, 6]
])

print(LA.det(d))