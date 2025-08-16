# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        ans = 0
        curr =0

        def dfs(node):

            nonlocal ans
            nonlocal curr

            if not node:
                return 0

            curr = curr*10 + node.val

            if node.left is None and node.right is None:
                ans += curr

            else:
                dfs(node.left)
                dfs(node.right)

            curr //= 10


        dfs(root)

        return ans

        

     