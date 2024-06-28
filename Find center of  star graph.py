#Input: edges = [[1,2],[2,3],[4,2]]
#utput: 2
#Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

class Solution:
    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]

#Example
solution = Solution()
edges = [[1,2],[2,3],[4,2]]
print(solution.findCenter(edges))