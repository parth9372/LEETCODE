#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

# Example usage
solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(f"The reversed string is: {s}")


