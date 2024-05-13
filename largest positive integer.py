#Example 1
def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum


nums = [-1, 2, -3, 3]
print(maxSubArray(nums))





