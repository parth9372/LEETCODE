#Input: piles = [2,7,9,4,4]
#Output: 10
#Explanation:

#If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
#If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.#So we return 10 since it's larger.

class Solution(object):
    def stoneGameII(self, piles):
        dp = {}  # Dictionary to store the results of subproblems for memoization

        def score(alice, idx, M):
            # Base case: if we've reached the end of the piles, no more stones can be taken
            if idx == len(piles):
                return 0

            # Check if the result for this state is already computed
            if (alice, idx, M) in dp:
                return dp[(alice, idx, M)]

            # Initialize the result based on who's turn it is
            if alice:
                res = 0
            else:
                res = float('inf')

            total = 0  # Total number of stones taken in this turn

            # Consider taking x piles where x ranges from 1 to 2 * M
            for x in range(1, 2 * M + 1):
                if idx + x > len(piles):  # If taking x piles exceeds available piles, stop
                    break
                total += piles[idx + x - 1]  # Add stones from the current pile to total

                # Recursively calculate the score for the next state
                if alice:
                    res = max(res, total + score(not alice, idx + x, max(M, x)))
                else:
                    res = min(res, score(not alice, idx + x, max(M, x)))

            # Store the result in the memoization dictionary
            dp[(alice, idx, M)] = res
            return res

        # Start the game with Alice's turn, starting at index 0, with M initially set to 1
        return score(True, 0, 1)

#Example
solution = Solution()
piles = [2,7,9,4,4]
print(solution.stoneGameII(piles))
