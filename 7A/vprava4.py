a = int(input("Ввести ціле a: "))
b = int(input("Ввести ціле b: "))
c = int(input("Ввести ціле c: "))

if (a==b) and (b==c):
    print(3)
elif (a==b) or (b==c) or (a==c):
    print(2)
else:
    print(0)

match a:
    case 1: 
        print(1)
    case 2:
        print(2)
    case _:
        print("none")

