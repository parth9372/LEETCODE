#nput: s = "hello"

#utput: 13

#Explanation:

#The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be
#|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

class Solution:
    def scoreOfString(self, s):
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i - 1]) - ord(s[i]))
        return ans

# Example usage
solution = Solution()
s = "hello"
print(f"The score of the string '{s}' is: {solution.scoreOfString(s)}")
