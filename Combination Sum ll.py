#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output:
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(idx, curr_sum, elem):
            if curr_sum == target:
                ans.append(elem[:])
                return

            if idx == n or curr_sum > target:
                return

            elem.append(candidates[idx])
            backtrack(idx + 1, curr_sum + candidates[idx], elem)
            elem.pop()
            # skipping the duplicates
            while idx + 1 < n and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, curr_sum, elem)

        backtrack(0, 0, [])
        return ans

# Example
solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]  # Removed the trailing comma
target = 8  # Removed the trailing comma
print(solution.combinationSum2(candidates, target))

