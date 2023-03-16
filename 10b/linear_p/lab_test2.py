import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Функція обмеження
def constraint1(x1):
    return 500 - 4 * x1

def constraint2(x1):
    return 150 - x1

def constraint3(x1):
    return 300 - 4 * x1

x1 = np.linspace(0, 200, 400)

# Значення обмежень
x2_1 = constraint1(x1)
x2_2 = np.full_like(x1, 300)
x2_3 = constraint2(x1)
x2_4 = constraint3(x1)

# Побудова графіку
plt.plot(x1, x2_1, label="4x1 + x2 <= 500")
plt.plot(x1, x2_2, label="x2 <= 300")
plt.plot(x1, x2_3, label="x1 + x2 <= 150")
plt.plot(x1, x2_4, label="4x1 + x2 <= 300")

plt.xlim(0, 200)
plt.ylim(0, 350)
plt.xlabel("x1")
plt.ylabel("x2")

plt.fill_between(x1, np.minimum(x2_1, np.minimum(x2_2, np.minimum(x2_3, x2_4))), color="gray", alpha=0.5)
plt.legend()

plt.show()

# Вирішення задачі лінійного програмування
c = [-1, -1]  # Коефіцієнти цільової функції (зі знаком мінус для максимізації)
A = [[4, 1], [0, 1], [1, 1], [4, 1]]  # Матриця обмежень
b = [500, 300, 150, 300]  # Вектор правих частин обмежень
bounds = [(0, None), (0, None)]  # Нижні та верхні межі змінних x1 та x2

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
print("Оптимальний розв'язок:", res.x)
print("Максимальне значення цільової функції:", -res.fun)
