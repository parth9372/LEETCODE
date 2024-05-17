#input: quality = [10,20,5], wage = [70,50,30], k = 2
#Output: 105.00000
#Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

import heapq


def mincostToHireWorkers(quality, wage, k):
    workers = sorted((w / q, q, w) for q, w in zip(quality, wage))

    # Min-heap to keep track of the k smallest qualities
    heap = []
    sum_q = 0
    result = float('inf')

    for ratio, q, w in workers:
        heapq.heappush(heap, -q)
        sum_q += q

        if len(heap) > k:
            sum_q += heapq.heappop(heap)

        if len(heap) == k:
            result = min(result, ratio * sum_q)

    return result


# Test the function
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(f"{mincostToHireWorkers(quality, wage, k):.5f}")  # Output: 105.00000
