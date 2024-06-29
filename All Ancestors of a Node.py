#Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
#Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
#Explanation:
#The above diagram represents the input graph.
#- Nodes 0, 1, and 2 do not have any ancestors.
#- Node 3 has two ancestors 0 and 1.
#- Node 4 has two ancestors 0 and 2.
#- Node 5 has three ancestors 0, 1, and 3.
#- Node 6 has five ancestors 0, 1, 2, 3, and 4.
#- Node 7 has four ancestors 0, 1, 2, and 3.

class Solution(object):
    def getAncestors(self, n, edges):
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        for i in range(n):
            visit = [False] * n
            self.dfs(graph, i, i, res, visit)

        for i in range(n):
            res[i].sort()

        return res

    def dfs(self, graph, parent, curr, res, visit):
        visit[curr] = True
        for dest in graph[curr]:
            if not visit[dest]:
                res[dest].append(parent)
                self.dfs(graph, parent, dest, res, visit)

# Example
solution = Solution()
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(solution.getAncestors(n, edgeList))
