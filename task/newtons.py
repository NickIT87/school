# какое ускорение приобретет тело массой m под действием силы F?
# a = F / m

def input_data(msg = 'm, F') -> float:
    while True:
        try:
            data:float = float(input(f"Введите значение - '{msg}': "))
            return data
            break
        except:
            print("Input error, try again!")


def main():
    m:float = input_data("m")
    F:float = input_data("F")
    a:float = F / m
    print(f"Ответ: Ускорение = {a} м/с.")


if __name__ == "__main__":
    main()