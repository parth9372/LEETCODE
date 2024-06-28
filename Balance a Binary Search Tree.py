#Input: root = [1,null,2,null,3,null,4,null,null]
#Output: [2,1,3,null,null,null,4]
#Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

class Solution:
    def balanceBST(self, root):
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        def build_balanced_bst(elements):
            if not elements:
                return None
            mid = len(elements) // 2
            node = TreeNode(elements[mid])
            node.left = build_balanced_bst(elements[:mid])
            node.right = build_balanced_bst(elements[mid + 1:])
            return node

        sorted_elements = in_order_traversal(root)
        return build_balanced_bst(sorted_elements)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
arr = [1, None, 2, None, 3, None, 4, None, None]
root = insert_level_order(arr, None, 0, len(arr))

solution = Solution()
new_root = solution.balanceBST(root)

# Print the updated BST
in_order_traversal(new_root)

