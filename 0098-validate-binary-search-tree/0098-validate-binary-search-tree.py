# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        lower = float("-inf")
        upper = float("inf")

        stack = [(root, lower, upper)]

        while stack:

            node, low, high = stack.pop()

            if not node:
                continue

            if node.val <= low or node.val >= high:
                return False

            
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))

        
        return True




        