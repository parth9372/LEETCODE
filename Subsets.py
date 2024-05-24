#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution(object):
    def subsets(self, nums):
        result = []
        n = len(nums)
        subset_count = 1 << n
        for i in range(subset_count):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result

#Example
solution = Solution()
num = [1,2,3]
result = solution.subsets(num)
print(result)