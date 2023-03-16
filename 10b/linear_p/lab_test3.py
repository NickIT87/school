import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_x1_plus_x2", pulp.LpMaximize)

# Створення змінних
x1 = pulp.LpVariable("x1", 0, None, pulp.LpContinuous)
x2 = pulp.LpVariable("x2", 0, None, pulp.LpContinuous)

# Функція цілі
model += x1 + x2, "Objective Function"

# Обмеження
model += 4 * x1 + x2 <= 500
model += x2 <= 300
model += x1 + x2 <= 150
model += 4 * x1 + x2 <= 300

# Вирішення задачі за допомогою симплекс-методу
status = model.solve(pulp.PULP_CBC_CMD(msg=1, solver=pulp.CPLEX_PY(solverType=pulp.CPLEX_PY.CPX_ALG_AUTOMATIC)))

# Виведення результатів
print("Status:", pulp.LpStatus[status])
print("Оптимальний розв'язок:")
print("x1 =", pulp.value(x1))
print("x2 =", pulp.value(x2))
print("Максимальне значення цільової функції:", pulp.value(model.objective))
