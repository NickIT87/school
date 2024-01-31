app_name = "Oцінки"
print(app_name + "\n")

mark = int(input("Введіть Вашу оцінку: "))

match mark:
    case 1 | 2 | 3:
        print("Початковий рівень")
    case 4 | 5 | 6:
        print("Середній рівень")
    case 7 | 8 | 9:
        print("Достатній рівень")
    case 10 | 11 | 12:
        print("Високий рівень")
    case _:
        print("Невідомий рівень")
    
if mark == 1 or mark == 2 or mark == 3:
    print("Початковий рівень")
elif mark == 4 or mark == 5 or mark == 6:
    print("середній рівень")
elif mark == 7 or mark == 8 or mark == 9:
    print("достатній рівень")
elif mark == 10 or mark == 11 or mark == 12:
    print("Високий рівень")

if mark < 4:
    print("Початковий рівень")
elif mark > 3 and mark < 7:
    print("середній рівень")
elif mark > 7 and mark < 10:
    print("достатній рівень")
elif mark > 9:
    print("Високий рівень")