# Знаходимо індекс мінімального елемента 
# в несортованій частині
# Обмінюємо знайдений мінімальний елемент 
# з першим елементом у відсортованій частині

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Приклад використання:
unsorted_list = [4, 2, 7, 1, 9, 5, 3]
print("Unsorted List:")
print(unsorted_list)
selection_sort(unsorted_list)
print("Sorted List:")
print(unsorted_list)
