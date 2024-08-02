#Input: nums = [0,1,0,1,1,0,0]
#Output: 1
#Explanation: Here are a few of the ways to group all the 1's together:
#[0,0,1,1,1,0,0] using 1 swap.
#[0,1,1,1,0,0,0] using 1 swap.
#[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
#There is no way to group all 1's together with 0 swaps.
#Thus, the minimum number of swaps required is 1

class Solution:
    def minSwaps(self, nums):
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx

#Example
solution = Solution()
nums = [0,1,0,1,1,0,0]
print(solution.minSwaps(nums))