#Input: n = 2
#Output: 8
#Explanation: There are 8 records with length 2 that are eligible for an award:
#"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
#Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

class Solution:
    def checkRecord(self, n):
        kMod = 10 ** 9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for i in range(n):
            p0, p1, p2, q0, q1, q2 = dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][1], dp[1][2]

            # Append P
            dp[0][0] = (p0 + p1 + p2) % kMod

            # Append L
            dp[0][1] = p0

            # Append L
            dp[0][2] = p1

            # Append A or append P
            dp[1][0] = (p0 + p1 + p2 + q0 + q1 + q2) % kMod

            # Append L
            dp[1][1] = q0

            # Append L
            dp[1][2] = q1

        return sum(dp[0] + dp[1]) % kMod

#Example:
n = 2
sol = Solution()
print(sol.checkRecord(n))