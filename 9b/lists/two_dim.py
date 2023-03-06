# Практична робота 8. Складання і виконання алгоритмів знаходження сум 
# і кількостей значень елементів табличних величин за заданими умовами.

# створення двовимірного списку (матриці або таблиці)
a = [ [1, 2], [3, 4] ]

# цикл опрацювання кожного елементу матриці
for i in a:
    print(i)
    for j in i:
        print(j)

print("\n================================\n")

for i in range(len(a)):
    #print(a[i])
    for j in range(len(a[i])):
        #print(a[i][j])
        a[i][j] += 1

# друк модифікованої матриці 
print(a)

# конструкція генерації списку
# b = [1, 2, 3, 4]
# for i in range(5, 101):
#     b.append(i)

# list comprehension - вираз що динамічно створює список
b = []
for i in range(10):
    b.append([ j for j in range(1, 11) ])

# idx = range(1, 11)
# c = [ [i for i in idx] for j in idx ]

# рахування суми елементів
print(sum(sum(b,[])))

print(sum(map(sum, b)))

ansv = 0
for i in range(len(b)):
    ansv += sum(b[i])
print(ansv)


# 1. сума елементів що задовільняють певним умовам:
# сумму парних елементів масива

# 1.1
# pairs_elems = []
# for i in b:
#     if i % 2 == 0:
#         pairs_elems.append(i)
# print(sum(pairs_elems))

# 1.2
# print(sum(list(filter(lambda n: n % 2 == 0, b))))


# 2. сума кількості елементів що задовільняють певним умовам:
# перші 10 елементів або останні 20

# x = b[:10]
# print(sum(x))

# y = b[-20:]
# print(sum(y))
