#Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
#Output: 2
#Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.

class Solution(object):
    def countSeniors(self, details):

        counter = 0
        for i in details:
            if int(i[11:13]) > 60:
                counter += 1
        return counter

#Example
solution = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(solution.countSeniors(details))
