#Input: s = ("catsanddog",wordDict) = ["cat","cats","and","sand","dog"]
#Output: ["cats and dog","cat sand dog"]


class Solution(object):
    def wordBreak(self, s, wordDict):

        res = []
        current_seq = []
        wordSet = set(wordDict)

        def dfs(start):
            if start == len(s):
                res.append("".join(current_seq[:-1]))
                # maybe clear current_seq?
                return
            for j in range(start + 1, len(s) + 1):
                if s[start: j] in wordSet:
                    current_seq.append(s[start:j])
                    current_seq.append(" ")
                    dfs(j)
                    current_seq.pop()
                    current_seq.pop()

        dfs(0)
        return res

# Example usage:
solution = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(solution.wordBreak(s, wordDict))


