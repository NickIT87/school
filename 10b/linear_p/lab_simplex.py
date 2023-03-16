from ortools.linear_solver import pywraplp

# Створення симплекс-солвера
solver = pywraplp.Solver.CreateSolver('GLOP')

# Створення змінних
x1 = solver.NumVar(0, solver.infinity(), 'x1')
x2 = solver.NumVar(0, solver.infinity(), 'x2')

# Функція цілі
solver.Maximize(x1 + x2)

# Обмеження
solver.Add(4 * x1 + x2 <= 500)
solver.Add(x2 <= 300)
solver.Add(x1 + x2 <= 150)
solver.Add(4 * x1 + x2 <= 300)

# Розв'язок задачі
status = solver.Solve()

# Виведення результатів
if status == pywraplp.Solver.OPTIMAL:
    print('Оптимальний розв\'язок:')
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    print('Максимальне значення цільової функції:', solver.Objective().Value())

    # # Виведення симплекс-таблиць
    # print('\nСимплекс-таблиці:')
    # for i in range(solver.NumVariables()):
    #     print('x{}:'.format(i + 1), end=' ')
    #     for j in range(solver.NumConstraints() + 1):
    #         print(solver.GetTableauCoefficient(j, i), end=' ')
    #     print()
else:
    print('Проблема не вирішена')


import numpy as np
import matplotlib.pyplot as plt

# Функція обмеження
def constraint1(x1):
    return 500 - 4 * x1

def constraint2(x1):
    return 150 - x1

def constraint3(x1):
    return 300 - 4 * x1

x1_vals = np.linspace(0, 200, 400)

# Значення обмежень
x2_1 = constraint1(x1_vals)
x2_2 = np.full_like(x1_vals, 300)
x2_3 = constraint2(x1_vals)
x2_4 = constraint3(x1_vals)

# Побудова графіку
plt.plot(x1_vals, x2_1, label="4x1 + x2 <= 500")
plt.plot(x1_vals, x2_2, label="x2 <= 300")
plt.plot(x1_vals, x2_3, label="x1 + x2 <= 150")
plt.plot(x1_vals, x2_4, label="4x1 + x2 <= 300")


plt.xlim(0, 200)
plt.ylim(0, 350)
plt.xlabel("x1")
plt.ylabel("x2")

plt.fill_between(x1_vals, np.minimum(x2_1, np.minimum(x2_2, np.minimum(x2_3, x2_4))), color="gray", alpha=0.5)
plt.plot(50, 100, 'bo', label='C (50, 100)')
plt.legend()

# Відображення оптимальної точки
opt_x1 = x1.solution_value()
opt_x2 = x2.solution_value()
plt.scatter(opt_x1, opt_x2, color="red", marker="o", label="Оптимальна точка")
plt.legend()
plt.grid(True)
plt.show()
