#Input: logs = ["d1/","d2/","../","d21/","./"]
#Output: 2
#Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

class Solution(object):
    def minOperations(self, logs):
        ans = 0
        for s in logs:
            if s == "../" and ans: ans -= 1
            elif s != "./" and s != "../": ans += 1
        return ans

#Example
solution = Solution()
logs = ["d1/","d2/","../","d21/","./"]
print(solution.minOperations(logs))
