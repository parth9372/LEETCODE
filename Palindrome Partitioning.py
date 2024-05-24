#Input:-s = "aab"
#Output:- [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result

#Example
s ="aab"
solution = Solution()
output = solution.partition(s)
print(output)