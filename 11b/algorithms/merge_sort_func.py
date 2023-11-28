def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

# Example usage:
my_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(my_array.copy())  # Make a copy to keep the original array unchanged
print("Original array:", my_array)
print("Sorted array:", sorted_array)
