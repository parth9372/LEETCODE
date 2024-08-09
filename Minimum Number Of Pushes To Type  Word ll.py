#Input: word = "abcde"
#Output: 5
#Explanation: The remapped keypad given in the image provides the minimum cost.
#"a" -> one push on key 2
#"b" -> one push on key 3
#"c" -> one push on key 4
#"d" -> one push on key 5
#"e" -> one push on key 6
#Total cost is 1 + 1 + 1 + 1 + 1 = 5.
#It can be shown that no other mapping can provide a lower cost.

class Solution(object):
    def minimumPushes(self, word):
        count = [0] * 26
        for x in word:
            idx = ord(x) - ord('a')
            count[idx] += 1

        count = sorted(count, reverse=True)
        ans = sum(count[:8]) * 1
        ans += sum(count[8:16]) * 2
        ans += sum(count[16:24]) * 3
        ans += sum(count[24:]) * 4
        return ans
#Example
solution = Solution()
word = "abcde"
print(solution.minimumPushes(word))
