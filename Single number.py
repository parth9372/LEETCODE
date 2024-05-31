#Input: nums = [1,2,1,3,2,5]
#Output: [5, 3]
#Explanation:  [5, 3] is also a valid answer.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in nums:
            xor ^= i

        # 101100
        # 101011
        # 010100

        lastBit = xor & ~(xor - 1)
        res = 0
        for i in nums:
            if lastBit & i == 0:
                res ^= i

        return [res, xor ^ res]

#Example
nums = [1,2,1,3,2,5]
solution = Solution()
print(solution.singleNumber(nums))