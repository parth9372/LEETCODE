#Input: nums = [5,3,2,4]
#Output: 0
#Explanation: We can make at most 3 moves.
#n the first move, change 2 to 3. nums becomes [5,3,3,4].
#In the second move, change 4 to 3. nums becomes [5,3,3,3].
#In the third move, change 5 to 3. nums becomes [3,3,3,3].
#After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans

#Example
solution = Solution()
nums = [5,3,2,4]
print(solution.minDifference(nums))
