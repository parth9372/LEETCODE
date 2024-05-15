#Input: happiness = [1,2,3], k = 2
#Output: 4
#Explanation: We can pick 2 children in the following way:
#- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
#- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
#The sum of the happiness values of the selected children is 3 + 1 = 4.

def max_happiness(happiness, k):
    # Sort the happiness values in non-ascending order
    happiness.sort(reverse=True)

    # Initialize the total happiness sum
    total_happiness = 0

    # Iterate through the sorted happiness array
    for i in range(k):
        # Select the child with the highest happiness value
        total_happiness += happiness[i]

        # Decrease the happiness of unselected children
        for j in range(i + 1, len(happiness)):
            happiness[j] -= 1
            if happiness[j] <= 0:
                break

    return total_happiness


# Example usage
happiness_values = [1, 2, 3]
k = 2
result = max_happiness(happiness_values, k)
print(f"Maximum happiness sum: {result}")
