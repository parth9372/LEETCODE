#Input: arr = [1,2,3,5], k = 3
#Output: [2,5]
#Explanation: The fractions to be considered in sorted order are:
#1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
#The third fraction is 2/5.


import heapq

def kth_fractions(arr, k):
    heap = []
    for numerator in arr:
        for denominator in arr:
            if denominator != 0:
                heapq.heappush(heap, (numerator / denominator, numerator, denominator))

    for _ in range(k):
        result, numerator, denominator = heapq.heappop(heap)
        if not heap:
            break
    return [numerator, denominator]

arr = [1, 2, 3, 5]
k = 3
print(kth_fractions(arr, k))
