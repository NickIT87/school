
def add(A, B):
    return A + B


def subtract(A, B):
    return A - B


def divide(A, B):
    return A / B


def multiply(A, B):
    return A * B


def main():
    A = int(input("Ввести ціле А: "))
    ops = input("Введіть математичний оператор: ")
    B = int(input("Ввести ціле B: "))

    # match ops:
    #     case '+':
    #         print(add(A, B))
    #     case '-':
    #         print(subtract(A, B))
    #     case '*':
    #         print(multiply(A, B))
    #     case '/':
    #         print(divide(A, B))
    #     case _:
    #         print("Error")
    
    if ops == '+':
        print(add(A, B))
    elif ops == '-':
        print(subtract(A, B))
    elif ops == '*':
        print(multiply(A, B))
    elif ops == '/':
        print(divide(A, B))
    else:
        print("Error")


if __name__ == "__main__":
    main()
