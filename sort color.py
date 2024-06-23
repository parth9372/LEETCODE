#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums):
        count = [0] * 3

        for num in nums:
            count[num] += 1

        index = 0

        for i in range(3):
            for j in range(count[i]):
                nums[index] = i
                index += 1

# Example
solution = Solution()
nums = [2,0,2,1,1,0]
solution.sortColors(nums)
print(nums)

