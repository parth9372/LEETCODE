#Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
#Output: 6
#Explanation: Alice can achieve the maximum sum of 6 using a single operation:
#- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
#The total sum of values is 2 + 2 + 2 = 6.
#It can be shown that 6 is the maximum achievable sum of values.

class Solution(object):
    def maximumValueSum(self, nums, k, edges):

        n, cnt, min_diff = len(nums), 0, float('inf')
        for i, v in enumerate(nums):
            if v ^ k > v:
                nums[i] ^= k
                cnt += 1
            min_diff = min(min_diff, nums[i] - (nums[i] ^ k))
        return sum(nums) - (min_diff if cnt & 1 else 0)

#ANOTHER CODE
class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        n = len(nums)
        cnt = 0
        min_diff = float('inf')

        # Iterate over each number in nums
        for i, v in enumerate(nums):
            # Check if XOR operation is beneficial
            if v ^ k > v:
                nums[i] ^= k
                cnt += 1
            # Track the minimum difference when applying the XOR
            min_diff = min(min_diff, abs(nums[i] - (nums[i] ^ k)))

        # Calculate the sum of the modified array
        result_sum = sum(nums)

        # Adjust the sum based on the count of modifications
        if cnt % 2 == 1:
            result_sum -= min_diff

        return result_sum


# Example usage
solution = Solution()
print(solution.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))  # Output: 6
