import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def intersection_points(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    
    if d > r1 + r2:
        return 0  # Окружности не пересекаются
    elif d < abs(r1 - r2):
        return 0  # Одна окружность внутри другой, нет пересечений
    elif d == 0 and r1 == r2:
        return -1  # Окружности совпадают, бесконечно много пересечений
    elif d == r1 + r2 or d == abs(r1 - r2):
        return 1  # Окружности касаются друг друга в одной точке
    else:
        return 2  # Окружности пересекаются в двух точках

# Ввод данных
x1, y1, r1, x2, y2, r2 = map(float, input().split())

# Вызов функции и вывод результата
result = intersection_points(x1, y1, r1, x2, y2, r2)
print(result)

# input:    0 0 5 5 0 1
# output:   2