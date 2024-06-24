#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5

class Solution(object):
    def judgeSquareSum(self, c):
        divisor = 2
        while divisor * divisor <= c:
            if c % divisor == 0:
                exponentCount = 0
                while c % divisor == 0:
                    exponentCount += 1
                    c //= divisor
                if divisor % 4 == 3 and exponentCount % 2 != 0:
                    return False
            divisor += 1
        return c % 4 != 3

#Example
solution = Solution()
c = 5
print(solution.judgeSquareSum(c))

