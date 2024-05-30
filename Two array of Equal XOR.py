#Input: arr = [2,3,1,6,7]
#Output: 4
#Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

class Solution(object):
    def countTriplets(self, arr):
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]

        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)

        return count

#Example
arr = [2,3,1,6,7]
solution = Solution()
print(solution.countTriplets(arr))


