#Input: arr = ["d","b","c","b","c","a"], k = 2
#Output: "a"
#Explanation:
#The only distinct strings in arr are "d" and "a".
#"d" appears 1st, so it is the 1st distinct string.
#"a" appears 2nd, so it is the 2nd distinct string.
#Since k == 2, "a" is returned.

from collections import defaultdict

class Solution(object):
    def kthDistinct(self, arr, k):
        d = defaultdict(lambda: 0)
        # Count the frequency of each element in the array
        for x in arr:
            d[x] += 1

        count = 0
        # Find the k-th distinct element
        for x in arr:
            if d[x] == 1:
                count += 1
                if count == k:
                    return x
        return ""

# Example usage
solution = Solution()
arr = ["d", "b", "c", "b", "c", "a"]  # Corrected: this should be a list, not a tuple
k = 2
print(solution.kthDistinct(arr, k))  # Output should be "a"
