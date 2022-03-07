# найти сумму чисел трехзначного числа

a = 253111      # 10
cnt = len(str(a))       # 4

ansv = []

while cnt:
    cnt -= 1
    x = a // 10
    y = a % 10
    a = x
    ansv.append(y)

print(sum(ansv))