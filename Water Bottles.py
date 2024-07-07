#Input: numBottles = 9, numExchange = 3
#Output: 13
#Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 9 + 3 + 1 = 13.

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        totalBottles = numBottles

        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            remainingBottles = numBottles % numExchange
            totalBottles += newBottles
            numBottles = newBottles + remainingBottles

        return totalBottles

# Example
solution = Solution()
numBottles = 9
numExchange = 3
print(solution.numWaterBottles(numBottles, numExchange))

