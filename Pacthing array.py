#Input: nums = [1,3], n = 6
#Output: 1
#Explanation:
#Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
#Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
#Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
#So we only need 1 patch.

class Solution(object):
    def minPatches(self, nums, n):
        missing = 1
        patches = 0
        index = 0

        while missing <= n:
            if index < len(nums) and nums[index] <= missing:
                missing += nums[index]
                index += 1
            else:
                missing += missing
                patches += 1

        return patches

#Example
solution = Solution()
nums = [1,3]
n = 6
result = solution.minPatches(nums, n)
print(result)