#Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
#Output: 3
#Explanation: The figure above describes the graph.
#The neighboring cities at a distanceThreshold = 4 for each city are:
#City 0 -> [City 1, City 2]
#City 1 -> [City 0, City 2, City 3]
#City 2 -> [City 0, City 1, City 3]
#City 3 -> [City 1, City 2]
#Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        distance = [[float('inf')] * n for _ in range(n)]  # Initialize distance matrix with infinity

        for i in range(n):
            distance[i][i] = 0  # Distance to itself is 0

        for edge in edges:
            distance[edge[0]][edge[1]] = edge[2]
            distance[edge[1]][edge[0]] = edge[2]

        # Floyd-Warshall algorithm to find all-pairs shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        ans = -1
        mini = float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and distance[i][j] <= distanceThreshold:
                    count += 1
            if count < mini or (count == mini and i > ans):
                mini = count
                ans = i

        return ans

# Example
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
solution = Solution()
print(solution.findTheCity(n, edges, distanceThreshold))
