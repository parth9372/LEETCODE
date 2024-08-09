#Input: target = [1,2,3,4], arr = [2,4,1,3]
#Output: true
#Explanation: You can follow the next steps to convert arr to target:
#1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
#2- Reverse subarray [4,2], arr becomes [1,2,4,3]
#3- Reverse subarray [4,3], arr becomes [1,2,3,4]
#There are multiple ways to convert arr to target, this is not the only way to do so.

class Solution(object):
    def canBeEqual(self, target, arr):
        # Sort both lists
        target.sort()
        arr.sort()

        # Compare each element in the lists
        for i in range(len(arr)):
            if arr[i] != target[i]:
                return False

        # Return True if all elements match
        return True


# Example usage
solution = Solution()
target = [1, 2, 3, 4]  # Corrected: this should be a list, not a tuple
arr = [2, 4, 1, 3]
print(solution.canBeEqual(target, arr))  # Output: True

