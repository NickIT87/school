def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Розділяємо масив на три частини
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3

        # Перевірка, чи значення знаходиться в першій частині
        if arr[one_third] == target:
            return one_third
        # Перевірка, чи значення знаходиться в другій частині
        elif arr[two_third] == target:
            return two_third
        # Пошук в першій або другій частині залежно від значення
        elif arr[one_third] > target:
            right = one_third - 1
        elif arr[two_third] < target:
            left = two_third + 1
        # Пошук в останній частині
        else:
            left = one_third + 1
            right = two_third - 1

    return -1  # Значення не знайдено

# Приклад використання
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = ternary_search(sorted_array, target_value)

if result != -1:
    print(f"Значення {target_value} знаходиться на позиції {result}.")
else:
    print(f"Значення {target_value} не знайдено в масиві.")
