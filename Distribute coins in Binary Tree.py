#Input: root = [3,0,0]
#Output: 2
#Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

class Solution:
    def distributeCoins(self, root):
        def traverse(node):
            if not node:
                return 0
            left_excess = traverse(node.left)
            right_excess = traverse(node.right)
            total_excess = node.val + left_excess + right_excess - 1
            self.moves += abs(total_excess)
            return total_excess

        self.moves = 0
        traverse(root)
        return self.move


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def traverse(node):
            if not node:
                return 0
            left_excess = traverse(node.left)
            right_excess = traverse(node.right)
            total_excess = node.val + left_excess + right_excess - 1
            self.moves += abs(total_excess)
            return total_excess

        self.moves = 0
        traverse(root)
        return self.moves

# Example usage:
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)

solution = Solution()
result = solution.distributeCoins(root)
print("Output:", result)  # Output: 2
