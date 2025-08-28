# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        low = float("-inf")
        up = float("inf")


        def validate(node, lower, upper):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False

            
            return validate(node.right, node.val, upper) and validate(node.left, lower, node.val)


        return validate(root, low, up)



        