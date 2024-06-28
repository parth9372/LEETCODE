#Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root):
        if root:
            self.bstToGst(root.right)  # Traverse the right subtree
            self.sum += root.val  # Update the sum
            root.val = self.sum  # Update the current node's value
            self.bstToGst(root.left)  # Traverse the left subtree
        return root

# Helper function to insert nodes into the BST
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp

        if root is not None:
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Helper function to print in-order traversal of the tree
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)

# Example
arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root = insert_level_order(arr, None, 0, len(arr))

solution = Solution()
new_root = solution.bstToGst(root)

# Print the updated BST
in_order_traversal(new_root)



