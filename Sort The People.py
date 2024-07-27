#Input: names = ["Mary","John","Emma"], heights = [180,165,170]
#Output: ["Mary","Emma","John"]
#Explanation: Mary is the tallest, followed by Emma and John.

class Solution(object):
    def sortPeople(self, nombres, alturas):
        nuevoMapa  = {}
        for i in range(len(nombres)):
            nuevoMapa [alturas[i]] = nombres[i]

        alturas.sort()

        respuesta = [None] * len(alturas)
        indice = 0
        for altura in reversed(alturas):
            respuesta[indice] = nuevoMapa[altura]
            indice += 1

        return respuesta

#Example
solution = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(solution.sortPeople(names,heights))

