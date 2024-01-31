import random

a = input("Enter code: ")
a = list(a)

for i in range(len(a)):
     a[i] = int(a[i])

vib = random.randint(1, 5)
b = a.count(vib)

print(vib, b)