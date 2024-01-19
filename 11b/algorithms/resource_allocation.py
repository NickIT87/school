import matplotlib.pyplot as plt

def resource_allocation(tasks, resources):
    n = len(tasks)
    dp = [[0] * (resources + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(resources + 1):
            if j >= tasks[i - 1]:
                dp[i][j] = max(dp[i - 1][j], tasks[i - 1] + dp[i - 1][j - tasks[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    # Додавання графіків
    plt.figure(figsize=(12, 6))

    # Графік для кожного завдання
    for i in range(n):
        plt.plot(range(resources + 1), dp[i + 1], label=f'Task {i + 1}')

    plt.title('Resource Allocation Dynamic Programming')
    plt.xlabel('Resources')
    plt.ylabel('Total Value')

    # Додавання анотацій
    for i in range(resources + 1):
        for j in range(n):
            plt.annotate(f'{dp[j + 1][i]}', (i, dp[j + 1][i]), textcoords="offset points", xytext=(-5,5), ha='center', fontsize=8)

    max_value = dp[n][resources]
    w = resources
    allocated_tasks = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            allocated_tasks.append(i - 1)
            w -= tasks[i - 1]

    print("Максимальна вартість:", max_value)
    for i in allocated_tasks:
        print("Обранe завдання: ", tasks[i])
    print("індекси завдань: ", allocated_tasks)

    # Додавання легенди
    plt.legend()
    plt.show()

    return max_value, allocated_tasks

# Приклад використання
tasks = [3, 4, 5, 6]
resources = 10
print("Задачі: ", tasks)
print("Ресурси: ", resources)
max_value, allocated_tasks = resource_allocation(tasks, resources)
# print("Максимальна вартість:", max_value)
# print("Обрані завдання:", allocated_tasks)
