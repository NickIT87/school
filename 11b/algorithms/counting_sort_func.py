from functools import reduce

def counting_sort(arr):
    min_val, max_val = min(arr), max(arr)
    range_of_elements = max_val - min_val + 1

    def count_occurrences(acc, el):
        acc[el - min_val] += 1
        return acc

    count = reduce(count_occurrences, arr, [0] * range_of_elements)

    def accumulate_counts(acc, i):
        acc[i] += acc[i - 1]
        return acc

    count = reduce(accumulate_counts, range(1, len(count)), count)

    def build_output(output, el):
        output[count[el - min_val] - 1] = el
        count[el - min_val] -= 1
        return output

    return reduce(build_output, reversed(arr), [0] * len(arr))

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)
