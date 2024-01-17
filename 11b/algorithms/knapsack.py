def knapsack(items, capacity):
    items.sort(key=lambda x: x[2] / x[1], reverse=True)  # Сортуємо предмети за відношенням цінності до ваги у спадаючому порядку
    total_value = 0
    knapsack_contents = []

    for item in items:
        if capacity >= item[1]:  # Перевіряємо, чи можна вмістити цей предмет у рюкзак
            knapsack_contents.append(item[0])
            total_value += item[2]
            capacity -= item[1]

    return knapsack_contents, total_value

# Приклад використання
items = [("Предмет 1", 2, 10), ("Предмет 2", 3, 5), ("Предмет 3", 5, 15), ("Предмет 4", 1, 7)]
capacity = 10

result_items, result_value = knapsack(items, capacity)

print("Обрані предмети:", result_items)
print("Загальна цінність:", result_value)
