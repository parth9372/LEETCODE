#Input: expression = "-1/2+1/2"
#Output: "0/1"

from fractions import Fraction


class Solution(object):
    def fractionAddition(self, expression):
        def parse_expression(expression):
            # List to store parsed fractions
            fractions = []
            i = 0
            while i < len(expression):
                # Determine the sign of the fraction
                if expression[i] == '+' or expression[i] == '-':
                    sign = expression[i]
                    i += 1
                else:
                    sign = '+'

                # Find the end of the fraction (numerator/denominator)
                num_start = i
                while i < len(expression) and expression[i] != '+' and expression[i] != '-':
                    i += 1
                num_end = i

                # Extract numerator and denominator
                numerator, denominator = map(int, expression[num_start:num_end].split('/'))

                # Apply the sign to the numerator if needed
                if sign == '-':
                    numerator = -numerator

                # Add the fraction to the list
                fractions.append(Fraction(numerator, denominator))

            return fractions

        def calculate(fractions):
            # Sum all fractions and format the result
            result = sum(fractions)
            return "{}/{}".format(result.numerator, result.denominator)

        # Parse the expression and calculate the result
        fractions = parse_expression(expression)
        return calculate(fractions)

#Example
solution = Solution()
expression = "-1/2+1/2"
print(solution.fractionAddition(expression))
