#Input: position = [1,2,3,4,7], m = 3
#Output: 3
#Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3.
#We cannot achieve a larger minimum magnetic force than 3.

class Solution:
    def maxDistance(self, position, m):
        position.sort()
        n = len(position)
        low = 1
        high = position[-1]-position[0]
        while low <= high:
            mid = (low+high)//2
            balls_placed = 1
            prev_position = position[0]
            for i in range(1, n):
                if position[i]-prev_position >= mid:
                    balls_placed += 1
                    prev_position = position[i]
            if balls_placed >= m:
                low = mid+1
                highest_force = mid
            else:
                high = mid-1
        return highest_force

#Example
solution = Solution()
position = [1,2,3,4,7]
m = 3
print(solution.maxDistance(position, m))

