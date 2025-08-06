# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        hm = {0:1}

        def dfs(node, prefix):

            if not node:
                return 0

            prefix += node.val
            count = hm.get(prefix - targetSum, 0)


            hm[prefix] = hm.get(prefix, 0) + 1

            count += dfs(node.left, prefix)
            count += dfs(node.right, prefix)

            hm[prefix] -= 1

            return count

        return dfs(root, 0)

