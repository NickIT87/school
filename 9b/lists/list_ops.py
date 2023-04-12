n: int = int(input('кількість цифр = '))
mas: list = []

for i in range(n):
    print("чергова цифра = ", end="")
    mas.append(int(input()))

print(
    "Уведений список: ", 
    ''.join(str(x) for x in mas)
)