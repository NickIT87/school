from ortools.linear_solver import pywraplp

# Створення симплекс-солвера
solver = pywraplp.Solver.CreateSolver('GLOP')

# Створення змінних
y1 = solver.NumVar(0, solver.infinity(), 'y1')
y2 = solver.NumVar(0, solver.infinity(), 'y2')
y3 = solver.NumVar(0, solver.infinity(), 'y3')
y4 = solver.NumVar(0, solver.infinity(), 'y4')

# Функція цілі
solver.Minimize(500*y1 + 300*y2 + 150*y3 + 300*y4)

# Обмеження
solver.Add(4*y1 + y2 + y3 + 4*y4 >= 1)
solver.Add(y1 + y3 >= 1)
solver.Add(y2 + y3 >= 1)

# Розв'язок задачі
status = solver.Solve()

# Виведення результатів
if status == pywraplp.Solver.OPTIMAL:
    print('Objective value =', solver.Objective().Value())
    print('y1 =', y1.solution_value())
    print('y2 =', y2.solution_value())
    print('y3 =', y3.solution_value())
    print('y4 =', y4.solution_value())
else:
    print('The problem does not have an optimal solution.')


# Минимизировать функцию G = 500y1 + 300y2 + 150y3 + 300y4

# при ограничениях:

# 4y1 + y2 + y3 + 4y4 >= 1
# y1 + y3 >= 1
# y2 + y3 >= 1

# где y1, y2, y3 и y4 - переменные, 
# соответствующие ограничениям исходной задачи.

# Ограничение 4y1 + y2 + y3 + 4y4 >= 1 соответствует 
# первому ограничению исходной задачи 4x1 + x2 <= 500, 
# y1 + y3 >= 1 - второму ограничению, 
# y2 + y3 >= 1 - третьему ограничению. 
# Переменные y1, y2, y3 и y4 соответствуют ограничениям 
# в том же порядке, что и ограничения в исходной задаче.