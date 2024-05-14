#Input: score = [5,4,3,2,1]
#Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
#Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

def findRelativeRanks(score):
    # Sort the scores and create a dictionary to map scores to their ranks
    sorted_score = sorted(score, reverse=True)
    rank_map = {score: str(i + 1) if i > 2 else ["Gold Medal", "Silver Medal", "Bronze Medal"][i] for i, score in enumerate(sorted_score)}

    # Map the ranks back to the original scores
    return [rank_map[score] for score in score]

# Test the function
score = [5, 4, 3, 2, 1]
print(findRelativeRanks(score))
