# алгоритм сортування обміном (бульбашкове сортування)
from tester import *

@timing_decorator
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@timing_decorator
def book_sort(arr):
    n = len(arr)
    for j in range(n-1):
        for k in range(j+1, n):
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]


if __name__ == '__main__':
    # Приклад використання:
    unsorted_list1 = [4, 2, 7, 1, 9, 5, 3]
    unsorted_list2 = [4, 2, 7, 1, 9, 5, 3]
    print("Unsorted Lists: ", unsorted_list1, unsorted_list2)
    bubble_sort(unsorted_list1)
    book_sort(unsorted_list2)
    print("Sorted Lists: ", unsorted_list1, unsorted_list2)