#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).


class Solution(object):
    def merge(self, A, start, mid, end, buff):
        left, right = start, mid + 1
        s = end - start + 1

        for i in range(s):
            i0 = start + i
            if left > mid:
                buff[i0] = A[right]
                right += 1
            elif right > end:
                buff[i0] = A[left]
                left += 1
            elif A[left] < A[right]:
                buff[i0] = A[left]
                left += 1
            else:
                buff[i0] = A[right]
                right += 1

        for i in range(start, start + s):
            A[i] = buff[i]

    def mergeSort(self, A, start, end, buff):
        if end <= start:
            return

        mid = start + (end - start) // 2
        self.mergeSort(A, start, mid, buff)
        self.mergeSort(A, mid + 1, end, buff)
        self.merge(A, start, mid, end, buff)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        buff = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, buff)
        return nums

# Example
solution = Solution()
nums = [5, 2, 3, 1]
print(solution.sortArray(nums))


