#Input: s = "abccccdd"
#Output: 7
#Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:

        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

        ans = 0
        odd_count_found = False


        for key in hm:
            if hm[key] % 2 == 0:
                ans += hm[key]
            else:
                ans += hm[key] - 1
                odd_count_found = True


        if odd_count_found:
            ans += 1

        return ans

# Example
s = "abccccdd"
solution = Solution()
print(solution.longestPalindrome(s))
