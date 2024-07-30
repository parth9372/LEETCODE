#Input: s = "aababbab"
#Output: 2
#Explanation: You can either:
#Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
#Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb")

class Solution:
    def minimumDeletions(self, s):
        ans, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans

#Example
solution = Solution()
s = "aababbab"
print(solution.minimumDeletions(s))

