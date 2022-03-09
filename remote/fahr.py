def celsius_to_fahr(c: float):
    return 9 / 5 * c + 32


def fahr_to_celsius(f: float):
    return 5 / 9 * (f - 32) 


def start():
    while True:
        try:
            usr_input = float(input("Введите число: \n"))
            break
        except:
            print("Ошибка ввода!")

    print(f"Т-ра по шкале Цельсия: {usr_input} в Фаренгейтах: ",
        int(celsius_to_fahr(usr_input)))
    print(f"Т-ра по шкале Фаренгейта: {usr_input} в Цельсиях: ",
        int(fahr_to_celsius(usr_input)))
    

if __name__ == "__main__":
    start()