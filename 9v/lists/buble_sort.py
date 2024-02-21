# алгоритм сортування обміном (бульбашкове сортування)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def book_sort(arr):
    n = len(arr)
    for j in range(n-1):
        for k in range(j+1, n):
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]

# Приклад використання:
unsorted_list = [4, 2, 7, 1, 9, 5, 3]
print("Unsorted List:")
print(unsorted_list)
#bubble_sort(unsorted_list)
book_sort(unsorted_list)
print("Sorted List:")
print(unsorted_list)