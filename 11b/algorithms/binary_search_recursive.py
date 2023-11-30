def binary_search_recursive(arr, target, low, high):
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
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        # If the target is in the left half, search in the left half
        return binary_search_recursive(arr, target, low, mid - 1)

# Wrapper function for the initial call
def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
