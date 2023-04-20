import numpy as np
import matplotlib.pyplot as plt

# Встановлюємо розмір графіку
plt.figure(figsize=(8, 8))

# Визначаємо розмірність графіку та область, яка буде відображена
max_iter = 100
xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5

# Створюємо двовимірний масив для зберігання значень кольорів
color = np.zeros((800, 800))

# Обчислюємо значення кольорів для кожної точки на графіку
for i in range(800):
    for j in range(800):
        # Визначаємо комплексне число для поточної точки на графіку
        c = complex(xmin + (xmax - xmin) * i / 800, ymin + (ymax - ymin) * j / 800)
        z = complex(0, 0)
        # Обчислюємо значення за формулою Мандельброта
        for k in range(max_iter):
            z = z*z + c
            if abs(z) > 2:
                break
        # Зберігаємо значення кольору для поточної точки
        color[j, i] = k

# Відображаємо графік фрактала Мандельброта
plt.imshow(color, cmap='hot', extent=(xmin, xmax, ymin, ymax))
plt.title("Mandelbrot Set")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.show()
