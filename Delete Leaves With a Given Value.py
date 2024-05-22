#Input: root = [1,2,3,2,null,2,4], target = 2
#Output: [1,null,3,null,4]
#Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
#After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

class Solution(object):
    def removeLeafNodes(self, root, target):

        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root