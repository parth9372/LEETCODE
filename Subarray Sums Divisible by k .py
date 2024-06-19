#Input: nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with a sum divisible by k = 5:
#[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

class Solution(object):
    def subarraysDivByK(self, nums, k):
        sum = 0
        count = 0
        mp = {}
        mp[0] = 1  # always one prefix sum that is initially 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k  # Calculate the remainders of current sum

            if rem < 0:  # Handle negative remainders to ensure they are positive
                rem = k + rem

            if rem in mp:  # If remainder has seen before, it means there are subarrays
                count += mp[rem]  # which sum to multiple of k. Add the count of occurrences

            if rem in mp:
                mp[rem] += 1  # Increment the count for this remainder in the map
            else:
                mp[rem] = 1

        return count

#Example
solution = Solution()
nums = [4, 5, 0, -2, -3, 1]
k = 5
result = solution.subarraysDivByK(nums, k)
print(result)