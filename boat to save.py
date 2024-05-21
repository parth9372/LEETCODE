#Input: people = [1,2], limit = 3
#Output: 1
#Explanation: 1 boat (1, 2)
def num_boats(people, limit):

    people.sort()

    left, right = 0, len(people) - 1

    boats = 0


    while left <= right:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1

        boats += 1

    return boats


people = [1, 2]
limit = 3
print(num_boats(people, limit))
