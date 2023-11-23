# алгоритм сортування обміном (бульбашкове сортування)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Приклад використання:
unsorted_list = [4, 2, 7, 1, 9, 5, 3]
print("Unsorted List:")
print(unsorted_list)
bubble_sort(unsorted_list)
print("Sorted List:")
print(unsorted_list)