def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Повертаємо індекс, якщо знайдено
    return -1  # Повертаємо -1, якщо не знайдено


# Приклад використання:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Елемент {target_value} знайдений в позиції {result}.")
else:
    print(f"Елемент {target_value} не знайдений в списку.")
