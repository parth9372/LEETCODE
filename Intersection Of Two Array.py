#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ans = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

# Example
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersect(nums1, nums2))

