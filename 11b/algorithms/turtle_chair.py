import matplotlib.pyplot as plt
import numpy as np


def turtle_steps(N, m, n):
    # Створюємо масив dp для збереження проміжних результатів.
    # dp[i] буде містити мінімальну кількість днів для виходу з ями глибиною i.
    dp = [float('inf')] * (N + 1)
    # Початковий стан: для виходу з ями глибиною 0 не потрібно жодного дня.
    dp[0] = 0

    intermediate_results = []

    # Перебираємо всі глибини ями від 1 до N.
    for i in range(1, N + 1):
        intermediate_results.append(dp.copy())
        # Якщо черепашці можна піднятися на висоту m, оновлюємо dp[i - m].
        if i - m >= 0:
            dp[i] = min(dp[i], dp[i - m] + 1)
        # Якщо черепашці можна спуститися на висоту n, оновлюємо dp[i - n].
        if i - n >= 0:
            dp[i] = min(dp[i], dp[i - n] + 1)

    # Результатом є мінімальна кількість днів для виходу з ями глибиною N.
    return dp, intermediate_results

# Приклад використання
N = 10  # глибина ями
m = 2   # висота, на яку можна підніматися
n = 3   # висота, на яку можна спускатися

result = turtle_steps(N, m, n)
print(f"Черепашці потрібно {result} днів, щоб вибратися з ями.")

def plot_turtle_steps(N, m, n):
    final_result, intermediate_results = turtle_steps(N, m, n)

    fig, axes = plt.subplots(nrows=1, ncols=len(intermediate_results) + 1, figsize=(15, 5))

    # Plot initial state
    axes[0].plot(np.arange(N + 1), intermediate_results[0], marker='o', linestyle='-', color='b')
    axes[0].set_title('Step 0')
    axes[0].set_xlabel('Depth of the Pit')
    axes[0].set_ylabel('Minimum Days')
    axes[0].grid(True)

    for i in range(1, len(intermediate_results) + 1):
        axes[i].plot(np.arange(N + 1), intermediate_results[i - 1], marker='o', linestyle='-', color='b')
        axes[i].set_title(f'Step {i}')
        axes[i].set_xlabel('Depth of the Pit')
        axes[i].set_ylabel('Minimum Days')
        axes[i].grid(True)

    # Plot final state
    axes[-1].plot(np.arange(N + 1), final_result, marker='o', linestyle='-', color='b')
    axes[-1].set_title('Final Result')
    axes[-1].set_xlabel('Depth of the Pit')
    axes[-1].set_ylabel('Minimum Days')
    axes[-1].grid(True)

    plt.tight_layout()
    plt.show()


plot_turtle_steps(N, m, n)
