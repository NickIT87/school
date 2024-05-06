import numpy as np

# Створення тривимірного вектора
vector_3d = np.array([1, 2, 3])

# Додавання двох тривимірних векторів
vector_3d_2 = np.array([4, 5, 6])
result_vector = vector_3d + vector_3d_2

print("Результат додавання:", result_vector)

# Скалярний добуток двох тривимірних векторів
dot_product = np.dot(vector_3d, vector_3d_2)
print("Скалярний добуток:", dot_product)

# Векторний добуток двох тривимірних векторів
cross_product = np.cross(vector_3d, vector_3d_2)
print("Векторний добуток:", cross_product)
