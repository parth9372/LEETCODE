#Input: original = [1,2,3,4], m = 2, n = 2
#Output: [[1,2],[3,4]]
#Explanation: The constructed 2D array should contain 2 rows and 2 columns.
#The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
#he second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

import numpy as np

class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        # Use NumPy to reshape the 1D array into a 2D array
        arr2D = np.array(original).reshape(m, n)
        return arr2D.tolist()

# Example usage
solution = Solution()
original = [1, 2, 3, 4, 5, 6]
m, n = 2, 3
print(solution.construct2DArray(original, m, n))
