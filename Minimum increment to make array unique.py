#Input: nums = [1,2,2]
#Output: 1
#Explanation: After 1 move, the array could be [1, 2, 3]

class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ans += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return ans

#Example
solution =Solution()
nums = [1,2,2]
print(solution.minIncrementForUnique(nums))
