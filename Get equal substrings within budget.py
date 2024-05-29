#Input: s = "abcd", t = "bcdf", maxCost = 3
#Output: 3
#Explanation: "abc" of s can change to "bcd".
#That costs 3, so the maximum length is 3.

class Solution(object):
    def equalsubstring(self, s, t, maxcost):
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        left = 0
        total_cost = 0
        max_length = 0

        for right in range(n):
            total_cost += cost[right]

            while total_cost > maxcost:
                total_cost -= cost[left]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage:
s = "abcd"
t = "bcdf"
maxcost = 3
solution = Solution()
print(solution.equalsubstring(s, t, maxcost))
