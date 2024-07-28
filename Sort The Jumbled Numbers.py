#Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
#Output: [338,38,991]
#Explanation:
#Map the number 991 as follows:
#1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
#2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
#Therefore, the mapped value of 991 is 669.
#338 maps to 007, or 7 after removing the leading zeros.
#38 maps to 07, which is also 7 after removing leading zeros.
#Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
#Thus, the sorted array is [338,38,991].

class Solution:
    def sortJumbled(self, mapping, nums):

        mapped_list = []
        for i, num in enumerate(nums):
            s = str(num)
            n = ''.join(str(mapping[int(ch)]) for ch in s)
            mapped_list.append((num, int(n), i))

        mapped_list.sort(key=lambda x: (x[1], x[2]))

        sorted_nums = [t[0] for t in mapped_list]

        return sorted_nums

# Example usage
sol = Solution()
mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
nums = [990, 332, 981, 330]
sorted_nums = sol.sortJumbled(mapping, nums)
print(sorted_nums)

