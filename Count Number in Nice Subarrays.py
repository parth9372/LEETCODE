#Input: nums = [1,1,2,1,1], k = 3
#Output: 2
#Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        cnt = [0] * (n + 1)
        cnt[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += cnt[t - k]
            cnt[t] += 1
        return ans

#Exaple
solution =Solution()
nums = [1,1,2,1,1]
k = 3
print(solution.numberOfSubarrays(nums, k))
