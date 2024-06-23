#Input: seats = [3,1,5], students = [2,7,4]
#Output: 4
#Explanation: The students are moved as follows:
#- The first student is moved from from position 2 to position 1 using 1 move.
#- The second student is moved from from position 7 to position 5 using 2 moves.
#- The third student is moved from from position 4 to position 3 using 1 move.
#In total, 1 + 2 + 1 = 4 moves were used.

class Solution:
    def minMovesToSeat(self, seats, students):
        pos = [0] * 101
        n = len(seats)
        for i in range(n):
            pos[seats[i]] += 1
            pos[students[i]] -= 1
        res = 0
        current = 0
        for i in pos:
            res += abs(current)
            current += i
        return res

#Example
solution = Solution()
seats = [3,1,5]
students = [2,7,4]
result = solution.minMovesToSeat(seats, students)
print(result)