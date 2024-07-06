#Input: n = 4, time = 5
#Output: 2
#Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
#After five seconds, the 2nd person is holding the pillow.

class Solution:
    def passThePillow(self, n, time):
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))

# Example
solution = Solution()
n = 4
time = 5
print(solution.passThePillow(n, time))

