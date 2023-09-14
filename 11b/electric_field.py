def electric_field(q, r):
    k = 8.99e9  # Постоянная Кулона в Н * м^2 / Кл^2
    E = 2 * k * abs(q) / (r**2)
    return E

# Данные из задачи
q = 8e-9  # Заряд в Кл
r = 0.2  # Расстояние в метрах

# Вызываем функцию и печатаем результат
electric_field_result = electric_field(q, r)
print(f"Напряженность электрического поля: {electric_field_result} Н/Кл")
