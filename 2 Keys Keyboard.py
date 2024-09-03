#Input: n = 3
#Output: 3
#Explanation: Initially, we have one character 'A'.
#In step 1, we use Copy All operation.
#In step 2, we use Paste operation to get 'AA'.
#In step 3, we use Paste operation to get 'AAA'.

class Solution:
    def minSteps(self, n):
        if n == 1:
            return 0

        steps = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1

        return steps

#Example
solution = Solution()
n = 3
print(solution.minSteps(n))
