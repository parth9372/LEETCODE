#Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
#Output: 13
#Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4.
#After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10].
#The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        arr = []
        i = 0
        while i < n:
            prefix = 0
            for j in range(i, n):
                prefix += nums[j]
                arr.append(prefix)
            i += 1
        arr.sort()
        return sum(arr[left-1:right]) % 1000000007

# Example usage
solution = Solution()
nums = [1, 2, 3, 4]  # Corrected: this should be a list, not a tuple
n = 4  # Corrected: this should be an integer, not a tuple
left = 1  # Corrected: this should be an integer, not a tuple
right = 5  # Corrected: this should be an integer, not a tuple
print(solution.rangeSum(nums, n, left, right))  # Output should be 13


