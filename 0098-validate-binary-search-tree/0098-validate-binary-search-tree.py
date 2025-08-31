# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, float("-inf"), float("inf"))]

        while stack:

            node, l, h = stack.pop()

            if node.val <= l or node.val >= h:
                return False

            if node.left:
                stack.append((node.left, l, node.val))

            if node.right:
                stack.append((node.right, node.val, h))

        return True

            

            


        