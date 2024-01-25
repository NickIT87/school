import matplotlib.pyplot as plt

def optimal_schedule(orders, max_time):
    n = len(orders)
    dp = [0] * (max_time + 1)

    for i in range(n):
        for t in range(max_time, orders[i]['start_time'] - 1, -1):
            dp[t] = max(dp[t], dp[t - orders[i]['duration']] + orders[i]['profit'])

    return dp[max_time]

# Пример использования:
orders = [
    {'start_time': 1, 'duration': 3, 'profit': 50},
    {'start_time': 2, 'duration': 2, 'profit': 20},
    {'start_time': 5, 'duration': 1, 'profit': 30},
    {'start_time': 8, 'duration': 2, 'profit': 25}
]

max_available_time = 10

# Вычисление максимальной выгоды
result = optimal_schedule(orders, max_available_time)

# Визуализация графика
times = list(range(max_available_time + 1))
profits = [0] + [optimal_schedule(orders, t) for t in range(1, max_available_time + 1)]

plt.plot(times, profits, marker='o')
plt.title('Максимальная выгода в зависимости от времени')
plt.xlabel('Время')
plt.ylabel('Максимальная выгода')
plt.grid(True)
plt.show()
