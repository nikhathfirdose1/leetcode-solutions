# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = 0
        def dfs(node):

            nonlocal d
            if node == None:
                return 0

            else:
                left = dfs(node.left)

                right = dfs(node.right)

                d = max(d, (left + right))

            return max(left, right) + 1

        
        dfs(root)

        return d

        
        