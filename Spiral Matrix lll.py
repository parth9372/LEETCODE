#Input: rows = 1, cols = 4, rStart = 0, cStart = 0
#Output: [[0,0],[0,1],[0,2],[0,3]]

class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        i, j = rStart, cStart

        diri, dirj = 0, 1  # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and (-1 < j < cols):
                res.append([i, j])

            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri  # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res

# Example
solution = Solution()
rows = 1
cols = 4
rStart = 0
cStart = 0
print(solution.spiralMatrixIII(rows, cols, rStart, cStart))

