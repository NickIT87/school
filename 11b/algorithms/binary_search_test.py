import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds to execute")
        return result
    return wrapper


@timing_decorator
def binary_search_iterative(arr, target):
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


def binary_search_recursive_body(arr, target, low, high):
    # Base Case: If the search range is empty, the target is not in the array
    if low > high:
        return -1
    
    # Calculate the middle index
    mid = (low + high) // 2

    # Check if the middle element is the target
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # If the target is in the right half, search in the right half
        return binary_search_recursive_body(arr, target, mid + 1, high)
    else:
        # If the target is in the left half, search in the left half
        return binary_search_recursive_body(arr, target, low, mid - 1)


@timing_decorator
def binary_search_recursive(arr, target):
    return binary_search_recursive_body(arr, target, 0, len(arr) - 1)


arr = [i for i in range(1, 110000000)]
target = 77777
result_iterative = binary_search_iterative(arr, target)
result_recursive = binary_search_recursive(arr, target)
