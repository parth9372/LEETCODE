#Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
#Output: 39
#Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

class Solution:
    def matrixScore(self, grid):
        n = len(grid[0])
        maxNum, nums = int('1'*n,2), []

        for row in grid:
            num = int(''.join(map(str,row)),2)
            nums.append(max(num, num^maxNum))       # row flip move
            ans = s = sum(nums)
            k = 1

        for i in range(n-1):
            flip = sum([n^k for n in nums]) - s     # column flip move
            if flip > 0: ans += flip
            k*= 2

        return ans

#Example
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
solution = Solution()
output = solution.matrixScore(grid)
print(output)


