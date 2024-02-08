# побудова опуклої оболонки. 
import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(points):
    n = len(points)
    if n < 3:
        return "Cannot build convex hull for less than 3 points."

    pivot = min(points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(points, key=lambda point: (math.atan2(point[1] - pivot[1], point[0] - pivot[0]), point))

    stack = [pivot, sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])

    return stack

# Приклад використання
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points)
print("Опукла оболонка:", convex_hull)
