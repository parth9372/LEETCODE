#Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
#Output: [2,2,2,1,4,3,3,9,6,7,19]

class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr2_numbers = {num: idx for idx, num in enumerate(arr2)}

        arr1.sort(key = lambda x: (arr2_numbers.get(x, len(arr2)), x))
        return arr1

#Example
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
result = solution.relativeSortArray(arr1, arr2)
print(result)

