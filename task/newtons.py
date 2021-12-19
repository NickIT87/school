# какое ускорение приобретет тело массой m под действием силы F?
# a = F / m

def main() -> List[float]:
    while True:
        try:
            m:float = float(input("Введите значение массы тела в килограммах: "))
            print(m)
            break
        except:
            print("try again")


if __name__ == "__main__":
    main()