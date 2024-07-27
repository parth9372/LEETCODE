#Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
#Output: "UURL"
#Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """

        def find(node, val, path):
            if node is None:
                return False
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False

        p1 = []
        p2 = []
        find(root, startValue, p1)
        find(root, destValue, p2)

        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()

        return 'U' * len(p1) + ''.join(p2[::-1])


# Helper function to build a tree from a list
def build_tree_from_list(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Example
root = build_tree_from_list([5, 1, 2, 3, 0, 6, 4])
startValue = 3
destValue = 6
solution = Solution()
print(solution.getDirections(root, startValue, destValue))
