# підключаємо залежності (програмні бібліотеки)
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import numpy as np

# зазначимо вектори
a_vector = np.array([1, 4])
b_vector = np.array([4, 1])

# обчислення модуля векторів
magnitude_a = np.linalg.norm(a_vector)
magnitude_b = np.linalg.norm(b_vector)
# друк результатів
print("Magnitude of A vector:", magnitude_a)
print("Magnitude of B vector:", magnitude_b)

# визначимо вектор, що лежить в площині, де лежать a та b
c_vector = np.cross(a_vector, b_vector)
# обчислення скалярного потрійного добутку
scalar_triple_product = np.dot(a_vector, c_vector)
print(scalar_triple_product)
# перевірка на компланарність
if np.allclose(scalar_triple_product, 0):
    print("Vectors are coplanar.")
else:
    print("Vectors are not coplanar.")


# об'єкти ліній
l1 = LineString([[0, a_vector[0]], [1, a_vector[1]]])
l2 = LineString(
    [
        [0, b_vector[0]],
        [1, b_vector[1]]
    ]
)
# знаходження перетину
l1_l2 = l1.intersection(l2)
# массив точок перетину
points = list(l1_l2.coords)

# друк графіку
plt.plot(a_vector, color='green', label="A vector")
plt.plot(b_vector, color='blue', label="B vector")
plt.scatter(
    points[0][0],
    points[0][1],
    label='intersection point',
    color='red',
    marker='.',
    s=300
)

plt.grid(True)
plt.legend()
plt.show()
