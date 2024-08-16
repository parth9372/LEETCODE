#Input: nums = [1,3,1], k = 1
#Output: 0
#Explanation: Here are all the pairs:
#(1,3) -> 2
#(1,1) -> 0
#(3,1) -> 2
#Then the 1st smallest distance pair is (1,1), and its distance is 0.

class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]

        def count_pairs(max_distance):
            count, j = 0, 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= max_distance:
                    j += 1
                count += j - i - 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

# Example
solution = Solution()
nums = [1, 3, 1]  # Removed the trailing comma
k = 1  # Removed the trailing comma
print(solution.smallestDistancePair(nums, k))

