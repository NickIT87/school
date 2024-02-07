a = int(input("Ввести ціле а: "))

n = 0

while a > 0:
    z = a % 10
    a = a // 10
    n = n * 10
    n = n + z
    print(z, a, n)
