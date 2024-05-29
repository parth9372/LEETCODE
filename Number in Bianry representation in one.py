#Input: s = "1101"
#Output: 6
#Explanation: "1101" corressponds to number 13 in their decimal representation.
#Step 1) 13 is odd, add 1 and obtain 14.
#Step 2) 14 is even, divide by 2 and obtain 7.
#Step 3) 7 is odd, add 1 and obtain 8.
#Step 4) 8 is even, divide by 2 and obtain 4.
#Step 5) 4 is even, divide by 2 and obtain 2.
#Step 6) 2 is even, divide by 2 and obtain 1.

class Solution(object):
    def numSteps(self, s):
        res = 0
        carry = 0
        n = len(s)


        for i in range(n - 1, 0, -1):
           if int(s[i]) + carry == 1:
              carry = 1
              res += 2
           else:
                res += 1


        return res + carry


# Example usage
s = "1101"
solution = Solution()
print(solution.numSteps(s))