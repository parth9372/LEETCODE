#Input: heights = [1,1,4,2,1,3]
#Output: 3
#Explanation:
#heights:  [1,1,4,2,1,3]
#expected: [1,1,1,2,3,4]
#Indices 2, 4, and 5 do not match.

class Solution:
    def heightChecker(self, heights):
        expected = [0] * (max(heights) + 1)
        for h in heights:
            expected[h] += 1
        i = res = 0
        for j in range(1, len(expected)):
            while expected[j]:
                if heights[i] != j:
                    res += 1
                expected[j] -= 1
                i += 1
        return res

#Example
solution = Solution()
heights = [1,1,4,2,1,3]
result = solution.heightChecker(heights)
print(result)