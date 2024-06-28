#Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
#Output: 43
#Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
#- The road (0,1) has an importance of 2 + 4 = 6.
#- The road (1,2) has an importance of 4 + 5 = 9.
#- The road (2,3) has an importance of 5 + 3 = 8.
#- The road (0,2) has an importance of 2 + 5 = 7.
#- The road (1,3) has an importance of 4 + 3 = 7.
#- The road (2,4) has an importance of 5 + 1 = 6.
#The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
#It can be shown that we cannot obtain a greater total importance than 43.

class Solution(object):
    def maximumImportance(self, n, roads):
        degree = [0] * n

        # Calculate the degree of each city
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        # Create a list of cities and sort by degree
        cities = list(range(n))
        cities.sort(key=lambda x: -degree[x])

        # Assign values to cities starting from the highest degree
        total_importance = 0
        for i in range(n):
            total_importance += (n - i) * degree[cities[i]]

        return total_importance

# Example
solution = Solution()
n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
print(solution.maximumImportance(n, roads))  # Corrected to pass an integer

