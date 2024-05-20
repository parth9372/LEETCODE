#Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
#Output: [[9,9],[8,6]]
#Explanation: The diagram above shows the original matrix and the generated matrix.
#Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

class Solution:
    def largestLocalUtil(self, grid, x, y, add_value):
        max_val = 0

        for i in range(x, x + 3):
            for j in range(y, y + 3):
                max_val = max(max_val, grid[i][j])

        return max_val

    def largestLocal(self, grid, add_value):
        n = len(grid)
        m = n - 2

        ans = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                ans[i][j] = self.largestLocalUtil(grid, i, j, add_value)

        return ans

sol = Solution()
grid = [
    [9,9,8,1],
    [5,6,2,6],
    [8,2,6,4],
    [6,2,2,2]
]
add_value = 10
print(sol.largestLocal(grid, add_value))
