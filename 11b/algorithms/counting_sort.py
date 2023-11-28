def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count the occurrences of each element in the input array
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Modify count array to store cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)
