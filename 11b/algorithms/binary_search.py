def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # знаходимо середину списку

        if arr[mid] == target:
            return mid  # елемент знайдено
        elif arr[mid] < target:
            low = mid + 1  # шуканий елемент знаходиться в правій частині
        else:
            high = mid - 1  # шуканий елемент знаходиться в лівій частині

    return -1  # елемент знайдено

# приклад використання
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"елемент {target_element} знайдено за індексом {result}.")
else:
    print(f"елемент {target_element} не знайдено")
