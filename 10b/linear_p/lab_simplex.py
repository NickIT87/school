from ortools.linear_solver import pywraplp

# Створення симплекс-солвера
solver = pywraplp.Solver.CreateSolver('simplex')

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

    # Виведення симплекс-таблиць
    print('\nСимплекс-таблиці:')
    for i in range(solver.NumVariables()):
        print('x{}:'.format(i + 1), end=' ')
        for j in range(solver.NumConstraints() + 1):
            print(solver.GetTableauCoefficient(j, i), end=' ')
        print()
else:
    print('Проблема не вирішена')
