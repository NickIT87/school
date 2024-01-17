A = input("Введіть значення: ")


def main(A):
    A = int(A)
    if type(A) == int:
        print("number")
    else:
        print("string")

    # ...
    

main(A)