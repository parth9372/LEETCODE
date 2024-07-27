#Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
#Output: [[3,0,0],[0,0,1],[0,2,0]]
#Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
#The row conditions are the following:
#- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
#- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
#The column conditions are the following:
#- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
#- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
#Note that there may be multiple correct answers.


from collections import defaultdict, deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        rowGraph = defaultdict(list)
        for u, v in rowConditions:
            rowGraph[u].append(v)

        colGraph = defaultdict(list)
        for u, v in colConditions:
            colGraph[u].append(v)

        def topoSort(graph):
            inDegree = {i: 0 for i in range(1, k + 1)}
            for u in graph:
                for v in graph[u]:
                    inDegree[v] += 1
            queue = deque([i for i in inDegree if inDegree[i] == 0])
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for v in graph[node]:
                    inDegree[v] -= 1
                    if inDegree[v] == 0:
                        queue.append(v)
            return order if len(order) == k else []

        rowOrder = topoSort(rowGraph)
        colOrder = topoSort(colGraph)

        if not rowOrder or not colOrder:
            return []

        rowMap = {num: i for i, num in enumerate(rowOrder)}
        colMap = {num: i for i, num in enumerate(colOrder)}

        result = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            result[rowMap[i]][colMap[i]] = i

        return result

# Example
k = 3
rowConditions = [[1, 2], [3, 2]]
colConditions = [[2, 1], [3, 2]]
solution = Solution()
print(solution.buildMatrix(k, rowConditions, colConditions))
