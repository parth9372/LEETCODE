#Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
#Output: [[1,2,null,4],[6],[7]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root, to_delete):
        s = set(to_delete)
        res = []

        def dfs(root, flag):
            if not root:
                return None
            toDelete = (root.val in s)
            root.left = dfs(root.left, toDelete)
            root.right = dfs(root.right, toDelete)
            if not toDelete and flag:
                res.append(root)
            return None if toDelete else root

        dfs(root, True)
        return res


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
root_list = [1, 2, 3, 4, 5, 6, 7]
to_delete = [3, 5]
root = build_tree_from_list(root_list)
solution = Solution()
result = solution.delNodes(root, to_delete)


# Function to print the trees in the result list
def print_trees(trees):
    def serialize(root):
        if not root:
            return 'None'
        return f'{root.val},({serialize(root.left)}),({serialize(root.right)})'

    return [serialize(tree) for tree in trees]


print(print_trees(result))

