
def max_sum_sequence_2(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    # Обчислюємо максимальну суму для кожного елемента
    dp = [0] * n
    dp[0] = nums[0]

    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp


# print(max_sum_sequence([1, 2, 3]))


def max_sum_subsequence(arr):
    n = len(arr)
    
    # Initialize an array to store maximum sum subsequence ending at each position
    max_sum = [0] * n
    
    # Base case: maximum sum subsequence ending at the first position is the value at that position
    max_sum[0] = arr[0]
    
    # Iterate through the array to calculate maximum sum subsequence ending at each position
    for i in range(1, n):
        max_sum[i] = max(arr[i], max_sum[i-1] + arr[i])
    
    # The maximum sum subsequence is the maximum value in the 'max_sum' array
    max_sequence_sum = max(max_sum)
    
    return max_sequence_sum

# Example usage:
arr = [1, -2, 3, 10, -4, 7, 2, -5]
result = max_sum_subsequence(arr)
print("Maximum Sum Subsequence:", result)

print(max_sum_sequence_2(arr))
