import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np

def plot_polygon_and_point(vertices, point):
    fig, ax = plt.subplots()

    # Відображення багатокутника
    polygon = Polygon(vertices, closed=True, edgecolor='black')
    ax.add_patch(polygon)

    # Відображення точки
    point_circle = Circle(point, 0.05, color='red', fill=True)
    ax.add_patch(point_circle)

    # Встановлення меж графіку
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def distance_between_point_and_polygon(point, polygon_vertices):
    # Визначення відстані між точкою та багатокутником
    distances = [np.linalg.norm(np.array(point) - np.array(v)) for v in polygon_vertices]
    min_distance = min(distances)
    return min_distance

# Приклад використання
vertices = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Координати вершин багатокутника
point_location = (0.8, 0.8)  # Координати точки

# Обчислення відстані між точкою та багатокутником
distance = distance_between_point_and_polygon(point_location, vertices)
print(f'Відстань між точкою та багатокутником: {distance}')

plot_polygon_and_point(vertices, point_location)
