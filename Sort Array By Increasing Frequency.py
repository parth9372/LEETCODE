#Input: nums = [1,1,2,2,2,3]
#Output: [3,1,1,2,2,2]
#Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

# Example
solution = Solution()
nums = [1, 1, 2, 2, 2, 3]
print(solution.frequencySort(nums))



