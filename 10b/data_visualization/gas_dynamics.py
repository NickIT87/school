# моделювання динаміки газу в закритій посудині
import pygame
import random

# Задаємо початкові параметри
size = (800, 600)  # Розмір екрану
n_particles = 100  # Кількість частинок
radius = 5  # Радіус частинок
speed = 1  # Початкова швидкість частинок
color = (255, 255, 255)  # Колір частинок

# Створюємо частинки
particles = []
for i in range(n_particles):
    x = random.randint(radius, size[0]-radius)
    y = random.randint(radius, size[1]-radius)
    vx = random.uniform(-speed, speed)
    vy = random.uniform(-speed, speed)
    particles.append([x, y, vx, vy])

# Ініціалізуємо Pygame
pygame.init()

# Створюємо окреме вікно з грою
game_display = pygame.display.set_mode(size)
pygame.display.set_caption("Динаміка газу")

# Запускаємо головний цикл гри
running = True
while running:
    # Обробляємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлюємо положення частинок
    for p in particles:
        # Відбиваємо частинки від стінок контейнера
        if p[0] < radius or p[0] > size[0]-radius:
            p[2] = -p[2]
        if p[1] < radius or p[1] > size[1]-radius:
            p[3] = -p[3]

        # Оновлюємо положення частинки
        p[0] += p[2]
        p[1] += p[3]

    # Малюємо частинки на екрані гри
    game_display.fill((0, 0, 0))
    for p in particles:
        pygame.draw.circle(game_display, color, (int(p[0]), int(p[1])), radius)
    pygame.display.flip()

# Завершуємо Pygame
pygame.quit()
