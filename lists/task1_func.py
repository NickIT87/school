from functools import reduce    # импорт служебной ф-ии reduce

# функциональное программирование
# осуществить подсчет суммы квадратов нечетных элементов массива

m: list = [1,2,3,4,5,6,7,8,9]   # объявление списка перечислением

x: list = list(filter(lambda n: n % 2 == 1, m))

s: list = list(map(lambda n: n * n, x))

a: int = reduce(lambda p, n: p + n, s)

print(x)
print(s)
print(a)