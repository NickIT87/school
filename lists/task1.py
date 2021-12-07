# data
m: list = [1,2,3,4,5,6,7,8,9]
x: list = []
s: list = []
a: int = 0
# odd loop
for i in m:
    if i % 2 == 1:
        x.append(i)
# squares loop
for i in x:
    s.append(i * i)
# addition
a = sum(s)
print(a)