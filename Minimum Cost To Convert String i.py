#Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
#Output: 28
#Explanation: To convert the string "abcd" to string "acbe":
#- Change value at index 1 from 'b' to 'c' at a cost of 5.
#- Change value at index 2 from 'c' to 'e' at a cost of 1.
#- Change value at index 2 from 'e' to 'b' at a cost of 2.
#- Change value at index 3 from 'd' to 'e' at a cost of 20.
#The total cost incurred is 5 + 1 + 2 + 20 = 28.
#It can be shown that this is the minimum possible cost.

class Solution(object):
    def floydWarshall(self, adjList):
        numVertices = 26
        dist = [[float('inf')] * numVertices for _ in range(numVertices)]

        for i in range(numVertices):
            dist[i][i] = 0  # Initialize distance to self as 0
            for neighbor in adjList[i]:
                dist[i][neighbor[0]] = min(dist[i][neighbor[0]], neighbor[1])

        for k in range(numVertices):
            for i in range(numVertices):
                for j in range(numVertices):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    def minimumCost(self, source, target, original, changed, cost):
        numVertices = 26
        adjList = [[] for _ in range(numVertices)]

        for i in range(len(cost)):
            from_char = ord(original[i]) - ord('a')
            to_char = ord(changed[i]) - ord('a')
            transformationCost = cost[i]
            adjList[from_char].append((to_char, transformationCost))

        dist = self.floydWarshall(adjList)
        totalCost = 0

        for i in range(len(source)):
            sourceChar = ord(source[i]) - ord('a')
            targetChar = ord(target[i]) - ord('a')
            if source[i] != target[i]:
                if dist[sourceChar][targetChar] == float('inf'):
                    return -1
                totalCost += dist[sourceChar][targetChar]

        return totalCost

# Example
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
solution = Solution()
print(solution.minimumCost(source, target, original, changed, cost))

