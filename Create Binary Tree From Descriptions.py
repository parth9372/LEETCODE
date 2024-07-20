#Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
#Output: [50,20,80,15,17,19]
#Explanation: The root node is the node with value 50 since it has no parent.
#The resulting binary tree is shown in the diagram.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        child = set()
        nodes = {}
        for p, c, left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            child.add(c)
        # Find the root (the node that is never a child)
        root = None
        for p, c, left in descriptions:
            if p not in child:
                root = nodes[p]
                break
        return root

# Example
solution = Solution()
descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
root = solution.createBinaryTree(descriptions)

# Function to print the tree in a readable format for verification
def print_tree(node, depth=0):
    if node:
        print(" " * depth * 2 + str(node.val))
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)

print_tree(root)


