#Input: rowSum = [3,8], colSum = [4,7]
#Output: [[3,0],
#         [1,7]]
#Explanation:
#0th row: 3 + 0 = 3 == rowSum[0]
#1st row: 1 + 7 = 8 == rowSum[1]
#0th column: 3 + 1 = 4 == colSum[0]
#1st column: 0 + 7 = 7 == colSum[1]
#The row and column sums match, and all matrix elements are non-negative.
#Another possible matrix is: [[1,2],
 #                            [3,5]]

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        numRows = len(rowSum)
        numCols = len(colSum)
        result = [[0] * numCols for _ in range(numRows)]

        i, j = 0, 0

        while i < numRows and j < numCols:
            val = min(rowSum[i], colSum[j])
            result[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return result

# Example
rowSum = [3, 8]
colSum = [4, 7]
solution = Solution()
print(solution.restoreMatrix(rowSum, colSum))

