#Input:["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
#Output:[null, 4, 5, 5, 8, 8]
#Explanation:-
#KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
#kthLargest.add(3);   // return 4
#kthLargest.add(5);   // return 5
#kthLargest.add(10);  // return 5
#kthLargest.add(9);   // return 8
#kthLargest.add(4);   // return 8

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Convert nums into a heap
        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        # If after adding the new value, the heap has more than k elements, pop the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is now the k-th largest element
        return self.nums[0]

# Example usage:

# Initializing KthLargest with k=3 and the list [4, 5, 8, 2]
kthLargest = KthLargest(3, [4, 5, 8, 2])

# Performing add operations and printing the results
print(kthLargest.add(3))  # Should return 4
print(kthLargest.add(5))  # Should return 5
print(kthLargest.add(10)) # Should return 5
print(kthLargest.add(9))  # Should return 8
print(kthLargest.add(4))  # Should return 8



