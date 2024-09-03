#Input: num = 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
# So you need to output 2.

class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()

        mask = (1 << bit_length) - 1

        return num ^ mask

#Example
solution = Solution()
num = 5
print(solution.findComplement(num))
