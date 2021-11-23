from math import pow, sqrt


print("Введите коэффициенты: \n")
# цикл ввода коэффициентов 
while True:
    try:
        a = float(input("a: "))
        if a == 0:
            raise exception
        b = float(input("b: "))
        c = float(input("c: "))
        break
    except:
        print("Ошибка ввода, введите число!")

# найдем дискриминант
D = pow(b, 2) - 4 * a * c
print(D)

if D < 0:
    print("Вещественных корней нет!")
elif D == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f"Корни уравнения: х1 = {x1}, x2 = {x2}")
    # проверка
    # print(a*pow(x1, 2) + b * x1 + c)  # = 0
    # print(a*pow(x2, 2) + b * x2 + c)  # = 0


# тестовые данные:
# 4 4 4
# 16 -8 1
# 5 7 2
