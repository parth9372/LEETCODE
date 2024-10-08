#Input: n = 10
#Output: 12
#Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

import heapq


class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2, 3, 5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)

        for _ in range(n):
            curr = heapq.heappop(uglyHeap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heapq.heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)

        return curr


# Example
solution = Solution()
n = 10
print(solution.nthUglyNumber(n))
