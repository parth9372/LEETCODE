#Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
#Output: 3
#Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
#We need 3 bouquets each should contain 1 flower.
#After day 1: [x, _, _, _, _]   // we can only make one bouquet.
#After day 2: [x, _, _, _, x]   // we can only make two bouquets.
#After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
                if total >= m:
                    return True
            return False

        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1

        return low
#Example
solution = Solution()
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(solution.minDays(bloomDay, m, k))
