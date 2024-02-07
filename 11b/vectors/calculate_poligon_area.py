# обчислення площі прямокутника
def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0

    for i in range(n):
        x1, y1, z1 = vertices[i]
        x2, y2, z2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0
    return area


# Приклад використання:
polygon_vertices = [(0, 0, 0), (0, 4, 0), (3, 4, 0), (3, 0, 0)]
area = calculate_polygon_area(polygon_vertices)
print("Площа многокутника:", area)

