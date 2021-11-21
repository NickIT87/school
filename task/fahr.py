cycle = True

while cycle:
    celsius = input("Введите значение температуры по шкале Цельсия: ")
    try:
        celsius = float(celsius)
        cycle = False
    except:
        print("Ввод должен быть числом!")

print(celsius * 1.8 + 32)