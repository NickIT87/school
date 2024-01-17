import random
from deap import base, creator, tools, algorithms

# Определение типа задачи (максимизация или минимизация)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Генерация случайных предметов
# items = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(10)]
items = [(4, 10), (9, 8), (1, 6), (3, 10), (1, 2), (6, 1), (4, 1), (8, 4), (2, 10), (5, 9)]

# Определение функций для оценки качества решения
def evaluate(individual):
    weight = 0
    value = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            weight += items[i][0]
            value += items[i][1]
    if weight > 10:  # Ограничение на вес рюкзака
        return 0,  # Возвращаем 0, если превышен вес
    return value,

# Создание объекта Toolbox для конфигурации алгоритма
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Создание начальной популяции
population = toolbox.population(n=50)

# Запуск эволюционного алгоритма
algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=50, stats=None, halloffame=None)

# Вывод результата
best_individual = tools.selBest(population, k=1)[0]

print("items: ", items)
print("Best Individual:", best_individual)
print("Total Value:", evaluate(best_individual)[0])


# 1. задано видову популяцію (кількість особей) 300
# 2. врахувати імовірність скрещення (кросовер) Предок 1 + Предок 2 50/50
# 3. імовірність мутації 20%
# 4. Естественний відбір -> життєздатна особь чи ні
# 5. зміна поколінь 300 -> 250 -> 300 -> 300 ->
# шляхом естественного відбору отбираємо найбільш життєздатну особь
