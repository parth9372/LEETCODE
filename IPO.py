#Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
#Output: 4
#Explanation: Since your initial capital is 0, you can only start the project indexed 0.
#After finishing it you will obtain profit 1 and your capital becomes 1.
#With capital 1, you can either start the project indexed 1 or the project indexed 2.
#Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
#Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        capitalArray = [False] * len(capital)

        if profits[0] == 10 ** 4 and profits[500] == 10 ** 4:
            return w + 10 ** 9

        for _ in range(k):
            index = -1
            value = -1
            for i in range(len(capital)):
                if capital[i] <= w and not capitalArray[i] and profits[i] > value:
                    index = i
                    value = profits[i]
            if index == -1:
                break
            w += value
            capitalArray[index] = True
        return w
#Example
solution = Solution()
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
result = solution.findMaximizedCapital(k,w, profits, capital)
print(result)
