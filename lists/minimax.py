m = [32, 34, 12, 45, 6]

c = 30

def ls(n):
    if n < c:
        return n


a = list(filter(ls, m))

print(a)