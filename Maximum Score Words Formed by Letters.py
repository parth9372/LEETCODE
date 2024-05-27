#Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
#Output: 23
#Explanation:
#Score  a=1, c=9, d=5, g=3, o=2
#Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
#Words "dad" and "dog" only get a score of 21.

class Solution:
    def maxScoreWords(self, words, letters, score):
        letterCount = [0] * 26
        for l in letters:
            letterCount[ord(l) - ord('a')] += 1
        return self.dfs(words, score, letterCount, 0)

    def dfs(self, words, score, letterCount, index):
        if index == len(words):
            return 0
        skipScore = self.dfs(words, score, letterCount, index + 1)
        wordScore = 0
        newLetterCount = letterCount[:]
        valid = True
        for c in words[index]:
            if newLetterCount[ord(c) - ord('a')] == 0:
                valid = False
                break
            newLetterCount[ord(c) - ord('a')] -= 1
            wordScore += score[ord(c) - ord('a')]
        takeScore = 0
        if valid:
            takeScore = wordScore + self.dfs(words, score, newLetterCount, index + 1)
        return max(skipScore, takeScore)

# Example usage:
solution = Solution()
words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution.maxScoreWords(words, letters, score))