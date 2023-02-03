a = '123'

b = []

for i in range(1, len(a)):
    b.append([a[i-1], a[i]])

print(b)