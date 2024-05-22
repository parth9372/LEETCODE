#Input: root = [2,1,3,null,null,0,1]
#Output: true
#Explanation: The above diagram illustrates the evaluation process.
#The AND node evaluates to False AND True = False.
#The OR node evaluates to True OR False = True.
#The root node evaluates to True, so we return true.

class Solution(object):
    def evaluateTree(self, root):
        if not root.left:
            return root.val == 1
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        if root.val == 2:
            return left_val or right_val
        return left_val and right_val

