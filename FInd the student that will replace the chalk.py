#Input: chalk = [5,1,5], k = 22
#Output: 0
#Explanation: The students go in turns as follows:
#- Student number 0 uses 5 chalk, so k = 17.
#- Student number 1 uses 1 chalk, so k = 16.
#- Student number 2 uses 5 chalk, so k = 11.
#- Student number 0 uses 5 chalk, so k = 6.
#- Student number 1 uses 1 chalk, so k = 5.
#- Student number 2 uses 5 chalk, so k = 0.
#Student number 0 does not have enough chalk, so they will have to replace it.

class Solution(object):
    def chalkReplacer(self, chalk, k):
        # Calculate the total sum of all elements in the chalk array
        allSum = sum(chalk)

        # Calculate the remainder of k when divided by allSum
        # This determines how much chalk remains after several full cycles
        mod = k % allSum

        # Iterate through the chalk array
        for i in range(len(chalk)):
            # If the current student's chalk usage is more than the remaining chalk, return their index
            if chalk[i] > mod:
                return i
            # Otherwise, subtract the current student's chalk usage from the remaining chalk
            mod -= chalk[i]

        # This line should never be reached since the problem guarantees a solution.
        return -1

# Example usage
solution = Solution()
chalk = [5, 1, 5]
k = 22
print(solution.chalkReplacer(chalk, k))

