#Input: s = "cdbcbbaaabab", x = 4, y = 5
#Output: 19
#Explanation:
#- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
#- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
#- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
#- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
#Total score = 5 + 4 + 5 + 5 = 19.

class Solution(object):
    def maximumGain(self, s, x, y):
        def gain(s, a, b, points):
            stack = []
            score = 0
            for char in s:
                if char == b and stack and stack[-1] == a:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        if x > y:
            s, gain1 = gain(s, 'a', 'b', x)
            s, gain2 = gain(s, 'b', 'a', y)
        else:
            s, gain1 = gain(s, 'b', 'a', y)
            s, gain2 = gain(s, 'a', 'b', x)

        return gain1 + gain2


# Example
solution = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
print(solution.maximumGain(s, x, y))  # Output should be 19
