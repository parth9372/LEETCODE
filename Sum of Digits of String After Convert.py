#Input: s = "iiii", k = 1
#Output: 36
#Explanation: The operations are as follows:
#- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
#- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
#Thus the resulting integer is 36.

class Solution(object):
    def getLucky(self, s, k):
        # Convert each character in the string to its corresponding numeric value
        number = ''
        for x in s:
            number += str(ord(x) - ord('a') + 1)

        # Perform the transformation `k` times
        while k > 0:
            temp = 0
            for x in number:
                temp += int(x)  # Sum the digits of the current number
            number = str(temp)  # Convert the sum back to a string
            k -= 1
        return int(number)  # Return the final result as an integer

# Example usage
solution = Solution()
s = "iiii"
k = 1
print(solution.getLucky(s, k))

