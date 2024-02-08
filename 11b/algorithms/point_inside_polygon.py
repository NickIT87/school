def is_point_inside_polygon(point, polygon) -> bool:
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside

# Приклад використання:
polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
point_inside = (2, 2)
point_outside = (5, 5)

print(is_point_inside_polygon(point_inside, polygon))  # True
print(is_point_inside_polygon(point_outside, polygon))  # False
