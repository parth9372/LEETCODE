#Input: nums = [1,3]
#Output: 6
#Explanation: The 4 subsets of [1,3] are:
#- The empty subset has an XOR total of 0.
#- [1] has an XOR total of 1.
# [3] has an XOR total of 3.
# [1,3] has an XOR total of 1 XOR 3 = 2.
#0 + 1 + 3 + 2 = 6

class Solution:
    def subsetXORSum(self, nums):
        n = len(nums)

        def find_sum(cur_ind, cur_num):
            if cur_ind == n: # if we reached the bound of the array then just return accumulated XORed number so far
                return cur_num

            include_in_xor = find_sum(cur_ind + 1, cur_num ^ nums[cur_ind]) # Sum if we include this elements
            not_include_in_xor = find_sum(cur_ind + 1, cur_num) # Sum if we don't include this element

            return include_in_xor + not_include_in_xor # Sum of both occasions

        return find_sum(0, 0) # cur_num initially = 0 cause 0 ^ (any_number) = any_number

#Example

solution = Solution()
num = [1, 3]
result = solution.subsetXORSum(num)
print(result)


