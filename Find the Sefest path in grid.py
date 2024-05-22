#Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
#Output: 0
#Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

from collections import deque
from heapq import heappop, heappush
class Solution(object):
    def maximumSafenessFactor(self, grid):

        row, col = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return 0
        safeness = [[-1] * col for _ in range(row)]
        q = deque([])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    safeness[r][c] = 0
                    q.append((0, r, c))

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            dis, r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and safeness[nr][nc] == -1:
                    safeness[nr][nc] = dis + 1
                    q.append((dis + 1, nr, nc))

        heap = [(-safeness[row - 1][col - 1], row - 1, col - 1)]
        seen = set([(row - 1, col - 1)])

        while heap:
            dis, r, c = heappop(heap)
            if (r, c) == (0, 0):
                return -dis

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen:
                    safe = max(dis, -safeness[nr][nc])
                    heappush(heap, (safe, nr, nc))
                    seen.add((nr, nc))

        return -1

sol = Solution()
grid = [
    [1,0,0],
    [0,0,0],
    [0,0,1]
]

print(sol.maximumSafenessFactor(grid))