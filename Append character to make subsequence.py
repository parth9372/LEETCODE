#Input: s = "coaching", t = "coding"
#Output: 4
#Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
#Now, t is a subsequence of s ("coachingding").
#It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

class Solution:
    def appendCharacters(self, s, t):
        m = len(s)
        n = len(t)

        i = 0
        j= 0
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
                i += 1

            return n - j

# Example usage
solution = Solution()
s = "coaching"
t = "coding"
result = solution.appendCharacters(s, t)
print(f"The number of characters to append to '{s}' to make it contain '{t}' as a subsequence is: {result}")