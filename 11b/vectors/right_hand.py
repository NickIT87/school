import numpy as np

def right_hand_rule(v1, v2):
    result = np.cross(v1, v2)
    return result

# Приклад використання правила правої руки
v1 = np.array([1, 0, 0])  # Вектор 1
v2 = np.array([0, 1, 0])  # Вектор 2

result_vector = right_hand_rule(v1, v2)

print("Вектор 1:", v1)
print("Вектор 2:", v2)
print("Векторний добуток (результат):", result_vector)
